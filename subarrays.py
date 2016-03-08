#find the count of increasing sub arrays

def increasing(array) :
	List = []
	if len(array) > 1 :
		for i in array :
			for j in array[1:] :
				if i < j :
					List.append([i,j])
	else :
		return 1
	return len(List)

n = input()
i = 0
while (i < n) :
	N = input()		# size of array
	elements = raw_input()	
	array = map(int,elements.split())
	print increasing(array)
	i = i + 1
