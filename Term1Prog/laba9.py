
def input_string():  # Input string and symbols to find
    uString = input('Enter your string: ')
    symbols = input('Enter symbols: ')
    return uString, symbols

def solution(string, symbol):  # Solution of the task
    result = []
    for word in string.split(): # Check every word in string
        end = len(word) - len(symbol)
        if word[0:len(symbol)] == word[end:] and word[0:len(symbol)] == symbol: # Conditions from the task
            result.append(word)
    return result

def output(array):  # Output the results
    print('Words:', ' '.join(array))

usersString, usersSymbol = input_string()
processed = solution(usersString, usersSymbol)
output(processed)
