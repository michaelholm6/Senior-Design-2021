import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import animation
import random
colors = ['blue','darkgreen','green','yellow','red','peru','brown','grey','black']
cmap = matplotlib.colors.ListedColormap(colors, name='colors', N=None)
X= np.zeros((100,100))
for i in range(0,100):
    for j in range(0,100):
        if 10<=i<=20 and 0<=j<=75:
            X[i,j]= 4#mud path
        elif 5<=i<=25 and 75<j<=95:
            X[i,j]=5#wood
        elif 40<=i<=77 and 30<=j<=80:
            X[i,j]=-1 #water
        elif 80<=i<=93 and 50<=j<=66:
            X[i,j]=6 #metal storage house
        elif 27<i<35:
            if 10<=j<=17 or 25<=j<=33 or 45<=j<=52 or 66<=j<=74 or 80<=j<=86:
                X[i,j]=0 #tree
            else:
                if i%2==0 and j%2==0:
                    X[i,j] = 2 # dried grass
                else:
                    X[i,j] = 1# normal grass
        else:
            if i%2==0 and j%2==0:
                X[i,j]= 2 # dried grass
            else:
                X[i,j]=1#normal grass
X[1,1]=3
fig = plt.figure()
im = plt.imshow(X,cmap=cmap)
numbers=[-1,0.4,0.6,0.7,0,0.3,0.5,0.2,-2]
def animate(i):
    im.set_data(X)
    for i in range(1, 99):
        for j in range(1, 99):
            if X[i, j] == 3:
                flame = 0
                a = random.uniform(0, 1)
                for e in range(i - 1, i + 2):
                    for w in range(j - 1, j + 2):
                        if X[e, w]==0:
                            if a<numbers[1]:
                                X[e, w] = 3
                                flame += 1
                        elif X[e, w]==1:
                            if a<numbers[2]:
                                X[e, w] = 3
                                flame += 1
                        elif X[e, w]==2:
                            if a<numbers[3]:
                                X[e, w] = 3
                                flame += 1
                        elif X[e, w]==4:
                            if a<numbers[5]:
                                X[e, w] = 3
                                flame += 1
                        elif X[e, w]==5:
                            if a<numbers[6]:
                                X[e, w] = 3
                                flame += 1
                        elif X[e, w]==6:
                            if a<numbers[7]:
                                X[e, w] = 3
                                flame += 1
                if flame == 0:
                    X[i, j] = 7

interval = 500
anim = animation.FuncAnimation(fig, animate, interval=interval, frames=1000)
plt.show()



