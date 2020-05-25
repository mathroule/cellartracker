"""Errors for CellarTracker."""


class AuthenticationError(Exception):
    """Wrong username or password."""


class CannotConnect(Exception):
    """Unable to connect to client."""
