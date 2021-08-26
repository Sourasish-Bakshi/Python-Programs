import numpy
import operator
import itertools

print("Enter the Roll, marks1, marks2, marks3, marks4 of the five students in a single line: ")
ele=list(map(int, input().split(" ")))
matrix=numpy.array(ele).reshape(5, 5)
print("The resultant Matrix is: ")
print(matrix)

stud0=matrix[0,1]+matrix[0,2]+matrix[0,3]
stud1=matrix[1,1]+matrix[1,2]+matrix[1,3]
stud2=matrix[2,1]+matrix[2,2]+matrix[2,3]
stud3=matrix[3,1]+matrix[3,2]+matrix[3,3]
stud4=matrix[4,1]+matrix[4,2]+matrix[4,3]

d= {"Roll 1":stud0, "Roll 2":stud1, "Roll 3":stud2, "Roll 4:":stud3, "Roll 5":stud4}
sort=dict(sorted(d.items(), key=operator.itemgetter(1),reverse=True))
top5=dict(itertools.islice(sort.items(), 5))
print("The top 5 students and the sum of their marks of the first 3 subjects is: ",top5)
