import math

def gcd(a,b):
    if(a==0):
        return b
    else:
        return gcd(b%a, a)

def lcm(a): 
    val = a[0]
    for i in range(1,len(a)):
        val = val*a[i]//math.gcd(val, a[i])
    return val
  
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
GCD=gcd(a,b)
print("GCD is: ",GCD)

l=[]
n=int(input("Enter the number of elements for LCM: "))
print("Enter the elements:")
for i in range(n):
    ele=int(input())
    l.append(ele)

LCM=lcm(l)
print("LCM is: ",LCM)