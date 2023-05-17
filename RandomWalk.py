class RandomWalk
    def_init_(self, num_points=5000):
    "Attributes of walk"
    self.num_points = num_points

    #walks start at 0,0
    self.x_values = [0]
    self.y_values = [0]

    def fill_walk(self):

        while len(self.x_values) < self.num_points
            x_direction = choice ([1,-1])
            x_distance = choice ([0,1,2,3,4])
            y_step = y_direction * y_distance

            #reject redundant moves
            if x_step == 0 and y_step == 0:
                continue

            #calculate new position
            x = self.x_values[-1]+ x_step
            y = self.y_values[-1]+ y_step

            self.x_values.append(x)
            self.y_values.append(y)

import matplotlib.pyplot as plt
from random_walk import RandomWalk
rw = RandomWalk()
rw.fill_walk()
#plotpoints
plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(rw.x_values,iw.y_values, s=15)
plt.show()

