slices_input = input("Enter how many slices of pizza you want:")
slices = int(slices_input)

total_cost = slices * 1.5

money_input = input("Enter how many dollars you have: ")
money = int(money_input)

if total_cost > money:
    print("You do not have enough money to buy this much pizza!")
  
else:
    change = money - total_cost
    print("Here is your change:", change)
