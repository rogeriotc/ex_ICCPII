#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 18:33:36 2020

@author: rogerio
"""

import tipo_triangulo


class Testtriangulo:

    def teste1(self):
        tri = tipo_triangulo.Triangulo(1, 1, 1)
        assert tri.perimetro() == 3
#        assert tri.tipo_lado() == 'equilatero'
#        print(tri.tipo_lado())
    