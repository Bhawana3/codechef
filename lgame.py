n = input()
lead = 0
p1 = 0
p2 = 0

for i in range(n) :
	x,y = raw_input().split()
	p1 = p1 + int(x)
	p2 = p2 + int(y)
	diff = abs(p1-p2)
	if lead < diff :
		lead = diff 
		if p1 < p2 :
			winner = 2
		else :
			winner = 1
print winner , lead
