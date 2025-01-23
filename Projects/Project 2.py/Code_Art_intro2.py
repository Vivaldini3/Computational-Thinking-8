# ###############################################
# ### SETUP ###
import turtle
# ###############################################

t = turtle.Turtle()
t.speed( 2000 )

#Spiral
t.penup()
t.goto(0, 0)
t.pendown()

colors = ["black","purple","green","pink"]
for i in range (1500) :
    t.color (colors[i% 4] )
    t.forward (1 + i)
    t.left (72 + 1)



t.penup()
t.goto(-100, -80)
t.color("blue")
t.pendown()

#blue circle
for i in range(400) :
    t.forward(200)
    t.left(90 + 1)

#yellow circle
t.penup()
t.goto(-10, -70)
t.pendown()
t.color("yellow")
for i in range(300) :
    t.forward(130)
    t.left(90 + 1)

#red circle
t.penup()
t.goto(-45, -5)
t.pendown()
t.color("red")
for i in range(400) :
    t.forward(70)
    t.left(90 + 1)



#black circle
t.penup()
t.goto(-90, 30)
t.pendown()
t.color("black")
for i in range(400) :
    t.forward(30)
    t.left(90 + 1)


#purple circle
t.penup()
t.goto(60, -30)
t.pendown()
t.color("purple")
for i in range(400) :
    t.forward(300)
    t.left(90 + 1)


#green circle
t.penup()
t.goto(5, -45)
t.pendown()
t.color("green")
for i in range(400) :
    t.forward(10)
    t.left(90 + 1)



#pink circle
t.penup()
t.goto(305, -85)
t.pendown()
t.color("pink")
for i in range(400) :
    t.forward(120)
    t.left(90 + 1)


#orange circle
t.penup()
t.forward(137)
t.left(27)
t.pendown()
t.color("orange")
for i in range(400) :
    t.forward(40)
    t.left(90 + 1)


#cyan circle
t.penup()
t.goto(-300, -85)
t.pendown()
t.color("cyan")
for i in range(400) :
    t.forward(248)
    t.left(90 + 1)


# ###############################################
# ### ENDING ###
turtle.exitonclick()
# ###############################################