print('Кравченко О.О. ІС-93 Лабораторна рoбота №6 Варіант 13')

firstNum = float(input('Enter number s: ')) # S initialization
secondNum = float(input('Enter number t: ')) # P Initialization

def formula (a, b): # Formula for h(a, b)
    return (a / (1 + b**2)) + (b / (1 + a**2)) - (a - b)**3

number1 = formula(firstNum - secondNum, firstNum * secondNum)**2 # First number for searching max number
number2 = formula(firstNum - secondNum, firstNum * secondNum)**4 # Second number for searching max number

print("First number for comparing: %0.4f" %number1)
print("Second number for comparing: %0.4f" %number2)

if number1 > number2: # Searching max number
    maximum = number1
else: 
    maximum = number2

print("Max number: %0.4f" %maximum)

result = formula(firstNum, secondNum) + maximum + formula(1, 1) # Our final formula

print('Our result = %0.4f' %result)
