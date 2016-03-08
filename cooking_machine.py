

def find_power_of_2(a,b) :
	import math
	if a > b :
		if a % 2 == 0 :
			n = math.log(a)
			m = math.log(b)
			power = int(n/m)
			return power 
		else :
			a = ((a -1)/2)
			n = math.log(a)
			m = math.log(b)
			power = int(n/m)
			return power + 1
	else :
		if a % 2 == 0 :
			n = math.log(a)
			m = math.log(b)
			power = int(m/n)
			return power
		else :
			a = int((a-1)/2)
			n = math.log(a)
			m = math.log(b)
			power = int(m/n)
			return power + 1
print find_power_of_2(3,8)
