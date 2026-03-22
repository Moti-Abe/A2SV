import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    
    p = []
    for _ in range(n):
        a, b = map(int, input().split())
        p.append((b, a))  # store as (b, a)
    
    p.sort()
    
    ans = 0
    cur = 0
    i, j = 0, n - 1
    
    # Convert to list of lists since we modify p[j][0]
    p = [[b, a] for (b, a) in p]
    
    while i <= j:
        if cur >= p[i][0]:
            ans += p[i][1]
            cur += p[i][1]
            i += 1
        else:
            while i <= j and cur < p[i][0]:
                need = p[i][0] - cur
                take = min(need, p[j][1])
                
                ans += 2 * take
                cur += take
                p[j][1] -= take
                
                if p[j][1] == 0:
                    j -= 1
    
    print(ans)

if __name__ == "__main__":
    solve()