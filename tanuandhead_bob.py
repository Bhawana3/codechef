# First line contains T, number of people observed by Tanu.
#Each person is described in two lines. First line of the description contains a single integer N, the number of gestures recorded for this person. Next line contains a string of N characters, each character can be "Y", "N" or "I".


n = input()
i = 0
while (i < n) :
	N = input()
	r = raw_input()
	if len(r) == N :
		if ('I' in r):
			print 'INDIAN'
		elif ('Y' in r): 
			print 'NOT INDIAN'
		elif ('Y' not in r) and ('I' not in r):	
			print 'NOT SURE'
	i += 1
