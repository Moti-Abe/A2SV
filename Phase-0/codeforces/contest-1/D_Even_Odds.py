#problem D. Even Odds
#link: https://codeforces.com/gym/666791/problem/D

import math
n, k = map(int, input().split())

half = math.ceil(n/2)
if half >= k:
    print(k*2 -1)
else:
    print(((k- half)*2))