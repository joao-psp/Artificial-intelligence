
import numpy as np

def degrau(u):
    y = np.zeros(shape=u.shape, dtype = np.int32)

    for i in range(0, u.shape[0]):
        if len(u.shape) > 1:
            for j in (range(0,u.shape[1])):
                if u[i][j] >= 1:
                    y[i][j] =1
                else:
                    y[i][j] = 0
        else:
            if u[i] >= 1:
                y[i] =1
            else:
                y[i] = 0
    return y

def erro(e):
    E = 0
    i = 0
    for i in range(0, e.shape[0]):
        Es = 0
        j = 0
        for j in range(0, e.shape[1]):
            Es += pow(e[i][j],2)
        E+= Es / j
    E = E / i
    return E

def manipulArquivo():
    arq = open('wine.data','r')  # Le arquivo de dados e sepaara em entrada e saida
    saidas = []
    entradas = []

    for linha in arq:
        linha = linha[:-1]
        linha = linha.split(',')

        saidas.append(int(linha[0]))
        entradas.append([float(i) for i in linha[1:] ])
    arq.close()

    print(len(saidas))


    for i in range(0, len(saidas)):
        s = []
        if saidas[i] == 1:
            saidas[i] = [1,0,0]
        elif saidas[i] ==2:
            saidas[i] = [0,1,0]
        elif saidas[i] ==3:
            saidas[i] = [0,0,1]
    print(entradas)
    return entradas, saidas

def perceptron(max_it, alpha, entrada, saida):
    X = entrada
    W = np.zeros(shape=(saida.shape[0],entrada.shape[1]))
    D = saida
    b = np.zeros(shape=(D.shape[0],1))
    erro = []
    tempo = []

    t = 1
    E = 1
    e = np.zeros(shape=d.shape)

    while(t<max_it and E > 0):
        u = np.matmul(w,x) + b
        y = degrau(u)
        e = D - y
        W = W + np.matmul((alpha * e), np.transpose(x))
        b = b + alpha * e
        E = erro(e)
        tempo.append(t)
        erro.append(E)
        t= t+1


def main():
    X, D = manipulArquivo()
    MI = 100
    alpha = 0.1

    perceptron(MI, alpha, X, D)
