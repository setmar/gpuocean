import unittest
import time
import numpy as np
import sys
import gc
import pycuda.driver as cuda

from testUtils import *

from gpuocean.utils import Common
from stochastic.RandomNumbers_test import RandomNumbersTest


class RandomNumbersLCGTest(RandomNumbersTest):
    """
    Executing all the same tests as RandomNumbersTest, but
    using the LCG algorithm for random numbers.
    """
        
    def useLCG(self):
        return True