 # grade steel

n = input()
i = 0
while (i < n ) :
	grades = raw_input()
	grades_list = map(int ,grades.split())
	hardness = grades_list[0]
	carbon = grades_list[1]
	strength = grades_list[2]
	if (hardness > 50 and carbon < 0.7 and strength > 5600 ) :
		print 10
	elif (hardness > 50 and carbon < 0.7) :
		print 9
	elif (carbon < 0.7 and strength > 5600) :
		print 8
	elif (hardness > 50 and strength > 5600 ) :
		print 7
	elif (hardness > 50 or carbon < 0.7 or strength > 5600 ) :
		print 6
	else :
		print 5

	i += 1
