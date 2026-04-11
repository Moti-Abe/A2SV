n , t = map(int, input().split())
arr = list(map(int, input().split()))

total_books_he_reads = 0
total_min = 0

left , right = 0, 0

while right < n:
    total_min += arr[right]
    if total_min > t:
        total_min -= arr[left]
        left += 1
        right += 1
        
    else:
        right += 1

total_books_he_reads = max(total_books_he_reads, right - left)
print(total_books_he_reads)


