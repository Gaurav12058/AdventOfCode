from functools import cmp_to_key


def violatesRule(list, rules):
    for rule in rules:
        if(rule[0] in list and rule[1] in list):
            if(list.index(rule[0]) > list.index(rule[1])):
                return True
    return False

def rulesf(x,y):
    if (x, y) in rules:
        return -1
    # If y should come before x
    elif (y, x) in rules:
        return 1
    # If no direct relationship exists, consider them equal
    else:
        return 0

with open("input_day5.txt", "r") as file:
    
    rules = []

    orders = []
    for line in file:
        if "|" in line:
            rules.append((int(line[0:2]), int(line[3:5])))
        if "," in line:
            orders.append(list(map(int, line.strip().split(","))))


    sum = 0
    correctOrders = list(orders)
    incorrectOrders = []
    for order in orders:
        if(violatesRule(order, rules)):
            correctOrders.remove(order)
            incorrectOrders.append(order)
            continue
    
    for order in correctOrders:
        sum += order[len(order)//2]

    print("Part 1:", sum)


    sum = 0
    newOrders = []
    newOrder = []
    for order in incorrectOrders:
        # for num in order:
        #     for index in range(len(newOrder)+1):
        #         newOrder.insert(index, num)
        #         if(violatesRule(newOrder, rules)):
        #             newOrder.remove(num)
        #         else:
        #             break
        # newOrders.append(newOrder)
        # newOrder = []
        order.sort(key=cmp_to_key(rulesf))
        sum += order[len(order)//2]
        
    # for order in newOrders:
    #     sum += order[len(order)//2]

    print("Part 2:", sum)
