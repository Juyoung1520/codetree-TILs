n, m = map(int,input().split())
grid =[[*map(int,input().split())] for _ in range(n)]

sum = 0

for row in range(n):
    
    for col in range(n):
        if col+1 == n:
            continue
        count = 1
        k = grid[row][col]
        if k != grid[row][col+1]:
            continue
        else:
            count += 1
    if count >= m:
        sum += 1
        

        
for col in range(n):

    for row in range(n):
        if row+1 == n:
            continue
        count = 1
        k = grid[row][col]
        if k != grid[row+1][col]:
            continue
        else:
            count += 1
    if count >= m:
        sum += 1
            

print(sum)