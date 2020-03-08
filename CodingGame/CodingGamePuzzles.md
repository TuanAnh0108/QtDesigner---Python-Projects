# **Practice Loop**
```.py

  while 1:
    enemy_1 = input()  # name of enemy 1
    dist_1 = int(input())  # distance to enemy 1
    enemy_2 = input()  # name of enemy 2
    dist_2 = int(input())  # distance to enemy 2

    # Write an action using print

    # Enter the code here
    
    if dist_1 < dist_2:
        print(enemy_1)
    else:
        print(enemy_2)
```

# **The Descent**

```.py
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


# game loop
while 1:
    max = 0
    imax = 0
    for i in range(8):
        mountain_h = int(input()) # represents the height of one mountain, from 9 to 0. Mountain heights are provided from left to right.
        if mountain_h > max:  
            max = mountain_h
            imax = i

    print(imax)
```

# **The power of Thor**
```.py
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]
dir = ""
# game loop
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
```

# **There is no spoon**
```.py
width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
lines = []
for i in range(height):
    line = input()  # width characters, each either 0 or .
    lines.append(list(line))
for y in range(height):
    for x in range(width):
       if lines[y][x]== ".":
           continue
       rx = ry = bx = by = -1
       try:
           for tx in range(x+1, width):
               if(lines[y][tx]=='0'):
                   rx = tx
                   ry = y
                   break
       except Exception:
           pass
       try:
           for ty in range(y+1, height):
               if(lines[ty][x]=='0'):
                   bx = x
                   by =ty
                   break
       except Exception:
           pass
       print("{0} {1} {2} {3} {4} {5}".format(x, y, rx, ry, bx, by))
```
