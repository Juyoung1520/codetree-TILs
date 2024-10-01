n = int(input())
grid = []  

for i in range(n):
    # 입력받은 문자열을 리스트에 추가
    grid.append(list(map(int, input().split())))  # 각 입력을 정수 리스트로 변환하여 추가


def get_num_of_gold(row_s, row_e, col_s, col_e):
    num_of_gold = 0

    for row in range(row_s, row_e+1):
        for col in range(col_s, col_e+1):
            num_of_gold += grid[row][col]

    return num_of_gold

max_gold = 0
for row in range(n):
    if row+2 >= n :
        continue
    for col in range(n):
        if col+2 >= n:
            continue
        
        max_gold = max(max_gold, get_num_of_gold(row, row+2, col, col+2))
print(max_gold)