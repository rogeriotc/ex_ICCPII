#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 17:50:39 2020

@author: rogerio

Na classe triângulo, definida na Questão 1, escreva o metodo tipo_lado() que
 devolve uma string dizendo se o triângulo é:

isósceles (dois lados iguais)

equilátero (todos os lados iguais)

escaleno (todos os lados diferentes)

Note que se o triângulo for equilátero, a função não deve devolver isóceles.
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
            tipo_l = 'equilátero'
        elif self.a == self.b or self.a == self.c \
            or self.b == self.c:
            tipo_l = 'isósceles'
        return tipo_l


# if __name__ == '__main__':
#     t = Triangulo(3, 3, 3)
#     tt = Triangulo(3, 4, 4)
#     u = Triangulo(3, 4, 5)
#     print(t.perimetro())
#     print(t.tipo_lado())
#     print(tt.perimetro())
#     print(tt.tipo_lado())
#     print(u.perimetro())
#     print(u.tipo_lado())
