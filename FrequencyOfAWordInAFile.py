fname = input ("Enter the name of the file: ") 
words = input ("Enter the word to be searched: ") 
count=0 
f= open (fname, 'r')
for i in f:
    word = i.split(" ") 
for j in word: 
    if(j==words): 
        count=count+1 
print ("Number of occurrences of the word: ", count)
