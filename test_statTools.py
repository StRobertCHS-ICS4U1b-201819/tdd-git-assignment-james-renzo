import pytest
from statTools import *

def test_mean_basic():
    assert(mean([1,2,3,4,5]) == 3)

def test_mean_zero():
    assert(mean([0]) == 0)

def test_mean_longAndLarge():
    assert(mean([10,20,30,40,50,60,70,80,90,100]) == 55)

def test_mean_decimal():
    assert(mean([1.5,1.2,3.4,5.6]) == 2.92)

def test_mean_illegal():
    assert(mean("Illegal Input") == "None")
