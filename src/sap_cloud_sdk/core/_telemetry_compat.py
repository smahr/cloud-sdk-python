"""Conditional telemetry imports for modules that use telemetry as optional dependency.

This module provides a centralized way to handle optional telemetry dependencies.
When telemetry packages are not installed, it provides no-op implementations.
"""

try:
    from sap_cloud_sdk.core.telemetry import Module, Operation, record_metrics
    TELEMETRY_AVAILABLE = True
except ImportError:
    TELEMETRY_AVAILABLE = False
    # Provide no-op implementations when telemetry is not available
    Module = None  # type: ignore
    Operation = None  # type: ignore

    def record_metrics(*args, **kwargs):  # type: ignore
        """No-op decorator when telemetry is not available."""
        def decorator(func):
            return func
        if args and callable(args[0]):
            # Called without parentheses: @record_metrics
            return args[0]
        # Called with parentheses: @record_metrics(...)
        return decorator


__all__ = ["Module", "Operation", "record_metrics", "TELEMETRY_AVAILABLE"]
