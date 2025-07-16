import math
n = int(input())
n = (n * (n + 1)) // 2
if math.sqrt(n) == int(math.sqrt(n)):
	print("Qiziqarli")
else:
	print("Qiziq emas")