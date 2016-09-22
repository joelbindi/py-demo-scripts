"""Locate maximum value."""

import numpy as np
import time
from decimal import *


def get_max_index(a):
    """Return the index of the maximum value in given 1D array."""
    # TODO: Your code here


def test_run():
    # a = np.array([9, 6, 2, 3, 12, 14, 7, 10], dtype=np.int32)  # 32-bit integer array
    t1 = time.time()
    print 'MLT'
    # Find the maximum and its index in array
    # print a.max()
    t2 = time.time()
    print t2
    tInt = float(t2 - t1)
    tInt = round(tInt,8)
    print 'the time taken is', tInt, 'seconds'
 
if __name__ == "__main__":
    test_run()
