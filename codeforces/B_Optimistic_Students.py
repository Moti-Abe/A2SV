import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
m = int(data[1])

# Read the n student answer strings
students = []
idx = 2
for i in range(n):
    students.append(data[idx])
    idx += 1

# Read the m point values
a = []
for i in range(m):
    a.append(int(data[idx]))
    idx += 1

# For each question, find the most popular answer
total = 0
for j in range(m):
    count = [0] * 5  # A=0, B=1, C=2, D=3, E=4
    for i in range(n):
        ans = students[i][j]
        pos = ord(ans) - ord('A')
        count[pos] += 1
    max_students = max(count)
    total += max_students * a[j]

print(total)