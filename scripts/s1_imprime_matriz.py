#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 02:09:10 2020

@author: rogerio

Como proposto na primeira vídeo-aula da semana, escreva uma função
imprime_matriz(matriz), que recebe uma matriz como parâmetro e imprime a
 matriz, linha por linha. Note que NÃO se deve imprimir espaços após o último
 elemento de cada linha!
"""


def imprime_matriz_2(matriz):
    for linha in matriz:
        print(linha)


def imprime_matriz(matriz):
    for linha in matriz:
        for i in range(len(linha)-1):
            print(linha[i], end=' ')
        print(linha[-1])
