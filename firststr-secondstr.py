str1 = input("Enter first string: ") 
str2 = input("Enter second string: ") 
a = list(set(str1)-set(str2)) 
print("The letters present in the first string but not in the second string are: ") 
for i in a: 
    print(i)
