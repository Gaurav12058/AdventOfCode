from sympy import symbols, Eq, solve
import re


input = open("input", "r").readlines()

ans = 0

machines = []
for i in range(0, len(input), 4):
    matcha = re.search(r"X\+(\d+), Y\+(\d+)", input[i])
    matchb = re.search(r"X\+(\d+), Y\+(\d+)", input[i+1])
    target = re.search(r"X\=(\d+), Y\=(\d+)", input[i+2])
    machines.append((int(matcha.group(1)),int(matcha.group(2)),int(matchb.group(1)),int(matchb.group(2)),int(target.group(1))+10000000000000,int(target.group(2))+10000000000000))

ans = 0
for machine in machines:
    a, b = symbols('a b')

    eq1 = Eq(machine[0] * a + machine[2] * b, machine[4])
    eq2 = Eq(machine[1] * a + machine[3] * b, machine[5])

    solution = solve([eq1, eq2], (a, b))

    if solution:
        if solution[a].is_integer and solution[b].is_integer:
            ans += solution[a] * 3 + solution[b]

print(ans)