actual_cost=float(input("Please enter the actual product cost: "))
sale_amount=float(input("Please enter the sale amount: "))
if (sale_amount >actual_cost):
  amountpaid=sale_amount-actual_cost
  print("Total profit = {0}".format(amountpaid))
else :
  print( "No profit")
  


