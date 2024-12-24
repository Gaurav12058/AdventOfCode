input = open("input", "r").read().strip()

cache = {}
blinks = 75

def recur(num, index):
    if (num, index) in cache:
        return cache[(num,index)]
    
    result = 0

    if(index == blinks):
        result = 1
    elif num == "0":
        result = recur("1", index+1)
    elif(len(num) % 2 == 0):
        midpoint = len(num)//2
        num1, num2 = num[:midpoint], num[midpoint:]
        zeros = 0
        for i2, n in enumerate(num2):
            if n == "0" and i2 != len(num2)-1:
                zeros += 1
            else:
                break
        result = recur(num1, index+1) + recur(num2[zeros:], index+1)
    else:
        result = recur(str(int(num)*2024), index+1)
    
    cache[(num,index)] = result
    return result


nums = input.split()
ans = 0
for num in nums:
    ans += recur(num, 0)

print(ans)