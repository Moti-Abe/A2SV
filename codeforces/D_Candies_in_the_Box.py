import math

n, k = map(int, input().split())

# solve for p
D = 9 + 8 * (n + k)
p = (-3 + int(math.isqrt(D))) // 2

# number of eaten candies
e = n - p

print(e)