# count no. of 4 in a number

def count_four(string) :
	count = 0
	i = 0
	while ( i < len(string)):
		if string[i] == '4' :
			count += 1
		i = i + 1
	return count

n = input()
i = 0
while ( i < n ) :
	num = raw_input()
	count4 = count_four(num)
	i = i + 1
	print count4
