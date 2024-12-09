with open("input", "r") as file:
    blocks = []
    while True:
        c1 = file.read(1)
        c2 = file.read(1)
        if c2 == '':
            blocks.append((c1,'0'))
            break
        blocks.append((c1, c2))

string = []
nums = 0
for index, (block, space) in enumerate(blocks):
    if block != '0':
        string.append(list(index for i in range(int(block))))
    if space != '0':
        string.append(list("." for i in range(int(space))))
    nums += int(block)


for i in range(len(blocks) - 1, 0, -1):
    for i2, l in enumerate(reversed(string)):
        if l[0] == i:
            fileIndex = len(string) - i2 - 1
            break
    for index, l in enumerate(string):
        if l[0] == "." and len(l) >= int(blocks[i][0]) and index <= fileIndex:
            string.insert(index, list(string[fileIndex]))
            for i3 in range(int(blocks[i][0])):
                string[fileIndex + 1][i3] = '.'
                l.pop()
            if not l:
                string.remove(l)
            break

nstring = []
for list in string:
    for value in list:
        nstring.append(value)


ans = 0
for i, num in enumerate(nstring):
    if num == ".":
        continue
    else:
        ans += i*num


print(ans)