"""Alias generators for converting between different capitalization conventions."""
import re

__all__ = ('to_pascal', 'to_camel')


def to_pascal(snake: str) -> str:
    """Convert a snake_case string to PascalCase.

    Args:
        snake: The string to convert.

    Returns:
        The PascalCase string.
    """
    camel = snake.title()
    return re.sub('([0-9A-Za-z])_(?=[0-9A-Z])', lambda m: m.group(1), camel)


def to_camel(snake: str) -> str:
    """Convert a snake_case string to camelCase.

    Args:
        snake: The string to convert.

    Returns:
        The converted camelCase string.
    """
    camel = to_pascal(snake)
    return re.sub('(^_*[A-Z])', lambda m: m.group(1).lower(), camel)
