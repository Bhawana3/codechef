
def palindrome(string) :
	i = 0
	j = -1
	while (i < len(string)) :
		if string[i] == string[j] :
			return 1
		return 0	
		j -= 1
		i += 1

n = input()
i = 0
while (i < n) :
	numbers = raw_input()
	num_list = map(int,numbers.split())
	a = num_list[0]
	b = num_list[1]
	total = 0
	for num in range(a,b+1) :
		p = palindrome(str(num))
		if p == 1 :	
			total += num
	print total
	i += 1
