import time
import random

print("This programme calculates final payout for sales on e-commerce websites. Such as: \n -Ebay \n -Depop \n")

currency = input("Please enter your desired currency: ")

loop = 1 
while loop == 1:
    site = input("Please enter chosen e-commerce site from the list: ")
    print("Calculating... \n")
    time.sleep(1)
    if site == "Ebay" or site == "ebay":
        
        print("Ebays current fees are 12.8% plus 30p of the final value of the order \n")
        payment = int(input("Enter Ebay sale price: "))
        payment = 0.872 * payment
        payment = payment - 0.3
        shipping = int(input("Enter shipping costs: "))
        payment = payment - shipping
        payment = round(payment, 2)
        print("Calculating... \n")
        time.sleep(1)
        print("Your final payout ammout will be: ", payment, currency)
        repeat = input("Would you like to calculate another payment?: ")
        print("Calculating... \n")
        time.sleep(1)
        if repeat == "yes" or repeat == "Yes":
            loop = 1
        else:
            loop = 0
            
    elif site == "Depop" or site == "depop":
        print("Depop and Paypal fees currently total 13.49% \n")
        payment = int(input("Enter Depop sale price: "))
        payment = 0.8651 * payment
        shipping = int(input("Enter shipping costs: "))
        payment = payment - shipping
        payment = round(payment, 2)
        print("Calculating... \n")
        time.sleep(1)
        print("Your final payout ammout will be: ", payment, currency)
        repeat = input("Would you like to calculate another payment?: ")
        print("Calculating... \n")
        time.sleep(1)
        if repeat == "yes" or repeat == "Yes":
            loop = 1
            
        else:
            loop = 0
        
    else:
        print("Website not supported.")
        loop = 1

print("Thanks for using!")
print("Built by Hugh Stanway")
