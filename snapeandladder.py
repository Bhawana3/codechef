import math

n = input()
i = 0
while (i<n) :
	ladders = raw_input()
	ladders_list = map(int,ladders.split())

	B = ladders_list[0]
	LS = ladders_list[1]

	min_RS = math.sqrt(abs((LS*LS) - (B*B)))
	max_RS = math.sqrt(abs((LS*LS) + (B*B)))
	
	print min_RS,max_RS
	
	i += 1
