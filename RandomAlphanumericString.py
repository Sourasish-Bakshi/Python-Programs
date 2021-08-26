import random
import string

def f1(x,y):
	return chr(random.randint(ord(x), ord(y)))

def alphanumstr(length):
    p = string.ascii_letters+string.digits
    result = ''.join((random.choice(p) for i in range(length)))
    lower = f1('a','z')
    num = str(random.randint(0,9))
    total = upper + lower + num + result
    print(total)

i=1
c=0
print("The 50 random alphanumeric strings are: ")

while i <= 50:
    upper = f1('A','Z')
    alphanumstr(3)
    if upper == 'A':
        c=c+1
    i+=1

print("The number of passwords starting with A are: ",c)