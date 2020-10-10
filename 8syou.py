import math

math.pow(2, 3)

import random

random.randint(0, 100)

import statistics

nums = [1, 5, 33, 12, 46, 33, 2]
statistics.mean(nums)

statistics.median(nums)

statistics.mode(nums)

import keyword

keyword.iskeyword("for")
keyword.iskeyword("football")


def print_hello():
    print_("Hello")


import hello

hello.print_hello()

# code in module1
print("Hello")

# code in module2
import module1

if __name__ == "__main__":
    print("Hello")

# code in module2
import hello
