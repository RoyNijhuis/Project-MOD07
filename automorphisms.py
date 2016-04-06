import copy
from colorrefinement import *

automorphisms = []
count = 0

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

        return 1
    return len(automorphisms)


def checkNumberOfAutomorphismsOneGraph2(graph):
    global automorphisms
    global count
    count = 0
    automorphisms = []
    checkNumberOfAutomorphisms2(graph, copy.deepcopy(graph))
    if count > 1:
        return count* len(automorphisms)
    else: return 1 * len(automorphisms)


def checkNumberOfAutomorphisms2(graphOriginal, graphImage):
    global automorphisms
    global count
    originalMap, imageMap = colorrefinex(graphOriginal, graphImage)

    for color, vertices in originalMap.items():
        if len(vertices) > 1:
            for vertex in imageMap[color]:
                if (vertices[0]._label, vertex._label) not in automorphisms:
                    newColor = max(originalMap.keys())+1

                    vertices[0].colornum = newColor
                    vertex.colornum = newColor

                    originalCopy = copy.deepcopy(graphOriginal)
                    imageCopy = copy.deepcopy(graphImage)

                    refine1, refine2 = colorrefinex(originalCopy, imageCopy)

                    result = isBijection(refine1, refine2)

                    if result == 1:
                        cycles = generateCycles(refine1, refine2)
                        if len(cycles) == 1: automorphisms.append(cycles)
                        else: count += 1
                    elif result == 2:
                        checkNumberOfAutomorphisms(originalCopy, imageCopy)

                    vertices[0].colornum = color
                    vertex.colornum = color
            break


def generateCycles(map1, map2):
    cycles = []
    for color, vertex in map1.items():
        original = vertex[0]._label
        image = map2[color][0]._label
        if original != image:
            if original < image:
                cycles.append((original, image))
    return cycles