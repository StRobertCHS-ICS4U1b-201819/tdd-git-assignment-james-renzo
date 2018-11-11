import pytest
from statTools import *

def test_mean_basic():
    assert(mean([1, 2, 3, 4, 5]) == 3)

def test_mean_zero():
    assert(mean([0]) == 0)

def test_mean_longAndLarge():
    assert(mean([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 55)

def test_mean_decimal():
    assert(mean([1.5, 1.2, 3.4, 5.6]) == 2.92)

def test_mean_illegal():
    assert(mean("Illegal Input") == "Illegal parameter, please input a number")

def test_median_basic():
    assert(median([1,2,3,4,5]) == 3)

def test_median_evenNumList():
    assert(median([1,2,3,4]) == 2)

def test_median_unSorted():
    assert(median([1,5,2,4,3]) == 3)

def test_median_zero():
    assert(median([0]) == 0)

def test_median_decimalAndLong():
    assert(median([3.1,3.2,3.3,3.4,3.6,3.7,3.8,3.9,4.0]) == 3.6)

def test_median_illegal():
    assert(mean("Illegal Input") == "Illegal parameter, please input a number")

def test_mode_basic():
    assert(mode([1,2,2,3,4]) == 2)

def test_mode_basic2():
    assert(mode([3,1,4,4,7])== 4)

def test_mode_zero():
    assert(mode([0]) == 0)

def test_mode_multiMode():
    assert(mode([0,1,1,2,2,3,4,5]) == 1)

def test_mode_decimalAndLong():
    assert(mode([0.1,0.2,0.3,0.5,0.8,0.4,1.1,1.1,2.3,3.4,5.5,1.1]) == 1.1)

def test_mode_illegal():
    assert(mode("Illegal Input") == "Illegal parameter, please input a number")

def test_range_basic():
    assert(range([1,2,3,4,5]) == 4)

def test_range_basic2():
    assert(range([2,3,4,5,7]) == 5)

def test_range_illegal():
    assert(range("Illegal Input") == "Illegal parameter, please input a number")

def test_range_decimal():
    assert(range([1.2,1.3,1.1,1.4,1.5,1.6]) == 0.5)

def test_range_zero():
    assert(range([0]) == 0)

