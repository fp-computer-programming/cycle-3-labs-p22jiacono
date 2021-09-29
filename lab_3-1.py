#Author:JTI 9/29/21

x= int(input("Enter number of Points: "))

if x >= 15:
    print("You won Gold!")
else:
    if x >= 12:
        print("You won silver!")
    else:
        if x < 9:
            print(" You did not win a metal.")
        else:
            print("You won bronze!")
