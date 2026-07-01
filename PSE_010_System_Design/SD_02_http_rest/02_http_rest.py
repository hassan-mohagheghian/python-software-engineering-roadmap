# System Design - HTTP & REST Basics
# -----------------------------------------------------------------------------
# HTTP (HyperText Transfer Protocol) is the foundation protocol of the web.
#
# It defines how clients (browsers, mobile apps, services) communicate with
# servers using a request-response model.
#
# REST (Representational State Transfer) is an architectural style built on top
# of HTTP that defines how APIs should be designed.
#
# -----------------------------------------------------------------------------
# Core Idea:
#
# Client (HTTP Request) → Server → Process → HTTP Response → Client
#
# -----------------------------------------------------------------------------
# HTTP Characteristics:
#
# 1. Stateless
#    - Each request is independent
#    - Server does not store client state between requests
#
# 2. Request-Response Model
#    - Client sends request
#    - Server returns response
#
# 3. Uses methods (verbs)
#    - GET    → read data
#    - POST   → create data
#    - PUT    → update/replace data
#    - PATCH  → partial update
#    - DELETE → remove data
#
# 4. Uses status codes
#    - 2xx → success
#    - 4xx → client error
#    - 5xx → server error
#
# -----------------------------------------------------------------------------
# REST Principles:
#
# 1. Resource-based
#    - Everything is a resource (users, orders, products)
#
# 2. Stateless communication
#    - No session stored on server
#
# 3. Uniform interface
#    - Standard HTTP methods are used consistently
#
# 4. Representation of resources
#    - JSON is commonly used
#
# Example:
#
# GET /users/1 → fetch user
# POST /users   → create user
#
# -----------------------------------------------------------------------------
# Real-world examples:
#
# - Web APIs (FastAPI, Django REST Framework)
# - Mobile app backends
# - Microservices communication
# - Public APIs (Stripe, GitHub API, Twitter API)
# -----------------------------------------------------------------------------

import json

# -----------------------------------------------------------------------------
# Simple HTTP Server Simulation
# -----------------------------------------------------------------------------


class HttpRequest:
    def __init__(self, method: str, path: str, body=None):
        self.method = method
        self.path = path
        self.body = body


class HttpResponse:
    def __init__(self, status_code: int, data=None):
        self.status_code = status_code
        self.data = data

    def to_json(self):
        return json.dumps({"status_code": self.status_code, "data": self.data})


# -----------------------------------------------------------------------------
# Server (REST-like API)
# -----------------------------------------------------------------------------


class UserService:
    """
    Simulates a REST API backend for users.
    """

    def __init__(self):
        self.users = {1: {"id": 1, "name": "Alice"}, 2: {"id": 2, "name": "Bob"}}

    def handle_request(self, request: HttpRequest) -> HttpResponse:
        """
        Very simplified HTTP routing logic.
        """

        # GET /users/1
        if request.method == "GET" and request.path.startswith("/users/"):
            user_id = int(request.path.split("/")[-1])
            user = self.users.get(user_id)

            if user:
                return HttpResponse(200, user)
            return HttpResponse(404, {"error": "User not found"})

        # POST /users
        if request.method == "POST" and request.path == "/users":
            new_id = max(self.users.keys()) + 1
            self.users[new_id] = {"id": new_id, "name": request.body.get("name")}
            return HttpResponse(201, self.users[new_id])

        return HttpResponse(400, {"error": "Bad request"})


# -----------------------------------------------------------------------------
# Client Simulation
# -----------------------------------------------------------------------------


class ApiClient:
    """
    Simulates a client calling HTTP REST APIs.
    """

    def __init__(self, server: UserService):
        self.server = server

    def get_user(self, user_id: int):
        request = HttpRequest("GET", f"/users/{user_id}")
        response = self.server.handle_request(request)
        print("GET Response:", response.to_json())

    def create_user(self, name: str):
        request = HttpRequest("POST", "/users", body={"name": name})
        response = self.server.handle_request(request)
        print("POST Response:", response.to_json())


# -----------------------------------------------------------------------------
# Usage Example
# -----------------------------------------------------------------------------


def main():
    server = UserService()
    client = ApiClient(server)

    client.get_user(1)
    client.get_user(99)

    client.create_user("Charlie")


if __name__ == "__main__":
    main()
