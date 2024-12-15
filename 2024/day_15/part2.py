inp = open("input", "r").read().strip()


walls = set()
boxes = set()
robot = (0,0)
moves = []


for y, r in enumerate(inp.split("\n")):
    if y == 0:
        gridDim = len(r)
        wgridDim = gridDim * 2
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
                robot = y, x*2
            elif c == "#":
                walls.add((y,x*2))
                walls.add((y,x*2+1))
            elif c == "O":
                boxes.add((y,x*2,x*2+1))

for i, (dy, dx) in enumerate(moves):
    boxesToMove = set()
    doMoves = True
    if dy == 0:
        for scaler in range(1, wgridDim, 2):
            if((robot[0], robot[1]+dx*scaler, robot[1]+dx*scaler+dx) in boxes or (robot[0], robot[1]+dx*scaler+dx, robot[1]+dx*scaler) in boxes):
                boxesToMove.add((robot[0], robot[1]+dx*scaler, robot[1]+dx*scaler+dx))
            elif((robot[0], robot[1]+dx*scaler) in walls):
                doMoves = False
                break
            else:
                break
        if(doMoves):
            for box in boxesToMove:
                if box in boxes:
                    boxes.remove(box)
                else:
                    boxes.remove((box[0],box[2],box[1]))
            for box in boxesToMove:
                boxes.add((box[0],box[1]+dx,box[2]+dx))
            robot = (robot[0]+dy, robot[1]+dx)
    else:
        check = set()
        check.add(robot)
        while(len(check) != 0):
            pos = check.pop()

            if ((pos[0]+dy, pos[1], pos[1]+1) in boxes or (pos[0]+dy, pos[1]+1, pos[1]) in boxes) and not (pos[0]+dy, pos[1], pos[1]+1) in boxesToMove and not (pos[0]+dy, pos[1]+1, pos[1]) in boxesToMove:
                boxesToMove.add((pos[0]+dy, pos[1], pos[1]+1))
                check.add((pos[0]+dy, pos[1]))
                check.add((pos[0]+dy, pos[1]+1))

            elif ((pos[0]+dy, pos[1], pos[1]-1) in boxes or (pos[0]+dy, pos[1]-1, pos[1]) in boxes) and not (pos[0]+dy, pos[1], pos[1]-1) in boxesToMove and not (pos[0]+dy, pos[1]-1, pos[1]) in boxesToMove:
                boxesToMove.add((pos[0]+dy, pos[1], pos[1]-1))
                check.add((pos[0]+dy, pos[1]))
                check.add((pos[0]+dy, pos[1]-1))

            if(pos[0]+dy, pos[1]) in walls:
                doMoves = False
                break

        if(doMoves):
            for box in boxesToMove:
                if box in boxes:
                    boxes.remove(box)
                else:
                    boxes.remove((box[0],box[2],box[1]))
            for box in boxesToMove:
                boxes.add((box[0]+dy,box[1],box[2]))
            robot = (robot[0]+dy, robot[1]+dx)


ans = 0

for box in boxes:
    if(box[1] < box[2]):
        ans += box[0]*100 + box[1]
    else:
        ans += box[0]*100 + box[2]

print(ans)