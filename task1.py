from typing import Sequence
import random
import time
from functools import reduce

def my_func():
    """Function lambda.
    Take 2 numbers and raises a number to a power.
    """
    func = lambda a, x: a**x
    print(func(2, 7))