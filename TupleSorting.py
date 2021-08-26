flag=1
l=[]
l1=[]
while(flag):
    choice='y'
    t=[]
    while(choice != 'n'):
        ele = int(input("Enter elements in the tuple:"))
        t.append(ele)
        choice = input("Press n to stop adding more elements to this tuple else press y: ")
    l1.append(t[1])
    t1=tuple(t)
    l.append(t1)
    flag=int(input("Press 1 to continue adding tuples, else press 0: "))

l1.sort()

print("The list of tuples sorted by the second element of each tuple is:")
for num in l1:
    for each in l:
        if (num == each[1]):
            print(each)
