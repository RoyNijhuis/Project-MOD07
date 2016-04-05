import copy
from colorrefinement import *

automorphisms = []

def checkNumberOfAutomorphismsOneGraph(graph):
    global automorphisms
    automorphisms = []
    return checkNumberOfAutomorphisms(graph, copy.deepcopy(graph))

def checkNumberOfAutomorphisms(graphOriginal, graphImage):
    global automorphisms
    originalMap, imageMap = colorrefinex(graphOriginal, graphImage)

    for color, vertices in originalMap.items():
        if len(vertices) > 1:
            for vertex in imageMap[color]:
                newColor = max(originalMap.keys())+1

                vertices[0].colornum = newColor
                vertex.colornum = newColor

                originalCopy = copy.deepcopy(graphOriginal)
                imageCopy = copy.deepcopy(graphImage)

                refine1, refine2 = colorrefinex(originalCopy, imageCopy)

                result = isBijection(refine1, refine2)

                if result == 1:
                    cycles = generateCycles(refine1, refine2)
                    automorphisms.append(cycles)
                elif result == 2:
                    checkNumberOfAutomorphisms(originalCopy, imageCopy)

                vertices[0].colornum = color
                vertex.colornum = color
            break
    return len(automorphisms)

def generateCycles(map1, map2):
    cycles = []
    for color, vertex in map1.items():
        original = vertex[0]._label
        image = map2[color][0]._label
        if original != image:
            if original < image:
                cycles.append((original, image))
    return cycles