N = int(input())

def ifgroup(stri: str):
    ls_alpahs = []
    seq = 0
    try:
        for i in range(len(stri)):
            if seq:
                if stri[i + 1] == stri[i]:
                    seq = 1
                else:
                    seq = 0
            else:
                if stri[i] in ls_alpahs:
                    return False
                else:
                    ls_alpahs.append(stri[i])
                    if stri[i + 1] == stri[i]:
                        seq = 1
    except IndexError:
        return True
"abc".find()
cnt = 0
for i in range(N):
    S = input()
    if ifgroup(S):
        cnt += 1
print(cnt)