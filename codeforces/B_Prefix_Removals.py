t = int(input())
from collections import deque
for _ in range(t):
    s = input()
    arr = deque()
    for i in range(len(s)):
        arr.append(s[i])

    mp = {}
    for i in range(len(s)):
        mp[s[i]] = mp.get(s[i], 0)+1
    for i in range(len(s)):
        if mp[s[i]] > 1:
            mp[s[i]] -= 1
            arr.popleft()
        else:
            break
    s = "".join(arr)
    print(s)