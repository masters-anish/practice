#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 10:15:28 2020

@author: anish
"""


import cProfile

def slow_function():
    total = 0.0
    ]=
    for i, _ in enumerate(range(10000)):
        
        for j, _ in enumerate(range(1, 10000)):
            total += (i * j)

    return total

cProfile.run('slow_function()', sort='time')

