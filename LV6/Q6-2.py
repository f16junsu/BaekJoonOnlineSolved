def d(n):
    tmp = str(n)
    sum = n
    for c in tmp:
        sum += int(c)
    return sum

ls = list(range(10000, 0, -1))
result = []
for i in ls:
    try:
        num = d(i)
        result.insert(0, i)
        result.remove(num)
    except ValueError:
        continue

for i in result:
    print(i)