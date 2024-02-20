#Digital Root: takes integer and returns sum of digits
def digital_roots(n):
    digits = str(n)
    sum = 0
    for digit in digits:
        sum = sum + int(digit)
    return sum