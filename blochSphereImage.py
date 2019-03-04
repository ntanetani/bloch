from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import random

fig = plt.figure()
ax = fig.gca(projection='3d')

u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = np.outer(np.cos(u), np.sin(v))
y = np.outer(np.sin(u), np.sin(v))
z = np.outer(np.ones(np.size(u)), np.cos(v))

theta = random.uniform(0, np.pi)
phi = random.uniform(0, 2*np.pi)
scale = [-1.0,-0.9,-0.8,-0.7,-0.6,-0.5,-0.4,-0.3,-0.2,-0.1,0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
scale0 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

ax.plot_wireframe(x, y, z, color='darkgrey', linewidth=0.2)
ax.plot(scale,scale0,scale0, color="blue", marker="|")
ax.plot(scale0,scale,scale0, color="red", marker="|")
ax.plot(scale0,scale0,scale, color="green", marker="_")
ax.scatter(0,0,0, color="black")
ax.quiver(0,0,0,np.sin(theta)*np.cos(phi),np.sin(theta)*np.sin(phi),np.cos(theta), color = "black")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
plt.show()
