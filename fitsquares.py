# fit 2*2 squares in an isoscelous triangle of size input by user


n = input()
i = 0
while ( i < n ) :
	p = input()
	power = pow((p/2),2)
	print ((power - (p/2))/2)
	i = i + 1


