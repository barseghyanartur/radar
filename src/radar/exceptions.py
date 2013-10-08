__title__ = 'radar.exceptions'
__version__ = '0.3'
__build__ = 0x000003
__author__ = 'Artur Barseghyan'
__all__ = ('UnrecognisedDateFormat', 'InvalidDateRange')

class UnrecognisedDateFormat(ValueError):
    """
    Unrecognised date format.
    """
    pass

class InvalidDateRange(ValueError):
    """
    Invalid date range.
    """
    pass
