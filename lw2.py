from numpy.linalg import matrix_power

dataUndir = []  # Array with connected verteces and amount of verteces, ribs for undirected graph
dataUndirPairs = []
vertecesUndirPairs = []  # Array with pairs of connected verteces for undirected graph

dataDir = []  # Array with connected verteces and amount of verteces, ribs for directed graph
dataDirPairs = []
vertecesDirPairs = []  # Array with pairs of connected verteces for directed graph

# Asking user
matrixUndirEntry = int(input('Show distance and reachability matrices of undirected graph?(yes-1, no-0) '))
matrixDirEntry = int(input('Show distance and reachability matrices of directed graph?(yes-1, no-0) '))

# Get information from the first file (data.txt)
for line in open('data.txt'):  # Read file and input all data to dataUndirPairs[]
    dataUndirPairs.append(line.split())
    for index in line:
        if not index.isspace():
            dataUndir.append(int(index))
vertecesUndirPairs = [[int(j) for j in i] for i in dataUndirPairs]
vertecesUndirPairs = vertecesUndirPairs[1:]
vertecesUndir = dataUndir[2:]  # Array with verteces of undirected graph

# Get information from the second file (data2.txt)
for line in open('data2.txt'):  # Read file and input all data to dataDirPairs[]
    dataDirPairs.append(line.split())
    for index in line:
        if not index.isspace():
            dataDir.append(int(index))
vertecesDirPairs = [[int(j) for j in i] for i in dataDirPairs]
vertecesDirPairs = vertecesDirPairs[1:]
vertecesDir = dataDir[2:]  # Array with verteces of directed graph


# UNDIRECTED GRAPH

# Create adjacency matrix of undirected graph
matrixAdjUndir = [[0] * dataUndir[0] for i in range(dataUndir[0])]  # Create matrix with 0's
for number in vertecesUndirPairs:
    matrixAdjUndir[number[0] - 1][number[1] - 1] = 1  # Add 1 to row of first vertex
    matrixAdjUndir[number[1] - 1][number[0] - 1] = 1  # Add 1 to row of second vertex

# Create distance matrix of undirected graph
disUndir = [[0] * dataUndir[0] for i in range(dataUndir[0])]  # Create matrix with 0's
nonZeroCells = []  # List with previous nonzero cells to skip them while we are looking for nonzero values on next iteration
for count in range(dataUndir[0]):  # Take the nth degree (n = number of verteces) of the adjacency matrix and look for nonzero values
    matrixDis = matrix_power(matrixAdjUndir, count + 1)
    for row in range(len(matrixDis)):
        for column in range(len(matrixDis)):
            if matrixDis[row][column] != 0 and not [row, column] in nonZeroCells:
                disUndir[row][column] = count + 1
                nonZeroCells.append([row, column])

for count in range(dataUndir[0]):
    disUndir[count][count] = 0  # Main diagonal always 0


# Distance and reachability matrices of undirected graph
if matrixUndirEntry:
    matrixOut = int(input('Show the result only on screen or write it to the file?(file-1, screen-0) '))

    # Create reachability matrix
    reachUndir = [[0] * dataUndir[0] for i in range(dataUndir[0])]  # Create matrix with 0's
    for row in range(len(reachUndir)):
        for column in range(len(reachUndir)):
            if disUndir[row][column] != 0:
                reachUndir[row][column] = 1

    for count in range(dataUndir[0]):
        reachUndir[count][count] = 1  # Main diagonal always 1

    # Print on screen
    disUndirOut = '\n'
    for row in disUndir:
        disUndirOut += '|'
        disUndirOut += ' '.join([x.rjust(2) for x in map(str, row)])
        disUndirOut += ' |\n'

    reachUndirOut = '\n'
    for row in reachUndir:
        reachUndirOut += '|'
        reachUndirOut += ' '.join([x.rjust(2) for x in map(str, row)])
        reachUndirOut += ' |\n'

    print('\nUNDIRECTED GRAPH'
          f'\nDistance matrix:\n{disUndirOut}\n'
          f'Reachability matrix:\n{reachUndirOut}\n')

    # Print on screen and write to user's file
    if matrixOut:
        file = open(input('Enter path to file: '), 'a')
        file.write('\nUNDIRECTED GRAPH')
        file.write(f'\nDistance matrix:\n{disUndirOut}\n')
        file.write(f'Reachability matrix:\n{reachUndirOut}\n')
        file.close()


