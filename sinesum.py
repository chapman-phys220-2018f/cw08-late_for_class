#!/usr/bin/env python3

import numpy as np

def sinesum(t=.01*2*np.pi, n=1, T = 2*np.pi):

    kmin = 1
    kmax = n
    dk = 1

    k = np.arange(kmin, kmax + dk, dk)
    gk = ((4/np.pi) * (((1 / 2*k-1) * np.sin(2*(2*k-1)*np.pi*t / T))))
    sum_gk = np.trapz(gk, k, dk)
    return sum_gk