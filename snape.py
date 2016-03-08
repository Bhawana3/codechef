import math
t=int(raw_input())
for t in range(t):
    a,b=raw_input().split()
    a=int(a)
    b=int(b)
    print (math.sqrt(b**2-a**2))
    print(math.sqrt(b**2+a**2)) 
