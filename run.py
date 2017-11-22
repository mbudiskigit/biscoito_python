#!/usr/bin/python
# -*- coding: utf-8 -*-

import random

from flask import Flask,jsonify

app = Flask(__name__)


@app.route("/biscoito")
def index():
    return selecionar_palavra_biscoito()




def selecionar_palavra_biscoito():
    
    # lendo o arquivo que contém as definições de palavras
    arquivo = open("frases.txt", "r")
    palavras = []

    for linha in arquivo:
        palavras.append(linha.strip())

    arquivo.close()

    indice = random.randrange(0, len(palavras))

    # a palavra biscoito
    return  palavras[indice]


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=3000)


