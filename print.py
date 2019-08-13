def fun(s):
    for i in s:
        print('\n', i)
        if any(letter.isalnum() for letter in i):
            print('Alnum', True)
        if any(letter.isalpha() for letter in i):
            print('Alpha', True)
        if any(letter.isdigit() for letter in i):
            print('Digit', True)
        if any(letter.isupper() for letter in i):
            print('Upper', True) 
        if any(letter.islower() for letter in i):
            print('Lower', True)

s = input().split()
fun(s)
