# System Design - Client Server Model
# -----------------------------------------------------------------------------
# The Client-Server model is the most fundamental architecture in distributed
# systems and web applications.
#
# It describes how two systems interact:
#
# - Client: initiates requests (browser, mobile app, frontend service)
# - Server: processes requests and returns responses (backend API, database API)
#
# Communication happens over a network using protocols such as HTTP/HTTPS.
#
# -----------------------------------------------------------------------------
# Core Idea:
#
# Client → Request → Server → Process → Response → Client
#
# -----------------------------------------------------------------------------
# Key Characteristics:
#
# 1. Separation of concerns
#    - Client handles UI / user interaction
#    - Server handles business logic and data
#
# 2. Stateless communication (in HTTP)
#    - Each request is independent
#    - Server does not remember previous requests by default
#
# 3. Scalability
#    - Multiple clients can connect to one server
#    - Server can be scaled horizontally using load balancers
#
# -----------------------------------------------------------------------------
# Real-world examples:
#
# - Browser (Client) → Web Server (Flask/Django/FastAPI)
# - Mobile App → REST API Backend
# - Frontend React App → Backend Microservice
# - CLI tool → Remote API service
# -----------------------------------------------------------------------------

import time

# -----------------------------------------------------------------------------
# Server Simulation
# -----------------------------------------------------------------------------


class Server:
    """
    Represents a backend server that processes requests.
    """

    def process_request(self, request: str) -> str:
        """
        Simulate request processing.
        """
        print(f"[Server] Received request: {request}")

        # Simulate processing time
        time.sleep(1)

        response = f"Processed: {request}"

        print(f"[Server] Sending response: {response}")

        return response


# -----------------------------------------------------------------------------
# Client Simulation
# -----------------------------------------------------------------------------


class Client:
    """
    Represents a client that sends requests to a server.
    """

    def __init__(self, server: Server):
        # Dependency Injection: server is provided externally
        self.server = server

    def send_request(self, request: str):
        print(f"[Client] Sending request: {request}")

        response = self.server.process_request(request)

        print(f"[Client] Received response: {response}")


# -----------------------------------------------------------------------------
# Usage Example
# -----------------------------------------------------------------------------


def main():
    server = Server()
    client = Client(server)

    client.send_request("Get user profile")
    client.send_request("Fetch orders")
    client.send_request("Update settings")


if __name__ == "__main__":
    main()
