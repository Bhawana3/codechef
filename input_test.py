
# Enter 2 numbers

num = raw_input()
num_list = num.split()
n = num_list[0]
k = num_list[1]
intn= int(n)
intk= int(k)

num_list = []
count = 0
for t in range(intn):
	t = raw_input()
	intt = int(t)
	num_list.append(intt)
for i in num_list :
	if (i%intk == 0):
		count = count + 1
print count
