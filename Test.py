# DSC510
# Week 4
# Programing Assignment Week 3 Conditional Statements
# Author Logan Quandt
# 9/22/2021

def main():
    print("Week 4 assignment: Completed")

def cost_calculation (a, b):
    calculated_cost = a * b
    return calculated_cost

print("Welcome!")
company_name = input('What is your company name?')
try:
    quantity = float(input('How many feet of Fiber Optic Cable are you looking to purchase today?'))
except:
    quantity = float(input("You entered a invalid number, please try again."))
if quantity > 0 and quantity < 100:
    price = 0.87
elif quantity >= 100 and quantity < 250:
    price = 0.80
elif quantity >= 250 and quantity < 500:
    price = 0.70
else:
    price = 0.50

final_price = cost_calculation(quantity, price)
print('Receipt')
print("Company Name:" + company_name)
print("Length in Feet:" + str(quantity))
print("Price per Foot:$" + str(price))
print("Calculated Cost (Fee times quantity ordered:$" + str(final_price))
print("Amount Paid:$" + str(final_price))

if __name__ == '__main__':
    main()
