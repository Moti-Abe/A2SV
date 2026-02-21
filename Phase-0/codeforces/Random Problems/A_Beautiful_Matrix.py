matrix = []
for _ in range(5):
     row = list(map(int, input().strip().split()))
     matrix.append(row)



for i in range(5):
     for j in range(5):
          if matrix[i][j] == 1:
               moves = abs(2 - i) + abs(2 - j)
               print(moves)
               break