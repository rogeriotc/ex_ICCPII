#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 18:56:04 2020

@author: rogerio

Escreva, na classe Triangulo, o método retangulo() que devolve True se o
 triângulo for retângulo, e False caso contrário.
"""


class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        perim = self.a + self.b + self.c
        return perim

    def tipo_lado(self):
        tipo_l = 'escaleno'
        if self.a == self.b and self.a == self.c:
            tipo_l = 'equilatero'
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            tipo_l = 'isosceles'
        return tipo_l

    def retangulo(self):
        e_retangulo = False
        if self.a**2 == self.b**2 + self.c**2 or self.b**2 == self.a**2 + \
           self.c**2 or self.c**2 == self.b**2 + self.a**2:
            e_retangulo = True
        return e_retangulo
