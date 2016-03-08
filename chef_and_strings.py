# compute minimal and maximal difference between two strings entered by user

n = input()
i = 0
while (i < n) :
	string1 = raw_input()
	string2 = raw_input()
	j = 0
	maximal = 0
	minimal = 0
	while (j < len(string1)) :
		if string1[j] == '?' or string2[j] == '?' :
			maximal += 1
		else:
			if string1[j] != string2[j] :
				maximal += 1
				minimal += 1
			else :
				minimal += 0
		j += 1
	print str(minimal) + ' ' + str(maximal)
	i += 1
