def initialize(m,t):
    pass


def percepton(max_it,bias, X,val_determ):
'''
    #separar dados de classes
    #se classe = 1 add [1 0 0]
        classe = 2 add [0 1 0]
        classe = 3 add [0 0 1]
        X é matrix sem a classe
        D ->
'''
    t = 1
    E = 1
    y[] = 0
    e[]= 0
    while(t < max_it and E > 0):
        E = 0
        for(i in size of colums):
            y[i] = X[i] + b;
            e[i] = d[i] - y[i]
            w = w + b*e[i]*x[i]
            b = b + b*e[i]
            E = E + e[i]*e[i]
        t = t+1
