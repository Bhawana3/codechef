# calculate the minimum number of operations required to find the minimum

n = input()
i = 0
while ( i < n ) :
	size = input()   	# enter a number
	r = raw_input()		# enter space separated numbers equal to the size 
	List = map(int,r.split())
	count = 0
	while True :
		mini = min(List[0:2])
		count += mini
		List.remove(max(List[0:2]))
		if len(List) == 1 :
			break
	print count
	i += 1
