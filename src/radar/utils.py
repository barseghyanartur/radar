__title__ = 'radar.utils'
__version__ = '0.3'
__build__ = 0x000003
__author__ = 'Artur Barseghyan'
__all__ = ('parse', 'gettext')

import datetime

from radar.exceptions import UnrecognisedDateFormat
from radar.defaults import FORMATS

gettext = lambda s: s

def parse(timestamp, formats=None):
    """
    Parse the given datetime according to the format given.

    :param str timestamp:
    :param list formats: List of formats.
    :return datetime.datetime:

    :example:
    >>> [("%Y-%m-%dT%H:%M:%S", True), ("%Y-%m-%d", False)]
    """
    if formats is None:
        formats = FORMATS
    else:
        assert isinstance(formats, list)

    for date_format, is_datetime in formats:
        try:
            dt = datetime.datetime.strptime(timestamp, date_format)
            if is_datetime:
                return dt
            else:
                return dt.date()
        except:
            pass

    raise UnrecognisedDateFormat(gettext("Unrecognised date format"))
