while (True):
    x=int(input("Menu \n1) Number of student in a dept \n2) Maximum marks in a dept \n3) Search student details with Name \n4) Search student details with Roll number \n5) Exit"))
    if x==1:
        with open("student.txt",'r') as f1:
            dept=input("Enter the Department: ")
            lst=f1.readlines()
            n=0
            for i in range(len(lst)):
                if lst[i][0]=='R':
                    continue
                else:
                    s=lst[i].split()
                    if dept==s[len(s)-1]:
                        n+=1
            if n==0:
                print("No student found!!")
            else:
                print("Total number of students in the department is: "+str(n))
    
    elif x==2:
       with open("student.txt",'r') as f2:
            dept=input("Enter the Department: ")
            lst=f2.readlines()
            mm=0
            for i in range(len(lst)):
                if lst[i][0]=='R':
                    continue
                else:
                    s=lst[i].split()
                    if dept==s[len(s)-1]:
                        if mm < int(s[len(s)-2]):
                            mm=int(s[len(s)-2])
            print("Max marks in the department is: "+str(mm))
            
    elif x==3:
        with open("student.txt",'r') as f3:
            lst=f3.readlines()
            name=input("Enter the Name: ")
            for i in range(len(lst)):
                if lst[i][0]=='R':
                    continue
                else:
                    s=lst[i].split()
                    if name==s[1]:
                        print(lst[i])
                        break
            else:
                print("Student detail has not been found!!!")
    elif x==4:
        with open("student.txt",'r') as f4:
            lst=f4.readlines()
            roll=int(input("Enter the Roll Number: "))
            for i in range(len(lst)):
                if lst[i][0]=='R':
                    continue
                else:
                    s=lst[i].split()
                    if roll==int(s[0]):
                        print(lst[i])
                        break
            else:
                print("Student detail has not been found!!!")

    elif x==5:
        break
    
    else:
        print("Please enter a valid option!!")
