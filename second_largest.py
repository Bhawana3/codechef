# find the second largest from three numbers

n = input()
i = 0
while (i < n) :
	num = raw_input() 	 # enter 3 numbers separated by space
	string_list = num.split()
	num_list = map(int , string_list)
	a = num_list[0]
	b = num_list[1]
	c = num_list[2]
	if a > b and a > c :
		if b > c :
			print b
		else :
			print c
	elif a < b and a < c :
		if b > c :
			print c
		else :
			print b
	else :
		print a
	i += 1
