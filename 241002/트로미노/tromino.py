n, m = map(int,input().split())
grid = [
    list(map(int,input().split()))
    for _ in range(n)
]

max_value = 0
for i in range(1,n):
    for j in range(1,n):
        max_value = max(max_value, grid[i-1][j-1] + grid[i-1][j] + grid[i][j], grid[i][j-1] + grid[i-1][j] + grid[i][j], grid[i][j-1] + grid[i-1][j-1] + grid[i][j], grid[i-1][j-1] + grid[i][j-1] + grid[i-1][j])

for i in range(n):
    for j in range(2,n):
        max_value = max(max_value, grid[i][j-2]+grid[i][j-1]+grid[i][j])

for j in range(n):
    for i in range(2,n):
        max_value = max(max_value, grid[i-2][j]+grid[i-1][j]+grid[i][j])

print(max_value)