from typing import Dict, List, Union
from typing_extensions import NotRequired, TypedDict

# Define a single form error
class FormError(TypedDict):
  code: str  # Error code as a string
  message: str  # Error message as a string

# Wrapper for a list of form errors
class FormErrorWrapper(TypedDict):
  _errors: List[FormError]

# Recursive type for nested form errors
FormErrors = Union[FormErrorWrapper, Dict[str, "FormErrors"]]

# General error type with optional nested form errors
class Error(TypedDict):
  code: int  # HTTP or general error code
  message: str  # Human-readable error message
  errors: NotRequired[FormErrors]  # Optional nested form errors

# Base class for handling errors
class BaseError:
  status: int = 0  # Default status code
