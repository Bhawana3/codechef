# find the smallest number of notes required to get the number entered
def smallest_number(List,number) :
	total = 0
        j = 0
        while j < len(List):
        	k = number/List[j] 
        	total = total + k
        	number = number % List[j]
		j += 1
	return total

n = input()
i = 0
while ( i < n ) :
	num = input()
	if num >= 100 :
		l = [100,50,10,5,2,1]
		print smallest_number(l,num)
	if 50 <= num < 100 :
		l = [50,10,5,2,1]
		print smallest_number(l,num)
	if 10 <= num < 50 :
		print smallest_number([10,5,2,1],num)
	if 5 <= num < 10 :
		print smallest_number([5,2,1],num)
	if 2 <= num < 5 :
		print smallest_number([2,1],num)
	if 2 > num >= 1 :
		print  smallest_number([1],num)
	if num == 0 :
		print num
	i += 1
