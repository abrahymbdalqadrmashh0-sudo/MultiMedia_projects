item1 = 50
item2 = 30
item3 = 20
budget = 100
total_cost = item1 + item2 + item3
print("Total cost of items:", total_cost)
print("Budget:", budget)
if total_cost <= budget:
    remaining = budget - total_cost
    print(" You are within budget. Money left:", remaining)
else:
    needed = total_cost - budget
    print(" You are over budget! You need", needed, "more.")