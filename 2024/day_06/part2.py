def checkForLoop(i, j, direction, map):
    visited = set()
    while True:
        if not (0 <= j < len(map[0]) and 0 <= i < len(map)):
            return False
        if(map[i][j] == "#"):
            i, j = moveBack(i, j, direction)
            direction = turnRight(direction)
        if((i,j,direction) in visited):
            return True
        visited.add((i,j, direction))
        i, j = moveForward(i, j, direction)


def turnRight(direction):
    return (direction + 1) % 4


def moveBack(i, j, direction):
    if(direction == 0):
        i += 1
    elif(direction == 2):
        i -= 1
    elif(direction == 1):
        j -= 1
    elif(direction == 3):
        j += 1
    return i, j


def moveForward(i, j, direction):
    if(direction == 0):
        i -= 1
    elif(direction == 2):
        i += 1
    elif(direction == 1):
        j += 1
    elif(direction == 3):
        j -= 1
    return i, j


map = []
direction = 0

with open("input", "r") as file:
    for line in file:
        line = line.strip()
        map.append(line)
        if "^" in line:
            i = map.index(line)
            j = line.index("^")

visited = set()
positions = 0

map = [list(row) for row in map]
for x in range(len(map)):
    for y in range(len(map[x])):
        if(map[x][y] != "#"):
            map[x][y] = "#"
            positions += checkForLoop(i, j, direction, map)
            map[x][y] = "."

print(positions)