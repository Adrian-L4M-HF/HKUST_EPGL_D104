# D104 Summer 2022
# Circle and Cross

import turtle

# Create a new turtle with color c, and move it to the coordinates, (x, y)
def create_turtle(c, x=0, y=0):
    new_turtle = turtle.Turtle()
    new_turtle.shape("turtle")
    new_turtle.shapesize(2, 2)
    new_turtle.pensize(5)
    new_turtle.color(c, c)
    new_turtle.up()
    new_turtle.goto(x, y)
    return new_turtle

# draw the game board
def draw_game_board():
    turtle.hideturtle()
    turtle.up()
    turtle.speed(0)
    turtle.goto(-cell_size, cell_size)
    turtle.down()
    for _ in range(4):
        turtle.forward(cell_size)
        turtle.right(90)
    turtle.forward(cell_size)
    for _ in range(4):
        turtle.forward(cell_size)
        turtle.right(90)
    turtle.up()

# draw a cross  with the turtle, t, with center (x, y) with height, s
def draw_cross(t, x, y, s):
    t.up()
    t.goto(x-s/2, y-s/2)
    t.down()
    t.goto(x+s/2, y+s/2)
    t.up()
    t.goto(x-s/2, y+s/2)
    t.down()
    t.goto(x+s/2, y-s/2)
    t.up()

# draw a circle with the turtle, t, with center (x, y) and diameter, s
def draw_circle(t, x, y, s):
    t.up()
    t.goto(x, y-s/2)
    turtle.setheading(0)
    t.down()
    t.circle(s/2)    

# Play() function is the event handler for the onscreenclick event
def play(x, y):
    global circle_turtle, cross_turtle
    if y > 0 and y < cell_size and x < cell_size and x > -cell_size:
        # TODO 1: 
        # Step 1: if x is smaller than zero, call draw_cross() function 
        #         with the 4 arguments:
        #                 cross_turtle, -cell_size/2, cell_size/2, cell_size
        if x < 0:
            draw_cross(cross_turtle, -cell_size/2, cell_size/2, cell_size)
        # Step 2: otherwise, call draw_circle() function 
        #         with the 4 arguments:
        #                 circle_turtle, cell_size/2, cell_size/2, cell_size
        else:
            draw_circle(circle_turtle, cell_size/2, cell_size/2, cell_size)

    else:
        # clear, reset and init the game again
        turtle.clearscreen()
        draw_game_board()
        circle_turtle = create_turtle("red", cell_size/2, 0)
        cross_turtle = create_turtle("green", -cell_size/2, 0)    
        turtle.onscreenclick(play)


# main part of the program
cell_size = 50
turtle.setworldcoordinates(-cell_size*2, -cell_size*2, cell_size*2, cell_size*2)
draw_game_board()
circle_turtle = create_turtle("red", cell_size/2, 0)
cross_turtle = create_turtle("green", -cell_size/2, 0)    

# TODO 2:
# Bind the event handler, play, with the onscreenclick()
turtle.onscreenclick(play)

turtle.done()
