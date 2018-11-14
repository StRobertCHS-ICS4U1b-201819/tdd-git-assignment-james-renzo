import pytest
from statTools import *

def test_variance_basic1():
    assert(variance([3+4+5+6+7]))

def test_range_basic0():
    assert(range([9, 4, 6, 7, 8]) == 9)

def test_range_basic1():
    assert(range([0]) == 0)

def test_range_basic2():
    assert(range([9, 4, 2, 5, 10]) == 10)
    
def test_range_basic_large3():
    assert(range([80, 90, 100, 190]) == 190)

def test_deviance_basic0():
    assert(deviant([1, 4, 20, 9, 10]))
    
def test_deviance_basic1():
    assert(deviant([0]) == 0)
       
def test_deviance_large1():
    assert(deviant([100, 99, 64, 190, 435]))
    
def test_lowerQuartile_0():
    assert(lowQuartile([1, 2, 3, 4, 5, 6, 7]) == 2)
    
def test_lowerQuartile_illegal():
    assert(lowQuartile(["This is pie"]) == "error")
    
def test_lowerQuartile_1():
    assert(lowQuartile([0]) == 0)

def test_lowerQuartile_2():
    assert(lowQuartile([0, 1, 2, 3]) == 0.5)
    
def test_lowerQuartile_3():
    assert(lowQuartile([0, 6, 7, 10, 43, 54, 65, 67, 87, 89]) == 7)
    
def test_higherQuartile_0():
    assert(highQuartile([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == 0)
    
def test_higherQuartile_illegal():
    assert(highQuartile(["quarter"]) == "error")
