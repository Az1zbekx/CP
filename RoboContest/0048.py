n = int(input())
k, t = 0, 1
for i in range(1, n + 1):
    while k < i:
        print(t, end = ' ')
        t += 1
        k += 1
    print()
    k = 0
    
    