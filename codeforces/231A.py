t = int(input())
cnt = 0
for i in range(t):
    l = list(map(int, input().split()))
    if l.count(1) >= 2:
        cnt += 1
print(cnt)