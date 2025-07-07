x = int(input())
k = [0, 1]
for i in range(2, 46):
	k.append(k[i - 1] + k[i - 2])
print(k[x] * 2)