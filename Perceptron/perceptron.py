import numpy as np


def initialize(m,t):
    for i in t:
        m[i] = 0;
    return m

def percepton(max_it,alpha, X,D): # num maximo de iteracoes, bias, dados, matriz com saida
    '''
        #separar dados de classes
        #se classe = 1 add [1 0 0]
            classe = 2 add [0 1 0]
            classe = 3 add [0 0 1]
            X e matrix sem a classe
            D ->
    '''
    initialize(W,3)
    initialize(b,1)

    t = 1
    E = 1
    y = []
    e = []
    while(t < max_it and E > 0):
        E = 0
        for i in 13:
            y[i] = f(W,X[i],b) # valor da saida

            e[i] = D[i] - y[i]
            W = W + b*e[i]*x[i]
            b = b + b*e[i]
            E = E + e[i]*e[i]
        t = t+1
