# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 17:16:11 2024

@author: zmzhang
"""

import numpy as np
from scipy import signal

def boxcar(x, window_size):
    window = signal.boxcar(window_size)/window_size
    xs = signal.convolve(x, window, mode='same')
    return xs

def savgol_coef(hws,p,d):
    m = np.arange(-hws,hws+1)
    M = np.ones((m.shape[0],1))
    for i in range(p):
        M=np.c_[M,m**(i+1)]
    H=np.dot(np.linalg.inv(np.dot(M.T,M)),M.T)
    c=np.zeros((1,p+1))
    c[0,d]=np.prod(np.arange(1,d+1))
    return np.dot(c,H)