def factorial(n) :
	count = 1 ; i = 1
	while(i <= n) :
		count = count * i
		i = i + 1
	return count

num = raw_input()
num_int = int(num)
num_list = []
for i in range(num_int) :
	input_num = raw_input()
	int_input_num = int(input_num)
	num_list.append(int_input_num)

for j in num_list :
	f = factorial(j)
	print f
