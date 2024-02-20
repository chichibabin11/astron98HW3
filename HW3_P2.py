# Minimum and Maximum : takes list of number and return min max value as tuple
def min_max(numbers):
    min_value = max_value = numbers[0]
    for val in numbers:
        if val < min_value:
            min_value = val
        elif val > max_value:
            max_value = val
    return min_value, max_value 