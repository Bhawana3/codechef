# find the minimum number of squares can be formed from the rectangle.


def multiples(n) :
	multiple = []
	for i in range(1,n+1) :
		if n % i == 0 :
			multiple.append(i)
	return multiple


def HCF(x,y) :
	diff = abs(x - y)
	m = multiples(diff)
	h = []
	for i in m :
		if (x % i == 0 and y % i ==0) :
			h.append(i)
	return max(h)
 
n = input()
i = 0
while (i < n) :
	r = raw_input()
	x,y = map(int,r.split())
	num = HCF(x,y)
	print ((x/num)*(y/num))
	
	i += 1
