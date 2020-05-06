from collections import Counter

data = []  # Array with connected vertexes and amount of vertexes, ribs
dataPairs = []
vertexesPairs = []  # Array with pairs of connected vertexes

# Asking user
matrixEntry = int(input('Show incidence and adjacency matrixes?(yes-1, no-0) '))
degreeEntry = int(input('Show degree of a vertex of a graph?(yes-1, no-0) '))
specialVertexesEntry = int(input('Show hanging and isolated vertexes?(yes-1, no-0) '))

# Get information from the file
for line in open('data.txt'):  # Read file and input all data to dataPairs[]
    dataPairs.append(line.split( ))
    for index in line:
        if not index.isspace():
            data.append(int(index))
vertexesPairs = [[int(j) for j in i] for i in dataPairs]
vertexesPairs = vertexesPairs[1:]
vertexes = data[2:]  # Array with vertexes


# Incidence and adjacency matrixes
if matrixEntry:
    matrixOut = int(input('Show the result only on screen or write it to the file?(file-1, screen-0) '))

    matrixInc = [[0] * data[1] for i in range(data[0])]  # Create 2 matrix with 0's to fill them
    matrixAdj = [[0] * data[0] for i in range(data[0])]

    for index,number in enumerate(vertexesPairs):
        matrixInc[number[0] - 1][index] = -1
        matrixInc[number[1] - 1][index] = 1
        if number[0] == number[1]:  # If rib is a loop
            matrixInc[number[0] - 1][index] = 2

        matrixAdj[number[0] - 1][number[1] - 1] = 1  # Add 1 to row of first vertex
        matrixAdj[number[1] - 1][number[0] - 1] = 1  # Add 1 to row of second vertex

    matrixIncOut = '\n'  # Output for matrix
    for row in matrixInc:
        matrixIncOut += '|'
        matrixIncOut += ' '.join([x.rjust(2) for x in map(str, row)])
        matrixIncOut += '|\n'
    print('Incidence matrix:\n', matrixIncOut)

    matrixAdjOut = '\n'  # Output for matrix
    for row in matrixAdj:
        matrixAdjOut += '|'
        matrixAdjOut += ' '.join([x.rjust(2) for x in map(str, row)])
        matrixAdjOut += '|\n'
    print('Adjacency matrix:\n', matrixAdjOut)

    if matrixOut:  # Print on screen and write to user's file
        file = open(input('Enter path to file: '), 'a')
        file.write(f'Incidence matrix:\n{matrixIncOut}')
        file.write(f'Adjacency matrix:\n{matrixAdjOut}')
        file.close()


# Degree of a vertex of a graph
if degreeEntry:
    degreeOut = int(input('Show the result only on screen or write it to the file?(file-1, screen-0) '))
    degree = []  # Vertexes' degrees
    degreeValues = set()
    degreeFlag = False
    amountKeys = 0

    degree = Counter(vertexes)
    for keys in degree.items():  # If we have an isolated vertex 
        amountKeys +=1
    while data[0] > amountKeys:
        amountKeys += 1
        degree[amountKeys] = 0
    for value in degree.values():  # Check for regular graph
        degreeValues.add(value)
    if len(degreeValues) == 1:
        degreeFlag = True
    
    # Print on screen
    for key,value in degree.items():
        print(f'Degree of vertex {key} is {value}')

    if degreeFlag:
        print(f'This graph is regular, its degree is {value}')
    else:
        print('This graph isn\'t regular')
    if degreeOut:  # Print on screen and write to user's file
        file = open(input('Enter path to file: '), 'a')
        for key,value in degree.items():
            file.write(f'\nDegree of vertex {key} is {value}')

        if degreeFlag:
            file.write(f'\nThis graph is regular, its degree is {value}\n')
        else:
            file.write('\nThis graph isn\'t regular\n')
        file.close()


# Hanging and isolated vertexes
if specialVertexesEntry:
    # Create adjacency matrix
    vertexesOut = int(input('Show the result only on screen or write it to the file?(file-1, screen-0) '))
    matrixAdj = [[0] * data[0] for i in range(data[0])]
    for index,number in enumerate(vertexesPairs):
        matrixAdj[number[0] - 1][number[1] - 1] = 1  # Add 1 to row of first vertex
        matrixAdj[number[1] - 1][number[0] - 1] = 1  # Add 1 to row of second vertex

    zeroRow = [0 for count in range(data[0])]
    hangingList = []  # Indexes of hanging vertexes
    isolatedList = []  # Indexes of isolated vertexes

    for index,row in enumerate(matrixAdj):
        loopRow = [0 for count in range(data[0])]  # Row with vertex that only have a loop
        loopRow[index] += 1
        ribs = 0  # Amount of ribs
        if row == zeroRow or row == loopRow:
            isolatedList.append(str(index + 1))

        for element in row:
            if element == 1:
                ribs += 1
        if ribs == 1 and row != loopRow:
            hangingList.append(str(index + 1))
    # Print on screen
    if hangingList == []:
        print('There is no hanging vertexes')
    else:
        print('Hanging vertexes:', ', '.join(hangingList))
    if isolatedList == []:
        print('There is no isolated vertexes')
    else:
        print('Isolated vertexes:', ', '.join(isolatedList))

    if vertexesOut:  # Print on screen and write to user's file
        file = open(input('Enter path to file: '), 'a')
        if hangingList == []:
            file.write('\nThere is no hanging vertexes')
        else:
            file.write(f"\nHanging vertexes: {','.join(hangingList)}")
        if isolatedList == []:
            file.write('\nThere is no isolated vertexes')
        else:
            file.write(f"\nIsolated vertexes: {', '.join(isolatedList)}")
        file.close()
