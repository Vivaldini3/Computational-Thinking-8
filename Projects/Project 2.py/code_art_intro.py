# ###############################################
# ### SETUP ###
import turtle
# ###############################################

t = turtle.Turtle()
t.penup()
t.goto(-100, -10)
t.color("green")
t.pendown()


for i in range(10) :
    t.forward(10)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.penup()
    t.forward(20)
    t.pendown()
   



# ###############################################
# ### ENDING ###
turtle.exitonclick()
# ###############################################
