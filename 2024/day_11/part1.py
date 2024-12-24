input = open("input", "r").read().strip()

nums = input.split()

skip = False
for i in range(25):
    for index, num in enumerate(nums):
        if skip:
            skip = False
            continue
        if num == "0":
            nums[index] = "1"
        elif(len(num) % 2 == 0):
            midpoint = len(num)//2
            num1, num2 = num[:midpoint], num[midpoint:]
            nums[index] = num1
            zeros = 0
            for i2, n in enumerate(num2):
                if n == "0" and i2 != len(num2)-1:
                    zeros += 1
                else:
                    break
            nums.insert(index, num2[zeros:])
            skip = True
        else:
            nums[index] = str(int(num)*2024)

print(len(nums))