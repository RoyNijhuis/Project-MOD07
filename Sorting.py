def mergesort(colorVertexMap):
    if len(colorVertexMap) == 1:
        return colorVertexMap

    l1 = colorVertexMap[:len(colorVertexMap)/2]
    l2 = colorVertexMap[len(colorVertexMap)/2:]

    l1 = mergesort(l1)
    l2 = mergesort(l2)

    return merge(l1,l2)

def merge(l1, l2):
    c = []

    while len(l1) > 0 and len(l2) > 0:
        if l1[0][1] > l2[0][1]:
            c.append(l2[0])
            l2.remove(l2[0])
        else:
            c.append(l1[0])
            l1.remove(l1[0])

    while len(l1) > 0:
        c.append(l1[0])
        l1.remove(l1[0])
    while len(l2) > 0:
        c.append(l2[0])
        l2.remove(l2[0])
    return c