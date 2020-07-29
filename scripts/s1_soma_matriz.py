#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 11:05:59 2020

@author: rogerio

Escreva a função soma_matrizes(m1, m2) que recebe 2 matrizes e devolve uma
 matriz que represente sua soma caso as matrizes tenham dimensões iguais. Caso
 contrário, a função deve devolver False.
"""


def soma_matrizes(m1, m2):
    if dimensoes_iguais(m1, m2):
        soma = []
        for lin in range(len(m1)):
            temp_linha = []
            for col in range(len(m1[0])):
                temp_linha.append(m1[lin][col] + m2[lin][col])
            soma.append(temp_linha)
        return soma
    else:
        return False


def dimensoes_iguais(m1, m2):
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        return True
    else:
        return False
