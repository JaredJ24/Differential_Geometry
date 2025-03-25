import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create figures for different visualizations
fig1 = plt.figure(figsize=(10, 8))
ax1 = fig1.add_subplot(111, projection='3d')

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
ax1.plot(x, y, z, 'b', linewidth=2, label='Helix')

# Sample points to show tangent vectors
sample_indices = np.arange(0, len(t), 100)
ax1.quiver(x[sample_indices], y[sample_indices], z[sample_indices], 
          dx[sample_indices], dy[sample_indices], dz[sample_indices], 
          color='r', length=0.5, normalize=True, label='Tangent Vectors')

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
ax1.quiver(x[sample_indices], y[sample_indices], z[sample_indices], 
          nx[sample_indices], ny[sample_indices], nz[sample_indices], 
          color='g', length=0.5, normalize=True, label='Normal Vectors')

# Sample points to show binormal vectors
ax1.quiver(x[sample_indices], y[sample_indices], z[sample_indices], 
          bx[sample_indices], by[sample_indices], bz[sample_indices], 
          color='purple', length=0.5, normalize=True, label='Binormal Vectors')

# Set labels and title
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
ax1.set_title('Helix with Frenet Frame Vectors')
ax1.legend()

# Set equal aspect ratio
ax1.set_box_aspect([1,1,1])

# Save the figure
plt.savefig('/home/ubuntu/MIT_Differential_Geometry_18.950_Textbook/supplementary_materials/visualizations/chapter1/helix_with_frenet_frame.png', dpi=300, bbox_inches='tight')

# Create a figure for arc length visualization
fig2 = plt.figure(figsize=(10, 6))
ax2 = fig2.add_subplot(111)

# Calculate arc length
arc_length = np.sqrt(a**2 + b**2) * t
arc_length_normalized = arc_length / arc_length[-1]

# Plot parameter vs arc length
ax2.plot(t, arc_length, 'b-', linewidth=2)
ax2.set_xlabel('Parameter t')
ax2.set_ylabel('Arc Length s(t)')
ax2.set_title('Arc Length as a Function of Parameter')
ax2.grid(True)

# Save the figure
plt.savefig('/home/ubuntu/MIT_Differential_Geometry_18.950_Textbook/supplementary_materials/visualizations/chapter1/arc_length_parameter.png', dpi=300, bbox_inches='tight')

# Create a figure for curvature visualization
fig3 = plt.figure(figsize=(12, 10))

# Create a 3D axis for the circle
ax3 = fig3.add_subplot(221, projection='3d')

# Circle parameters
radius = 1
theta = np.linspace(0, 2*np.pi, 100)
x_circle = radius * np.cos(theta)
y_circle = radius * np.sin(theta)
z_circle = np.zeros_like(theta)

# Plot the circle
ax3.plot(x_circle, y_circle, z_circle, 'b-', linewidth=2)
ax3.set_title(f'Circle (Constant Curvature = {1/radius})')
ax3.set_xlabel('X')
ax3.set_ylabel('Y')
ax3.set_zlabel('Z')
ax3.set_box_aspect([1,1,0.1])

# Create a 3D axis for the straight line
ax4 = fig3.add_subplot(222, projection='3d')

# Line parameters
t_line = np.linspace(0, 2, 100)
x_line = t_line
y_line = np.zeros_like(t_line)
z_line = np.zeros_like(t_line)

# Plot the line
ax4.plot(x_line, y_line, z_line, 'r-', linewidth=2)
ax4.set_title('Straight Line (Curvature = 0)')
ax4.set_xlabel('X')
ax4.set_ylabel('Y')
ax4.set_zlabel('Z')
ax4.set_box_aspect([1,1,1])

# Create a 3D axis for the ellipse
ax5 = fig3.add_subplot(223, projection='3d')

# Ellipse parameters
a_ellipse = 2
b_ellipse = 1
theta = np.linspace(0, 2*np.pi, 100)
x_ellipse = a_ellipse * np.cos(theta)
y_ellipse = b_ellipse * np.sin(theta)
z_ellipse = np.zeros_like(theta)

# Calculate curvature of ellipse
curvature_ellipse = (a_ellipse * b_ellipse) / ((a_ellipse**2 * np.sin(theta)**2 + b_ellipse**2 * np.cos(theta)**2)**(3/2))

# Plot the ellipse
ax5.plot(x_ellipse, y_ellipse, z_ellipse, 'g-', linewidth=2)
ax5.set_title('Ellipse (Variable Curvature)')
ax5.set_xlabel('X')
ax5.set_ylabel('Y')
ax5.set_zlabel('Z')
ax5.set_box_aspect([1,0.5,0.1])

# Create a 2D axis for the curvature plot
ax6 = fig3.add_subplot(224)

# Plot curvature of ellipse
ax6.plot(theta, curvature_ellipse, 'g-', linewidth=2)
ax6.set_title('Curvature of Ellipse vs Parameter')
ax6.set_xlabel('Parameter θ')
ax6.set_ylabel('Curvature κ(θ)')
ax6.grid(True)
ax6.set_xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
ax6.set_xticklabels(['0', 'π/2', 'π', '3π/2', '2π'])

plt.tight_layout()
plt.savefig('/home/ubuntu/MIT_Differential_Geometry_18.950_Textbook/supplementary_materials/visualizations/chapter1/curvature_examples.png', dpi=300, bbox_inches='tight')

# Create a figure for reparametrization visualization
fig4 = plt.figure(figsize=(12, 6))

# Create a 2D axis for the original parametrization
ax7 = fig4.add_subplot(121)

# Non-uniform parametrization (faster at the beginning, slower at the end)
t_nonuniform = np.linspace(0, 1, 100)**2 * 2*np.pi
x_nonuniform = np.cos(t_nonuniform)
y_nonuniform = np.sin(t_nonuniform)

# Plot points at equal parameter intervals
interval = 10
ax7.plot(x_nonuniform, y_nonuniform, 'b-', linewidth=2)
ax7.plot(x_nonuniform[::interval], y_nonuniform[::interval], 'ro', markersize=8)
ax7.set_title('Non-Uniform Parametrization\n(Points at Equal Parameter Intervals)')
ax7.set_xlabel('X')
ax7.set_ylabel('Y')
ax7.set_aspect('equal')
ax7.grid(True)

# Create a 2D axis for the arc length parametrization
ax8 = fig4.add_subplot(122)

# Uniform (arc length) parametrization
t_uniform = np.linspace(0, 2*np.pi, 100)
x_uniform = np.cos(t_uniform)
y_uniform = np.sin(t_uniform)

# Plot points at equal parameter intervals
ax8.plot(x_uniform, y_uniform, 'b-', linewidth=2)
ax8.plot(x_uniform[::interval], y_uniform[::interval], 'ro', markersize=8)
ax8.set_title('Arc Length Parametrization\n(Points at Equal Parameter Intervals)')
ax8.set_xlabel('X')
ax8.set_ylabel('Y')
ax8.set_aspect('equal')
ax8.grid(True)

plt.tight_layout()
plt.savefig('/home/ubuntu/MIT_Differential_Geometry_18.950_Textbook/supplementary_materials/visualizations/chapter1/reparametrization.png', dpi=300, bbox_inches='tight')

print("Visualizations created successfully!")
