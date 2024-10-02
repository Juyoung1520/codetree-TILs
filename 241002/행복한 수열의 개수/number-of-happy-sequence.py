n, m = map(int,input().split())
grid =[[*map(int,input().split())] for _ in range(n)]


sum = 0

for row in range(n):
    count = 0
    for col in range(n):
        if col+1 >= n:
            continue
        k = grid[row][col]
        if k != grid[row][col+1]:
            k = grid[row][col+1]
            count = 0 #리셋
        elif k == grid[row][col+1]:
            if count >= m-1:
                continue
            count += 1

    sum += count
        


for col in range(n):
    count = 0
    for row in range(n):
        if row+1 >= n:
            continue
        k = grid[row][col]
        if k != grid[row+1][col]:
            k = grid[row+1][col]
            count = 0
        elif k == grid[row+1][col]:
            if count >= m-1:
                continue
            count += 1
            
    sum += count

print(sum)