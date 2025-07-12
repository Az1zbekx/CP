a, b = map(int, input().split())
print(a * b if a * b >= (a + b) * 2 else (a + b) * 2)