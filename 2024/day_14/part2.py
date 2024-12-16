import re

def updatePosition(robot, seconds):
    posx, posy, velx, vely = robot

    posx += seconds * velx
    posy += seconds * vely

    posx %= maxx
    posy %= maxy

    return(posx, posy, velx, vely)

inp = open("input", "r").read().strip()

robots = []

for l in inp.split("\n"):
    nums = re.findall(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", l)
    robots.append(tuple(map(int, nums[0])))

maxx = 101
maxy = 103

seconds = int(input("seconds: "))
# ans = 7520
while True:

    for i, robot in enumerate(robots):
        robots[i] = updatePosition(robot, seconds)

    output = []
    for i in range(maxy):
        line = []
        for j in range(maxx):
            line.append(".")
        output.append(line)

    for robot in robots:
        output[robot[1]][robot[0]] = "#"

    outputs = str()
    for i in range(maxy):
        line = str()
        for j in range(maxx):
            line += output[i][j]
        print(line)
    
    print(seconds)
    seconds += 1
    temp = input()
