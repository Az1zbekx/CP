n = int(input())
if n < 4 or n % 4 != 0:
	print(-1)
else:
	print((n // 4) * 2)