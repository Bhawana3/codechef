# find the smallest pair

n = input()
i = 0
while( i < n ) :
	p = input()
	a = raw_input()
	a_list = map(int,a.split())
	List = []
	x = 0
	y = 1
	while (y < len(a_list)) :
		total = a_list[x] + a_list[y]
		List.append(total)
		x += 1
		y += 1
	i += 1
	print min(List)
