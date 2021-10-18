"""
This code creates a datetime.time object from a string.

- Is it easy to verify that it works correctly?
- Do you see any obvious errors?
- How would you modify it to be easier to read?
"""

import datetime

def create_time_from_timestamp(timestamp: str) -> datetime.time:
    """Create a datetime.time object from a string in the form 'hh:mm:ss'.

    Args:
    timestamp - string containing a timestamp in the format 'hh:mm:ss'

    Returns:
    a datetime.time object with value equal to the timestamp

    Raises:
    ValueError if timestamp is not a string in form "hh:mm:ss"

    Example:
    >>> t = create_time_from_timestamp("9:23:15")
    >>> type(t)
    <class 'datetime.time'>
    >>> print(t)
    09:23:15
    """
    args = timestamp.split(":")
    if len(args) != 3:
        raise ValueError('Timestamp must be "hh:mm:ss"')
    (hours, minutes, seconds) = args
    # if the timestamp is not valid, this may raise TypeError or ValueError
    if is_valid_time(hours, minutes, seconds):
        return datetime.time(int(hours), int(minutes), int(seconds))
    # otherwise the timestamp is invalid
    return ValueError('Timestamp must be "hh:mm:ss"')


def is_valid_time(hours, minutes, seconds):
    """Verify the timestamp components are a valid time.

    Raises:
        ValueError if hours, minutes, seconds not contains correct values.
    """
    return 0 <= int(hours) <= 23 and 0 <= int(minutes) < 60 and 0 <= int(seconds) < 60
