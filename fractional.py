n = int(input("Enter the number of items : "))
items = []
for i in range(n):
    weight = int(input(f"Enter the weight for {i+1}th item"))
    profit = int(input(f"Enter the profit for {i+1}th item"))
    items.append([weight,profit])
capacity = int(input("Enter the max capacity : "))
for item in items:
    ratio = item[1]/item[0]
    item.append(ratio)
items.sort(key=lambda x : x[2],reverse = True)

total_profit = 0
remaining_capacity = capacity

for item in items:
    
    weight = item[0]
    profit = item[1]
    
    if weight <= remaining_capacity:
        total_profit += profit
        remaining_capacity -= weight
    else:
        fraction = remaining_capacity / weight
        total_profit += profit * fraction
        remaining_capacity = 0
        break
print("Maximum Profit : ",total_profit)

