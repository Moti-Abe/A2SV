t = int(input())
 
for _ in range(t):
    s = input().strip()
    
    digits = list(map(int, s))
    total = sum(digits)
    
    # Already beautiful
    if total <= 9:
        print(0)
        continue
    
    need = total - 9
    reductions = []
    
    for i in range(len(digits)):
        if i == 0:
            # first digit can't become 0
            reductions.append(digits[i] - 1)
        else:
            reductions.append(digits[i])
    
    # Take biggest reductions first
    reductions.sort(reverse=True)
    
    moves = 0
    reduced = 0
    
    for r in reductions:
        reduced += r
        moves += 1
        if reduced >= need:
            break
    
    print(moves)