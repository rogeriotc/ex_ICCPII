#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 18:36:37 2020

@author: rogerio
"""

def fatorial(n):
    if n <= 1:
        return 1
    return n*fatorial(n-1)