# Radius, diameter, center, tiers of graph

connectivity = True

for row in reachUndir:  # If there is at least 1 isolated vertex, then graph is disconnected
    if 0 in row:
        connectivity = False

if connectivity:
    # Diameter search
    maxSum = 0  # Sum of distances
    diameter = 0
    zeroRow = [0 for i in range(dataUndir[0])]  # Row of isolated vertex
    farVertex = None
    for index, row in enumerate(disUndir):  # Looking for the farthest vertex (its sum of   distances is the biggest one)
        if maxSum < sum(row):
            maxSum = sum(row)
            farVertex = index
    for distance in disUndir[farVertex]:
        if diameter < distance:
            diameter = distance

    # Radius search
    radius = 0
    minSum = maxSum
    nearVertex = None
    for index, row in enumerate(disUndir):  # Looking for the nearest vertex - our center (its sum  of distances is the smallest one)
        if minSum > sum(row) and row != zeroRow:
            minSum = sum(row)
            nearVertex = index
    for distance in disUndir[nearVertex]:
        if radius < distance:
            radius = distance

    # Tiers search for all verteces
    allTiers = []
    for vertex,row in enumerate(disUndir):
        vertexTiers = [[] * max(row) for i in range(max(row))]
        for index, distance in enumerate(row):
            if distance != 0:
                vertexTiers[distance - 1].append(str(index + 1))
        allTiers.append(vertexTiers)

# Print on screen
    tiersOut = '\n'
    for position, row in enumerate(allTiers):
        tiersOut += 'Tiers of vertex ' + str(allTiers.index(row) + 1)
        if row != []:  # row = [] - there are no connected verteces
            for index, array in enumerate(row):
                tiersOut += f'\nVerteces of {index + 1} tier: ' + ', '.join(array)
        else:
            tiersOut += '\nThere are no tieres because it\'s isolated vertex'
        if position + 1 != len(allTiers):
            tiersOut += '\n\n'
        else:
            tiersOut += '\n'
    print('\nUNDIRECTED GRAPH'
          f'\nRadius of graph: {radius}'
          f'\nDiameter of graph: {diameter}'
          f'\nCenter of graph is vertex {nearVertex + 1}')
    print(tiersOut)
else:
    print('\nUNDIRECTED GRAPH'
          '\nIt\'s a disconnected graph so there is no radius, diameter and center of graph\n')


# DIRECTED GRAPH

# Create adjacency matrix of directed graph
matrixAdjDir = [[0] * dataDir[0] for i in range(dataDir[0])]  # Create matrix with 0's
for number in vertecesDirPairs:
    matrixAdjDir[number[0] - 1][number[1] - 1] = 1  # Add 1 to row of first vertex

# Create distance matrix of directed graph
disDir = [[0] * dataDir[0] for i in range(dataDir[0])]  # Create matrix with 0's
nonZeroCells = []  # List with previous nonzero cells to skip them while we are looking for nonzero values on next iteration
for count in range(dataDir[0]):  # Take the nth degree (n = number of verteces) of the adjacency matrix and look for nonzero values
    matrixDis = matrix_power(matrixAdjDir, count + 1)
    for row in range(len(matrixDis)):
        for column in range(len(matrixDis)):
            if matrixDis[row][column] != 0 and not [row, column] in nonZeroCells:
                disDir[row][column] = count + 1
                nonZeroCells.append([row, column])
            elif matrixDis[row][column] == 0 and not [row, column] in nonZeroCells:
                disDir[row][column] = 'inf'  # inf = infinity
for count in range(dataDir[0]):
    disDir[count][count] = 0  # Main diagonal always 0

# Create reachability matrix
reachDir = [[0] * dataDir[0]
              for i in range(dataDir[0])]  # Create matrix with 0's
for row in range(len(reachDir)):
    for column in range(len(reachDir)):
        if disDir[row][column] != 0 and disDir[row][column] != 'inf':
            reachDir[row][column] = 1
for count in range(dataDir[0]):
    reachDir[count][count] = 1  # Main diagonal always 1

