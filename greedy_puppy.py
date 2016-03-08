n = input()
i = 0
while (i < n) :
	r = raw_input()		# enter 2 numbers separated by space
	r_list = map(int,r.split())
	coins = r_list[0]
	people = r_list[1]
	maximum = 0
	while (people > 1) :
		if maximum < (coins % people) : 
			maximum = (coins % people)	
		people -= 1
	print maximum
	i += 1
