lst=[]
n=int(input("Enter number of elements:"))
print("Enter the elements:")
for i in range(0,n):
    ele=int(input())
    lst.append(ele)

lst2=[]
for i in lst:
    if i not in lst2:
        lst2.append(i)

print("The list after deleting duplicates is:",lst2)