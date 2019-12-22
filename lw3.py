from prettytable import PrettyTable

data = []  # Array with connected vertices and amount of vertices, ribs
dataPairs = []
verticesPairs = []  # Array with pairs of connected vertices

wideEntry = int(input('Please choose vertex (>0): '))
deepEntry = int(input('Please choose vertex (>0): '))

# Get information from the file data.txt
for line in open('data.txt'):  # Read file and input all data to dataPairs[]
    dataPairs.append(line.split())
    for index in line:
        if not index.isspace():
            data.append(int(index))
verticesPairs = [[int(j) for j in i] for i in dataPairs]
verticesPairs = verticesPairs[1:]

# Create adjacency matrix of directed graph
matrixAdj = [[0] * data[0] for i in range(data[0])]  # Create matrix with 0's
for number in verticesPairs:
    matrixAdj[number[0] - 1][number[1] - 1] = 1  # Add 1 to row of first vertex


# WIDE

queue = []  # List with all used vertices
queue.append(wideEntry - 1)
queueModified = queue.copy()  # List with queue of directed graph
bfsNumber = 1  # Number of iterations with adding vertices
queueOut = [[wideEntry - 1]]  # Matrix with all iterations

for vertex in queue:
    for index, number in enumerate(matrixAdj[queueModified[0]]):
        if number == 1 and not index in queue:  # Conditions for searching unique vertex
            queueModified.append(index)
            queue.append(index)
            bfsNumber += 1
            array = queueModified.copy()
            queueOut.append(array)

    queueModified.pop(0)
    array = queueModified.copy()
    queueOut.append(array)


# DEEP
stack = []  # List with queue of directed graph
stack.append(deepEntry - 1)
stackModified = stack.copy()  # List with queue of directed graph
dfsNumber = 1  # Number of iterations with adding vertices
stackOut = [[deepEntry - 1]]  # Matrix with all iterations

for vertex in range(data[0]):
    previousQueueVertex = stackModified[-1]
    for index, number in enumerate(matrixAdj[stackModified[-1]]):
        if number == 1 and not index in stack:  # Conditions for searching unique vertex
            stackModified.append(index)
            stack.append(index)
            dfsNumber += 1
            array = stackModified.copy()
            stackOut.append(array)
            break  # Because we are looking not in depth but in breadth

    while previousQueueVertex != stackModified[-1]:  # If there are no adjusted vertices anymore then delete last number from stack
        previousQueueVertex = stackModified[-1]
        for index, number in enumerate(matrixAdj[stackModified [-1]]):
            if number == 1 and not index in stack:  # Conditions for searching unique vertex
                stackModified.append(index)
                stack.append(index)
                dfsNumber += 1
                array = stackModified.copy()
                stackOut.append(array)
                break  # Because we are looking not in depth but in breadth

    stackModified.pop(-1)
    array = stackModified.copy()
    stackOut.append(array)


# Print on screen
queueOutStr = [[str(x + 1) for x in row] for row in queueOut]
queueOutStr[-1] = ['_']
stackOutStr = [[str(x + 1) for x in row] for row in stackOut]
stackOutStr[-1] = ['_']
count2 = '_'

count1 = 0
print('\nBFS: \n')
BFS = PrettyTable()
BFS.field_names = ['Vertex', 'BFS-number', 'All vertices']
for index, row in enumerate(queueOutStr):
    if len(row) > len(queueOut[index - 1]):  # If we didn't add vertex in this row
        count1 += 1
        BFS.add_row([row[-1], count1, ','.join(row)])
    else:
        try:
            BFS.add_row([count2, count2, ','.join(row)])
        except IndexError:  # If this is the last row
            BFS.add_row([count2, count2, count2])

print(BFS)

count1 = 0
print('\nDFS: \n')
DFS = PrettyTable()
DFS.field_names = ['Vertex', 'DFS-number', 'All vertices']
for index, row in enumerate(stackOutStr):
    if len(row) > len(stackOut[index - 1]):  # If we didn't add vertex in this row
        count1 += 1
        DFS.add_row([row[-1], count1, ','.join(row)])
    else:
        try:
            DFS.add_row([count2, count2, ','.join(row)])
        except IndexError:  # If this is the last row
            DFS.add_row([count2, count2, count2])

print(DFS)