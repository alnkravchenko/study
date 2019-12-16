import random

print('Кравченко О.О. ІС-93 Лабораторна рoбота №8 Варіант 13')

originalArray = []  # Array with random numbers
modifiedArray = []  # Result of modifying originalArray in loops
matrix = []  # Modified matrix from the task
array = []
flag = False  # Flag for breaking the loop when condition from our task is true

def input_size():  # Input size of matrix
    number = int(input('Enter size of matrix: '))
    return number

def create_matrix(capacity):  # Creating matrix from the task
    # Row with random real numbers with 2 digits after the dot
    for index in range(capacity):
        originalArray.append(round(random.uniform(-100.0, 100.0), 2))

    print('Original array:', originalArray)

    modifiedArray = originalArray.copy()
    matrix.append(originalArray)
    for row in range(capacity):
        if modifiedArray[0] != originalArray[-1]:  # Condition from our task
            modifiedArray.append(modifiedArray.pop(0))
            array = modifiedArray.copy()
            matrix.append(array)
            print(f'{row+1} changing: {array}')

def output_matrix():  # Output matrix
    print('Our matrix:')
    for row in matrix:
        print('|', end=' ')
        for number in row:
            print('%6.2f' % number, end=' ')
        print('|')


size = input_size()
create_matrix(size)
output_matrix()
