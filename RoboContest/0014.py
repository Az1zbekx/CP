def pow(a, n):
	if n == 0:
		return 1
	if n % 2 == 0:
		x  = pow(a, n//2)
		return x * x % 1000000007
	return a * pow(a, n - 1) % 1000000007
n, k = map(int, input().split())
print(pow((1 + k), n))