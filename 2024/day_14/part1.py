import re

def updatePosition(robot, seconds):
    posx, posy, velx, vely = robot

    posx += seconds * velx
    posy += seconds * vely

    posx %= maxx
    posy %= maxy

    return(posx, posy, velx, vely)

input = open("input", "r").read().strip()

robots = []

for l in input.split("\n"):
    nums = re.findall(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", l)
    robots.append(tuple(map(int, nums[0])))

maxx = 101
maxy = 103
seconds = 100


for i, robot in enumerate(robots):
    robots[i] = updatePosition(robot, seconds)


quads = [0,0,0,0]
for robot in robots:
    if(0 <= robot[0] < maxx//2 and 0 <= robot[1] < maxy//2):
        quads[0] += 1
    elif(0 <= robot[0] < maxx//2 and maxy//2 + 1 <= robot[1] < maxy ):
        quads[1] += 1
    elif(maxx//2 + 1 <= robot[0] < maxx and 0 <= robot[1] < maxy//2):
        quads[2] += 1
    elif(maxx//2 + 1 <= robot[0] < maxx and maxy//2 + 1 <= robot[1] < maxy):
        quads[3] += 1

ans = 1
for quad in quads:
    ans *= quad
print(ans)