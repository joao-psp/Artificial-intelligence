import numpy as np
import matplotlib.pyplot as plt

class Perceptron(object):
    """Implements a perceptron network"""
    def __init__(self, input_size, saida, epochs=10000, alpha=0.001):
        # print("init")
        self.W = np.random.rand(saida,input_size)
        self.b = np.zeros(shape=(saida,1))
        self.alpha = alpha
        self.erro = 0
        self.total = 0
        self.epochs = epochs
        self.E = []
        # print('\n')

    def step(self, x):   # aplica a funcao degrau
        # print("activation_fn")
        # print(x.shape)
        if x >= 1:
            y = 1
        else:
            y = 0
        return y

    def predict(self, x): # f(Wx+b)
        z = np.matmul(self.W,x).reshape(1,1) + self.b
        a = self.step(z)
        return a


    def perceptron(self, X, d): # algortmo para treino

        t =0
        E = 1
        while (t < self.epochs and E > 0):
            E = 0
            for i in range(X.shape[0]):
                x = X[i]
                y = self.predict(x)
                # print(" jh fds")
                e = d[i] - y
                aux = x.reshape(1,9) # mudar pro numero de saidas
                #e = e.reshape(1,1
                self.W = self.W + self.alpha* e*aux
                self.b = self.b + self.alpha*e
                E = E + e*e
            self.erro = E
            t= t+1

    def accuracy(self,actual,predicted):  # verifica se a saida e igual a desejada

        teste = 0
        if(actual==predicted ):
            self.total +=1


def manipulaArquivo():
    arq = open('breast-cancer-wisconsin.data','r')  # Le arquivo de dados e sepaara em entrada e saida
    saidas = []
    entradas = []

    for linha in arq:
        linha = linha[:-1]
        linha = linha.split(',')

        saidas.append(int(linha[10]))
        entradas.append([float(i) for i in linha[1:10] ])
    arq.close()
    #print(entradas)

    for i in range(0, len(saidas)):
        s = []
        if saidas[i] == 2: # no arquivo, 2 não tem cancer, 4  tem
            saidas[i] = 0
        elif saidas[i] == 4:
            saidas[i] = 1

    return np.array(entradas), np.array(saidas)

def main():

    X, d = manipulaArquivo()


    aux = np.mean(X,axis=0)   # normaliza arquivo
    aux2 = np.std(X, axis=0)
    X = (X-aux)/aux2


    treino = X[:466]    #separa o banco em teste e treino
    d_treino = d[:466]

    teste = X[467:699]
    d_teste = d[467:699]

    #print(X[0])

    perceptron = Perceptron(input_size=9, saida=1,epochs=1000) #treina a base
    perceptron.perceptron(treino, d_treino)

    for i in range(0,teste.shape[0]):
        perceptron.accuracy(perceptron.predict(teste[i]),d_teste[i]) # testa a base

    print("Alpha = 0.001, max_epochs = 10000")

    print("\n Matrix W ")
    print(perceptron.W)
    print("\n bias")
    print(perceptron.b)

    print("\nAccuracy: ")
    print(perceptron.total/teste.shape[0]) # mostra a accuracy

    print("\nErro E")
    print(perceptron.erro)



main()
