import turtle
import random

# Set up the screen and turtle
screen = turtle.Screen()      
screen.bgcolor("black")     

# Set up the turtle
t = turtle.Turtle()        
t.speed(3)
t.pensize(25)          
t.shape("turtle")
t.pencolor("white")
t.fillcolor("white")             
turtle.colormode(255)         # Use RGB color mode with values from 0 to 255

def draw_rectangle(width, height):
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)

# Setup the turtle
t.penup()
t.goto(-350, -150)
t.pendown()
t.pencolor(14, 82, 201)
draw_rectangle(630, 300)

# Function to change color gradually (RGB)
def change_color(r, g, b, increment):
    r += increment            
    g += increment           
    b += increment           
    if r > 255:             
        r = 255
    if g > 255:               
        g = 255
    if b > 255:           
        b = 255
    return r, g, b          

# Draw the letter A with a gradient
def draw_A(r, g, b, increment):
    t.left(60)                # Turn the turtle 60 degrees to the left
    t.pencolor(r, g, b)       # Set the pen color to the current RGB values
    t.forward(120)            # Move forward 120 units to draw the first leg of 'A'
    
    r, g, b = change_color(r, g, b, increment)  # Update the color for gradient effect
    t.pencolor(r, g, b)       # Set the new pen color
    t.right(120)              # Turn 120 degrees to the right
    t.forward(120)            # Draw the second leg of 'A'
    
    r, g, b = change_color(r, g, b, increment)
    t.pencolor(r, g, b)
    t.backward(50)            # Move backward 50 units to the middle of the leg
    
    r, g, b = change_color(r, g, b, increment)
    t.pencolor(r, g, b)
    t.right(120)              # Turn 120 degrees to the right
    t.forward(60)             # Draw the crossbar of 'A'
    
    t.penup()                 
    #move to the starting position for the next letter 
    t.backward(140)              
    t.right(90)
    t.backward(45)                                      
    t.pendown()               
    return r, g, b           

# Draw the letter N with a gradient
def draw_N(r, g, b, increment): 
    t.pencolor(r, g, b)
    t.forward(100)            # Draw the left vertical line of 'N'
    
    r, g, b = change_color(r, g, b, increment)
    t.pencolor(r, g, b)
    t.right(150)              # Turn to draw the diagonal line
    t.forward(115)            # Draw the diagonal line of 'N'
    
    r, g, b = change_color(r, g, b, increment)
    t.pencolor(r, g, b)
    t.left(150)               # Adjust to draw the right vertical line
    t.forward(100)            # Draw the right vertical line of 'N'
    
    t.penup()
    t.backward(100)           # Move back to the baseline
    t.right(90)               # Face forward
    t.forward(60)             # Move to the position for the next letter
    t.pendown()
    return r, g, b

# Draw the letter D with a gradient
def draw_D(r, g, b, increment):
    t.left(90)                # Face upward to start drawing 'D'
    t.pencolor(r, g, b)
    t.forward(100)            # Draw the vertical line of 'D'
    
    r, g, b = change_color(r, g, b, increment)
    t.pencolor(r, g, b)
    t.right(90)               # Face right to draw the curve
    t.circle(-50, 180)        # Draw a half-circle to form the curved part
    
    t.penup()

    t.right(70)                # Adjust orientation
    t.backward(40)            # Move down to the baseline
    t.right(90)               # Face forward
    t.forward(100)             # Move to the position for the next letter
    t.pendown()
    return r, g, b

# Draw the letter Y with a gradient
def draw_Y(r, g, b, increment):
    t.left(50)                # Turn left to start the left branch of 'Y'
    t.pencolor(r, g, b)
    t.forward(110)            # Draw the left branch
    
    r, g, b = change_color(r, g, b, increment)
    t.pencolor(r, g, b)
    t.right(190)
    t.penup()              # Turn around to draw the right branch
    t.forward(110)            # Move back to the starting point
    t.pendown()

    r, g, b = change_color(r, g, b, increment)
    t.pencolor(r, g, b)
    # Move halfway back
    t.penup()
    t.backward(50)             
    t.pendown()

    r, g, b = change_color(r, g, b, increment)
    t.pencolor(r, g, b)
    t.right(130)              # Turn to draw the right branch of 'Y'
    t.forward(60)             # Draw the right branch
    
    
    t.left(60)                # Adjust orientation back to horizontal
    t.penup()
    t.forward(40)             
    t.right(90)
    t.forward(100)            # Move down to the baseline
    t.left(90)
    t.pendown()
    return r, g, b

# Set the starting position
t.penup()
t.goto(-250, -50)      
t.pendown()

# Set the initial color (starting with blue)
r, g, b = 0, 0, 255           # Initialize RGB values to blue
increment = 10                # Set the increment for color change

# Draw the letters A, N, D, Y with a gradient effect
r, g, b = draw_A(r, g, b, increment)  
r, g, b = draw_N(r, g, b, increment)  
r, g, b = draw_D(r, g, b, increment)  
r, g, b = draw_Y(r, g, b, increment)

# Draw stars in random positions
def draw_star(size):
    for _ in range(5):
        t.forward(size)
        t.right(144)
for _ in range(12):
    t.speed(0)
    t.pensize(3)
    t.penup()
    t.goto(random.randint(-400, 400), random.randint(-300, 300))
    t.pendown()
    draw_star(random.randint(5, 25))

t.hideturtle()                
turtle.done()               




