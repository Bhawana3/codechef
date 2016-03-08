# add two numbers

n = input()
numlist = []
i = 0
while (i < n) :
	r = raw_input()
	rn = r.split()
	r1 = int(rn[0])
	r2 = int(rn[1])
	sum = r1 + r2
	numlist.append(sum)
	i = i + 1

for num in numlist :
	print num
