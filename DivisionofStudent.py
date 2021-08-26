m1=int(input("Enter marks in subject 1: "));
m2=int(input("Enter marks in subject 2: "));
m3=int(input("Enter marks in subject 3: "));
m4=int(input("Enter marks in subject 4: "));
perc=(m1+m2+m3+m4)/4;
if(perc>=75):
    print("Division 1");
elif(perc>=65):
    print("Division 2");
elif(perc>=50):
    print("Division 3");
else:
    print("Failed");