import copy

from colorrefinement import *
from graphIO import *
from automorphisms import *

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
    for color, vertices in map1.items():
        if len(vertices) > 1:
            for v in vertices:
                print(depth, "", len(map2[color]))
                for v2 in map2[color]:
                    colorx = max(map1.keys())+1

                    v.colornum = colorx
                    v2.colornum = colorx

                    graph1copy = copy.deepcopy(graph1)
                    graph2copy = copy.deepcopy(graph2)
                    #print("refine :", v, ",",v2)
                    refine1, refine2 = colorrefinex(graph1copy, graph2copy)
                    result = isBijection(refine1, refine2)
                    #print("bijection result:", result)
                    #print(str(result) + "refine 1 : " + str(refine1) + "\n refine 2 : " + str(refine2))
                    if result == 1:
                        return True
                    elif result == 2:
                        depth += 1
                        print("depth to: " + str(depth))
                        boole = branch(graph1copy, graph2copy, refine1, refine2)
                        depth -= 1
                        #print("depth back to: " + str(depth))
                        if boole:
                            return True

                    v.colornum = color
                    v2.colornum = color
                return False
    return False


def determineIsos(path, graphtype, auto):
    G = loadgraph(path, graphtype, True)
    writeDOT(G[0][0], 'test2')
    grouped = []
    different = []
    graphnumber = 0
    for graph in G[0]:
        print(grouped)
        found = False
        counter = 0
        for diff in different:
            if checkIsomorphism(copy.deepcopy(diff), copy.deepcopy(graph)):
                found = True
                grouped[counter].append(graphnumber)
                break
            counter += 1
        if not found:
            different.append(graph)
            grouped.append([graphnumber])
        graphnumber += 1

    if auto:
        print("starting autos")
        results = []
        numb = 0
        for dif in different:
            autos = checkNumberOfAutomorphismsOneGraph(dif)
            results.append([grouped[numb],autos])# autos(dif)])
            numb += 1
    else:
        return grouped

    return results

depth = 0