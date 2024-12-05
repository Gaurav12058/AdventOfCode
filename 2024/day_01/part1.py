list1 = []
list2 = []

with open("input.txt", "r") as file:
    for line in file:
        num1, num2 = line.strip().split("   ")
        num1, num2 = int(num1), int(num2)

        list1.append(num1)
        list2.append(num2)

list1.sort()
list2.sort()

distance = 0
for num1, num2 in zip(list1, list2):
    distance += abs(num2-num1)

print(distance)