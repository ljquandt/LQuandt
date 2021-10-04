# DSC510
# Week 5
# Programing Assignment Week 5 Loops
# Author Logan Quandt
# 9/29/2021

def performCalculation(operation_to_perform):
    numberone=input("Enter Number 1: ")
    numbertwo=input("Enter Number 2: ")
    calculatedtotal=eval(numberone + operation_to_perform + numbertwo)
    print("Caclculated Answer: ", calculatedtotal)

def calculateAverage():
    total=0
    count=int(input("Enter amount of numbers: "))
    for value in range(count):
        entered_number= float(input("Enter a number: "))
        total+=entered_number
    average=total / count
    print("The average value is: ", average)


def main():
    operation_to_perform=input("Please enter operation (+,-,*,/ or Avg) or enter -1 to end program: ")
    while operation_to_perform in ["+","-","*","/","Avg"]:
        if operation_to_perform == "Avg":
            calculateAverage()
        else:
            performCalculation(operation_to_perform)
        operation_to_perform=input("Please enter operation (+,-,*,/ or Avg) or -1 to end program: ")

if __name__ == '__main__':
    main()

