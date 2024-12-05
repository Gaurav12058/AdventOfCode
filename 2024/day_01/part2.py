list1 = []
list2 = []

with open("input.txt", "r") as file:
    for line in file:
        num1, num2 = line.strip().split("   ")
        num1, num2 = float(num1), float(num2)

        list1.append(num1)
        list2.append(num2)

similarity = 0
for num1 in list1:
    duplicates = list2.count(num1)
    similarity += num1 * duplicates

print(similarity)
