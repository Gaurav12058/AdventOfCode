inp = open("input", "r").read().strip()

walls = set()
boxes = set()
robot = (0,0)
moves = []

for y, r in enumerate(inp.split("\n")):
    if y == 0:
        gridDim = len(r)
    if y >= gridDim:
        if y == gridDim:
            continue
        for c in r:
            if c == "^":
                moves.append((-1,0))
            elif c == ">":
                moves.append((0,1))
            elif c == "<":
                moves.append((0,-1))
            elif c == "v":
                moves.append((1,0))
    else:
        for x, c in enumerate(r):
            if c == "@":
                robot = y, x
            elif c == "#":
                walls.add((y,x))
            elif c == "O":
                boxes.add((y,x))


for i, (dy, dx) in enumerate(moves):
    boxesToMove = set()
    doMoves = True
    for scaler in range(1, gridDim):
        if((robot[0]+dy*scaler, robot[1]+dx*scaler) in boxes):
            boxesToMove.add((robot[0]+dy*scaler, robot[1]+dx*scaler))
        elif((robot[0]+dy*scaler, robot[1]+dx*scaler) in walls):
            doMoves = False
            break
        else:
            break
    
    if(doMoves):
        for box in boxesToMove:
            boxes.remove(box)
        for box in boxesToMove:
            boxes.add((box[0]+dy,box[1]+dx))
        robot = (robot[0]+dy, robot[1]+dx)

ans = 0
for box in boxes:
    ans += box[0]*100 + box[1]

print(ans)