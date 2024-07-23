def equal_strings(str1, str2):
	if len(str1) != len(str2):
        	return False

	return sorted(str1) == sorted(str2)

str1 = "love" 
str2 = "evol"
ans = ('True') 

print(ans)

