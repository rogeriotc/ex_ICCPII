#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 15:21:40 2020

@author: rogerio

Escreva a função conta_letras(frase, contar="vogais"), que recebe como primeiro
 parâmetro uma string contendo uma frase e como segundo parâmetro uma outra
 string. Este segundo parâmetro deve ser opcional.

Quando o segundo parâmetro for definido como "vogais", a função deve devolver
 o numero de vogais presentes na frase. Quando ele for definido como
 "consoantes", a função deve devolver o número de consoantes presentes na
 frase. Se este parâmetro não for passado para a função, deve-se assumir o
 valor "vogais" para o parâmetro.
"""


def conta_letras(frase, contar='vogais'):
    str_vogais = 'AaEeIiOoUu'
    num_vogais = 0
    for letra in frase:
        if letra in str_vogais:
            num_vogais += 1
    if contar == 'vogais':
        return num_vogais
    else:
        num_consoantes = len(frase.strip()) - (len(frase.strip().split())-1) \
                         - num_vogais  # caracteres - espaços - vogais
        return num_consoantes
