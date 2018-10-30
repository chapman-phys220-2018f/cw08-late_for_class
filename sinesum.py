#!/usr/bin/env python3
# -*- coding: utf-8 -*-

<<<<<<< HEAD
###
# Name: Abby Wheaton and Frank Entriken
# Student ID: 2299246, 2298368
# Email: wheaton@chapman.edu, entriken@chapman.edu
# Course: PHYS220/MATH220/CPSC220 Fall 2018
# Assignment: CW07
###

import numpy as np

def s(t,n, T=2*np.pi):
    """
    The s function computes the fourier series expansion of the original function f
    
    Parameters:
    t = alpha*T (float)
    n = number of terms to evaluate (int)
    T = constant used in the Fourier Series Expansion (float)
    """
    k = np.arange(1, n)
    s = ((1/(2*k-1))*np.sin((2*(2*k-1)*np.pi*t)/ T))
    return ((4/np.pi)*np.sum(s))

def f(t, T=2*np.pi):
    """
    the f function is a piece-wise function with three distinct values
    
    Parameters:
    t = alpha*T (float)
    T = constant that t is compared to in order to produce an output (float)
    """
    if t==0:
        return(0)
    if 0<t<T/2:
        return(1)
    if -T/2<t<0:
        return (-1)
    
    

=======
import numpy as np

def sinesum(t=.01*2*np.pi, n=1, T = 2*np.pi):

    kmin = 1
    kmax = n
    dk = 1

    k = np.arange(kmin, kmax + dk, dk)
    gk = ((4/np.pi) * (((1 / 2*k-1) * np.sin(2*(2*k-1)*np.pi*t / T))))
    sum_gk = np.trapz(gk, k, dk)
    return sum_gk
>>>>>>> 2a803965bbb7ab424468ebf0b3e7615c93094899
