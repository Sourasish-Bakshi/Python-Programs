l1 = [] 
n1 = int(input("Enter size of list 1: ")) 
print("Enter the elements for the 1st list: ") 
for i in range(n1): 
    val = int(input()) 
    l1.append(val) 
l2 = [] 
n2 = int(input("Enter size of list 2: ")) 
print("Enter the elements for the 2nd list: ") 
for j in range(n2): 
    val = int(input()) 
    l2.append(val) 
union = list(set().union(l1, l2)) 
print("The union is: ", union) 
