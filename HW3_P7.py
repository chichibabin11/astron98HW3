#Vowels: takes string and output number of vowels
def vowels(n):
    vowel = ("a", "i" , "u", "e", "o" , "A", "I", "U", "O", "E")
    i = 0 
    for words in n:
        if words in vowel:
            i = i + 1
    return i 
