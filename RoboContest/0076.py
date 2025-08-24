l = list(map(int, input().split()))
s = int(input())
if s > sum(l):
    print(s - sum(l))
else:
    print(0)