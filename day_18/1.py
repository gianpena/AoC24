from heapq import heappush, heappop
from aocinput import AOCInput

input = AOCInput(2024, 18)

n = 71

board = [['.' for j in range(n)] for i in range(n)]
cost = [[float('inf') for j in range(n)] for i in range(n)]
corrupted = 0


for line in input.lines():
    if corrupted == 1024: break
    c,r = map(int, line.split(","))
    board[r][c] = '#'
    corrupted += 1


hq = [(0, 0, 0)]
cost[0][0] = 0
d = [[-1,0],[1,0],[0,1],[0,-1]]

while hq:
    c, i, j = heappop(hq)
    if c > cost[i][j]: continue
    for di, dj in d:
        i2,j2 = i + di, j + dj
        if not (0 <= i2 < n and 0 <= j2 < n): continue
        if board[i2][j2] == '#': continue
        if 1 + cost[i][j] >= cost[i2][j2]: continue

        cost[i2][j2] = 1 + cost[i][j]
        heappush(hq, (cost[i2][j2], i2, j2))

print(cost[n-1][n-1])