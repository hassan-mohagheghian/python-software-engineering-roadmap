# System Design - DNS and Load Balancing
# -----------------------------------------------------------------------------
# This system explains how users are routed to the correct server in a
# distributed system.
#
# It combines two core components:
#
# 1. DNS (Domain Name System)
# 2. Load Balancer
#
# -----------------------------------------------------------------------------
# OVERALL FLOW
# -----------------------------------------------------------------------------
#
# User → DNS → Load Balancer → Server → Response → User
#
# -----------------------------------------------------------------------------
# 1. DNS (Domain Name System)
# -----------------------------------------------------------------------------
#
# DNS translates human-readable domains into IP addresses.
#
# Example:
#     www.example.com → 192.168.1.10
#
# Steps:
# - User enters domain in browser
# - DNS resolver finds IP address
# - IP is returned to client
#
# -----------------------------------------------------------------------------
# 2. LOAD BALANCER
# -----------------------------------------------------------------------------
#
# A Load Balancer distributes incoming traffic across multiple servers
# to ensure:
#
# - High availability
# - Scalability
# - Fault tolerance
#
# -----------------------------------------------------------------------------
# LOAD BALANCING ALGORITHMS
# -----------------------------------------------------------------------------
#
# 1. Round Robin
#    - Requests distributed sequentially
#
# 2. Least Connections
#    - Sends request to server with least active connections
#
# 3. IP Hash
#    - Same client always goes to same server
#
# -----------------------------------------------------------------------------
# REAL-WORLD ARCHITECTURE
# -----------------------------------------------------------------------------
#
#        DNS
#         ↓
#   Load Balancer
#     ↓   ↓   ↓
#   S1   S2   S3
#
# -----------------------------------------------------------------------------
# BENEFITS
# -----------------------------------------------------------------------------
#
# - Scales applications horizontally
# - Prevents server overload
# - Improves reliability
# - Enables fault tolerance
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# DNS SIMULATION
# -----------------------------------------------------------------------------


class DNS:
    """
    Simulates DNS resolution.
    """

    def __init__(self):
        self.domain_map = {"example.com": "192.168.1.1"}

    def resolve(self, domain: str) -> str:
        print(f"[DNS] Resolving domain: {domain}")
        return self.domain_map.get(domain, "0.0.0.0")


# -----------------------------------------------------------------------------
# SERVERS
# -----------------------------------------------------------------------------


class Server:
    def __init__(self, name: str):
        self.name = name
        self.connections = 0

    def handle_request(self, request: str):
        self.connections += 1
        print(f"[{self.name}] Handling request: {request}")


# -----------------------------------------------------------------------------
# LOAD BALANCER
# -----------------------------------------------------------------------------


class LoadBalancer:
    """
    Simple round-robin load balancer.
    """

    def __init__(self, servers):
        self.servers = servers
        self.index = 0

    def get_server(self):
        server = self.servers[self.index]
        self.index = (self.index + 1) % len(self.servers)
        return server

    def handle_request(self, request: str):
        server = self.get_server()
        server.handle_request(request)


# -----------------------------------------------------------------------------
# CLIENT
# -----------------------------------------------------------------------------


class Client:
    def __init__(self, dns: DNS, load_balancer: LoadBalancer):
        self.dns = dns
        self.load_balancer = load_balancer

    def send_request(self, domain: str, request: str):
        ip = self.dns.resolve(domain)
        print(f"[Client] Resolved {domain} → {ip}")

        self.load_balancer.handle_request(request)



# -----------------------------------------------------------------------------
# USAGE
# -----------------------------------------------------------------------------


def dns_lao():
    dns = DNS()

    servers = [
        Server("Server-1"),
        Server("Server-2"),
        Server("Server-3"),
    ]

    lb = LoadBalancer(servers)

    client = Client(dns, lb)

    client.send_request("example.com", "GET /users")
    client.send_request("example.com", "GET /orders")
    client.send_request("example.com", "POST /login")
    client.send_request("example.com", "GET /profile")


if __name__ == "__main__":
    main()
