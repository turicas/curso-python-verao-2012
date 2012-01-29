#!/usr/bin/env python
# coding: utf-8


def rot13(texto):
    resultado = list(texto)
    for indice, caractere in enumerate(resultado):
        valor_ascii = ord(caractere) + 13
        if 'a' <= caractere <= 'z':
            if valor_ascii > ord('z'):
                valor_ascii = (valor_ascii % ord('z')) + ord('a') - 1
            caractere = chr(valor_ascii)
        elif 'A' <= caractere <= 'Z':
            if valor_ascii > ord('Z'):
                valor_ascii = (valor_ascii % ord('Z')) + ord('A') - 1
            caractere = chr(valor_ascii)
        resultado[indice] = caractere
    return ''.join(resultado)
