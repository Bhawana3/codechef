#find substring 'CHEF' in the string given by user

s = raw_input()
i =0
count = 0
while (i < len(s)) :
	sub = 'CHEF'
	if sub in s :
		s = s.remove(sub)
		count += 1
	i += 1
	print count
	
