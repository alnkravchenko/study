
print('Кравченко О.О. ІС-93 Лабораторна рoбота №5 Варіант 13')

firstNum = int(input('Enter number p: ')) # p initialization 
secondNum = int(input('Enter number q: ')) # q initialization
dividers = [] # List with all needed dividers

for part in range(firstNum + 1): # Loop for searching dividers
    divider = part + 1 # Because loop starts from 0
    if firstNum % divider == 0 and secondNum % divider != 0 and divider % secondNum != 0: # Conditions for divider of first number and for checking coprime numbers (divider and second number)
        dividers.append(str(divider)) # Add divider into list of all dividers
print('All dividers for p and coprime numbers for q:', ', '.join(dividers))
