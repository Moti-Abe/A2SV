t = int(input())
 
for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    
    ans = 0
    one = float('-inf')
    for i in range (n):
        if s[i] == '1':
            if i - one >= k:
                ans += 1
            one = i
    print(ans)