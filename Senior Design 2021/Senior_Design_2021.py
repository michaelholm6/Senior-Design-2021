import numpy as np
import matplotlib.pyplot as plt
import random
mesh= np.zeros((100,100))
for i in range(0,100):
    for j in range(0,100):
        if 10<=i<=20 and 0<=j<=75:
            mesh[i,j]= 0.35 #mud path
        elif 5<=i<=25 and 75<j<=95:
            mesh[i,j]=0.5 #wood
        elif 40<=i<=77 and 30<=j<=80:
            mesh[i,j]=-1 #water
        elif 80<=i<=93 and 50<=j<=66:
            mesh[i,j]=0.2 #metal storage house
        elif 27<i<35:
            if 10<=j<=17 or 25<=j<=33 or 45<=j<=52 or 66<=j<=74 or 80<=j<=86:
                mesh[i,j]=0.4 #tree
            else:
                if i%2==0 and j%2==0:
                    mesh[i,j] = 0.8  # dried grass
                else:
                    mesh[i,j] = 0.7 # normal grass
        else:
            if i%2==0 and j%2==0:
                mesh[i,j]= 0.8 # dried grass
            else:
                mesh[i,j]=0.7 #normal grass
plt.imshow(mesh)
mesh[1,1]=0
for i in range(1,99):
    for j in range(1,99):
        a= random.uniform(0,1)
        if mesh[i,j]==0:
            for e in range(i-1,i+2):
                for w in range(j-1,j+2):
                    if a<mesh[e,w]:
                        mesh[e,w]=0
                    else:
                        continue
plt.figure()
plt.imshow(mesh)
plt.show()



