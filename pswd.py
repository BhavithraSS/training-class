pasw='PAssword1!!'

S = ['!','@','#','$','%','~','`','^','&','*','(',')','_','+','=','-']
upper,lower,number,special = 0,0,0,0

for n in pasw:
    if n.islower():
        lower=1
    if n.isnumeric():
        number=1
    if n.isupper():
        upper+=1
    if n in S:
        special+=1

if len(pasw) >= 6 and len(pasw) <= 12 and lower > 0 and number > 0 and special > 1 and upper > 1:
    print('OK')
else:
    print('TRY LATER')
