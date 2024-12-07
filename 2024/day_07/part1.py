from collections import deque

def tryValue(num, equation):
    num = bin(num)[2:].zfill(len(equation)-1)
    operators = deque()
    for operator in num:
        operators.append(operator)

    nums = deque(equation)

    for operator in range(len(operators)):
        num1 = nums.popleft()
        num2 = nums.popleft()
        op = operators.popleft()
        if(op == '0'):
            nums.appendleft(num1 + num2)
        else:
            nums.appendleft(num1 * num2)
    return nums.pop()

data = []

with open("input", "r") as file:
    for line in file:
        key, values = line.split(":")
        data.append([int(key)] + list(map(int, values.split())))

sum = 0
for equation in data:
    goal = equation.pop(0)
    for num in range(2**(len(equation)-1)):
        value = tryValue(num, equation)
        if(goal == value):
            sum += goal
            break

print(sum)