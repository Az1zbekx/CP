s = int(input())
l = list(map(int, input().split()))
if s <= sum(l):
	print("Yes")
else:
	print("No")