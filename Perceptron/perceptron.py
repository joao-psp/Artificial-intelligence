import numpy as np

class Perceptron(object):
    """Implements a perceptron network"""
    def __init__(self, input_size, saida, epochs=1, alpha=0.1):
        # print("init")
        self.W = np.zeros(shape=(saida,input_size))
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

    # def transpose1(self,x):
    #     #print(x.shape)
    #     y = np.zeros(shape=(13,x.shape[1]))
    #     y = x.T
    #     print(str(x.shape)+"njsdfnk")
    #     print(y)
    #     print(x)
    #     return y

    def perceptron(self, X, d):
        #aux = np.zeros(shape=(1,13))
        # print('\n')
        # print("fit")
        t =0
        E = 1
        while t < self.epochs:
            E = 0
            for i in range(X.shape[0]):
                x = X[i]
                y = self.predict(x)
                # print(" jh fds")
                e = d[i].reshape(3,1) - y
                aux = x.reshape(1,13)
                e = e.reshape(3,1)
                self.W = self.W + self.alpha*e * aux
                self.b = self.b + self.alpha*e
                E = E + e * e
                #print(e.shape)
                self.erro = E
            t= t+1

    def accuracy(self,actual,predicted):
        teste = 0
        for i in range(len(actual)):
            # print("----")
            # print(actual[i])
            # print(predicted[i])
            # print("------")
            if actual[i] == predicted[i]:
                teste+=1
            if(teste ==3):
                print("jbsdf")
                self.total+=1


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
    # X = np.array([
    #     [1,2,3,4,5,6,7,8,9,10,11,12,13],
    #     [1,2,3,4,5,6,7,8,9,10,11,12,13],
    #     [1,2,3,4,5,6,7,8,9,10,11,12,13],
    #     [1,5,65,53,123,3,312,321,231,231,123,123,3]
    # ])
    # d = np.array([[0,0,1],[0,1,0],[0,1,0],[0,0,1]])
    # print(d[0].shape)
    # print(d[0].transpose().shape)
    print(X.shape)
    print(d.shape)

    perceptron = Perceptron(input_size=13, saida=3,epochs=1)
    perceptron.perceptron(X, d)
    print(perceptron.W)
    print(perceptron.erro)
    print(perceptron.total/178)

main()
