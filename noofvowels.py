word=input ("Enter the Word: ");
count=0;
vowels=["A","a","E","e","I","i","O","o","U","u"];
for letter in word:
		if (letter in vowels):
			count+=1;
print("Number of vowels is:",count);