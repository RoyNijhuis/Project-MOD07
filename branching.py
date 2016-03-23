import copy

from colorrefinement import *
from graphIO import *

def checkIsomorphism(graph1, graph2):
    #Check if the graphs are a bijection, if so, the graphs are isomorphic
    map1, map2 = colorrefinex(graph1, graph2)

    #0: cannot be isomorphism, 1: bijection, 2: could be isomorphism(continue)
    result = isBijection(map1, map2)
    if result == 1:
        return True
    elif result == 0:
        return False

    #Branch recursively
    return branch(graph1, graph2, map1, map2)

def branch(graph1, graph2, map1, map2):
    global depth
    map11 = copy.copy(map1)
    map22 = copy.copy(map2)
    #Guess 2 vertices that could be twins
    #print("map1: " + str(map1.items()))
    #print("map2: " + str(map2.items()))

    for color, vertices in map1.items():
        if len(vertices) > 1:
            for v in vertices:
                for v2 in map2[color]:
                    colorx = max(map1.keys())+1
                    map11[color].remove(v)
                    map11[colorx] = [v]
                    map22[color].remove(v2)

                    map22[colorx] = [v2]

                    v.colornum = colorx
                    v2.colornum = colorx

                    graph1copy = copy.deepcopy(graph1)
                    graph2copy = copy.deepcopy(graph2)
                    refine1, refine2 = colorrefinex(graph1copy, graph2copy)
                    result = isBijection(refine1, refine2)
                    #print(str(result) + "refine 1 : " + str(refine1) + "\n refine 2 : " + str(refine2))
                    if result == 1:
                        return True
                    elif result == 2:
                        depth += 1
                        print("depth to: " + str(depth))
                        boole = branch(graph1, graph2, map11, map22)
                        depth -= 1
                        print("depth back to: " + str(depth))
                        if boole:
                            return True

                    map11[v.colornum].remove(v)
                    #map1[v.colornum].remove(v)
                    map11[color] = map11[color] + [v]

                    map22[v2.colornum].remove(v2)
                    #map2[v2.colornum].remove(v2)
                    map22[color] = map22[color] + [v2]

                    v.colornum = color
                    v2.colornum = color
    return False

G = loadgraph("C:\\Users\Edwin\\PycharmProjects\\Project-MOD07\\torus24.grl", basicgraphs.graph, True)
P = G[0][1]
Q = G[0][0]
depth = 0
writeDOT(P, 'test3')
time = clock()
print(checkIsomorphism(P, Q))
time = clock() - time
print(time)
writeDOT(P, 'test')
writeDOT(Q, 'test2')
