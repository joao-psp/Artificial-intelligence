import numpy as np
from sklearn.utils import shuffle


class Perceptron(object):
    """Implements a perceptron network"""
    def __init__(self, input_size, saida, epochs=10000, alpha=0.001):
        # print("init")
        self.W = np.random.rand(saida,input_size)
        self.b = np.zeros(shape=(saida,1))
        self.alpha = alpha
        self.erro = 0
        self.total = 0
        # print(self.b.shape)
        # print(self.W)
        # print(self.W.shape)
        self.epochs = epochs
        # print('\n')

    def step(self, x):
        # print("activation_fn")
        # print(x.shape)
        y = np.zeros(shape=(x.shape))
        for i in range(0, x.shape[0]):
            if(x[i] >=1):
                y[i] = 1
            else:
                y[i] = 0
        # print("y: ")
        # print(y)
        # print('\n')
        return y

    def predict(self, x):
        # print('\n')
        # print("Predict")
        # print(x.shape)
        # print(self.W.shape)
        z = np.matmul(self.W,x).reshape(3,1) + self.b
        # print(z)
        a = self.step(z)
        return a


    def perceptron(self, X, d):
        #aux = np.zeros(shape=(1,13))
        # print('\n')
        # print("fit")
        t =0
        E = 1
        while t < self.epochs and E>0:
            E = 0
            for i in range(X.shape[0]):
                x = X[i]
                y = self.predict(x)
                # print(" jh fds")
                e = d[i].reshape(3,1) - y
                aux = x.reshape(1,13)
                e = e.reshape(3,1)
                self.W = self.W + self.alpha* np.matmul(e,aux)
                self.b = self.b + self.alpha*e
                E = E + np.sum([value*value for value in e])
            print("Erro:")
            print(E)
                # self.erro = E
            t= t+1

        print(E)

    def accuracy(self,actual,predicted):
        print(actual)
        print(predicted)
        teste = 0
        if(actual[0]==predicted[0] and actual[1]==predicted[1] and actual[2]==predicted[2]):
            self.total +=1


def manipulaArquivo():
    arq = open('wine.data','r')  # Le arquivo de dados e sepaara em entrada e saida
    saidas = []
    entradas = []

    for linha in arq:
        linha = linha[:-1]
        linha = linha.split(',')

        saidas.append(int(linha[0]))
        entradas.append([float(i) for i in linha[1:] ])
    arq.close()

    for i in range(0, len(saidas)):
        s = []
        if saidas[i] == 1:
            saidas[i] = [1,0,0]
        elif saidas[i] ==2:
            saidas[i] = [0,1,0]
        elif saidas[i] ==3:
            saidas[i] = [0,0,1]
    #print(entradas)
    return np.array(entradas), np.array(saidas)

def main():

    X, d = manipulaArquivo()


    aux = np.mean(X,axis=0)
    #print(aux)
    aux2 = np.std(X, axis=0)
    #print(aux2)
    X = (X-aux)/aux2
    # print(X)


    treino = X[:115]
    d_treino = d[:115]
    #print(treino.shape)
    teste = X[116:178]
    d_teste = d[116:178]

    perceptron = Perceptron(input_size=13, saida=3,epochs=10000)
    perceptron.perceptron(treino, d_treino)

    for i in range(0,teste.shape[0]):
        # print(perceptron.predict(X[i]))
        # print(d[i])
        perceptron.accuracy(perceptron.predict(teste[i]),d_teste[i])
    print(perceptron.total/teste.shape[0])

    print(perceptron.W)
    #print(perceptron.erro)


main()