if matrixDirEntry:
    matrixDirOut = int(input('Show the result only on screen or write it to the file?(file-1, screen-0) '))

    # Print on screen
    disDirOut = '\n'
    for row in disDir:
        disDirOut += '|'
        disDirOut += ' '.join([x.rjust(3) for x in map(str, row)])
        disDirOut += ' |\n'

    reachDirOut = '\n'
    for row in reachDir:
        reachDirOut += '|'
        reachDirOut += ' '.join([x.rjust(2) for x in map(str, row)])
        reachDirOut += ' |\n'

    print('\nDIRECTED GRAPH'
          f'\nDistance matrix:\n{disDirOut}\n'
          f'Reachability matrix:\n{reachDirOut}\n')

    # Print on screen and write to user's file
    if matrixDirOut:
        file = open(input('Enter path to file: '), 'a')
        file.write('\nDIRECTED GRAPH')
        file.write(f'\nDistance matrix:\n{disDirOut}\n')
        file.write(f'Reachability matrix:\n{reachDirOut}\n')
        file.close()


# Type of connectivity:
typeConnect = ''

# Condition for strong graph

oneMatrix = [[1] * dataDir[0] for i in range(dataDir[0])]  # Create matrix with 1's
if reachDir == oneMatrix:
    typeConnect = 'a strongly connected'

# Condition for unilateral graph

reachDirTrans = [[reachDir[j][i] for j in range(len(reachDir[0]))] for i in range(len(reachDir))]  # [[11, 12, 13], [21,22,23], [31,32,33]] --> [[11,21,31], [12,22,32], [13,23,33]]
unilateralMatrix = [[0] * dataDir[0] for i in range(dataDir[0])]

for index, row in enumerate(reachDir):
    for column in range(len(row)):
        unilateralMatrix[index][column] = reachDir[index][column] + reachDirTrans[index][column]  # Sum of reachability and transposed reachability matrices
for count in range(dataDir[0]):
    unilateralMatrix[count][count] = 1  # Main diagonal always 1

connectivity2 = True
for row in unilateralMatrix:  # If there is no path between verteces at least in one direction, then graph isn't unilateral
    if 0 in row:
        connectivity2 = False
if connectivity2:
    typeConnect = 'an unilaterally connected'

# Condition for weakly conndected graph

# Create adjacency matrix of undirected graph with verteces from data2.txt
matrixAdjUndir2 = [[0] * dataDir[0]
                for i in range(dataDir[0])]  # Create matrix with 0's
for number in vertecesDirPairs:
    matrixAdjUndir2[number[0] - 1][number[1] - 1] = 1  # Add 1 to row of first vertex
    matrixAdjUndir2[number[1] - 1][number[0] - 1] = 1  # Add 1 to row of second vertex

# Create distance matrix of undirected graph with verteces from data2.txt
disUndir2 = [[0] * dataDir[0] for i in range(dataDir[0])]  # Create matrix with 0's
nonZeroCells2 = []  # List with previous nonzero cells to skip them while we are looking for nonzero values on next iteration

for count in range(dataDir[0]):  # Take the nth degree (n = number of verteces) of the adjacency matrix and look for nonzero values
    matrixDis2 = matrix_power(matrixAdjUndir2, count + 1)
    for row in range(len(matrixDis2)):
        for column in range(len(matrixDis2)):
            if matrixDis2[row][column] != 0 and not [row, column] in nonZeroCells2:
                disUndir2[row][column] = count + 1
                nonZeroCells2.append([row, column])
            elif matrixDis2[row][column] == 0 and not [row, column] in nonZeroCells2:
                disUndir2[row][column] = 'inf'  # inf = infinity
for count in range(dataDir[0]):
    disUndir2[count][count] = 0  # Main diagonal always 0

# Create reachability matrix
reachUndir2 = [[0] * dataDir[0]
            for i in range(dataDir[0])]  # Create matrix with 0's
for row in range(len(reachUndir2)):
    for column in range(len(reachUndir2)):
        if disUndir2[row][column] != 0 and disUndir2[row][column] != 'inf':
            reachUndir2[row][column] = 1
for count in range(dataDir[0]):
    reachUndir2[count][count] = 1  # Main diagonal always 1

connectivity3 = True
for row in reachUndir2:  # If there is at least 1 isolated vertex, then graph is disconnected
    if 0 in row:
        connectivity3 = False

if connectivity3:
    typeConnect = 'a weakly connected'
else:
    typeConnect = 'a disconnected'
print(f'\nThis is {typeConnect} directed graph')