from time import clock
from graphIO import *
import copy
from automorphisms import *

def distances(graph):
    done = False
    distance = 1
    #init
    maxi = 0
    for vertex in graph.V():
        if not hasattr(vertex, "colornum"):
            vertex.colornum = len(vertex.neigh)
        if vertex.colornum is None:
            vertex.colornum = len(vertex.neigh)
        if vertex.colornum > maxi:
            maxi = vertex.colornum
        vertex.list = []
        vertex.lastadded = []
        vertex.newlastadded = []
        vertex.newlist = []
        vertex.added = [vertex]#._label]

    for vertex in graph.V():
        if vertex.colornum < 0:
            vertex.colornum = maxi-vertex.colornum
            maxi += 1

    for vertex in graph.V():
        for vert in vertex.neigh:
            vertex.list += [(vertex.colornum, vert.colornum, 1)]
            vertex.added += [vert]#insert(vert._label, vertex.added)
            vertex.lastadded += [vert]

    while not done:
        for v in graph.V():
            for n in v.neigh:
                for a in n.lastadded:
                    if a not in v.added:#not existsin(a._label, v.added):
                        v.newlist += [(n.colornum, a.colornum, distance)]
                        v.newlastadded += [a]
        done = True
        change = False
        for v in graph.V():
            v.list += v.newlist
            v.newlist = []
            v.lastadded = []
            for a in v.newlastadded:
                if a not in v.added:#not existsin(a._label, v.added):
                    change = True
                    v.lastadded += [a]
                    v.added += [a]#insert(a._label, v.added)
            v.newlastadded = []
            if done and len(v.added) != (len(graph.V()) - 1):
                done = False
        if not change:
            done = True


def compare(graph1, graph2):
    vertlist = graph2.V()#copy.copy(graph2.V())
    for vertex in graph1.V():
        sort1 = sorted(vertex.list, key=lambda tup: (tup[2], tup[1], tup[0]))

        found = False
        for vertex2 in vertlist:

            sort2 = sorted(vertex2.list, key=lambda tup: (tup[2], tup[1], tup[0]))

            if sort1 == sort2:
                found = True
                vertlist.remove(vertex2)
                break
        if not found:
            return False
    if vertlist:
        return False
    return True


def determineIsos(path, graphtype, auto):
    G = loadgraph(path, graphtype, True)
    grouped = []
    different = []
    graphnumber = 0
    for graph in G[0]:
        distances(graph)
        found = False
        counter = 0
        for diff in different:
            if compare(diff, graph):
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
            groupeds = []
            for v in dif.V():
                v.list.sort(key=lambda tup: (tup[2], tup[1], tup[0]))
                found = False
                for i in groupeds:
                    if i[0].list == v.list:
                        found = True
                        i += [v]
                        break
                if not found:
                    groupeds.append([v])
            numbcol = 0
            for groupe in groupeds:
                for v in groupe:
                    v.colornum = numbcol
                numbcol += 1
            autos = checkNumberOfAutomorphismsOneGraph2(dif)
            results.append([grouped[numb],autos])# autos(dif)])

            numb += 1
        return results
    else: return grouped

automorphs = 0
def auto(graph):
    global automorphs
    global depth
    automorphs = 0
    depth = 1
    graph2 = copy.deepcopy(graph)
    distances(graph)
    distances(graph2)
    calcautos(graph, graph2)
    return automorphs


def calcautos(graph1, graph2):
    global automorphs
    global depth
    #originalMap, imageMap = colorrefinex(graphOriginal, graphImage)
    grouped = []
    for vertex in graph1.V():
        vertex.list.sort(key=lambda tup: (tup[2], tup[1], tup[0]))
        found = False
        for i in grouped:
            if i[0].list == vertex.list:
                found = True
                i += [vertex]
                break
        if not found:
            grouped.append([vertex])
    grouped2 = []
    for vertex in graph2.V():
        vertex.list.sort(key=lambda tup: (tup[2], tup[1], tup[0]))
        found = False
        for i in grouped2:
            if i[0].list == vertex.list:
                found = True
                i += [vertex]
                break
        if not found:
            grouped2.append([vertex])

    for vertices in grouped:
        if len(vertices) > 1:
            for vertic in grouped2:
                if vertic[0].list == vertices[0].list:
                    for v in vertic:
                        newColor = -depth
                        color = v.colornum
                        vertices[0].colornum = newColor
                        v.colornum = newColor

                        originalCopy = copy.deepcopy(graph1)
                        imageCopy = copy.deepcopy(graph2)

                        distances(originalCopy)
                        distances(imageCopy)
                        result = comparelists2(listsgraph(originalCopy), listsgraph(imageCopy))
                        if result == 1:
                            automorphs += 1
                        elif result == 2:
                            depth += 1
                            calcautos(originalCopy, imageCopy)
                            depth -= 1
                        vertices[0].colornum = color
                        v.colornum = color
                    break
            break


depth = 1


def listsgraph(graph):
    vertlist = []
    for v in graph.V():
        v.list.sort(key=lambda tup: (tup[2], tup[1], tup[0]))
        vertlist.append(v.list)
    return vertlist


def comparelists(list1, list2):
    list2copy = list2[:]
    for li in list1:
        found = False
        for l2 in list2copy:
            if li == l2:
                list2copy.remove(l2)
                found = True
                break
        if not found:
            return False
    return True


def comparelists2(list1, list2):
    list2copy = list2[:]
    biject = False
    for li in list1:
        found = False
        for l2 in list2copy:
            boole = li == l2
            if boole and not found:
                list2copy.remove(l2)
                found = True
                if biject:
                    break
            elif boole and found and not biject:
                biject = True
        if not found:
            return 0
    result = 1
    if biject:
        result = 2
    return result
