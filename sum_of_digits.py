#find the sum of digits entered

n = input()
i = 0
list_sum = []
while (i < n) :
	r = raw_input()
	total = 0
	j = 0
	for string in r :
		total = total + int(string)
	list_sum.append(total)
	i = i + 1

for t in list_sum :
	print t
