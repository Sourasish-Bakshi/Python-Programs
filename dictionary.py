str=input ("Enter the Sentence: ")
str1=str.split(" ")
str1.sort()
vowels=['A','a','E','e','I','i','O','o','U','u']
for word in str1:
	count=0
	for letter in word:
		if (letter in vowels):
			count+=1
	print(word,':',count)
