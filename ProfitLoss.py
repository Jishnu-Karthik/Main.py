Buying = float(input("Enter the amount for which you've bought the item:"))
Selling = float(input("Enter the amount for which you're selling the item:"))

if Selling > Buying:
	Amount = Selling - Buying
	print("The total profit is: {0}".format(Amount))

else:
	print("You are selling the item at no profit.")