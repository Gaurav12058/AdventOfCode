import re

with open("input.txt", "r") as file:

    # Part 1
    matches = re.findall(r"mul\((\d+),(\d+)\)", file.read())
    total = 0
    for a, b in matches:
        total += int(a) * int(b)
    print("Part 1:", total)

    file.seek(0)

    # Part 2
    total = 0
    do = True
    data = re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", file.read())
    for func in data:
        if "do()" in func:
            do = True
        elif "don't()" in func:
            do = False
        elif do:
            a, b = int(func[0]), int(func[1])
            total += a * b

    print("Part 2:", total)
