# System Design - Service Discovery
# -----------------------------------------------------------------------------
# Service Discovery is the mechanism that allows services to find and
# communicate with each other in a dynamic, distributed environment.
#
# In microservices, instances are constantly being created, destroyed,
# and moved. Hardcoding addresses doesn't work — services need a way
# to discover each other at runtime.
#
# -----------------------------------------------------------------------------
# Two Discovery Patterns:
#
# 1. Client-Side Discovery
#    - Client queries the Service Registry directly
#    - Client picks an instance and connects
#    - Example: Netflix Eureka + Ribbon
#
#    Client → Registry → gets instance list → picks one → connects
#
# 2. Server-Side Discovery
#    - Client connects to a Load Balancer / Router
#    - Load Balancer queries the Registry and routes
#    - Example: AWS ELB, Kubernetes Services, Consul + Nginx
#
#    Client → Load Balancer → Registry → routes to instance
#
# -----------------------------------------------------------------------------
# Key Components:
#
# 1. Service Registry
#    - Central database of all service instances and their addresses
#    - Services register themselves on startup
#    - Services deregister on shutdown
#    - Examples: Consul, etcd, Zookeeper, Eureka
#
# 2. Registration
#    - Self-registration: Service registers itself with the registry
#    - Third-party registration: Deploy tool (Consul-Registrator) registers
#
# 3. Health Checks
#    - Registry periodically checks if instances are alive
#    - Unhealthy instances are removed from the pool
#    - Types: HTTP /health endpoint, TCP port check, heartbeat
#
# 4. Deregistration
#    - Graceful shutdown: service deregisters before stopping
#    - Heartbeat timeout: registry removes if no heartbeat
#
# -----------------------------------------------------------------------------
# Real-world examples:
#
# - Consul (HashiCorp) — service mesh + discovery
# - Kubernetes Services — built-in DNS-based discovery
# - Netflix Eureka — client-side discovery
# - etcd / Zookeeper — used as registries
# - Istio / Linkerd — service mesh with sidecar discovery
# -----------------------------------------------------------------------------


import random
import time
from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional

# =============================================================================
# Service Instance
# =============================================================================


class HealthStatus(Enum):
    HEALTHY = "healthy"
    UNHEALTHY = "unhealthy"


@dataclass
class ServiceInstance:
    service_name: str
    host: str
    port: int
    metadata: Dict[str, str] = field(default_factory=dict)
    registered_at: float = field(default_factory=time.time)
    last_heartbeat: float = field(default_factory=time.time)
    health: HealthStatus = HealthStatus.HEALTHY

    @property
    def address(self) -> str:
        return f"{self.host}:{self.port}"

    def __repr__(self) -> str:
        return f"{self.service_name}@{self.address}[{self.health.value}]"


# =============================================================================
# Service Registry
# =============================================================================


class ServiceRegistry:
    """
    Central registry that tracks all service instances.
    Supports registration, deregistration, health checks, and discovery.
    """

    def __init__(self, heartbeat_timeout: float = 30.0):
        self._services: Dict[str, List[ServiceInstance]] = {}
        self.heartbeat_timeout = heartbeat_timeout
        self.event_log: List[str] = []

    def _log(self, msg: str):
        self.event_log.append(msg)

    def register(self, instance: ServiceInstance):
        name = instance.service_name
        if name not in self._services:
            self._services[name] = []
        self._services[name].append(instance)
        self._log(f"  [Registry] Registered {instance}")

    def deregister(self, instance: ServiceInstance):
        name = instance.service_name
        if name in self._services:
            self._services[name] = [
                i for i in self._services[name] if i.address != instance.address
            ]
            self._log(f"  [Registry] Deregistered {instance}")

    def heartbeat(self, instance: ServiceInstance):
        """Instance sends heartbeat to confirm it's alive."""
        instance.last_heartbeat = time.time()
        instance.health = HealthStatus.HEALTHY

    def discover(self, service_name: str) -> List[ServiceInstance]:
        """Return all healthy instances of a service."""
        instances = self._services.get(service_name, [])
        return [i for i in instances if i.health == HealthStatus.HEALTHY]

    def check_health(self):
        """Simulate health check — mark stale instances as unhealthy."""
        now = time.time()
        for name, instances in self._services.items():
            for instance in instances:
                age = now - instance.last_heartbeat
                if age > self.heartbeat_timeout:
                    instance.health = HealthStatus.UNHEALTHY
                    self._log(
                        f"  [Registry] {instance} marked UNHEALTHY "
                        f"(no heartbeat for {age:.0f}s)"
                    )

    def get_all_services(self) -> Dict[str, int]:
        """Return count of healthy instances per service."""
        return {
            name: len([i for i in insts if i.health == HealthStatus.HEALTHY])
            for name, insts in self._services.items()
        }


# =============================================================================
# Client-Side Discovery
# =============================================================================


class ClientSideDiscovery:
    """
    Client queries the registry directly, picks an instance, and connects.
    The client is responsible for load balancing and failover.
    """

    def __init__(self, registry: ServiceRegistry):
        self.registry = registry

    def get_instance(self, service_name: str) -> Optional[ServiceInstance]:
        instances = self.registry.discover(service_name)
        if not instances:
            return None
        # Simple random load balancing
        return random.choice(instances)

    def call_service(self, service_name: str, path: str) -> Optional[str]:
        instance = self.get_instance(service_name)
        if not instance:
            return f"[No healthy instance of {service_name}]"
        return f"→ {instance.address}{path} (via client-side discovery)"


