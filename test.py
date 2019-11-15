from tkinter import *

seta ='''X_cursor
arrow
based_arrow_down
based_arrow_up
boat
bogosity
bottom_left_corner
bottom_right_corner
bottom_side
bottom_tee
box_spiral
center_ptr
circle
clock
coffee_mug
cross
cross_reverse
crosshair
diamond_cross
dot
dotbox
double_arrow
draft_large
draft_small
draped_box
exchange
fleur
gobbler
gumby
hand1
hand2
heart
icon
iron_cross
left_ptr
left_side
left_tee
leftbutton
ll_angle
lr_angle
man
middlebutton
mouse
pencil
pirate
plus
question_arrow
right_ptr
right_side
right_tee
rightbutton
rtl_logo
sailboat
sb_down_arrow
sb_h_double_arrow
sb_left_arrow
sb_right_arrow
sb_up_arrow
sb_v_double_arrow
shuttle
sizing
spider
spraycan
star
target
tcross
top_left_arrow
top_left_corner
top_right_corner
top_side
top_tee
trek
ul_angle
umbrella
ur_angle
watch
xterm
'''
seta=seta.split("\n")
n = 0
def muda(event):
    global n
    n=n+1
    try:
        root.config(cursor=seta[n])
    except:
        n=0
        root.config(cursor=seta[n])
    print(seta[n])
    
def volta(event):
    global n
    n=n-1
    try:
        root.config(cursor=seta[n])
    except:
        n=0
        root.config(cursor=seta[n])
    print(seta[n])

root = Tk()
root.geometry('500x500+1000+100')
fbg1 = Frame(root, bg='black')
fbg1.pack(side=LEFT, fill=BOTH, expand=True)
fbg2 = Frame(root, bg='white')
fbg2.pack(side=LEFT, fill=BOTH, expand=True)
root.bind('<Button-1>', muda)
root.bind('<Button-3>', volta)


