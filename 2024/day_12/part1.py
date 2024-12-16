input = open("input", "r").read().strip()

def findPlot(c, i, j, seen):
    plot = set()
    recur(c, i, j, plot, seen)
    return plot

def recur(c, i, j, plot, seen):
    if not (0 <= i < len(g) and 0 <= j < len(g[0]) and g[i][j] == c) or (c, i, j) in seen:
        return
    
    seen.add((c,i,j))
    plot.add((i,j))

    for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        recur(c, i + di, j + dj, plot, seen)

def findPerimeter(plot):
    perimeter = 0
    for loc in plot:
        sides = 4
        for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            if (loc[0]+di,loc[1]+dj) in plot:
                sides -= 1
        perimeter += sides
    return perimeter


# grid input
g = [list(r) for r in input.split("\n")]

seen = set()
plots = []
for i, r in enumerate(g):
    for j, c in enumerate(r):
        if (c, i, j) in seen:
            continue
        plots.append(findPlot(c,i,j,seen))

ans = 0
for plot in plots:
    ans += len(plot) * findPerimeter(plot)

print(ans)