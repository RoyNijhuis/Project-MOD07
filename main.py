from branching import *
import branching
import distance


valid = False

while not valid:
    inputtype = input("use this as input? y/n")
    if inputtype == "y":
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
                output = branching.determineIsos(path, mygraphs.graph, auto)
            else:
                output = distance.determineIsos(path, mygraphs.graph, auto)
            valid = True
        except FileNotFoundError:
            print("Please enter a valid path...")
    else:
        valid = True
        path = "C:\\Users\Edwin\PycharmProjects\Project-MOD07\\cubes5.grl"
        auto = True
        alg = 0
        if alg == 0:
            output = branching.determineIsos(path, mygraphs.graph, auto)
        else:
            output = distance.determineIsos(path, mygraphs.graph, auto)

if auto:
    for l in output:
        print(l[0], "       ", l[1])
else:
    for l in output:
        print(l)