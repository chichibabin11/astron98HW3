#power of a number
def power(x,y):
    result = 1
    for i in range(y):
        result *= x
    return result

#test case
x = 2
y = 3
print(power(x,y))