# =============================================================================
# Server-Side Discovery (Load Balancer)
# =============================================================================


class ServerSideDiscovery:
    """
    Client connects to a Load Balancer. The LB queries the registry
    and routes the request. Client doesn't know about instances.
    """

    def __init__(self, registry: ServiceRegistry):
        self.registry = registry
        self._counter = 0

    def route_request(self, service_name: str, path: str) -> Optional[str]:
        instances = self.registry.discover(service_name)
        if not instances:
            return f"[No healthy instance of {service_name}]"

        # Round-robin
        instance = instances[self._counter % len(instances)]
        self._counter += 1
        return f"→ LB → {instance.address}{path} (via server-side discovery)"


# =============================================================================
# Service (self-registration)
# =============================================================================


class Service:
    """
    A service instance that self-registers with the registry
    and sends periodic heartbeats.
    """

    def __init__(
        self,
        name: str,
        host: str,
        port: int,
        registry: ServiceRegistry,
        heartbeat_interval: float = 5.0,
    ):
        self.instance = ServiceInstance(name, host, port)
        self.registry = registry
        self.heartbeat_interval = heartbeat_interval
        self.running = False

    def start(self):
        self.registry.register(self.instance)
        self.running = True
        self.send_heartbeat()

    def send_heartbeat(self):
        self.registry.heartbeat(self.instance)

    def stop(self):
        self.running = False
        self.registry.deregister(self.instance)

    def simulate_crash(self):
        self.running = False
        self.instance.health = HealthStatus.UNHEALTHY


# =============================================================================
# Usage
# =============================================================================


def main():
    print("=" * 65)
    print("SERVICE DISCOVERY — Finding Services Dynamically")
    print("=" * 65)

    registry = ServiceRegistry(heartbeat_timeout=10.0)

    # --- 1. Register services ---
    print("\n" + "-" * 65)
    print("1. SERVICE REGISTRATION")
    print("-" * 65)

    user_svc_1 = Service("user-service", "10.0.1.1", 8080, registry)
    user_svc_2 = Service("user-service", "10.0.1.2", 8080, registry)
    order_svc = Service("order-service", "10.0.2.1", 8080, registry)
    payment_svc = Service("payment-service", "10.0.3.1", 8080, registry)

    user_svc_1.start()
    user_svc_2.start()
    order_svc.start()
    payment_svc.start()

    print(f"\n  All services: {registry.get_all_services()}")

    # --- 2. Client-side discovery ---
    print("\n" + "-" * 65)
    print("2. CLIENT-SIDE DISCOVERY")
    print("   Client queries registry, picks instance, connects directly")
    print("-" * 65)

    client = ClientSideDiscovery(registry)
    for i in range(3):
        result = client.call_service("user-service", "/users/42")
        print(f"  Request {i + 1}: {result}")

    # --- 3. Server-side discovery ---
    print("\n" + "-" * 65)
    print("3. SERVER-SIDE DISCOVERY")
    print("   Client → Load Balancer → routes to instance")
    print("-" * 65)

    lb = ServerSideDiscovery(registry)
    for i in range(3):
        result = lb.route_request("user-service", "/users/42")
        print(f"  Request {i + 1}: {result}")

    # --- 4. Health checks ---
    print("\n" + "-" * 65)
    print("4. HEALTH CHECKS — Detecting failed instances")
    print("-" * 65)

    print("\n  Simulating user-service-1 crash (no more heartbeats):")
    user_svc_1.simulate_crash()

    print("  Simulating health check timeout...")
    # Simulate time passing (lower timeout for demo)
    registry.heartbeat_timeout = 0.1
    time.sleep(0.2)
    registry.check_health()

    print(f"\n  Healthy instances: {registry.get_all_services()}")
    result = client.call_service("user-service", "/users/42")
    print(f"  Request after crash: {result}")

    # --- 5. Deregistration ---
    print("\n" + "-" * 65)
    print("5. GRACEFUL DEREGISTRATION")
    print("-" * 65)

    print("\n  Order service shutting down gracefully:")
    order_svc.stop()
    print(f"  Healthy instances: {registry.get_all_services()}")

    # --- Summary ---
    print("\n" + "=" * 65)
    print("SUMMARY — Service Discovery Patterns")
    print("=" * 65)
    print("""
  Pattern          Pros                    Cons
  -------          ----                    ----
  Client-Side      Client controls         Client becomes complex
                   load balancing          Must handle failover
  Server-Side      Simpler client          Extra network hop
                   Centralized routing     Load balancer SPOF

  Key Components:
  - Service Registry: stores instance locations
  - Registration: services announce themselves
  - Health Checks: detect and remove dead instances
  - Deregistration: clean up on shutdown

  Real-world systems:
  - Consul, Kubernetes DNS, Netflix Eureka
  - Istio/Linkerd (service mesh with sidecar)
""")


if __name__ == "__main__":
    main()
