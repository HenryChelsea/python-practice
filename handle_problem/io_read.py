# coding: utf-8

"""
    handle_problem.io_read
    ~~~~~~~~~~~~~~~~~~~~~~

    test python io read.
"""
import itertools
from memory_profiler import profile
import time
import functools

FILE_PATH = 'word.txt'


def cal_spend_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        s_time = time.time()
        res = func(*args, **kwargs)
        e_time = time.time()
        print 'cpu cost time:( seconds )', e_time - s_time
        return res
    return wrapper


@cal_spend_time
@profile
def test1():
    """
    Line #    Mem usage    Increment   Line Contents
    ================================================
    28     20.8 MiB      0.0 MiB   @cal_spend_time
    29                             @profile
    30                             def test1():
    31     20.8 MiB      0.0 MiB       with open(FILE_PATH, 'rb') as f:
    32     20.8 MiB      0.0 MiB           for i in itertools.count():
    33     20.8 MiB      0.0 MiB               record = f.read(16)
    34     20.8 MiB      0.0 MiB               if not record:
    35     20.8 MiB      0.0 MiB                   break
    36     20.8 MiB      0.0 MiB           print "... test1 ", i


    cpu cost time:  2.93790197372
    :return:
    """
    with open(FILE_PATH, 'rb') as f:
        for i in itertools.count():
            record = f.read(16)
            if not record:
                break
        print "... test1 ", i



if __name__ == '__main__':
    test1()

