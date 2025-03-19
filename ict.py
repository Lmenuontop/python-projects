def rev(str1):
	rstr = ""
	i = len(str1)
	while i > 0:
		rstr += str1[i - 1]
		i = i - 1
	return rstr
print(rev("cow"))