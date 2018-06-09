# Anne Harris
# CS 325 - 400
# Homework 5
# May 13, 2018

# create empty adjacency list
adjList = {}

# read in file
# found help reading file into adjacency list using link below
# https://stackoverflow.com/questions/43473918/how-to-read-txt-file-and-create-dictionary-with-adjacency-list-python

# FILE NAME TO CHANGE
fileName = "wrestler2.txt"

with open(fileName, "r") as f:
    # read in all of the lines
    lines = f.readlines()
    # get number of players
    num = int(lines[0])
    # get number of rivals
    numRivals = int(lines[num+1])
    # count for for loop
    count = 0
    # count for inner if statement
    innerCount = 1
    for x in lines:
        count +=1
        if count > num+2 and innerCount <= numRivals:
            var = x.strip('\n')
            var = var.split(" ")
            # add to adjacency list
            adjList.setdefault(var[0],[]).append(var[1])
            adjList.setdefault(var[1],[]).append(var[0])
            innerCount += 1

# Print statement to check adjacency list
# print("AdjList: ", adjList)

# define teams
babyFaces = []
heel = []

# implement Breadth - first search to touch every node
# if distance from top is even make them a baby face
# if distance from top is odd make them a heel
# Implementation help from the link below
# https://stackoverflow.com/questions/46383493/python-implement-breadth-first-search
def BFS(graph, source):
    # list for all explored vertexes that we are done checking
    doneChecking = []
    # nodes to be checked
    queue = [source]
    # dictionary to keep track of the depth of each vertex for determining team
    depth = {}
    # initialize first vertex to 0 and visited
    depth[source] = 0
    visited = [source]

    # while there are vertices in the queue
    while queue:
        # remove vertex from the queue
        vertex = queue.pop(0)
        # add vertex to the done checking list
        doneChecking.append(vertex)
        #if the depth is even, add to baby faces
        if depth[vertex]%2 == 0:
            babyFaces.append(vertex)
        # if depth is odd add to heels
        else:
            heel.append(vertex)

        # get neighbors
        neighbors = graph[vertex]
        # add neighbors of vertex to queue
        for neighbor in neighbors:
            # if the neighbor has not been visited, add to the queue and visited list
            if neighbor not in visited:
                queue.append(neighbor)
                visited.append(neighbor)
                depth[neighbor] = depth[vertex]+1

    # return the vertices we've checked
    return doneChecking

# use key of first key in the adjacency list
key = list(adjList.keys())[0]
# call breadth-first search to check nodes and store in list called "checked"
checked = BFS(adjList, key)
# check to see if any other keys (vertices) weren't in the search
i = 0
for keys in adjList:
    if keys in checked:
        i += 1
    else:
        # call BFS from the new, unvisited key
        key2 = list(adjList.keys())[i]
        checked2 = BFS(adjList,key2)
        # add to checked list
        for x in checked2:
            checked.append(x)
        i += 1

# determine number of players in each group
numBabyFaces = len(babyFaces)
numHeels = len(heel)

# print results
if numBabyFaces == numHeels:
    print("Yes, possible")
    print("Baby Faces: ", babyFaces)
    print("Heels: ", heel)
else:
    print("Not possible")
