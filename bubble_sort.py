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
n = input()			# enter input number of test cases
num_list = []

i = 0
while(i < n) :
	num = input()	# enter number
	num_list.append(num)	#append numbers in the num_list
	i = i + 1


sorted_num_list = sort_numbers(num_list)

for i in sorted_num_list :
	print i


