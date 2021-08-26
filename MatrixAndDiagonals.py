import numpy 
row=int(input("Enter the number of rows: ")) 
col=int(input("Enter the number of columns: ")) 

print("Enter the elements row wise in a single line: ") 
ele=list(map(int, input().split(" "))) 
matrix=numpy.array(ele).reshape(row, col) 
print("The Matrix is: ")
print(matrix) 

primary_diag=matrix.diagonal()
print("The Primary Diagonal is: ",primary_diag)
print("The maximum value in the primary diagonal is: ",max(primary_diag))
print("The minimum value in the primary diagonal is: ",min(primary_diag))

secondary_diag=numpy.fliplr(matrix).diagonal()
print("The Secondary Diagonal is: ",secondary_diag)
print("The maximum value i the secondary diagonal is: ",max(secondary_diag))
print("The minimum value in the secondary diagonal is:",min(secondary_diag))
