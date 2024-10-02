n, m = map(int,input().split())
grid =[[*map(int,input().split())] for _ in range(n)]

sum = 0

for row in range(n):
    count = 0
    for col in range(n):
        k = grid[row][col]
        count += 1
        if col+1 == n:
            continue
        if k != grid[row][col+1]:
            count = 0
            continue
        else:
            count += 1
    if count >= m:
        sum += 1
        

        
for col in range(n):
    count = 0
    for row in range(n):
        k = grid[row][col]
        count += 1
        if row+1 == n:
            continue
        if k != grid[row+1][col]:
            count = 0
            continue
        else:
            count += 1
    if count >= m:
        sum += 1
            

print(sum)