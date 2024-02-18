# Raj Shah
# 2/4/24
# Intro To Programming Logic
# Project Name: Raj's Chai Software Sales
############################################

# A software company sells a Parcel that retails for $100
# Quantity discounts are given according to the following table:
###############################      
#      Quantity        Discount
#       < 10            0   ##
#       10-19           10% ##
#       20-49           20% ##
#       50-99           30% ##
#       100 or more     40% ##
##############################

# Design and write a program that asks the user to enter their name and the number of parcels purchased. 
# The program will display a sales receipt with the following information:

# Welcome
print("Welcome to Raj's Chai Software Sales")

# Display Package Price
print("Package Price = $100")


# Display Discount Table 
print("Quantity        Discount")
print(" < 10                 0 ")
print(" 10-19               10%")
print(" 20-49               20%")
print(" 50-99               30%")
print(" 100 or More         40%")


Package = 100.0


# Input the Name

Name = input("What is your name ?")
DP = 0 # Discount Percentage
ST = 0 # SubTotal 
TP = 0 # Total Recipt Price
Discount = 0 #Discount value


# Input the Quantity of Package

Qty_Str = input("Enter your Quantity: ")

Qty = int(Qty_Str)

ST = (Package * Qty)  # SubTotal Value
# If Logic
if Qty < 10:
    DP = 0
    Discount = (ST/100) * DP
elif Qty >= 10 and Qty <= 19:
    DP = 10
    Discount = (ST / 100) * DP
elif Qty >= 20 and Qty <= 49:
    DP = 20
    Discount = (ST/100) * DP
elif Qty >= 50 and Qty <= 99:
    DP = 30
    Discount = (ST / 100) * DP
elif Qty >= 100:
    DP = 40
    Discount = (ST/ 100) * DP
else:
    print("Invaild Quantity")

# Discount Value
 #   DV = (ST * DPP)
# Total Recipt Value
TP = ST-Discount

# Printing the Recipt
print("Name:",Name)
print("Quantity of Package:",Qty)
print("Discount Percentage:",DP)
print("Subtotal:",ST)
print("Discount Amount:",Discount)
print("Total Recipt Price:",TP)








