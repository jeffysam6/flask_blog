w = list(map(int,input().split(" ")))
initial = sum(w)
for _ in range(2):
	u,d = map(int,input().split(" "))
	sum += u*(-1) +d

print(initial + sum) 
