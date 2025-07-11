n = int(input())
l = [1 for i in range(n + 1)]
l[0] = l[1] = 0
i = 2
while i * i <= n:
	if l[i]:
		j = i * 2
		while j <= n:
			l[j] = 0
			j += i
	i += 1
print("Ali" if sum(l) % 2 == 1 else "Bobur")