t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    s = list(s)
    i = 0
    for i in range(n):
        if s[i] != s[0]:
            break
        if s[i] == '0':
            s[i] = '1'
        else:
            s[i] = '0'
    
    for j in range(i, n):
        if s[j] != s[i]:
            break
        if s[j] == '0':
            s[j] = '1'
        else:
            s[j] = '0'
    
    if s == s[::-1]:
        print("Yes")
    else:
        print("No")