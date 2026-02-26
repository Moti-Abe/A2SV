t = int(input())
total_days = t
mp = {}

while t > 0:
    t -= 1

    m = int(input())
    for i in range (m):
        s , h = input().split()
        h = int(h)
        mp[(s,h)] = mp.get((s, h), 0) + 1

max_value = max(mp.values())
RCR = (max_value/total_days)*100
if RCR >= 80:
    print("YES")
else:
    print("NO")