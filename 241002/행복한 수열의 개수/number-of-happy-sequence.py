n, m = map(int,input().split())
grid =[[*map(int,input().split())] for _ in range(n)]

happy_sequences = 0
if n == 1:
    happy_sequences = 2 if m == 1 else 0
else:
    for row in range(n):
        count = 1
        for col in range(1,n):
            if grid[row][col-1] == grid[row][col]:
                count += 1
            else:
                count = 1
            if count >= m:
                happy_sequences += 1
                break

        
    for col in range(n):
        count = 1
        for row in range(1,n):
            if grid[row-1][col] == grid[row][col]:
                count += 1
            else:
                count = 1
            if count >= m:
                happy_sequences += 1
                break



print(happy_sequences)