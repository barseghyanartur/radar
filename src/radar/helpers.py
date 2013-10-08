__title__ = 'radar.helpers'
__version__ = '0.3'
__build__ = 0x000003
__author__ = 'Artur Barseghyan'
__all__ = ('PY2', 'PY3', 'PYLE26', 'total_seconds')

import sys

PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3

PYLE26 = False # Python version is less or equal to 2.6

if PY2:
    try:
        MINOR = sys.version_info[1]
    except:
        MINOR = None

    if MINOR < 7:
        PYLE26 = True

# For Python versions less or equal to 2.6.
total_seconds = lambda td: (td.microseconds + (td.seconds + td.days * 24 * 3600) * 1e6) / 1e6