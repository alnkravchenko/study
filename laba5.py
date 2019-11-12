print('Кравченко О.О. ІС-93 Лабораторна рoбота №5 Варіант 13')

firstNum = int(input('Enter number p: ')) # p initialization
secondNum = int(input('Enter number q: ')) # q initialization
result = [] # List with all needed dividers

def dividers (number):  # Function for searching dividers
    divArray = []
    for divider in range(number + 1): # Loop for searching number's dividers
        if number % (divider + 1) == 0: # Condition for number's divider
            divArray.append(divider + 1)
    return set(divArray)

firstNumDividers = dividers(firstNum)  # All p's dividers
firstNumDividers.remove(1)  # Because first divider is always"1"
secondNumDividers = dividers(secondNum)  # All q's dividers
secondNumDividers.remove(1)  # Because first divider is always "1"

for element in firstNumDividers:  # Loop for searching dividers of p's divider
    elementDividers = dividers(element)
    if not elementDividers & secondNumDividers:  # Finding common dividers
        result.append(str(element))  # Add divider into list of all dividers

print('All dividers for p and coprime numbers for q:', ', '.join(result))
