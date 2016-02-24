from graph1ex1 import complete_graph
from Sorting import *


def colorRefinement(Graph):
    colorcoding = [None]*len(Graph.V())
    colorcodingnew = [None]*len(Graph.V())

    for index,item in enumerate(Graph.V()):
        colorcoding[index] = item, len(item.nbs())

    #TODO sort????!!
    colorcoding = mergesort(colorcoding)
    print(colorcoding)

    #TODO GET LAST
    lastusedcode = len(Graph.V())
    changed = True
    while changed:
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
                    currentnbs[i] = len(currentnbs[i].nbs())

                found = False
                #voor alle items in used check if same
                for item in used:
                    nbs = item[0].nbs()
                    for neigh in nbs:
                        if len(neigh.nbs()) in currentnbs:
                            currentnbs.remove(len(neigh.nbs()))
                        else:
                            break
                    if len(currentnbs) == 0:
                        found = True
                        part += [tuple]
                if not found :
                    part += [(tuple[0],lastusedcode+1)]
                    used += [(tuple[0],lastusedcode+1)]
                    lastusedcode += 1

            else:
                #add part to colornew
                colorcodingnew += part
                part = [tuple]
                used = [tuple]
                code = tuple[1]
            #bestaat color al in part

        colorcoding = colorcodingnew

    return colorcoding

#print(complete_graph(15))
print(colorRefinement(complete_graph(15)))