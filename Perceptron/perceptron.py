import numpy as np

class Perceptron(object):
    """Implements a perceptron network"""
    def __init__(self, input_size, saida, epochs=1):
        print("init")
        self.W = np.zeros(shape=(saida,input_size))
        print(self.W)
        print(self.W.shape)
        self.epochs = epochs
        print('\n')

    def step(self, x):
        print("activation_fn")
        print(x.shape)
        y = np.zeros(shape=(x.shape))
        for i in range(0, x.shape[0]):
            if(x[i] >=1):
                y[i] = 1
            else:
                y[i] = 0
        print("y: ")
        print(y)
        print('\n')
        return y

    def predict(self, x):
        print('\n')
        print("Predict")
        print(x.shape)
        print(self.W.shape)
        z = np.matmul(self.W,x)
        print(z.shape)
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
        print('\n')
        print("fit")
        t =0
        while t < self.epochs :
            for i in range(X.shape[0]):
                #print(X[i])
                x = X[i]
                y = self.predict(x)
                e = d[i] - y
                print("e")
                print(e)
                aux = x.reshape(1,13)
                e = e.reshape(3,1)
                print(e)
                print(aux)
                kl = e * aux
                print (kl)
                print(self.W.shape)
                self.W = self.W + e * aux
            t= t+1

def main():
    X = np.array([
        [1,2,3,4,5,6,7,8,9,10,11,12,13],
        [1,2,3,4,5,6,7,8,9,10,11,12,13],
        [1,2,3,4,5,6,7,8,9,10,11,12,13],
        [1,2,3,4,5,6,7,8,9,10,11,12,13]
    ])
    #print(X.shape)
    d = np.array([[0,0,1],[0,1,0],[0,1,0],[0,0,1]])
    # print(d[0].shape)
    # print(d[0].transpose().shape)

    perceptron = Perceptron(input_size=13, saida=3)
    perceptron.perceptron(X, d)
    print(perceptron.W)

main()
