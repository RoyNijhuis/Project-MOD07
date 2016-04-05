from graph1ex1 import complete_graph
from Sorting import *
from graphIO import *


def colorRefinement(Graph):
    colorcoding = [None]*len(Graph.V())
    colorcodingnew = []

    for index,item in enumerate(Graph.V()):
        colorcoding[index] = item, len(item.nbs())
        item.colornum = len(item.nbs())

    #TODO GET LAST
    lastusedcode = len(Graph.V())
    changed = True
    while changed:
        colorcoding = mergesort(colorcoding)
        print(colorcoding)
        changed = False
        part = []
        used = []
        code = None
        #voor elke vertex
        for i in range(len(colorcoding)):
            tuple = colorcoding[i]
            if tuple[1] == code:

                currentnbs = tuple[0].nbs()
                #bereken neighbours aantal neighbours
                for i in range(len(currentnbs)):
                    colorcd = None
                    for x in colorcoding:
                        if x[0] == currentnbs[i]:
                            colorcd = x[1]
                            break

                    currentnbs[i] = colorcd

                found = False
                #voor alle items in used check if same
                for item in used:
                    nbs = item[0].nbs()
                    for neigh in nbs:
                        colorcd = None
                        for x in colorcoding:
                            if x[0] == neigh:
                                colorcd = x[1]
                                break
                        if colorcd in currentnbs:
                            currentnbs.remove(colorcd)
                        else:
                            break
                    if len(currentnbs) == 0:
                        found = True
                        part += [(tuple[0],item[1])]
                if not found:
                    part += [(tuple[0],lastusedcode+1)]
                    used += [(tuple[0],lastusedcode+1)]
                    lastusedcode += 1
                    changed = True

            else:
                #add part to colornew
                colorcodingnew += part
                part = [tuple]
                used = [tuple]
                code = tuple[1]
            #bestaat color al in part
        colorcodingnew += part
        colorcoding = colorcodingnew
        colorcodingnew = []

    for v in colorcoding:
        v[0].colornum = v[1]
    return colorcoding

z = complete_graph(10)
vert = z.V()
z.addedge(vert[1], vert[9])
z.addedge(vert[3], vert[5])
print(colorRefinement(z))
writeDOT(z,'test.gr')
