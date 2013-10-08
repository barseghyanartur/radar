__title__ = 'radar.__init__'
__version__ = '0.3'
__build__ = 0x000003
__author__ = 'Artur Barseghyan'
__all__ = ('random_datetime', 'random_date', 'random_time')

import datetime
from random import randint

try:
    from dateutil.parser import parse
except:
    from radar.utils import parse

from radar.helpers import PYLE26, total_seconds
from radar.utils import gettext as _
from radar.exceptions import InvalidDateRange

def random_datetime(start=None, stop=None, parse=parse):
    """
    Generates a random ``datetime.datetime`` or ``datetime.date`` object from ranges given.

    :param mixed start: Can be either a ``datetime.datetime``, ``datetime.date`` or a ``str``. Defaults to 1970-01-01.
    :param mixed end: Can be either a ``datetime.datetime``, ``datetime.date`` or a ``str``. Defaults to
        ``datetime.datetime.now``.
    :param func parse: Parser function used to parse the date formats when ``start`` or ``stop`` arguments are strings.
    :return datetime.datetime:
    """
    if start is not None:
        assert isinstance(start, (datetime.datetime, datetime.date, str))
        if isinstance(start, str):
            start = parse(start)
    else:
        start = datetime.datetime(year=1979, month=1, day=1)

    if stop is not None:
        assert isinstance(stop, (datetime.datetime, datetime.date, str))

        if isinstance(stop, str):
            stop = parse(stop)
    else:
        stop = datetime.datetime.now()

    if start > stop:
        raise InvalidDateRange(_("Invalid date range: ``start`` should not be greater than ``stop``."))

    if PYLE26:
        random_datetime = start + datetime.timedelta(seconds=randint(0, int(total_seconds(stop - start))))
    else:
        random_datetime = start + datetime.timedelta(seconds=randint(0, int((stop - start).total_seconds())))

    return random_datetime

def random_date(start=None, stop=None, parse=parse):
    """
    Generates a random ``datetime.date`` object from ranges given.

    :param mixed start: Can be either a ``datetime.datetime``, ``datetime.date`` or a ``str``. Defaults to 1970-01-01.
    :param mixed end: Can be either a ``datetime.datetime``, ``datetime.date`` or a ``str``. Defaults to
        ``datetime.datetime.now``.
    :param func parse: Parser function used to parse the date formats when ``start`` or ``stop`` arguments are strings.
    :return datetime.date:
    """
    if start is None:
        start = datetime.date(year=1979, month=1, day=1)
    if stop is None:
        stop = datetime.date.today()

    d = random_datetime(start=start, stop=stop, parse=parse)
    return d

def random_time(start=None, stop=None, parse=parse):
    """
    Generates a random ``datetime.time`` object from ranges given.

    :param mixed start: Can be either a ``datetime.datetime``, ``datetime.date`` or a ``str``. Defaults to 1970-01-01.
    :param mixed end: Can be either a ``datetime.datetime``, ``datetime.date`` or a ``str``. Defaults to
        ``datetime.datetime.now``.
    :param func parse: Parser function used to parse the date formats when ``start`` or ``stop`` arguments are strings.
    :return datetime.time:
    """
    d = random_datetime(start=start, stop=stop, parse=parse)
    return d.time()
