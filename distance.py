from time import clock
from graphIO import *


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


def determineIsos(path, graphtype):
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

    print("starting autos")
    results = []
    numb = 0
    for dif in different:
        results.append([grouped[numb],1])# autos(dif)])
        numb += 1

    return results


depth = 1
def autos(graph):
    global depth
    grouped = []
    for vertex in graph.V():
        vertex.list.sort(key=lambda tup: (tup[2], tup[1], tup[0]))
        found = False
        for i in grouped:
            if i[0].list == vertex.list:
                i.append(vertex)
                found = True
                break
        if not found:
            grouped.append([vertex])

    count = 0
    lists = []
    counter = 0
    for i in grouped:
        if len(i)>1:
            lists.append([])
            for p in i:
                old = p.colornum
                p.colornum = -depth
                distances(graph)
                lists[counter].append((p,listsgraph(graph)))
                p.colornum = old
            counter += 1
    print("groups1: ", grouped)
    #print("lists1: ", lists)
    grouped = []
    for group in lists:
        for li in group:
            for lis in li[1]:
                lis.sort(key=lambda tup: (tup[2], tup[1], tup[0]))
            found = False
            for i in grouped:
                if comparelists(i[0][1],li[1]):
                    i.append(li)
                    found = True
                    break
            if not found:
                grouped.append([li])
    for i in grouped:
        print("groups2", [xs[0] for xs in i])
    any1 = False
    for i in grouped:
        if len(i)>1:
            any1 = True
            count = len(i)
            i[0][0].colornum = -depth
            depth += 1
            count *= autos(graph)
            break
    if not any1:
        return 1

    return count


def listsgraph(graph):
    vertlist = []
    for v in graph.V():
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


time = clock()
x = determineIsos("C:\\Users\Edwin\\PycharmProjects\\Project-MOD07\\products72.grl", mygraphs.graph)
for l in x:
    print(l[0], "       ", l[1])
print(clock()-time)



#G = loadgraph("C:\\Users\Edwin\\PycharmProjects\\Project-MOD07\\torus24.grl", mygraphs.graph, True)
'''
P = G[0][2]
Q = G[0][3]
time2 = clock()
distances(P)
time2 = clock() - time2
print("time distance(): ",time2)
time = clock()
distances(Q)
time = clock() - time
print(time)
time = clock()
print(compare(P, Q))
time = clock() - time
print(time)
time = clock()
print(countauto(P))
time = clock() - time
print(time)
'''
#writeDOT(G[0][1], 'test.gr')
#writeDOT(Q, 'test2')
