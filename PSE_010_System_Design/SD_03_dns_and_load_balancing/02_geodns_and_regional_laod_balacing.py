# System Design - GeoDNS + Regional Load Balancing (Complete Example)
# -----------------------------------------------------------------------------
# This system demonstrates real-world request routing based on user location.
#
# Architecture:
#
#   User
#    ↓
#   GeoDNS (select region)
#    ↓
#   Regional Load Balancer
#    ↓
#   Backend Servers
#
# -----------------------------------------------------------------------------
# Responsibilities:
#
# 1. GeoDNS:
#    - Determines user's region based on location (simulated here)
#    - Returns regional endpoint (not a server directly)
#
# 2. Load Balancer:
#    - Distributes traffic within a region
#    - Uses round-robin strategy
#
# 3. Servers:
#    - Handle actual business requests
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# GeoDNS (Location-based routing)
# -----------------------------------------------------------------------------


class GeoDNS:
    """
    Simulates geo-aware DNS routing.
    """

    def __init__(self):
        self.region_map = {
            "asia": "asia",
            "europe": "europe",
            "us": "us",
        }

    def resolve_region(self, user_location: str) -> str:
        print(f"[GeoDNS] Detecting user location: {user_location}")

        region = self.region_map.get(user_location, "us")

        print(f"[GeoDNS] Routing to region: {region}")

        return region


# -----------------------------------------------------------------------------
# Server
# -----------------------------------------------------------------------------


class Server:
    def __init__(self, name: str):
        self.name = name

    def handle_request(self, request: str):
        print(f"[{self.name}] Processing request: {request}")


# -----------------------------------------------------------------------------
# Regional Load Balancer
# -----------------------------------------------------------------------------


class LoadBalancer:
    """
    Distributes requests across servers in one region.
    """

    def __init__(self, region_name: str, servers: list[Server]):
        self.region_name = region_name
        self.servers = servers
        self.index = 0

    def route(self, request: str):
        server = self.servers[self.index]
        self.index = (self.index + 1) % len(self.servers)

        print(f"[{self.region_name} LB] Routing to {server.name}")
        server.handle_request(request)


# -----------------------------------------------------------------------------
# Global System (Combines DNS + Load Balancing)
# -----------------------------------------------------------------------------


class GlobalSystem:
    """
    End-to-end distributed system simulation.
    """

    def __init__(self):
        self.dns = GeoDNS()

        self.load_balancers = {
            "asia": LoadBalancer("ASIA", [Server("ASIA-1"), Server("ASIA-2")]),
            "europe": LoadBalancer("EUROPE", [Server("EU-1"), Server("EU-2")]),
            "us": LoadBalancer("US", [Server("US-1"), Server("US-2")]),
        }

    def handle_request(self, user_location: str, request: str):
        print("\n" + "=" * 60)

        # Step 1: DNS resolution (region selection)
        region = self.dns.resolve_region(user_location)

        # Step 2: Route to regional load balancer
        lb = self.load_balancers[region]

        # Step 3: Load balancer routes to server
        lb.route(request)

        print("=" * 60)


# -----------------------------------------------------------------------------
# Usage Example
# -----------------------------------------------------------------------------


def main():
    system = GlobalSystem()

    # Users from different locations
    system.handle_request("asia", "GET /users")
    system.handle_request("europe", "GET /orders")
    system.handle_request("us", "POST /login")
    system.handle_request("asia", "GET /products")
    system.handle_request("europe", "DELETE /account")


if __name__ == "__main__":
    main()
