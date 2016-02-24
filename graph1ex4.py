from graphIO import *
from basicgraphs import *
from graph1ex1 import complete_graph


def bfs(G, s):
    queue = []
    done = []
    queue.append(G[0])
    G[0].dist = 0
    counter = 0
    G[0]._label = str(G[0]._label) + " " + str(counter)
    while len(queue)>0:
        c = queue.pop(0)
        done.append(c)
        for i in c.nbs():
            i.dist = c.dist + 1
            if i == s:
                counter += 1
                i._label = str(i._label) + " " + str(counter)
                return i.dist
            elif i not in done:
                counter += 1
                i._label = str(i._label) + " " + str(counter)
                queue.append(i)
    return -1

z = complete_graph(15)
z.addvertex("X")
print(z)
b = bfs(z, z[6])
print(b)
print(z)
writeDOT(z, 'visualizedGRAPH.dot', False)