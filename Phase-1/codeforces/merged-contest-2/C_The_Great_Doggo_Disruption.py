n = int(input())

s = input()

mp = {}
isposible = False
for c in s:
    mp[c] = mp.get(c, 0) + 1
    if mp[c] > 1:
        isposible = True
        break
if isposible or n == 1:
    print("Yes")
else:
    print("No")