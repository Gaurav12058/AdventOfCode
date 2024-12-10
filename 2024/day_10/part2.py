def findNumPaths(i, j):
    def nextStep(i2, j2, num):
            if(num == 9):
                return 1
            
            paths = 0

            for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                ni, nj = i2 + di, j2 + dj
                if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] == num + 1:
                    paths += nextStep(ni, nj, num + 1)
            
            return paths
    
    return nextStep(i, j, 0)


input = open("input", "r").read().strip()

zeros = set()
grid = []
row = []
for i, line in enumerate(input.split("\n")):
    for j, char in enumerate(line):
        if(char != '\n'):
            row.append(int(char))
            if(char == "0"):
                zeros.add((i,j))
    grid.append(row)
    row = []

ans = 0
for zero in zeros:
        ans += findNumPaths(zero[0],zero[1])

print(ans)