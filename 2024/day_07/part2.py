from collections import deque

def toTernary(num):
    if num == 0:
        return "0"
    ternary = ""
    while num != 0:
        ternary = str(num % 3) + ternary
        num //= 3
    return ternary

def tryValue(num, equation):
    num = toTernary(num).zfill(len(equation)-1)
    operators = deque()
    for operator in num:
        operators.append(operator)

    nums = deque(equation)

    for operator in range(len(operators)):
        num1 = nums.popleft()
        num2 = nums.popleft()
        op = operators.popleft()
        if op == '0':
            nums.appendleft(num1 + num2)
        elif op == '1':
            nums.appendleft(num1 * num2)
        else:
            nums.appendleft(int(str(num1) + str(num2)))
    return nums.pop()

data = []

with open("input", "r") as file:
    for line in file:
        key, values = line.split(":")
        data.append([int(key)] + list(map(int, values.split())))

sum = 0
for equation in data:
    goal = equation.pop(0)
    for num in range(3**(len(equation)-1)):
        if(goal == tryValue(num, equation)):
            sum += goal
            break

print(sum)