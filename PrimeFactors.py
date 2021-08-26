def prime_factors(x):
    l=[]
    for i in range(1,x):
        if x%i==0:
            if i>2:
                for j in range(2,i):
                    if (i%j) == 0:
                        break
                else:
                    l.append(i)
    l=tuple(l)
    return l

lst=[]
lst=input("Enter the numbers separated by spaces:").split(" ")
for i in range(len(lst)):
    lst[i]=int(lst[i])
d={}
for k in lst:
    d[k]=prime_factors(k)
print(d)