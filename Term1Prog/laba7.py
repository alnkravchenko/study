import random

print('Кравченко О.О. ІС-93 Лабораторна рoбота №7 Варіант 13')

array = [] # C(n)
modificatedArray = [] # F(n)
modificatedNumber = 0 
amount = 0 # Amount of negative elements in array
summary = 0 # Summary of negative numbers from array
average = 0. # Average of negative numbers from array

def input_size():  # Inputs size of array C(n)
    capacity = int(input("Enter size of array C(n): "))
    return capacity

def creating_array(capacity):  # Creates array with random integers
    for index in range(capacity):  # Loop for filling array with random numbers from -100 to 100
        array.append(random.randint(-100, 100))
    print("Our primary array:", array)

def solution(capacity):  # Algorithm from the task4
    global amount, summary, average
    for number in array:  # Loop for searching negative numbers in array
        if number < 0:
            summary += number
            amount += 1  # Amount of negative elements in array
    average = abs(summary / amount)
    print("Average of negative numbers: ", average)

    for count in range((capacity // 2) + 1):  # Loop with even indexes of array
        modificatedNumber = array[2*count] * average  # Formula from task
        modificatedArray.append(int(modificatedNumber))

def output():  # Outputs the result
    print("F(n) =", modificatedArray)

size = input_size()
creating_array(size)
solution(size)
output()
