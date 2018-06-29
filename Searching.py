# Searching module:

def locate(element, array):
    # array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 24, 64, 101, 88, 8, 5, 25, 7, 6, 5, 3, 2, 1, 0, 101]
    # print("length: " + str(len(array)))
    # search all elements
    # element = 5
    loc = []
    j = 0
    try:
        while True:
            loc.append(array.index(element) + j)
            array.remove(element)
            j += 1
    except:  # after no more elements were found, reinsert the elements back in!
        [array.insert(i, element) for i in loc] 
    # print(loc)
    # print("Proof: ", [array[i] for i in loc])
    return loc




