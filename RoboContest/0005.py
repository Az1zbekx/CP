z = int(input())
if z == 0:
	print(-1)
else:
	if z > 0:
		n = z
	else:
		n = -z
	res, i  = 0, 1
	while i * i <= n:
		if n % i == 0:
			res+=1
			if i * i !=n:
				res+=1
		i+=1
	if res % 2 == 1 and z > 0:
		print(res + 1)
	else:
		print(res)