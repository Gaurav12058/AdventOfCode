def allIdsCorrectSpot(string, nums):
    for i in range(nums):
        if string[i] == ".":
            return False
    return True


with open("input", "r") as file:
    blocks = []
    while True:
        c1 = file.read(1)
        c2 = file.read(1)
        if c2 == '':
            blocks.append((c1,0))
            break
        blocks.append((c1, c2))


string = []
nums = 0
for index, (block, space) in enumerate(blocks):
    for i in range(int(block)):
        string.append(index)
    for i in range(int(space)):
        string.append(".")
    nums += int(block)
    

while not allIdsCorrectSpot(string, nums):
    for i, char in enumerate(reversed(string)):
        if char != ".":
            last = char
            lastInd = len(string) - i - 1
            break
    for i, char in enumerate(string):
        if not str(char).isdigit():
            string[i] = last
            string[lastInd] = "."
            break


ans = 0
for i, num in enumerate(string):
    if num == ".":
        break
    else:
        ans += i*num


print(ans)