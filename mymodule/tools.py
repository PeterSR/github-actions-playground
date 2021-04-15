from unittest import TestCase

import numpy as np
from scipy.interpolate import interp1d


def something_numpy():
    a = np.array([4, 4, 4])
    return a


def something_scipy():
    x = [1, 3]
    y = [1, 3]
    f = interp1d(x, y)
    v = f(2)
    return v
