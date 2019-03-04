from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1, projection = "3d", azim = 45, aspect='equal')
ax2 = fig.add_subplot(2, 2, 2, projection = "3d", azim = 45, aspect='equal')
ax3 = fig.add_subplot(2, 2, 3, projection = "3d", azim = 45, aspect='equal')
ax4 = fig.add_subplot(2, 2, 4, projection = "3d", azim = 45, aspect='equal')

def animate(i):
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = np.outer(np.cos(u), np.sin(v))
    y = np.outer(np.sin(u), np.sin(v))
    z = np.outer(np.ones(np.size(u)), np.cos(v))

    scale = np.arange(-1.0,1.1,0.1)
    scale0 = np.zeros(len(scale))

    theta = 0
    phi = 0

    ax1.cla()
    ax1.plot_wireframe(x, y, z, color="darkgrey", linewidth=0.2)
    ax1.plot(scale,scale0,scale0, color="blue", marker="|")
    ax1.plot(scale0,scale,scale0, color="red", marker="|")
    ax1.plot(scale0,scale0,scale, color="green", marker="_")
    ax1.scatter(0,0,0, color="black")
    ax1.quiver(0,0,0,np.sin(theta)*np.cos(phi),-np.sin(theta)*np.sin(phi)*np.cos(i/10)-np.cos(theta)*np.sin(i/10),-np.sin(theta)*np.sin(phi)*np.sin(i/10)+np.cos(theta)*np.cos(i/10), color="black")
    ax1.set_xlabel("X-axis")
    ax1.set_ylabel("Y-axis")
    ax1.set_zlabel("Z-axis")
    ax1.set_title("X-Rotation(θ=0 φ=0)")

    theta = 0
    phi = 0

    ax2.cla()
    ax2.plot_wireframe(x, y, z, color="darkgrey", linewidth=0.2)
    ax2.plot(scale,scale0,scale0, color="blue", marker="|")
    ax2.plot(scale0,scale,scale0, color="red", marker="|")
    ax2.plot(scale0,scale0,scale, color="green", marker="_")
    ax2.scatter(0,0,0, color="black")
    ax2.quiver(0,0,0,-np.sin(theta)*np.cos(phi)*np.cos(i/10)+np.cos(theta)*np.sin(i/10),np.sin(theta)*np.sin(phi),np.sin(theta)*np.cos(phi)*np.sin(i/10)+np.cos(theta)*np.cos(i/10), color="black")
    ax2.set_xlabel("X-axis")
    ax2.set_ylabel("Y-axis")
    ax2.set_zlabel("Z-axis")
    ax2.set_title("Y-Rotation(θ=0 φ=0)")

    theta = np.pi/2
    phi = 0

    ax3.cla()
    ax3.plot_wireframe(x, y, z, color="darkgrey", linewidth=0.2)
    ax3.plot(scale,scale0,scale0, color="blue", marker="|")
    ax3.plot(scale0,scale,scale0, color="red", marker="|")
    ax3.plot(scale0,scale0,scale, color="green", marker="_")
    ax3.scatter(0,0,0, color="black")
    ax3.quiver(0,0,0,np.sin(theta)*np.cos(phi)*np.cos(i/10)+np.sin(theta)*np.sin(phi)*np.sin(i/10),np.sin(theta)*np.cos(phi)*np.sin(i/10)-np.sin(theta)*np.sin(phi)*np.cos(i/10),np.cos(theta), color="black")
    ax3.set_xlabel("X-axis")
    ax3.set_ylabel("Y-axis")
    ax3.set_zlabel("Z-axis")
    ax3.set_title("Z-Rotation(θ=π/2 φ=0)")

    theta = np.pi
    phi = 0

    ax4.cla()
    ax4.plot_wireframe(x, y, z, color="darkgrey", linewidth=0.2)
    ax4.plot(scale,scale0,scale0, color="blue", marker="|")
    ax4.plot(scale0,scale,scale0, color="red", marker="|")
    ax4.plot(scale0,scale0,scale, color="green", marker="_")
    ax4.scatter(0,0,0, color="black")
    ax4.quiver(0,0,0,np.sin(theta)*np.cos(phi)*np.cos(i/10)+np.sin(theta)*np.sin(phi)*np.sin(i/10),np.sin(theta)*np.cos(phi)*np.sin(i/10)-np.sin(theta)*np.sin(phi)*np.cos(i/10),np.cos(theta), color="black")
    ax4.set_xlabel("X-axis")
    ax4.set_ylabel("Y-axis")
    ax4.set_zlabel("Z-axis")
    ax4.set_title("Z-Rotation(θ=π φ=0)")

ani = animation.FuncAnimation(fig, animate, interval=10, frames = int(20*np.pi))
ani.save("blochSphere.gif", writer = 'imagemagick', dpi=350)
#plt.show()
