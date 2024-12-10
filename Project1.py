###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

stage.set_background ("soccer field")



q1 = codesters.Square (-100, -100, 200, 'blue')
q2 = codesters.Square (100, -100, 200, 'yellow')
q3 = codesters.Square (-100, 100, 200, 'red')
q4 = codesters.Square (100, 100, -200, 'green')


s2 = codesters.Sprite ("Maldini, and R9", 100, 100)
s2.set_size(0.25)
s1 = codesters.Sprite ("Sports", -100, -100)
s1.set_size(0.15)
s3 = codesters.Sprite ("images", 100, -100)
s3.set_size(0.7)
s4 = codesters.Sprite ("i", -100, 100)
s4.set_size(0.7)


message1 = codesters.Text ("Vivaash Ketan Lamba", 0,220,"black")
message2 = codesters.Text ("I like soccer", 0,-220,"blue")