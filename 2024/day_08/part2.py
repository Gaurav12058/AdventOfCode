import re

input = open("input", "r").read().strip()

g = [list(r) for r in input.split("\n")]
m, n = len(g), len(g[0])

chars = set(re.findall(r"[a-zA-Z0-9]", input))

locations = []
for char in chars:
    for l in g:
        for c in l:
            if(c == char):
                locations.append((char, l.index(c), g.index(l)))

antiNodes = set()

for c1, x1, y1 in locations:
    for c2, x2, y2 in locations:
        if(c1 == c2 and (x1,y1) != (x2,y2)):
            tx1 = x1
            ty1 = y1
            dx, dy = x2-x1, y2-y1
            antiNodes.add((x1,y1))
            antiNodes.add((x2,y2))
            while(0 <= (x1-dx) < n and 0 <= (y1-dy) < m):
                x1 -= dx
                y1 -= dy
                antiNodes.add((x1,y1))
            while(0 <= (x2+dx) < n and 0 <= (y2+dy) < m):
                x2 += dx
                y2 += dy
                antiNodes.add((x2,y2))
            x1 = tx1
            y1 = ty1

print(len(antiNodes))