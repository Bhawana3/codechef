

n = input()
i = 0
while (i < n) :
	numbers = raw_input()
	num_list = map(int,numbers.split())

	if num_list[0] > num_list[1] :
		print '>'
	elif num_list[0] < num_list[1] :
		print '<'
	else :
		print '='
	i += 1
