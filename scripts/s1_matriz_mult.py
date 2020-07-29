#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 02:09:57 2020

@author: rogerio

Duas matrizes são multiplicáveis se o número de colunas da primeira é igual ao
 número de linhas da segunda. Escreva a função sao_multiplicaveis(m1, m2) que
 recebe duas matrizes como parâmetro e devolve True se as matrizes forem
 multiplicavéis (na ordem dada) e False caso contrário.
"""


def sao_multiplicaveis(m1, m2):
    ordem_m1 = [len(m1), len(m1[0])]
    ordem_m2 = [len(m2), len(m2[0])]
    if ordem_m1[1] == ordem_m2[0]:
        return True
    else:
        return False
