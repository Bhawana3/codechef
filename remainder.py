# find the remainder od a number

n = input()
i = 0
while( i < n) :
	r = raw_input()
	intr = r.split()
	m = map(int , intr)
	rem = m[0] % m[1]
	print rem
	i += 1
