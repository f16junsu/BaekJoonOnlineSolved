
ls = {666} | \
     {6660 + s for s in range(0, 10)} | \
     {s * 1000 + 666 for s in range(1, 10000)} | \
     {s * 10000 + 6660 + l for s, l in zip(range(1, 10), range(10))} | \
     {66600 + s for s in range(0, 100)} | \
     {s * 10000 + 6660 + l for s, l in zip(range(10, 100), range(10))} | \
     {s * 100000 + 66600 + l for s, l in zip(range(1, 10), range(100))} | \
     {666000 + s for s in range(0, 1000)} | \
     {s * 10000 + 6660 + l for s, l in zip(range(100, 1000), range(10))} | \
     {s * 100000 + 66600 + l for s, l in zip(range(10, 100), range(100))} | \
     {s * 100000 + 666000 + l for s, l in zip(range(1, 10), range(1000))} | \
     {6660000 + s for s in range(0, 10000)}

# ls = {"{}666{}".format(s, l) for s, l in (range(1, 1000), range(0, 1000))}
ls = list(ls)
ls.sort()
N = int(input())
print(ls[N - 1])

# 666 o
# x666 o 
# 666x o
# xx666 o
# x666x o
# 666xx o
# xxx666 o
# xx666x o
# x666xx o 
# 666xxx o
# xxxx666 o
# xxx666x o
# xx666xx o
# x666xxx