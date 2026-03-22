t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    
    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    if n == m == 1:
        print(-1)
        continue
    if m == 1:
        new_matrix = matrix[1:] + [matrix[0]]
        for row in new_matrix:
            print(*row)
        continue
       
    res = []
    for i in range(n):
        new_row = matrix[i][1:] + [matrix[i][0]]
        res.append(new_row)
    
    # shift the first row to end
    res = res[1:] + [res[0]]

    for row in res:
        print(*row)