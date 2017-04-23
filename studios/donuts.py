#Donut - Studio Assignment
#Completed in class 4/20/17

#Scenario:
#You run a hip new artisanal donut shop, the Loop Hole, which, in its short lifetime, has already
#rocked the boutique-desserts market with numerous “disruptions”

#Write a program which introduces the flavor of the day, and then takes the user’s order.

#Taking their order involves asking two questions:
# 1- How many donuts do they want to buy?
# 2- How much do you want to pay per donut?

#After getting input, you should:
# 1- Inform the user of the total cost of their order.
# 2- Don’t forget to include sales-tax, which is, let’s say, 5%.

#################################
welcome_message = "Welcome to the Loop Hole!\nToday's Manager's Special is:"
manager_special = "Crunch Jelly: A traditional jelly donut in which the jelly filling is entirely made of Capn' Crunch Berries!"

print(welcome_message)
print(manager_special)
donut_amt = float(input("How many donuts would you like?\n"))
donut_price = float(input("How much would like to pay per donut? (Suggested price is $4.35 each)\n"))
sales_tax = 0.05

prep_invoice = "Ok, let me prepare that for you...."
total_msg = "After tax, your total is: "
thank_you = "Thank you for snacking!  Loop back around here soon!"
total_amt = donut_amt * donut_price * (1 + sales_tax)

print(prep_invoice)
print(total_msg, "$" + str(round(total_amt, 2)))
print(thank_you)

##################################
#Here’s an example of how the finished program should behave:

#Welcome to the Loop Hole!
#Today's Manager's Special is:
#Crunch Jelly: A traditional jelly donut in which the jelly filling is made entirely of Capn' Crunch
#Berries Oops All Berries
#How many would you like?
#>>> 3.33333
#How much would you like to pay per donut (suggested price is $4.35 each)?
#>>> 2.5
#Ok, let me prepare that for you....
#After tax, your total is: $8.74999125
#Thank you for snacking! Loop back around here soon!
##############################
