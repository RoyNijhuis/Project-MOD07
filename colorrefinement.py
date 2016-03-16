from graph1ex1 import complete_graph
from graphIO import *
from time import clock

def colorrefine(Graph):

    colors = {}
    currentcol = 0
    for v in Graph.V():
        if v.colornum is None:
            v.colornum = len(v.nbs())
        if v.colornum > currentcol: currentcol = v.colornum
        if colors.get(v.colornum) is not None: colors[v.colornum] = colors.get(v.colornum) + [v]
        else: colors[v.colornum] = [v]
    change = True
    while change:
        change = False
        for key, colorx in colors.items():
            used = []
            for vertex in colorx:
                if not used:
                    used += [vertex]
                    vertex.colornumnew = vertex.colornum
                    continue
                clrs = []
                for neigh in vertex.nbs():
                    clrs += [neigh.colornum]
                found = False
                for vertexused in used:
                    clrscop = clrs.copy()
                    breaks = False
                    for neigh in vertexused.nbs():
                        if neigh.colornum in clrscop:
                            clrscop.remove(neigh.colornum)
                        else:
                            breaks = True
                            break
                    if len(clrscop) == 0 and not breaks:
                        vertex.colornumnew = vertexused.colornumnew
                        found = True
                if not found:
                    change = True
                    used += [vertex]
                    vertex.colornumnew = currentcol
                    currentcol += 1
        for key, colorx in colors.items():
            for y in colorx:
                if y.colornumnew is not None:
                    y.colornum, y.colornumnew = y.colornumnew, None
        colors = {}
        for v in Graph.V():
            if colors.get(v.colornum) is not None:
                colors[v.colornum] = colors.get(v.colornum) + [v]
            else:
                colors[v.colornum] = [v]
    return colors

G = loadgraph("C:\\Users\Edwin\\PycharmProjects\\Project-MOD07\\colorref_smallexample_2_49-1.grl",basicgraphs.graph, True)
P = G[0][0]
Q = G[0][1]

time = clock()
print(colorrefine(P))
time = clock() - time
print(time)

time = clock()
print(colorrefine(Q))
time = clock() - time
print(time)

writeDOT(P,'test')
writeDOT(Q,'test2')
