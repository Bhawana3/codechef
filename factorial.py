num = raw_input()
num_int = int(num)
input_list = []

for i in range(num_int) :
	input_num = raw_input()
	int_input_num = int(input_num)
	input_list.append(int_input_num)

for nu in input_list:
	j = 1 
	sum_n = 0
	while True:
		zeros = nu /(pow(5,j)) 
		sum_n = sum_n + zeros
		j = j + 1
		if zeros == 0 :
			break
	print sum_n 
