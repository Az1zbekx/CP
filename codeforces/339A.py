n = input()
l = n.split('+')
l.sort()
k = ""
for i in range(len(l)):
    k += l[i]
    if i < len(l) - 1:
        k += '+'
print(k)