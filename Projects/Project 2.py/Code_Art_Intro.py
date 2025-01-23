# ###############################################
# ### SETUP ###
import turtle
# ###############################################

t = turtle.Turtle()
t.speed( 2000 )
t.penup()
t.goto(-350, 50)
t.color("blue")
t.pendown()


for i in range(500) :
    t.forward(100)
    t.left(90 + 1)
t.color("yellow")
t.penup()
t.goto(-170, 20)
t.pendown()
for i in range(500) :
    t.forward(100)
    t.left(90 + 1)
t.color("black")
t.penup()
t.goto(-170, 1000)
t.pendown()
for i in range(500) :
    t.forward(100)
    t.left(90 + 1)
t.color("green")
t.penup()
t.goto(-1, 20)
t.pendown()
for i in range(500) :
    t.forward(100)
    t.left(90 + 1)
t.color("red")
t.penup()
t.goto(190, 50)
t.pendown()
for i in range(500) :
    t.forward(100)
    t.left(90 + 1)


    
   



# ###############################################
# ### ENDING ###
turtle.exitonclick()
# ###############################################