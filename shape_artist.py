import turtle
t = turtle.Turtle()
import math

choice = input("Circle or square?")
if choice == "square":
    area = int(input("Enter an area:"))
    side_length = math.sqrt(area)
    counter = 1
    while counter <=4: 
        t.forward(side_length)
        t.left(90)
        counter = counter + 1
    print("Your shape is complete!")
    
    
    
elif choice == "circle":                              
    area = int(input("Enter an area:"))
    t.circle(area)
    print("Your shape is complete!")
    
else:
    print("My name is Inigo Montoya.")
    print("You have provided an invalid shape.")
    print("Prepare to die.")
        


