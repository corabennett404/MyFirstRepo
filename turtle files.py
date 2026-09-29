import turtle
# creates a reference to the drawing screen
t = turtle.Turtle()

for shape in range(36):
    for side in range(4):
        t.forward(80)
        t.right(90)
    t.right(10)
    
turtle.done()
                
                
