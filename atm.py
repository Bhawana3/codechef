draw=raw_input()
draw=draw.split()
x=int(draw[0])
y=float(draw[1])
if x%5 == 0 and x < (y-0.50):
    print(format((y-x-0.50),'.2f'))
else:
    print(format(y,'.2f'))
