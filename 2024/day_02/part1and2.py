def isSafe(row):
    return differBy1or3(row) and (increasing(row) or decreasing(row))


def differBy1or3(row):
    for i in range(len(row)-1):
        if(abs(row[i] - row[i+1]) < 1 or abs(row[i] - row[i+1]) > 3):
            return False
    return True


def increasing(row):
    for i in range(len(row)-1):
        if(row[i] > row[i+1]):
            return False
    return True


def decreasing(row):
    for i in range(len(row)-1):
        if(row[i] < row[i+1]):
            return False
    return True


rows = []
with open("input.txt", "r") as file:
    for line in file:
        row = list(map(int, line.strip().split()))
        rows.append(row)

# Part 1
safe = 0
for row in rows:
    if(isSafe(row)):
        safe += 1

print("Part 1: ", safe)


# Part 2
safe = 0
for row in rows:
    if(isSafe(row)):
        safe += 1
        continue
    for i in range(len(row)):
        newRow = list(row)
        del newRow[i]
        if(isSafe(newRow)):
            safe += 1
            break

print("Part 2: ", safe)
