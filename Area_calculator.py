#Area finding program
#Anami James
import math 

print("=======================================================================")
print("Area Calculator 📐")
print("=======================================================================")

print("1) Triangle")
print("2) Rectangle")
print("3) Square")
print("4) Circle")
print("5) Quit")

choice = int(input("Which shape: "))

while choice != 5 :
    if choice == 1 :
        base = int(input("Base: "))
        height = int(input("Height: "))
        area = (height * base) / 2
        print("The area is ", area)
    elif choice == 2 :
        length = int(input("Length: "))
        width= int(input("width: "))
        area = length * width
        print("The area is ", area)
    elif choice == 3 :
        side = int(input("Side: "))
        area = side ** 2
        print("The area is ", area)
    elif choice == 4 :
        radius = float(input("Radius: "))
        area = math.pi * (radius ** 2)
        print("The area is ", area)
    else : 
        print("Invalid choice, try again.")
    choice = int(input("Which shape: "))

if choice == 5 :
    print("Quitting the program , thanks for using it!")
