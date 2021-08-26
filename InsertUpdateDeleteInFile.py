while (True):
    x=int(input("Menu \n1)Insert \n2)Update \n3)Delete \n4)Exit \n\nEnter your choice: "))
    if x ==1:
        with open("student.txt",'a') as f:
            s=input("Enter your details in this format- Roll Number  Name  Address  Phone Number  HS Marks  Department")
            f.write('\n'+s)
    elif x== 2:
        f3 = open("student.txt", "r")
        lst = f3.readlines()
        line=int(input("Enter the line number which you want to change: "))
        s3=input("Enter the updated detail: ")
        lst[line-1] = s3+"\n"
        f3 = open("student.txt", "w")
        f3.writelines(lst)
        f3.close()
    elif x==3:
        with open("student.txt",'r') as f:
            lst=f.readlines()
            r=int(input("Enter the Roll Number "))
            for i in range(len(lst)):
                if lst[i][0]=='R':
                    continue
                else:
                    if r==int(lst[i][:3]):
                        s=lst[i]
                        lst.remove(s)
                        with open("student.txt",'w') as f:
                            f.writelines(lst)
                        break
                    else:
                        print("Not Found!")
    elif x==4:
        break
    else:
        print("Not a valid option!")
    
