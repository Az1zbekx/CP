x = int(input())
if x % 400 == 0 or (x % 4 == 0 and x % 100 != 0):
	print(f"12/09/{x:04d}")
else:
	print(f"13/09/{x:04d}")