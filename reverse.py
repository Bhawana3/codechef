# reverse the numbers entered
# input = 12345  output = 54321

def strip_leading_zeros(s):
	start_index = 0
	i = 0
	while(i < len(s)) :
		if s[i] == '0' :
			start_index += 1
		else :
			break
		i += 1
	return s[start_index:]

n = input()
i = 0
s = ''
while (i < n) :
	num = raw_input()
	r = int(num)
	j = r 
	while (j > 0) :
		a = j % 10
		s = s + str(a)
		j = j / 10
	i = i + 1

	new_s = strip_leading_zeros(s)	

	print new_s
	s = ''

