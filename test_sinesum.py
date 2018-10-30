#!/usr/bin/env python3

"""sinesum.py Test Module

Verify implementation of the Fourier sine series using numpy arrays.
"""

import math
import sinesum
import numpy as np

def test_s():
    """Test to ensure that the s function in sinesum is correct"""
    assert 0.67< sinesum.s(0.01*2*np.pi, 10)< 0.671
    
def test_f():
    """Test to ensure that the f function in sinesum is correct"""
    assert sinesum.f(0.01*2*np.pi)==1