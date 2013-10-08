import argparse
import simple_timer
import humanize
from dateutil.parser import parse as dateuitil_parser
import radar

times_generate = 100000

_ = lambda s: s

def test_dateutils_parser(times_generate):
    # Using dateutil parser
    print "Using dateutil parser\n=====================\n"

    timer = simple_timer.Timer()

    for i in xrange(times_generate):
        radar.random_datetime(start='2000-05-24T00:00:00', stop='2013-05-24T23:59:59', parse=dateuitil_parser)

    timer.stop()

    print "%s seconds elapsed" % timer.duration
    print "making it %s of objects generated per second\n" % humanize.intword(times_generate / timer.duration)


def test_radar_parser(times_generate):
    # Using radar parser
    print "Using radar parser\n=====================\n"

    timer = simple_timer.Timer()

    for i in xrange(times_generate):
        radar.random_datetime(start='2000-05-24T00:00:00', stop='2013-05-24T23:59:59', parse=radar.utils.parse)

    timer.stop()

    print "%s seconds elapsed" % timer.duration
    print "making it %s of objects generated per second\n" % humanize.intword(times_generate / timer.duration)


def test_parsed_dates(times_generate):
    # Using parsed dates
    print "Using parsed dates\n=====================\n"

    timer = simple_timer.Timer()

    start = radar.utils.parse('2000-05-24T00:00:00')
    stop = radar.utils.parse('2013-05-24T23:59:59')

    for i in xrange(times_generate):
        radar.random_datetime(start=start, stop=stop)
        #radar.random_datetime(start='2000-05-24T00:00:00', stop='2013-05-24T23:59:59')

    timer.stop()

    print "%s seconds elapsed" % timer.duration
    print "making it %s of objects generated per second\n" % humanize.intword(times_generate / timer.duration)


tests = (
    (test_dateutils_parser, _("Using dateutil parser")),
    (test_radar_parser, _("Using radar parser")),
    (test_parsed_dates, _("Using parsed dates"))
)


def choice(tests):
    test_choice = raw_input(_("Your choice: "))
    if test_choice in ('\q', '\quit'):
        return

    try:
        func = tests[int(test_choice)][0]
    except:
        print "Invalid choice %s. Please try again." % test_choice
        return choice(tests)

    print
    func(times_generate)

    choice(tests)


def main():
    parser = argparse.ArgumentParser(description="""
    Start the test.
    """)
    print "\nGenerate %s objects using... make your choice:\n" % humanize.intword(times_generate)
    for i, item in enumerate(tests):
        print "    (%s) %s" % (i, item[1])
    print """
    Type \\q to quit any time.
    """
    choice(tests)

if __name__ == "__main__":
    main()
