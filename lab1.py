# initializing string
given_str = "Howard University was founded in 1867" 
# frequency of each element in string 
freq = {} 
for i in given_str: 
 if i in freq: 
 
freq[i] += 1
 else:
 
freq[i] = 1
# printing result 
print("Count the frequency of all characters in example :\n "+ str(freq))
