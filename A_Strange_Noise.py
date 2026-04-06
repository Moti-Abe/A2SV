t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    s = s.lower()
    res = []
    res.append(s[0])
    for i in range(1,n):
        if s[i] != s[i-1]:
            res.append(s[i])
    res = "".join(res)
    if res == "meow":
        print("YES")
    else:
        print("NO")
    