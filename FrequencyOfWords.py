str=input ("Enter a string: ")
lst=[]
dict={}
lst=str.split(" ")
for each in lst:
    if (each in dict.keys()):
        dict[each]+=1
    else:
        dict[each]=1

print(dict)
