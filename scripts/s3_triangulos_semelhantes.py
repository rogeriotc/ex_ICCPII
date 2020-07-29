#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 18:56:22 2020

@author: rogerio

Ainda na classe Triangulo, escreva um método semelhantes(triangulo) que recebe
 um objeto do tipo Triangulo como parâmetro e verifica se o triângulo atual é
 semelhante ao triângulo passado como parâmetro. Caso positivo, o método deve
 devolver True. Caso negativo, deve devolver False.

Verifique a semelhança dos triângulos através do comprimento dos lados.
"""


class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def semelhantes(self, triangulo):
        lados_self = [self.a, self.b, self.c]
        lados_outro = [triangulo.a, triangulo.b, triangulo.c]
        lados_self.sort()
        lados_outro.sort()
        razao = lados_self[0] / lados_outro[0]
        if lados_self[1] == razao*lados_outro[1] and lados_self[2] == \
           razao*lados_outro[2]:
                return True
        else:
            return False
