# find the number of operations required to make GCD of all the grapes divisible by k.

def number_of_operations(List,k) :
	total = 0
	for i in List :
		if i > k :				# checks if number is greater than k
			if (i % k) >= (k/2) :		# if remainder is greater than k/2 then add diff
				diff = k - (i % k)
				total = total + diff 
			else :
				operation = i - (i % k)	# if remainder is less than k/2 then remove i % k
				total = total + (i % k) 
		else :
			diff = abs(i - k)
			total = total + diff
	return total
	
p = input()
i = 0
while ( i < p) :
	number = raw_input()
	n ,k = map(int,number.split())
	grapes = raw_input()
	grapes_in_bucket = map(int,grapes.split())
	print number_of_operations(grapes_in_bucket,k)
	i += 1
