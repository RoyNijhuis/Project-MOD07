import copy

from colorrefinement import *

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

    #Guess 2 vertices that could be twins
    for color, vertices in map1.items():
        if len(vertices) > 1:
            for v in vertices:
                for v2 in map2.get(color):
                    color = max(map1.keys())
                    oldV1Color = v.colornum
                    oldV2Color = v2.colornum
                    v.colornum = color
                    v2.colornum = color
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
                        branch(graph1, graph2, refine1, refine2)

                    v.colornum = oldV1Color
                    v2.colornum = oldV2Color
