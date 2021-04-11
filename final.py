
from psychopy import visual,core,clock,event
import random as r

def r_pos(x_loc_list,y_pos=0):
    """Pick a random position from a list, return it as part of an x,y tuple"""
    random_x_list_index = r.randint(0,len(x_loc_list)-1)
    output_coordinate_pair = (x_loc_list[random_x_list_index],0)
    return(output_coordinate_pair)

# experiment set up
win= visual.Window(size=(800,800))
fs = visual.TextStim(win, "+", color = "white", height = 0.2)
cue = visual.Rect(win,width=1,height = 0.3, lineColor="white")
cue.pos = (0,0)



# put a loop on this to run it multiple times 
# measuring reaction time

# background circles
circle_size = 0.25
circle_1 = visual.Circle(win,size=circle_size)
circle_2 = visual.Circle(win,size=circle_size)
circle_3 = visual.Circle(win,size=circle_size)
circle_4 = visual.Circle(win,size=circle_size)
circle_list =[circle_1,circle_2,circle_3,circle_4]

# currently they are unequal!!!!
circle_spread = 0.4
circle_x_positions = [-2*circle_spread,-1*circle_spread,1*circle_spread,2*circle_spread]

for idx,circle in enumerate(circle_list):
    circle.pos = (circle_x_positions[idx],0)
    circle.lineColor = "white"
    circle.fillColor = "white"
    pass

# target circle
target = visual.Circle(win, size = 0.25)
target.lineColor = "black"
target.fillColor = "black"

# helper function
def draw_background():
    fs.draw()
    cue.draw()
    [circle.draw() for circle in circle_list]
    return

def xp():
    target.pos = r_pos(circle_x_positions)
    draw_background()
    win.flip()
    core.wait(1)
    draw_background()
    target.draw()
    win.flip()

    k = event.waitKeys(keyList=["z","slash","q"])
    rtclock = clock.Clock()
    rt = rtclock.getTime()
    if (k[0] == "key") :
        core.quit()
    elif (k[0] == "z") :
        print("z")
    elif (k[0] == "slash") :
        print("/")
    else:
        pass
    print("rt = " + str(rt))
    return()

for i in range(3):
    xp()
    pass
core.quit()
