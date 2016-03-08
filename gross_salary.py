# calculate gross salary of an employee

n = input()
i = 0
while (i < n) :
	base = input()
	if base >= 1500 :
		HRA = 500
		DA = (0.98) * base
	elif base < 1500 :
		HRA = (0.1) * base
		DA = (0.9) * base
	gross = base + HRA + DA
	print'%g'%gross

	i += 1

