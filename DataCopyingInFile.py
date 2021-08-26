f = open ("marks.txt")
f1 = open ("new.txt", "w") 
for i in f: 
    sum=0 
    x=[] 
    x=i.split() 
    x=[int(j) for j in x] 
    for k in x: 
        sum=sum+k 
    if (((sum-x[0])/5) > 65): 
        f1.write(i) 
print ("The marksheet and id of students above 65 percent are: ") 
f2 = open("new.txt") 
l = f2.readlines() 
for y in l: 
    print(y)