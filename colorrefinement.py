from graph1ex1 import complete_graph
from graphIO import *
from time import clock

def colorrefine(Graph):

    colors = {}
    currentcol = 0
    for v in Graph.V():
        if not hasattr(v, "colornum") or v.colornum is None:
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


def colorrefinex(Graph, Graph2):

    colors = {}
    colors1 = {}
    colors2 = {}
    currentcol = 0

    for v in (Graph.V()+Graph2.V()):
        if not hasattr(v, "colornum") or v.colornum is None:
            v.colornum = len(v.nbs())
        if v.colornum > currentcol: currentcol = v.colornum
        if colors.get(v.colornum) is not None: colors[v.colornum] = colors.get(v.colornum) + [v]
        else: colors[v.colornum] = [v]
    for v in (Graph.V()):
        if colors1.get(v.colornum) is not None: colors1[v.colornum] = colors1.get(v.colornum) + [v]
        else: colors1[v.colornum] = [v]
    for v in (Graph2.V()):
        if colors2.get(v.colornum) is not None: colors2[v.colornum] = colors2.get(v.colornum) + [v]
        else: colors2[v.colornum] = [v]
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
        colors2 = {}
        colors1 = {}
        colors = {}
        for v in Graph.V()+Graph2.V():
            if colors.get(v.colornum) is not None:
                colors[v.colornum] = colors.get(v.colornum) + [v]
            else:
                colors[v.colornum] = [v]
        for v in Graph.V():
            if colors1.get(v.colornum) is not None:
                colors1[v.colornum] = colors1.get(v.colornum) + [v]
            else:
                colors1[v.colornum] = [v]
        for v in Graph2.V():
            if colors2.get(v.colornum) is not None:
                colors2[v.colornum] = colors2.get(v.colornum) + [v]
            else:
                colors2[v.colornum] = [v]
    return colors1, colors2


def isBijection(map1, map2):
    boole = 1
    for key, colorx in map1.items():
        if map2.get(key) is not None and len(colorx) == len(map2.get(key)):
            if len(colorx) > 1:
                boole = 2
        else:
            return 0
    return boole

