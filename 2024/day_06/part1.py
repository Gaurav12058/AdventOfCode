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


spaces = 0
visited = set()

while(0 <= j < len(map[0]) and 0 <= i < len(map)):
    
    if((map[i][j] == "." or map[i][j] == "^") and not (i,j) in visited):
        spaces += 1
    
    visited.add((i,j))

    if(map[i][j] == "#"):
        i, j = moveBack(i, j, direction)
        direction = turnRight(direction)
        
    i, j = moveForward(i, j, direction)

print(spaces)