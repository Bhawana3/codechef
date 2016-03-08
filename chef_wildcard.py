# input 2 strings
# output 'Yes' or 'No' if they are equal

n = input()
i = 0
while (i < n) :
	s1 = raw_input()
	s2 = raw_input()
	j = 0
	while ( j < len(s1)) :
		if (s1[j] != s2[j]) :
			print 'No'
			break
		elif (s1[j] == '?' or s2[j] == '?') or (s1[j] == s2[j]):
			j += 1
			print 'Yes'
	i += 1
