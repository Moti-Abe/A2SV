t = int(input())
 
for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    
    ans = 0
    last_one = -10**9 
    
    for i in range(n):
        if s[i] == '1':
            if i - last_one >= k:
                ans += 1
            last_one = i  
    
    print(ans)