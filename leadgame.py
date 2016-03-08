# calculate the winner of the game played by 2 players on the basis of lead score.
# input - first line - number 'n' which tells how many rounds should they play
#	- (second line to n lines) - shows the scores of 2 players separated by space (p1 p2)
# ouput - one line showing the winner and the lead.(Separated by space) 

scores = []
rounds =int(raw_input())
i = 0
while (i < rounds) :
	games = raw_input()      # 2 numbers separated by space
	i = i + 1
	game = games.strip().split()
	scores.extend(game)	# extending scores into a scores list

player1 = scores[0::2]		# scores of player1
player2 = scores[1::2]		# scores of player2

player1 = map(int,player1)	# converting scores into integer
player2 = map(int,player2)	# converting scores into integer

p1= [] 
total = 0
for i in player1 :
	total = total + i
	p1.append(total)

p2= []
total_2 = 0
for j in player2 :
	total_2 = total_2 + j
	p2.append(total_2)
lead_list = []
for i in range(len(p1)-1):
	lead = (p1[i] - p2[i])
	if lead > 0 :
		lead_list.append([1,abs(lead)])
	else :
		lead_list.append([2,abs(lead)])
m = max(lead_list , key = lambda x : x[1])
print (str(m[0]) + " "+ str(m[1]))
