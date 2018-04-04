# -*- coding: utf-8 -*-

class Graph: # Classe para instanciar os vertices do Grafo
    def __init__(self):
        self.nodes = set()
        self.edges = {}
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.set_edge(from_node, to_node, distance)
        self.set_edge(to_node, from_node, distance)

    def set_edge(self, from_node, to_node, distance):
        self.edges.setdefault(from_node, [])
        self.edges[from_node].append(to_node)
        self.distances[(from_node, to_node)] = distance

def build_heuristic_dict(): # Lê arquivo com a heuristica utilizada no A*
    h = {}
    with open("heuristics.txt", 'r') as file:
        for line in file:
            line = line.strip().split(",")
            node = line[0].strip()
            sld = int(line[1].strip())
            h[node] = sld
    return h


def astar(graph, start, goal): # Função A*

    closed_set = set() # Nodes que não serão mais abertos
    nodes = set()
    nodes.add(start)
    visited = {} # Nodes visitados

    g = {} # distancia percorrida para chegar ao node
    h = build_heuristic_dict() # heuritica de cada node
    f = {} # custo total

    g[start] = 0
    f[start] = g[start] + h[start]

    while nodes:
        x = None
        for node in nodes:
            if x is None:
                x = node
            elif f[node] < f[x]: # se custo total do node a ser verificado for menor que o node atual analisa-se o novo node
                x = node
        nodes.remove(x)

        if x == goal: # se node = destino
            return g, visited

        closed_set.add(x)
        for y in graph.edges[x]:
            if y in closed_set:
                continue
            temp = (g[x] + graph.distances[(x, y)]) + h[y]

            f2 = h[y] + graph.distances[(x, y)]


            if y not in nodes or temp < f[y]:
                nodes.add(y)
                visited[y] = x
                f[y] = temp
                g[y] = g[x] + graph.distances[(x,y)]

            tela = 'Estou em \t{0:16} Indo para\t {1:16} \t Custo F: {2:5} Custo G: {3:5} Custo H: {4:5}  Distancia: {5:5}'.format(x,y,temp,g[x],h[y],graph.distances[(x, y)])
            print (tela)
    return g, visited


def path(graph, start, goal):
    costs, paths = astar(graph, start, goal)
    route = [goal]

    while goal != start:
        route.append(paths[goal])
        goal = paths[goal]
    route.reverse() # troca os elemento de posição para a ordem ficar 'bonitinha'
    return route, costs

def build_graph():
    graph = Graph()

    file = open("graph.txt",'r')
    for line in file:
        line = line.split(',')

        from_node = line[0].strip()
        to_node = line[1].strip()
        weight = int(line[2].strip())

        if (from_node not in graph.nodes):
            graph.add_node(from_node)
        if (to_node not in graph.nodes):
            graph.add_node(to_node)

        graph.add_edge(from_node, to_node, weight)
    # print(graph.edges)
    # print('\n')
    # print(graph.distances)
    return graph

def main():
    graph = build_graph()

    b_path, costs = path(graph,'Lugoj','Bucharest') #substituir para saída e destino desejadas
    print("\nMelhor Caminho: \t\t\n")
    print(b_path)
    print('\n')
    print("Total de Cidades:" +str(len(b_path))) # Quantidade final do melhor caminho
    print("Custo Final: "+ str(costs['Bucharest'])) # custo final para chegar ao destino

main()
