import copy

from colorrefinement import *
from graphIO import *

def checkIsomorphism(graph1, graph2):
    #Check if the graphs are a bijection, if so, the graphs are isomorphic
    map1 = colorrefine(graph1)
    map2 = colorrefine(graph2)

    #0: cannot be isomorphism, 1: bijection, 2: could be isomorphism(continue)
    result = isBijection(map1, map2)
    if result == 1:
        return True
    elif result == 0:
        return False

    #Branch recursively
    return branch(graph1, graph2, map1, map2)

def branch(graph1, graph2, map1, map2):

    map11 = copy.deepcopy(map1)
    map22 = copy.deepcopy(map2)
    #Guess 2 vertices that could be twins
    print("map1: " + str(map1.items()))
    print("map2: " + str(map2.items()))

    for color, vertices in map1.items():
        if len(vertices) > 1:
            for v in vertices:
                for v2 in map2[color]:
                    colorx = max(map1.keys())+1
                    oldV1Color = v.colornum
                    oldV2Color = v2.colornum
                    p1 = None
                    for x in map11[v.colornum]:
                        if x._label == v._label:
                            p1 = x
                            break
                    if p1 is not None:
                         map11[v.colornum].remove(p1)

                    #map11[v.colornum].remove(v)
                    map11[colorx] = [p1]

                    p2 = None
                    for x in map22[v.colornum]:
                        if x._label == v._label:
                            p2 = x
                            break
                    if p2 is not None:
                         map22[v.colornum].remove(p2)

                    #map22[v2.colornum].remove(v2)
                    map22[colorx] = [p2]

                    p1.colornum = colorx
                    p2.colornum = colorx

                    graph1copy = copy.deepcopy(graph1)
                    graph2copy = copy.deepcopy(graph2)
                    refine1 = colorrefine(graph1copy)
                    refine2 = colorrefine(graph2copy)
                    result = isBijection(refine1, refine2)
                    graph1copy = None
                    graph2copy = None
                    if result == 1:
                        return True
                    elif result == 2:
                        if branch(graph1, graph2, map11, map22) == True:
                            return True

                    map11[p1.colornum].remove(p1)
                    #map1[v.colornum].remove(v)
                    map11[oldV1Color] = map11[oldV1Color] + [p1]

                    map22[p2.colornum].remove(p2)
                    #map2[v2.colornum].remove(v2)
                    map22[oldV2Color] = map22[oldV2Color] + [p2]

                    p1.colornum = oldV1Color
                    p2.colornum = oldV2Color
    return False


G = loadgraph("C:\\Users\Edwin\\PycharmProjects\\Project-MOD07\\torus24.grl", basicgraphs.graph, True)
P = G[0][1]
Q = G[0][2]
time = clock()
print(checkIsomorphism(P,Q))
time = clock() - time
print(time)

writeDOT(P,'test')
writeDOT(Q,'test2')