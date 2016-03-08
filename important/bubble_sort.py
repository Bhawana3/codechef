# sort input numbers in ascending order

def sort_numbers (l):
	k = len(l) - 1
	while (k > 0) :
		i = 0 ; j =1
		while(i < k-1) :
			if l[i] > l[j] :
				l[i],l[j] = l[j],l[i]
			i = i + 1
			j = j + 1
		k = k -1
	return l 
n = raw_input()
intn = int(n)
num_list = []

i = 0
while(i < intn) :
	num = raw_input()
	int_num = int(num)
	i = i + 1
	num_list.append(int_num)

sorted_num_list = sort_numbers(num_list)

for i in sorted_num_list :
	print i


