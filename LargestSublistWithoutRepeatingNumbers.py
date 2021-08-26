lst=[]
lst=input("Enter the numbers separated by spaces: ").split(" ")
for i in range(len(lst)):
    lst[i]=int(lst[i])
a=[]
k=0
b=[0,[]]
d={}
for i in range(len(lst)):
    if not(lst[i] in lst[:k]):
        a.append(lst[i])
        k=k+1
    else:
        d[tuple(a)]=len(a)
        k=0
        a=[]
d[tuple(a)]=len(a)
for i,j in d.items():
    if j > b[0]:
        b[0]=j
        b[1]=i
print(list(b[1]))