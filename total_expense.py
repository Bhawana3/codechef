# calculate total expenses

n = input()
i = 0
while ( i<n ) :
	p = raw_input()
	pr = p.split()
	input_list = map(int , pr)
	quantity = input_list[0]
	price = input_list[1]
	expense = quantity * price
	if quantity > 1000 :
		total_expense = expense - (0.1*expense)	
		print format(total_expense,'.6f')
	else : 
		print format(expense,'.6f')
	i += 1
