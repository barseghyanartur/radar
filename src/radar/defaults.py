__title__ = 'radar.defaults'
__version__ = '0.3'
__build__ = 0x000003
__author__ = 'Artur Barseghyan'
__all__ = ('FORMATS', 'DATE_TIME_FORMATS', 'DATE_FORMATS', 'TIME_FORMATS')

DATE_TIME_FORMATS = (
    "%Y-%m-%dT%H:%M:%S",
)

DATE_FORMATS = (
    "%Y-%m-%d",
)

TIME_FORMATS = (
    "%H:%M:%S",
)

# Tuples given. True means that the value should be parsed into a ``datetime.datetime`` object. When False is given
# parsed into a ``datetime.date`` object.
FORMATS = (
    ("%Y-%m-%dT%H:%M:%S", True),
    ("%Y-%m-%d", False),
)
