from graphIO import *
from branching import *
import distance

valid = False

while not valid:
    path = input("Please enter the path of the file...")
    alg = input("normal or other? 0 / 1")
    done = False
    auto = False
    while not done:
        type = input("Check for automorphisms? ('True' or 'False')")
        if type == "True":
            done = True
            auto = True
        elif type == "False":
            done = True
            auto = False

    try:
        if alg == 0:
            output = determineIsos(path, mygraphs.graph, auto)
        else:
            output = distance.determineIsos(path, mygraphs.graph, auto)
        valid = True
    except FileNotFoundError:
        print("Please enter a valid path...")

if auto:
    for l in output:
        print(l[0], "       ", l[1])
else:
    for l in output:
        print(l)