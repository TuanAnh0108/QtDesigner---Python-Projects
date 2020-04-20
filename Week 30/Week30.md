```.py

import math

list = []


class Bicycle:
    number_of_bicycle = 0

    def __init__(self, size, chain, tire_size):
        self.size = size
        self.chain = chain
        self.tire_size = tire_size

        self.tire_size = 29
        self.chain = 11
        self.size = "M"

        self.number_of_bicycle = self.number_of_bicycle + 1
        
    def showNumber(self):
        print(self.number_of_bicycle)
    
    def post_initialize(self):
        return self.size * int(math.pi)

    def spares(self):
        print(self.tire_size)
        print(self.chain)


class MountainBike(Bicycle):
    number_of_Mbike = 0

    def __init__(self, front_fork, rear_shock):
        self.front_fork = front_fork
        self.rear_shock = rear_shock

        self.tire_size = 27.5
        self.front_fork = 100
        self.rear_shock = 80

        self.number_of_Mbike = self.number_of_Mbike + 1
        
     def showNumber_MB(self):
         print(self.number_of_Mbike)

```
