# add first and last digit of a number

n = input()
i = 0
while ( i < n ) :
	r = raw_input()
	print (int(r[0]) + int(r[-1]))  
	i = i + 1
