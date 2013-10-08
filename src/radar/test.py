from __future__ import print_function

__title__ = 'radar.tests'
__version__ = '0.3'
__build__ = 0x000003
__author__ = 'Artur Barseghyan'
__all__ = ('RadarTest',)

import unittest
import datetime

import radar

PRINT_INFO = True
TRACK_TIME = False

def print_info(func):
    """
    Prints some useful info.
    """
    if not PRINT_INFO:
        return func

    def inner(self, *args, **kwargs):
        if TRACK_TIME:
            import simple_timer
            timer = simple_timer.Timer() # Start timer

        result = func(self, *args, **kwargs)

        if TRACK_TIME:
            timer.stop() # Stop timer

        print('\n{0}'.format(func.__name__))
        print('============================')
        print('""" {0} """'.format(func.__doc__.strip()))
        print('----------------------------')
        if result is not None:
            try:
                print(result)
            except Exception as e:
                print(result.encode('utf8'))

        if TRACK_TIME:
            print('done in {0} seconds'.format(timer.duration))

        return result
    return inner


def py2only(func):
    """
    Skips the test on Python 3.
    """
    if PY2:
        return func

    def dummy(self, *args, **kwargs):
        pass

    return dummy


class RadarTest(unittest.TestCase):
    """
    Tests of ``radar.utils``.
    """
    def setUp(self):
        pass

    @print_info
    def test_01_random_datetime(self):
        """
        Test ``radar.random_datetime``.
        """
        res = radar.random_datetime()
        self.assertTrue(isinstance(res, datetime.datetime))
        return res

    @print_info
    def test_02_random_date(self):
        """
        Test ``radar.random_datetime``.
        """
        res = radar.random_date()
        self.assertTrue(isinstance(res, datetime.date))
        return res

    @print_info
    def test_03_random_datetime_with_ranges_given(self):
        """
        Test ``radar.random_datetime`` with ranges given.
        """
        start = datetime.datetime(year=2000, month=5, day=24)
        stop = datetime.datetime(year=2013, month=5, day=24)

        res = radar.random_datetime(start=start, stop=stop)
        self.assertTrue(isinstance(res, datetime.datetime))
        self.assertTrue(res > start)
        self.assertTrue(res < stop)
        return res

    @print_info
    def test_04_random_date_with_ranges_given(self):
        """
        Test ``radar.random_date`` with ranges given.
        """
        start = datetime.date(year=2000, month=5, day=24)
        stop = datetime.date(year=2013, month=5, day=24)

        res = radar.random_date(start=start, stop=stop)
        self.assertTrue(isinstance(res, datetime.date))
        self.assertTrue(res > start)
        self.assertTrue(res < stop)
        return res

    @print_info
    def test_05_random_datetime_with_string_ranges_given(self):
        """
        Test ``radar.random_datetime`` with string ranges given.
        """
        start = '2012-05-24T00:00:00'
        stop='2013-05-24T23:59:59'

        dt_start = datetime.datetime(year=2012, month=5, day=24, hour=0, minute=0, second=0)
        dt_stop = datetime.datetime(year=2013, month=5, day=24, hour=23, minute=59, second=59)

        res = radar.random_datetime(start=start, stop=stop)
        self.assertTrue(isinstance(res, datetime.datetime))
        self.assertTrue(res > dt_start)
        self.assertTrue(res < dt_stop)
        return res

    @print_info
    def test_06_random_date_with_string_ranges_given(self):
        """
        Test ``radar.random_date`` with string ranges given.
        """
        start = '2012-05-24'
        stop='2013-05-24'

        dt_start = datetime.date(year=2012, month=5, day=24)
        dt_stop = datetime.date(year=2013, month=5, day=24)

        res = radar.random_date(start=start, stop=stop)
        self.assertTrue(isinstance(res, datetime.date))
        self.assertTrue(res > dt_start)
        self.assertTrue(res < dt_stop)
        return res

if __name__ == '__main__':
    unittest.main()
