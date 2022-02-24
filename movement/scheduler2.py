import sched
import time

s = sched.scheduler(time.time, time.sleep)
mult = 1


def activity_1(a='default'):
    print("activity_1", mult * round(time.time() - start, 2), a)


def activity_1_end(a='default'):
    print("activity_1_end", mult * round(time.time() - start, 2), a)


def activity_2(a='default'):
    print("activity_2", mult * round(time.time() - start, 2), a)


def activity_2_end(a='default'):
    print("activity_2_end", mult * round(time.time() - start, 2), a)


def activity_3(a='default'):
    print("activity_3", mult * round(time.time() - start, 2), a)


def activity_3_end(a='default'):
    print("activity_3_end", mult * round(time.time() - start, 2), a)


def print_some_times():
    print("start: ", round(time.time() - start, 2), " wall clock secs")
    # add activities to queue: time (sim clock secs), priority, name,
    #   arguments (positional or named)
    print("activity  time started(secs)  result")
    s.enter(2 / mult, 2, activity_1, argument=('positional',))
    s.enter(12 / mult, 1, activity_1_end, argument=('end',))
    s.enter(5 / mult, 3, activity_2, argument=('positional',))
    s.enter(7 / mult, 1, activity_2_end, argument=('end',))
    s.enter(5 / mult, 2, activity_3, argument=('positional',))
    s.enter(6 / mult, 2, activity_3_end, argument=('end',))
    s.run()
    s.run()
    s.enter(8 / mult, 1, activity_1_end,argument=('end',))
    s.run()
    print("finished: ", round(time.time() - start, 2), " wall clock secs")


start = time.time()
print("Mult: ", mult)
print_some_times()
