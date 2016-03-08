# count the number of times a person enters into the hotel
#output - minimum and maximum

n = input()
i = 0
while (i < n) :
	guards = raw_input()
	guard_list = map(int ,guards.split())
	guard1 = guard_list[0]
	guard2 = guard_list[1]
	print str((max(guard1,guard2))) + ' ' + str(guard1 + guard2) 
	i += 1
	
