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

def findSides(plot):
    fence = set()
    perimeterPlants = set(plot)
    for loc in plot:
        neighbors = 0
        for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            if (loc[0]+di,loc[1]+dj) in plot:
                neighbors += 1
        if neighbors == 4:
            perimeterPlants.remove(loc)

    for loc in perimeterPlants:
        if not (loc[0]-1, loc[1]) in plot:
            fence.add((loc[0]-1, loc[1]))
        if not (loc[0]+1, loc[1]) in plot:
            fence.add((loc[0]+1, loc[1]))
        if not (loc[0], loc[1]+1) in plot:
            fence.add((loc[0], loc[1]+1))
        if not (loc[0], loc[1]-1) in plot:
            fence.add((loc[0], loc[1]-1))

    count = 0

    read = set() 
    dir = 1
    # check on y axis to the right
    for loc in fence:
        if (loc[0], loc[1], dir) in read:
            continue
        
        if (loc[0],loc[1]+dir) in plot:
            read.add((loc[0],loc[1], dir))
            di = 1
            while(loc[0]+di,loc[1]) in fence and (loc[0]+di,loc[1]+dir) in plot:
                read.add((loc[0]+di,loc[1], dir))
                di += 1
            
            di = -1
            while(loc[0]+di,loc[1]) in fence and (loc[0]+di,loc[1]+dir) in plot:
                read.add((loc[0]+di,loc[1], dir))
                di -= 1

            count += 1

    dir = -1
    # check on y axis to the left
    for loc in fence:
        if (loc[0], loc[1], dir) in read:
            continue
        
        if (loc[0],loc[1]+dir) in plot:
            read.add((loc[0],loc[1], dir))
            di = 1
            while(loc[0]+di,loc[1]) in fence and (loc[0]+di,loc[1]+dir) in plot:
                read.add((loc[0]+di,loc[1], dir))
                di += 1
            
            di = -1
            while(loc[0]+di,loc[1]) in fence and (loc[0]+di,loc[1]+dir) in plot:
                read.add((loc[0]+di,loc[1], dir))
                di -= 1

            count += 1
    
    read = set()
    dir = 1
    # check on x axis on bottom
    for loc in fence:
        if (loc[0], loc[1], dir) in read:
            continue

        if (loc[0]+dir,loc[1]) in plot:
            read.add((loc[0],loc[1], dir))
            dj = 1
            while(loc[0],loc[1]+dj) in fence and (loc[0]+dir,loc[1]+dj) in plot:
                read.add((loc[0],loc[1]+dj, dir))
                dj += 1
            
            dj = -1
            while(loc[0],loc[1]+dj) in fence and (loc[0]+dir,loc[1]+dj) in plot:
                read.add((loc[0],loc[1]+dj, dir))
                dj -= 1

            count += 1

    dir = -1
    # check on x axis on top
    for loc in fence:
        if (loc[0], loc[1], dir) in read:
            continue

        if (loc[0]+dir,loc[1]) in plot:
            read.add((loc[0],loc[1], dir))
            dj = 1
            while(loc[0],loc[1]+dj) in fence and (loc[0]+dir,loc[1]+dj) in plot:
                read.add((loc[0],loc[1]+dj, dir))
                dj += 1
            
            dj = -1
            while(loc[0],loc[1]+dj) in fence and (loc[0]+dir,loc[1]+dj) in plot:
                read.add((loc[0],loc[1]+dj, dir))
                dj -= 1

            count += 1

    return count

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
    area = len(plot)
    sides = findSides(plot)
    ans += area * sides

print(ans)