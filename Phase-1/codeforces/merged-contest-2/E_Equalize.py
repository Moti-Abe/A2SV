t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    # Sort and remove duplicates → strictly increasing unique values
    a.sort()
    b = []
    for x in a:
        if not b or b[-1] != x:
            b.append(x)
    m = len(b)
    
    if m == 0:
        print(0)
        continue
    
    # Two pointers: maximum number of unique values with b[r] - b[l] <= n-1
    l = 0
    ans = 1
    for r in range(m):
        while b[r] - b[l] > n - 1 and l <= r:
            l += 1
        ans = max(ans, r - l + 1)
    
    print(ans)