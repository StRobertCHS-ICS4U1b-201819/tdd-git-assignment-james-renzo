import pytest
from statTools import *

def test_variance_basic1():
    assert(mean([3*2+4*2+5*2+6*2+7*2]))

def test_range_basic0():
    assert(range([9, 4, 6, 7, 8]) == 9)

def test_range_basic1():
    assert(range([0]) == 0)

def test_range_basic_large3():
    assert(range([80, 90, 100, 190]) == 190)

