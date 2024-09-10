def biggest_odd(s):
	max_odd = None
	for char in s:
		if int(char) % 2 != 0:
			if max_odd is None or int(char) > max_odd:
                		max_odd = int(char)
	return str(max_odd) if max_odd is not None else ""


s = "235569"
ans = biggest_odd(s)
 
# Function call
print(ans)





