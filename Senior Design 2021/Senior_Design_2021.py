import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib import colors
import random
X= np.zeros((100,100))
for i in range(0,100):
    for j in range(0,100):
        if 10<=i<=20 and 0<=j<=75:
            X[i,j]= 0.35 #mud path
        elif 5<=i<=25 and 75<j<=95:
            X[i,j]=0.5 #wood
        elif 40<=i<=77 and 30<=j<=80:
            X[i,j]=-3 #water
        elif 80<=i<=93 and 50<=j<=66:
            X[i,j]=0.2 #metal storage house
        elif 27<i<35:
            if 10<=j<=17 or 25<=j<=33 or 45<=j<=52 or 66<=j<=74 or 80<=j<=86:
                X[i,j]=0.4 #tree
            else:
                if i%2==0 and j%2==0:
                    X[i,j] = 0.8  # dried grass
                else:
                    X[i,j] = 0.7 # normal grass
        else:
            if i%2==0 and j%2==0:
                X[i,j]= 0.8 # dried grass
            else:
                X[i,j]=0.7 #normal grass
colors_list = [(0.2,0,0), (0,0.5,0), (1,0,0), 'orange']
cmap = colors.ListedColormap(colors_list)
bounds = [0,1,2,3]
norm = colors.BoundaryNorm(bounds, cmap.N)

def iterate(X):
    for i in range(1, 99):
        for j in range(1, 99):
            if X[i, j] == 0:
                flame = 0
                a = random.uniform(0, 1)
                for e in range(i - 1, i + 2):
                    for w in range(j - 1, j + 2):
                        if a < X[e, w]:
                            X[e, w] = 0
                            flame += 1
                if flame == 0:
                    X[i, j] = -1
    X1=X
    return X1

fig = plt.figure(figsize=(25/3, 6.25))
ax = fig.add_subplot(111)
ax.set_axis_off()
im = ax.imshow(X, cmap=cmap, norm=norm)#, interpolation='nearest')

# The animation function: called to produce a frame for each generation.
def animate(i):
    im.set_data(animate.X)
    animate.X = iterate(animate.X)
# Bind our grid to the identifier X in the animate function's namespace.
animate.X = X

# Interval between frames (ms).
interval = 100
anim = animation.FuncAnimation(fig, animate, interval=interval, frames=200)
plt.show()



