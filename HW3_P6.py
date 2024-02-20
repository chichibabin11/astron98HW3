#functions to find min and max using for loop
def min_value(number):
    min_value = number[0]
    for num in number:
        if num < min_value:
            min_value = num
    return min_value

def max_value(number):
    max_value = number[0]
    for num in number:
        if num > max_value:
            max_value = num
    return max_value

#functions to find min and max using while loop
def min_value(number):
    min_value = number[0]
    i = 1
    while i < len(number):
        if number[i] < min_value:
            min_value = number[i]
        i = i + 1
    return min_value

def max_value(number):
    max_value = number[0]
    i = 1 
    while i < len(number):
        if number[i] > max_value:
            max_value = number[i]
        i = i + 1
    return max_value



