from unittest import TestCase

import numpy as np

from mymodule.tools import something_numpy, something_scipy


class MyModuleTest(TestCase):

    def test_numpy(self):
        a = something_numpy()
        b = np.ones(3) * 4
        self.assertTrue(np.all(a == b))

    def test_scipy(self):
        v = something_scipy()
        self.assertEqual(v, 2)
