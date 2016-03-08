

n = input()
i = 0
while (i < n) :
	p = input()
	j = 0
	total = 0
	while (j < p) :
		size = raw_input()
		size_int = map(int,size.split())
		if len(size_int) > 1 :
			large = max(size_int)
			total = total + large
		j += 1
	print total
	i += 1
		
