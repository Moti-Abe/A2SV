def count_strings(n):
    chars = ['A', '2', 'S', 'V']
    
    # dp[i][prev][last]
    dp = {}
    
    # Base case: length = 1
    for c in chars:
        dp[(1, '', c)] = 1
    
    for i in range(2, n + 1):
        new_dp = {}
        for (length, pp, p), val in dp.items():
            if length != i - 1:
                continue
            for c in chars:
                if c == p:
                    continue
                if pp == 'S' and p == 'V' and c == 'A':
                    continue
                new_dp[(i, p, c)] = new_dp.get((i, p, c), 0) + val
        dp = new_dp
    
    return sum(dp.values())


n = int(input())
print(count_strings(n))