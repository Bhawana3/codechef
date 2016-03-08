# sum of triangle = 180 ( valid triangle)

n = input()
i = 0
while (i < n) :
	angles = raw_input()
	angle_list = map(int , angles.split())
	a = angle_list[0]
	b = angle_list[1]
	c = angle_list[2]
	if (a > 0 and b > 0 and c > 0) :
		if a + b + c == 180 :
			print "YES"
		else :
			print "NO"
	else :
		print "NO"
	i += 1
