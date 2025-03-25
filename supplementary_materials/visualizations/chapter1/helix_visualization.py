import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Create a figure and 3D axis
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Parameters for the helix
a = 1  # radius
b = 0.2  # pitch
t = np.linspace(0, 8*np.pi, 1000)  # parameter range

# Helix parametrization
x = a * np.cos(t)
y = a * np.sin(t)
z = b * t

# Calculate tangent vectors (normalized)
dx = -a * np.sin(t)
dy = a * np.cos(t)
dz = b * np.ones_like(t)

# Normalize tangent vectors
norm = np.sqrt(dx**2 + dy**2 + dz**2)
dx, dy, dz = dx/norm, dy/norm, dz/norm

# Plot the helix
ax.plot(x, y, z, 'b', linewidth=2, label='Helix')

# Sample points to show tangent vectors
sample_indices = np.arange(0, len(t), 100)
ax.quiver(x[sample_indices], y[sample_indices], z[sample_indices], 
          dx[sample_indices], dy[sample_indices], dz[sample_indices], 
          color='r', length=0.5, normalize=True, label='Tangent Vectors')

# Calculate curvature
curvature = a / (a**2 + b**2)
print(f"Curvature of the helix: {curvature}")

# Calculate normal vectors
nx = -np.cos(t)
ny = -np.sin(t)
nz = np.zeros_like(t)

# Normalize normal vectors
norm_n = np.sqrt(nx**2 + ny**2 + nz**2)
nx, ny, nz = nx/norm_n, ny/norm_n, nz/norm_n

# Calculate binormal vectors using cross product
bx = dy*nz - dz*ny
by = dz*nx - dx*nz
bz = dx*ny - dy*nx

# Sample points to show normal vectors
ax.quiver(x[sample_indices], y[sample_indices], z[sample_indices], 
          nx[sample_indices], ny[sample_indices], nz[sample_indices], 
          color='g', length=0.5, normalize=True, label='Normal Vectors')

# Sample points to show binormal vectors
ax.quiver(x[sample_indices], y[sample_indices], z[sample_indices], 
          bx[sample_indices], by[sample_indices], bz[sample_indices], 
          color='purple', length=0.5, normalize=True, label='Binormal Vectors')

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Helix with Frenet Frame Vectors')
ax.legend()

# Set equal aspect ratio
ax.set_box_aspect([1,1,1])

# Save the figure
plt.savefig('/home/ubuntu/MIT_Differential_Geometry_18.950_Textbook/supplementary_materials/visualizations/chapter1/helix_with_frenet_frame.png', dpi=300, bbox_inches='tight')

# Create an animation of a point traveling along the helix with its Frenet frame
fig2 = plt.figure(figsize=(10, 8))
ax2 = fig2.add_subplot(111, projection='3d')

# Plot the helix
helix_line, = ax2.plot([], [], [], 'b', linewidth=2)

# Vectors for the Frenet frame
tangent_arrow = ax2.quiver([], [], [], [], [], [], color='r', length=0.5)
normal_arrow = ax2.quiver([], [], [], [], [], [], color='g', length=0.5)
binormal_arrow = ax2.quiver([], [], [], [], [], [], color='purple', length=0.5)

# Point on the helix
point, = ax2.plot([], [], [], 'ko', markersize=8)

# Set labels and title
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')
ax2.set_title('Traveling Point on Helix with Frenet Frame')

# Set axis limits
ax2.set_xlim([-1.5, 1.5])
ax2.set_ylim([-1.5, 1.5])
ax2.set_zlim([0, 5])

# Set equal aspect ratio
ax2.set_box_aspect([1,1,1])

# Add a legend
ax2.legend(['Helix', 'Tangent', 'Normal', 'Binormal', 'Point'])

def init():
    helix_line.set_data([], [])
    helix_line.set_3d_properties([])
    point.set_data([], [])
    point.set_3d_properties([])
    return helix_line, tangent_arrow, normal_arrow, binormal_arrow, point

def update(frame):
    # Update helix line
    helix_line.set_data(x[:frame], y[:frame])
    helix_line.set_3d_properties(z[:frame])
    
    # Update point position
    point.set_data([x[frame]], [y[frame]])
    point.set_3d_properties([z[frame]])
    
    # Update Frenet frame vectors
    tangent_arrow.remove()
    normal_arrow.remove()
    binormal_arrow.remove()
    
    tangent_arrow = ax2.quiver(x[frame], y[frame], z[frame], 
                              dx[frame], dy[frame], dz[frame], 
                              color='r', length=0.5)
    
    normal_arrow = ax2.quiver(x[frame], y[frame], z[frame], 
                             nx[frame], ny[frame], nz[frame], 
                             color='g', length=0.5)
    
    binormal_arrow = ax2.quiver(x[frame], y[frame], z[frame], 
                               bx[frame], by[frame], bz[frame], 
                               color='purple', length=0.5)
    
    return helix_line, tangent_arrow, normal_arrow, binormal_arrow, point

# Create animation
ani = FuncAnimation(fig2, update, frames=np.arange(0, len(t), 10), 
                    init_func=init, blit=False, interval=50)

# Save the animation
ani.save('/home/ubuntu/MIT_Differential_Geometry_18.950_Textbook/supplementary_materials/visualizations/chapter1/helix_animation.mp4', 
         writer='ffmpeg', fps=30, dpi=200)

print("Visualizations created successfully!")
