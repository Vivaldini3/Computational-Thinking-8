# Section 1: setup
import codesters
from codesters import StageClass
stage = StageClass()

stage.set_background ("moon")
s1 = codesters.Sprite ("person1",0, -200)
s1.set_size(0.5)



# Section 2: define controls
def forward(sprite):
    sprite.forward (1)

def backward(sprite):
    sprite.backward (1)

def turn_left(sprite):
    heading=sprite.heading
    sprite.set_heading(heading + 1)

def turn_right(sprite):
    heading=sprite.heading
    sprite.set_heading(heading - 1)

def draw(sprite):
    sprite.pen_down()

def stop_drawing(sprite):
    sprite.pen_up()

def erase(sprite):
    sprite.pen_clear()

def red_pen(sprite):
    sprite.set_color("red")

def green_pen(sprite):
    sprite.set_color("green")

def blue_pen(sprite):
    sprite.set_color("blue")


# Section 3: define hide and show
def hide(sprite): 
    sprite.hide()

def show(sprite):
    sprite.show()



# Section 4: bind controls to specific keys
s1.event_key ("w",forward)
s1.event_key ("s", backward)
s1.event_key ("a", turn_left)
s1.event_key ("d", turn_right)
s1.event_key ("h", hide)
s1.event_key ("j", show)
s1.event_key ("o", draw)
s1.event_key ("r", red_pen)
s1.event_key ("g", green_pen)
s1.event_key ("b", blue_pen)
s1.event_key ("p", stop_drawing)
s1.event_key ("l", erase)
# Section 5: reminder message
print("Game has started. Open the screen using PORTS to play")