n = int(input())

one = ["bir", "ikki", "uch", "to'rt", "besh", "olti", "yetti", "sakkiz", "to'qqiz"]
ten = ["o'n", "yigirma", "o'ttiz", "qirq", "ellik", "oltmish", "yetmish", "sakson", "to'qson"]
res = ""
if n == 1000:
    res = "bir ming"
else:
    if n >= 100:
        res += one[(n // 100) - 1] + " yuz"
        n %= 100
        if n > 0:
            res += " "
    if n >= 10:
        res += ten[(n // 10) - 1]
        n %= 10
        if n > 0:
            res += " "
    if n > 0:
        res += one[n - 1]
print(res)
