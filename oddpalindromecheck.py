def palindromecheck(s):
    if(s == s[::-1]):
        return True
    else:
        return False
def oddcheck(s):
    if(len(s)%2 != 0):
        return True
    else:
        return False
list1=[]
n = int(input("Enter the number of elements for the list: "))
print("Enter the palindromes: ")
for i in range(n):
    str= input().lower()
    flag=palindromecheck(str)
    if(flag==False):
        print("Please enter palindromes!!")
        i=i-1
        continue
    list1.append(str)
print("The palindromes with odd lengths are: ")
for i in list1:
    if(oddcheck(i)):
        print(i)