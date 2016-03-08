# find number of safe houses for the thief to hide from cops

# house_Range is a list containing sublist of range of houses.
def find_safe_houses(house_range) :

	total = 0					# counts the number of houses which are safe to hide
	min_start = house_range[0][0]	
	max_end = house_range[0][1]
	for j in house_range[1:] :
		if max_end >= j[0] :			# start and end points overlap 
			max_end = j[1]
			if max_end >= 100 :
				max_end = 100
				total = total + 0
			else :
				max_end = j[1]	
				total += (100 - max_end)	# max_End changes to new max end
		else :
			min_start = j[0]			# houses doesn't overlap
			total += ((min_start - max_end) -1)	# safe houses 
			max_end = j[1]
			if max_end >= 100 :
				total += 0 
			else :
				total += (100 - max_end)
		return total

def start_end(List,range) : 
	range_list = []
	for number in List :
		start = (number - range)
		end = (number + range)
		if start < 1 :
			start = 1
		if end > 100 :
			end = 100
		range_list.append([start,end])
	return range_list

n = input()
i = 0
house_range = []
while (i < n) :
	h = raw_input()
	M,x,y = map(int,h.split())
	cops = raw_input()
	cops_no = map(int,cops.split())
	distance = x*y
	s =  start_end(cops_no,distance)
	
	print find_safe_houses(s)
	i += 1
