

def factor(n) :
	factors = []
	for i in range(1,n+1) :
		if n % i == 0 :
			factors.append(i)
	return factors


def HCF(x,y) :
	diff = abs(x - y)
	m = factor(diff)
	h = []
	for i in m :
		if (x % i == 0 and y % i ==0) :
			h.append(i)
	return max(h)


def LCM(x,y) :
	if x % y == 0 :
		return x
	elif y % x == 0 :
		return y
	else :
		small = min(x,y)
		i = small
		while ( i <= x*y) :
			if (i % x == 0 and i % y == 0 ) :
				return i
				break
			i += 1
n = input()
l = []
i = 0
while (i<n) :
	r = raw_input()
	a,b = map(int,r.split())

	print HCF(a,b) , LCM(a,b)
	i += 1
