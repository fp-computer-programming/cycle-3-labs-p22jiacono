#Author: JTI 9/30/21

a = input("Enter number of magic charge: ")
b = input("Enter number of shield charge: ")
if not int(a) >= 90 and int(b) >= 75: 
    print("The dragon burns you to a crisp.")
else:
    print("You defeated the dragon! But the princess is in another castle.")