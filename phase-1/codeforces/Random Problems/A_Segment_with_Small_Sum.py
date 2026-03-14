n, s = map(int , input().split())
arr = list(map(int, input().split()))

left , right = 0, 0
total = 0
max_len = 0

while right < n:
    total += arr[right]
    if total > s:
        total -= arr[left]
        left += 1
    
    
    max_len = max(max_len, right - left + 1)

    right += 1

print(max_len)

    
    
    