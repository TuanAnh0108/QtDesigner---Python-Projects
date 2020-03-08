import sys
import math

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position

light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]
dir = ""

while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    if (initial_tx > light_x and initial_ty > light_y):
        initial_tx -= 1
        initial_ty -= 1
        dir = "NW"
    elif (initial_tx > light_x and initial_ty < light_y):
        initial_tx -= 1
        initial_ty += 1
        dir = "SW"
    elif (initial_tx < light_x and initial_ty < light_y):
        initial_tx += 1
        initial_ty += 1
        dir = "SE"
    elif (initial_tx < light_x and initial_ty > light_y):
        initial_tx += 1
        initial_ty -= 1
        dir = "NE"
    elif (initial_tx > light_x):
        dir = "W"
    elif (initial_tx < light_x):
        dir = "E"
    elif (initial_ty > light_y):
        dir = "N"
    elif (initial_ty > light_y):
        dir = "S"
   
    print(dir)
