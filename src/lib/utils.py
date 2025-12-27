"""
Utility functions for the Todo CLI application.
"""
import logging
import sys
from typing import Any, Callable


def setup_logging(level: int = logging.INFO) -> None:
    """
    Set up basic logging configuration.
    
    Args:
        level: Logging level (default: INFO)
    """
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )


def handle_error(error: Exception, message: str = "An error occurred") -> None:
    """
    Handle an error by logging it and exiting with a non-zero code.
    
    Args:
        error: The exception that occurred
        message: Custom error message to display
    """
    logging.error(f"{message}: {str(error)}")
    print(f"Error: {message}: {str(error)}", file=sys.stderr)
    sys.exit(1)


def validate_task_id(task_id: int) -> bool:
    """
    Validate that a task ID is a positive integer.
    
    Args:
        task_id: The ID to validate
        
    Returns:
        bool: True if valid, raises ValueError if invalid
    """
    if not isinstance(task_id, int) or task_id <= 0:
        raise ValueError(f"Task ID must be a positive integer, got: {task_id}")
    return True


def safe_execute(func: Callable, *args, **kwargs) -> Any:
    """
    Safely execute a function, catching and handling any exceptions.
    
    Args:
        func: The function to execute
        *args: Arguments to pass to the function
        **kwargs: Keyword arguments to pass to the function
        
    Returns:
        The result of the function execution
    """
    try:
        return func(*args, **kwargs)
    except Exception as e:
        handle_error(e)