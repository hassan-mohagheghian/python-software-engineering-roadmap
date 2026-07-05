# Design Patterns - Chain of Responsibility Pattern
# -----------------------------------------------------------------------------
# The Chain of Responsibility Pattern is a behavioral design pattern that lets
# you pass a request along a chain of handlers. Each handler decides either to
# process the request or to pass it to the next handler in the chain.
#
# It decouples the sender of a request from its receiver, giving multiple
# objects a chance to handle the request.
#
# -----------------------------------------------------------------------------
# When to use:
#
# - More than one object may handle a request, and the handler is unknown
#   beforehand.
# - You want to send a request to one of several objects without specifying
#   the receiver explicitly.
# - The set of handlers should be specified dynamically.
#
# -----------------------------------------------------------------------------
# Key Idea:
#
#   Client -> Handler A -> Handler B -> Handler C -> None
#
#   Each handler holds a reference to the next handler.
#   A handler either handles the request or forwards it.
#
# -----------------------------------------------------------------------------
# Benefits:
#
# - Reduces coupling between sender and receiver.
# - Handlers can be added, removed, or reordered easily.
# - Follows Single Responsibility Principle (SRP).
# - Follows Open/Closed Principle (OCP).
#
# -----------------------------------------------------------------------------
# Example:
#
# A support ticket system where requests are escalated based on severity:
#   - BasicSupport handles low-severity issues.
#   - AdvancedSupport handles medium-severity issues.
#   - ManagerSupport handles high-severity issues.
#   - DirectorSupport handles critical issues.
# -----------------------------------------------------------------------------

from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import IntEnum


# -----------------------------------------------------------------------------
# Request
# -----------------------------------------------------------------------------


class Severity(IntEnum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4


@dataclass
class SupportRequest:
    description: str
    severity: Severity


# -----------------------------------------------------------------------------
# Handler (Abstract)
# -----------------------------------------------------------------------------


class SupportHandler(ABC):
    def __init__(self):
        self._next: SupportHandler | None = None

    def set_next(self, handler: "SupportHandler") -> "SupportHandler":
        self._next = handler
        return handler

    def handle(self, request: SupportRequest):
        if self._can_handle(request):
            self._process(request)
        elif self._next:
            print(f"  [{self.__class__.__name__}] Passing to next handler...")
            self._next.handle(request)
        else:
            print(f"  No handler found for: {request.description}")

    @abstractmethod
    def _can_handle(self, request: SupportRequest) -> bool:
        pass

    @abstractmethod
    def _process(self, request: SupportRequest):
        pass


# -----------------------------------------------------------------------------
# Concrete Handlers
# -----------------------------------------------------------------------------


class BasicSupport(SupportHandler):
    def _can_handle(self, request: SupportRequest) -> bool:
        return request.severity <= Severity.LOW

    def _process(self, request: SupportRequest):
        print(f"  [BasicSupport] Handled: {request.description}")


class AdvancedSupport(SupportHandler):
    def _can_handle(self, request: SupportRequest) -> bool:
        return request.severity <= Severity.MEDIUM

    def _process(self, request: SupportRequest):
        print(f"  [AdvancedSupport] Handled: {request.description}")


class ManagerSupport(SupportHandler):
    def _can_handle(self, request: SupportRequest) -> bool:
        return request.severity <= Severity.HIGH

    def _process(self, request: SupportRequest):
        print(f"  [ManagerSupport] Handled: {request.description}")


class DirectorSupport(SupportHandler):
    def _can_handle(self, request: SupportRequest) -> bool:
        return request.severity <= Severity.CRITICAL

    def _process(self, request: SupportRequest):
        print(f"  [DirectorSupport] Handled: {request.description}")


# -----------------------------------------------------------------------------
# Client
# -----------------------------------------------------------------------------


def create_support_chain() -> SupportHandler:
    basic = BasicSupport()
    advanced = AdvancedSupport()
    manager = ManagerSupport()
    director = DirectorSupport()

    basic.set_next(advanced).set_next(manager).set_next(director)
    return basic


# -----------------------------------------------------------------------------
# Usage
# -----------------------------------------------------------------------------


def main():
    chain = create_support_chain()

    requests = [
        SupportRequest("Password reset", Severity.LOW),
        SupportRequest("Software bug report", Severity.MEDIUM),
        SupportRequest("Server outage", Severity.HIGH),
        SupportRequest("Data breach", Severity.CRITICAL),
    ]

    for request in requests:
        print(f"\nRequest: {request.description} (severity: {request.severity.name})")
        chain.handle(request)


if __name__ == "__main__":
    main()
