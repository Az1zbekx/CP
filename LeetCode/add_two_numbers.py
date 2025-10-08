l1 = [2, 4, 3]
l2 = [5, 6, 4]
t1, t2 = 0, 0
nums = []
while l1:
    nums.append(l1.val)
    l1 = l1.next
for i in nums[::-1]:
    t1 *= 10
    t1 += i

nums = []
while l1:
    nums.append(l1.val)
    l1 = l1.next
for i in nums[::-1]:
    t2 *= 10
    t2 += i

t1 += t2
l = []
while t1:
    l.append(t1 % 10)
    t1 //= 10
return l