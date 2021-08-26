import random
c1=c2=c3=c4=0
for i in range(0, 100):
	n=random.randint(101,200)
	print(n, end=" ")
	if n<126:
		c1+=1
	elif n<151:
		c2+=1
	elif n<176:
		c3+=1
	else:
		c4+=1

print("\nFrequency in the 1st range = ",c1)
print("Frequency in the 2nd range = ",c2)
print("Frequency in the 3rd range = ",c3)
print("Frequency in the 4th range = ",c4)