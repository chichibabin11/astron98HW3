#Rotating Digits: input n rotate to the right one position 12345-> 51234
def rotate_digits(n):
    last_digit = n % 10 # get the last digit to be put in front
    remaining_digits = n // 10
    number = 0
    rem = remaining_digits
    
    while rem > 0:  #loops until rem = 0 then the number will count for how many digits were removed
        rem //= 10
        number = number + 1
    rotated_number = last_digit * (10 ** number) + remaining_digits
    return rotated_number