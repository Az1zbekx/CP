n, k = map(int, input().split())
l = list(map(int, input().split()))
x = l[k - 1]
ans = 0
for i in l:
    if i >= x and i > 0:
        ans += 1
print(ans)