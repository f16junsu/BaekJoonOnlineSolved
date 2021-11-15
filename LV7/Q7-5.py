S = input()
Stmp = S.lower()
li = []
numbers_each = []
max_character = []
max = 0
for c in Stmp:
    if c in li: continue
    li.append(c)
for c in li:
    numbers_each.append((c, Stmp.count(c)))
for t in numbers_each:
    if max < t[1]:
        max = t[1]
for t in numbers_each:
    if t[1] == max:
        max_character.append(t)
if (len(max_character) == 1):
    print(max_character[0][0].upper())
else:
    print('?')
