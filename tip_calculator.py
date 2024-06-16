# import necessary libraries

import sys
import tabulate
import warnings
warnings.filterwarnings("ignore")

# show menue

menue = {

    "Indian":{
        "Aloo Gobi": 80,
        "Butter Tikka" :60,
        "Chole Bhature" : 100,
        "Biryani":120,
        "Vada Pav": 50,
        "Chicken": 100,
        "Pasta": 70,
        "Pizza": 60,
        "Burger": 20,
        "Fries": 80
        },
    
    "chinese" :{
        "Chow Mein" :100,
        "Fried Rice": 70,
        "Fujian Red Wine Chicken":90,
        "Soy Egg" :60
    },

    "italian" :{
        "pizza":45,
        "pasta":58,
        "Franch Rice": 26,
        "Raspberry": 59
    }

}

print("--------Welcome to the Royal Restaurant--------")

bill = 0
person = 0

# ---------------------person counting on the table --------------------------------
"""This part of the code is asking the user to input the number of people in their group dining at the restaurant. It then checks if the total number of people exceeds 5, which is the table limit at the restaurant. If the limit is exceeded, it displays a message saying that the number of people is not allowed and exits the program using `sys.exit()`. This ensures that the restaurant's table limit is not exceeded."""

print("waiter : how many person you have sir ?")

people  = int(input("we are :"))
person += people

if person >5:
    print(f"sorry {person} people are not allowed our table limit is 5.")
    sys.exit()

# -----------------------------menue showing---------------------------------- 

"""This part of the code is creating a formatted table to display the menu items available at the restaurant. Here's a breakdown of what each step does:"""

table = []

for food , item in menue.items():
    table.extend([[food,item,price]  for item ,price in item.items()])

table = tabulate.tabulate(table,headers= ['Category','items','price'],tablefmt='grid')

print("here is your menue sir \n",table)

# ---------------------------taking orders from customers----------------------------------

# This part of the code is responsible for taking orders from the customers. Here's a breakdown of what it does:

print("what do you want to eat sir :")

is_order = True

while is_order:
    
    orders  = input("we want to eat :").title().split(",")
    for order in orders:
        order = order.strip()
        found = False
        for dish in menue:
            if order in menue[dish]:
                print(f"Here is your {dish} dish: {order} - ${menue[dish][order]}")
                bill += menue[dish][order]
                found = True
                break
        if not found :
            print(f"sorry {order} is not available")

    additional_order = input("what do want to oder again ?(yes/no) : ") #this is checkin if custome wants to place order again or not
    if additional_order == "no":
        is_order = False # this will be end the loop when customer don't want to place order again


# ----------------------display bill and tip ---------------------------


"""This part of the code is prompting the user to input the percentage of tip they would like to give for the service. The input is converted to an integer using `int(input())`."""
    
tip = int(input("what percentage of the tip you want to give : (choose  $1 to $20) : "))
print(f"thank you for the {(bill* person)* tip/100} tip here is your bill sir ${bill*person}")
print("thank you sir vist again.....")
        