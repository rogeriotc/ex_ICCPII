#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 11:05:04 2020

@author: rogerio
Escreva uma função dimensoes(matriz) que recebe uma matriz como parâmetro e
 imprime as dimensões da matriz recebida, no formato i X j.
"""


def dimensoes(matriz):
    colunas = len(matriz[0])
    linhas = 0
    for linha in matriz:
        linhas += int(linha[0]/linha[0])
    print('{}X{}'.format(linhas, colunas))
