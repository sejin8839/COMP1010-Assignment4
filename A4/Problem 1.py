# Assignment written by: ___Sejin Yoon_______

# The next line allows this file to access code in the other file.
# Just accept the need for it for now, but it will soon be explained.
from A4_shapes import *

# Write your assignment scripts in the lines that follow
# You may only make function calls to
# draw_up_triangle()
# draw_down_triangle()
# draw_box()
# to make the required shapes

# As an example, if the assignment required you to make an X shape using the function calls,
# you could write
draw_down_triangle()
draw_up_triangle()

print() # keep this line to add a space between sections

# Keep the above example in your final assignment.


# Part 1.a - add lines between this comment and the print statement to make a
# closed diamond shape by calling the above functions.

draw_up_triangle()
draw_down_triangle()
draw_down_triangle()
draw_down_triangle()
draw_up_triangle()


print() # keep this line to add a space between sections



# Part 1.b - add lines that make a house shape (roof and square house)
# by calling the above functions.

draw_up_triangle()
draw_box()
draw_box()
draw_box()
draw_box()
print() # keep this line to add a space between sections


# Part 1.c - add lines that make a rocket shape
# (nose cone with the point on top, 2 squares for a body, and an engine nozzle with the wide part aiming down)
# by calling the above functions.

draw_up_triangle()
draw_box()
draw_box()
draw_down_triangle()
draw_box()
draw_box()
draw_down_triangle()
draw_box()
draw_box()
draw_down_triangle()
print() # keep this line to add a space between sections

# Part 1.d - the code below will repeat a drawing 5 times. Add calls
# to the draw functions and your own print statements in the indented area
# to make a pretty repeating pattern of your design.

for count in range(0, 5):
    draw_up_triangle()
    draw_down_triangle()
    draw_box()
    draw_box()
    print()


