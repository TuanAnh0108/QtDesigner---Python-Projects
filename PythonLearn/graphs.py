1.
2. [HL] g(x) = 0.1*sin(0.1*m(x)), where m(x) = x^2, and x from 0 to 30 with steps of 0.05

import matplotlib.pyplot as pyplot
import math
x = []
y = []
min = 0

for i in range(600):
    x.append(min + 0.05 * (i+1))
    y.append(0.1 * math.sin(0.1 * (x[i]**2)))

pyplot.plot(x, y)
pyplot.xlabel('x')
pyplot.ylabel('y = 0.1 * sin(0.1 * m(x))')
