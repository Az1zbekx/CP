n = int(input())
if n <=3:
	print(0)
else:
	n -= 2
	print(((n * (n + 1)) // 2) - 1)