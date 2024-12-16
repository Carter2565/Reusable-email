"""
Reusable Email Package

This package provides tools for:
- Generating encryption keys.
- Encrypting and decrypting emails.
- Handling secure inbox operations.

Author: Carter2565
Version: 1.0.0
"""

__version__ = '0.1.0'

# Import key functions from submodules
from .crypto import generate_keys
from .inbox_manager import (
  Sync,
  Async
)


# Define the public API of the package
__all__ = [
  "generate_keys",
  "Sync",
  "Async"
  ]

