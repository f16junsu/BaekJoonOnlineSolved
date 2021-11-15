re=0
for i in range(int(input())):
    a=input()
    re+=list(a)==sorted(a, key=a.find)
    print(sorted(a, key=a.find))
print(re)