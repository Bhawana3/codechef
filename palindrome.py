# check if the number is palindrome or not

def palindrome(string) :
	i = 0
	j = -1
	while (i < len(string)) :
		if string[i] == string[j] :
			return 'wins'
		else : 
			return 'losses'
		j -= 1
		i += 1

n = input()
i = 0
while (i < n) :
	string = raw_input()
	print palindrome(string)
	i += 1
