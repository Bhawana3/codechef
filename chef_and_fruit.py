
def difference(List) :
	n = List[0]
	m = List[1]
	k = List[2]
	while (k > 0):
		if n > m :
			m = m + 1
		else :
			n = n + 1
		k = k - 1
	return abs(n-m)

n = input()
i = 0
f = []
while (i < n) :
	fruits = raw_input()
	fruit_list = map(int,fruits.split())
	f.append(fruit_list)
	i += 1

for diff in f :
	print difference(diff)
	 
			
