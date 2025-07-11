n = input()
print("YES" if len(n) % 2 == 1 and all(c in '13579' for c in n) else "NO")
1