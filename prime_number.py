# find number is prime or not

num = input()
i = 0
while (i<num) :
	n = input()
	if n == 1 or n == 0 :
		print 'no'
	if n == 2 :
		print 'yes'
	if n > 2 :
		j = 2
		isprime = True
		while (j < n) :  		# i is in range from 2 to n-1
			if n % j == 0 :	
				isprime = False		# if the number is divisible by i 
				print 'no'	# number has factors other then 1 and n, not a prime no. 
				break
			j += 1
		if isprime :
			print 'yes'
	i += 1
