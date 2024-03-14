#TMA4121: Matte4 OBLIG
#Skrevet av Sigve Smedshammer


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

# Parametere
Length_x = Length_y = 1.0  # Lengden av domenet i x- og y-retning
Nx = Ny = 50  # Antall gitterpunkter i x- og y-retning
T = 1.0  # Total tid
Nt = 200  # Antall tidssteg
alpha = 0.01  # Termisk diffusivitet

# Diskretisering
dx = Length_x / (Nx - 1)
dy = Length_y / (Ny - 1)
dt = T / Nt

# Initialbetingelser
u = np.zeros((Nx, Ny))

# Sett initialbetingelser: "Dirac" midt i rommet
u[Nx//2, Ny//2] = 10.0

# Oppsett av plottet
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = np.linspace(0, Length_x, Nx)
y = np.linspace(0, Length_y, Ny)
X, Y = np.meshgrid(x, y)
plot = [ax.plot_surface(X, Y, u, cmap="coolwarm")]

# Animasjonsfunksjon
def update_plot(frame, u, plot):
    un = u.copy()
    for i in range(1, Nx - 1):
        for j in range(1, Ny - 1):
            u[i, j] = un[i, j] + alpha * (dt / dx**2) * (un[i+1, j] - 2*un[i, j] + un[i-1, j]) + \
                                     alpha * (dt / dy**2) * (un[i, j+1] - 2*un[i, j] + un[i, j-1])
            
    plot[0].remove()
    plot[0] = ax.plot_surface(X, Y, u, cmap=cm.coolwarm)
    ax.set_title(f'Tidssteg: {frame}')
    ax.set_xlim(0, Length_x)
    ax.set_ylim(0, Length_y)
    ax.set_zlim(0, 0.05)
    

animation = FuncAnimation(fig, update_plot, frames=Nt, fargs=(u, plot), interval=10, blit=False)
animation.save("Varmelikning2D.gif")

plt.show()
