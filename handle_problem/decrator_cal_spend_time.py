# coding: utf-8

"""
    handle_problem.decrator_cal_spend_time
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Use for calculate fun spend time
"""

import time
import functools


def cal_spend_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        s_time = time.time()
        res = func(*args, **kwargs)
        e_time = time.time()
        # log: e_time - s_time
        print e_time - s_time
        return res

    return wrapper


@cal_spend_time
def test():
    for i in range(10):
        pass

if __name__ == '__main__':
    test()
