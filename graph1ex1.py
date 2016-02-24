from basicgraphs import *

def path(graph):
    for i in range(len(graph.V())-1):
        graph.addedge(graph[i], graph[i+1])




def cycle(graph):
    for i in range(len(graph.V())):
        graph.addedge(graph[i], graph[(i+1)%len(graph.V())])



def complete_graph(n):
    g = graph(n)
    cycle(g)
    return g



def disjointunion(G, H):
    return G





