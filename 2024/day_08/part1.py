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
            dx, dy = x2-x1, y2-y1
            node1 = (x1-dx, y1-dy)
            node2 = (x2+dx, y2+dy)
            if(0 <= node1[0] < n and 0 <= node1[1] < m):
                antiNodes.add(node1)
            if(0 <= node2[0] < n and 0 <= node2[1] < m):
                antiNodes.add(node2)

print(len(antiNodes))