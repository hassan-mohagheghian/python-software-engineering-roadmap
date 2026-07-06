# Design Patterns - Proxy Pattern
# -----------------------------------------------------------------------------
# The Proxy Pattern provides a surrogate (placeholder) for another object
# to control access to it.
#
# It sits between the client and the real object.
#
# -----------------------------------------------------------------------------
# When to use:
#
# - Lazy loading (create expensive objects only when needed)
# - Access control (security checks)
# - Caching
# - Logging / monitoring
# - Rate limiting
#
# -----------------------------------------------------------------------------
# Structure:
#
# Client → Proxy → Real Object
#
# -----------------------------------------------------------------------------

import time

# -----------------------------------------------------------------------------
# Real Object (Expensive Service)
# -----------------------------------------------------------------------------


class RealImage:
    def __init__(self, filename: str):
        self.filename = filename
        self._load()

    def _load(self):
        print(f"[REAL] Loading {self.filename} from disk...")
        time.sleep(2)

    def display(self):
        print(f"[REAL] Displaying {self.filename}")


# -----------------------------------------------------------------------------
# Proxy Object
# -----------------------------------------------------------------------------


class ImageProxy:
    def __init__(self, filename: str):
        self.filename = filename
        self._real_image = None

    def display(self):
        if self._real_image is None:
            print("[PROXY] Lazy loading RealImage...")
            self._real_image = RealImage(self.filename)
        else:
            print("[PROXY] Using cached image")

        self._real_image.display()


# -----------------------------------------------------------------------------
# EXTRA EXAMPLES (Real-world proxy use cases)
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# 1. Access Control Proxy
# -----------------------------------------------------------------------------


class SecureService:
    def access_data(self):
        print("[REAL SERVICE] Sensitive data accessed")


class SecureProxy:
    def __init__(self, user_role: str):
        self.user_role = user_role
        self._service = SecureService()

    def access_data(self):
        if self.user_role != "admin":
            print("[PROXY] Access denied: insufficient permissions")
            return

        print("[PROXY] Access granted")
        self._service.access_data()


# -----------------------------------------------------------------------------
# 2. Caching Proxy
# -----------------------------------------------------------------------------


class ExpensiveAPI:
    def fetch(self, key: str):
        print(f"[REAL API] Fetching data for {key}...")
        time.sleep(1)
        return {"data": f"value_for_{key}"}


class CachedAPIProxy:
    def __init__(self):
        self._api = ExpensiveAPI()
        self._cache = {}

    def fetch(self, key: str):
        if key in self._cache:
            print("[PROXY] Cache hit")
            return self._cache[key]

        print("[PROXY] Cache miss")
        result = self._api.fetch(key)
        self._cache[key] = result
        return result


# -----------------------------------------------------------------------------
# MAIN DEMO
# -----------------------------------------------------------------------------


def main():
    print("\n===== IMAGE PROXY =====")
    img = ImageProxy("cat.png")
    img.display()
    img.display()

    print("\n===== ACCESS CONTROL PROXY =====")
    admin = SecureProxy("admin")
    user = SecureProxy("guest")

    admin.access_data()
    user.access_data()

    print("\n===== CACHE PROXY =====")
    api = CachedAPIProxy()

    print(api.fetch("user_1"))
    print(api.fetch("user_1"))  # cached


if __name__ == "__main__":
    main()
