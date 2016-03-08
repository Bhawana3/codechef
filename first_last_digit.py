# find the sum of first and last digit of number entered

n = input()
i = 0
while ( i < n ) :
	p = raw_input()
	intp = int(p)
	last_digit = intp % 10
	if len(p) == 1 :
		print last_digit
	else :
		first_digit = intp/pow(10,(len(p)-1))
		print first_digit + last_digit 
	i = i + 1
