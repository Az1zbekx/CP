def pow(a, n):
	if n == 0:
		return 1
	if n % 2 == 0:
		x  = pow(a, n//2)
		return x * x % 1000000007
	return a * pow(a, n - 1) % 1000000007
n, k = map(int, input().split())
a = pow(k, n) - 1
b = k - 1
print(a * pow(b, 1000000005) % 1000000007)