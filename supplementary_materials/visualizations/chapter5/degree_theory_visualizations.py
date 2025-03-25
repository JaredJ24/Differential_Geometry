import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d
import matplotlib.animation as animation
from matplotlib.colors import LinearSegmentedColormap

# Set up the figure with multiple subplots
fig = plt.figure(figsize=(20, 15))
fig.suptitle('Degree Theory and Circle Maps Visualizations', fontsize=20)

# 1. Periodic Function and Circle Map
ax1 = fig.add_subplot(231)
ax1.set_title('Periodic Function f(t) = sin(2t)')

# Plot the periodic function
t = np.linspace(0, 2*np.pi, 1000)
f = np.sin(2*t)
ax1.plot(t, f, 'b-')
ax1.set_xlabel('t')
ax1.set_ylabel('f(t)')
ax1.grid(True)
ax1.set_xlim(0, 2*np.pi)
ax1.set_xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
ax1.set_xticklabels(['0', 'π/2', 'π', '3π/2', '2π'])

# 2. Circle Map Visualization
ax2 = fig.add_subplot(232)
ax2.set_title('Circle Map F(e^(it)) = e^(i3t)')

# Draw the input and output circles
theta = np.linspace(0, 2*np.pi, 100)
input_circle_x = np.cos(theta)
input_circle_y = np.sin(theta)
output_circle_x = np.cos(theta)
output_circle_y = np.sin(theta)

ax2.plot(input_circle_x, input_circle_y, 'b-', label='Input Circle')
ax2.plot(output_circle_x + 3, output_circle_y, 'r-', label='Output Circle')

# Mark points on the input circle and their images on the output circle
num_points = 8
t_points = np.linspace(0, 2*np.pi, num_points, endpoint=False)
input_points_x = np.cos(t_points)
input_points_y = np.sin(t_points)
output_points_x = np.cos(3*t_points) + 3
output_points_y = np.sin(3*t_points)

ax2.scatter(input_points_x, input_points_y, c='blue', s=50)
ax2.scatter(output_points_x, output_points_y, c='red', s=50)

# Connect input points to their images with arrows
for i in range(num_points):
    ax2.arrow(input_points_x[i], input_points_y[i], 
              output_points_x[i] - input_points_x[i], output_points_y[i] - input_points_y[i],
              head_width=0.1, head_length=0.1, fc='green', ec='green', alpha=0.5)

ax2.set_xlim(-1.5, 4.5)
ax2.set_ylim(-1.5, 1.5)
ax2.set_aspect('equal')
ax2.legend()
ax2.grid(True)

# 3. Winding Number Visualization
ax3 = fig.add_subplot(233)
ax3.set_title('Winding Number of a Curve')

# Draw a curve that winds around the origin
t = np.linspace(0, 2*np.pi, 1000)
r = 1 + 0.3 * np.sin(3*t)
x = r * np.cos(t)
y = r * np.sin(t)

ax3.plot(x, y, 'g-')
ax3.plot(0, 0, 'ro', markersize=5)  # Mark the origin

# Add arrows to show direction
for i in range(0, 1000, 100):
    ax3.arrow(x[i], y[i], (x[i+1]-x[i])*20, (y[i+1]-y[i])*20, 
              head_width=0.05, head_length=0.05, fc='blue', ec='blue')

ax3.set_xlim(-1.5, 1.5)
ax3.set_ylim(-1.5, 1.5)
ax3.set_aspect('equal')
ax3.grid(True)
ax3.text(0, 0, 'O', fontsize=12, ha='right', va='bottom')
ax3.text(0.5, 1.2, 'Winding Number = 1', fontsize=12, ha='center')

# 4. Brouwer Fixed Point Theorem Visualization
ax4 = fig.add_subplot(234)
ax4.set_title('Brouwer Fixed Point Theorem')

# Draw a disk
theta = np.linspace(0, 2*np.pi, 100)
r = np.linspace(0, 1, 20)
theta_grid, r_grid = np.meshgrid(theta, r)
x = r_grid * np.cos(theta_grid)
y = r_grid * np.sin(theta_grid)

# Create a continuous deformation of the disk
def deform(x, y):
    # A simple deformation that keeps points inside the disk
    dx = 0.3 * np.sin(2*np.pi*y)
    dy = 0.3 * np.sin(2*np.pi*x)
    # Ensure the deformation stays within the disk
    norm = np.sqrt((x+dx)**2 + (y+dy)**2)
    mask = norm > 1
    dx[mask] = dx[mask] * (1/norm[mask] - 0.01)
    dy[mask] = dy[mask] * (1/norm[mask] - 0.01)
    return x + dx, y + dy

x_deformed, y_deformed = deform(x, y)

# Plot the original and deformed disk
ax4.scatter(x.flatten(), y.flatten(), c='blue', s=1, alpha=0.3, label='Original Disk')
ax4.scatter(x_deformed.flatten(), y_deformed.flatten(), c='red', s=1, alpha=0.3, label='Deformed Disk')

# Find a fixed point (for visualization purposes)
distances = np.sqrt((x.flatten() - x_deformed.flatten())**2 + (y.flatten() - y_deformed.flatten())**2)
fixed_point_idx = np.argmin(distances)
fixed_point_x = x.flatten()[fixed_point_idx]
fixed_point_y = y.flatten()[fixed_point_idx]

ax4.scatter(fixed_point_x, fixed_point_y, c='green', s=100, label='Fixed Point')

ax4.set_xlim(-1.2, 1.2)
ax4.set_ylim(-1.2, 1.2)
ax4.set_aspect('equal')
ax4.legend()
ax4.grid(True)

# 5. Gauss-Bonnet Theorem Visualization
ax5 = fig.add_subplot(235, projection='3d')
ax5.set_title('Gauss-Bonnet Theorem: Surfaces with Different Euler Characteristics')

# Create a sphere (Euler characteristic 2)
u = np.linspace(0, 2*np.pi, 30)
v = np.linspace(0, np.pi, 30)
x = 0.7 * np.outer(np.cos(u), np.sin(v))
y = 0.7 * np.outer(np.sin(u), np.sin(v))
z = 0.7 * np.outer(np.ones(np.size(u)), np.cos(v))

# Calculate Gaussian curvature (constant for a sphere)
K = np.ones_like(x) * (1/0.7**2)  # K = 1/r^2 for a sphere of radius r

# Create a custom colormap for curvature
colors = plt.cm.viridis(K/np.max(K))
ax5.plot_surface(x, y, z, facecolors=colors, alpha=0.7)

# Add a text label for the sphere
ax5.text(0, 0, 1, "Sphere (χ = 2)\nTotal Curvature = 4π", fontsize=8)

# Create a torus (Euler characteristic 0)
R, r = 1.2, 0.3  # Major and minor radii
u = np.linspace(0, 2*np.pi, 30)
v = np.linspace(0, 2*np.pi, 30)
u_grid, v_grid = np.meshgrid(u, v)
x_torus = (R + r*np.cos(v_grid)) * np.cos(u_grid) + 3
y_torus = (R + r*np.cos(v_grid)) * np.sin(u_grid)
z_torus = r * np.sin(v_grid)

# Calculate Gaussian curvature for the torus
K_torus = np.cos(v_grid) / (r * (R + r*np.cos(v_grid)))

# Normalize for coloring
K_torus_norm = (K_torus - np.min(K_torus)) / (np.max(K_torus) - np.min(K_torus))
colors_torus = plt.cm.viridis(K_torus_norm)
ax5.plot_surface(x_torus, y_torus, z_torus, facecolors=colors_torus, alpha=0.7)

# Add a text label for the torus
ax5.text(3, 0, 0.5, "Torus (χ = 0)\nTotal Curvature = 0", fontsize=8)

ax5.set_xlim(-1, 4)
ax5.set_ylim(-1.5, 1.5)
ax5.set_zlim(-1, 1)
ax5.set_box_aspect([5, 3, 2])
ax5.set_axis_off()

# 6. Fourier Series Visualization
ax6 = fig.add_subplot(236)
ax6.set_title('Fourier Series Approximation of a Square Wave')

# Define the square wave function
def square_wave(t):
    return np.sign(np.sin(t))

# Define the Fourier series approximation
def fourier_approx(t, n_terms):
    result = np.zeros_like(t)
    for n in range(1, n_terms+1, 2):  # Only odd terms for square wave
        result += (4/(n*np.pi)) * np.sin(n*t)
    return result

t = np.linspace(0, 4*np.pi, 1000)
square = square_wave(t)

# Plot the square wave
ax6.plot(t, square, 'k-', label='Square Wave')

# Plot Fourier approximations with different numbers of terms
colors = ['b', 'g', 'r', 'c']
terms = [1, 3, 5, 10]
for i, n in enumerate(terms):
    approx = fourier_approx(t, n)
    ax6.plot(t, approx, colors[i], label=f'{n} term{"s" if n > 1 else ""}')

ax6.set_xlim(0, 4*np.pi)
ax6.set_ylim(-1.5, 1.5)
ax6.set_xlabel('t')
ax6.set_ylabel('f(t)')
ax6.grid(True)
ax6.legend()
ax6.set_xticks([0, np.pi, 2*np.pi, 3*np.pi, 4*np.pi])
ax6.set_xticklabels(['0', 'π', '2π', '3π', '4π'])

plt.tight_layout()
plt.savefig('/home/ubuntu/MIT_Differential_Geometry_18.950_Textbook/supplementary_materials/visualizations/chapter5/degree_theory_visualizations.png', dpi=300)

# Create additional visualizations

# 1. Winding Number Animation
fig_winding = plt.figure(figsize=(10, 10))
ax_winding = fig_winding.add_subplot(111)
ax_winding.set_title('Winding Number Animation')

# Create curves with different winding numbers
def create_curve(winding_number, t):
    r = 1 + 0.3 * np.sin(3*t)
    x = r * np.cos(winding_number * t)
    y = r * np.sin(winding_number * t)
    return x, y

t = np.linspace(0, 2*np.pi, 1000)
winding_numbers = [1, 2, 3]
colors = ['b', 'g', 'r']

for i, wn in enumerate(winding_numbers):
    x, y = create_curve(wn, t)
    ax_winding.plot(x, y, colors[i], label=f'Winding Number = {wn}')
    
    # Add arrows to show direction
    for j in range(0, 1000, 200):
        ax_winding.arrow(x[j], y[j], (x[j+1]-x[j])*20, (y[j+1]-y[j])*20, 
                  head_width=0.05, head_length=0.05, fc=colors[i], ec=colors[i])

ax_winding.plot(0, 0, 'ko', markersize=5)  # Mark the origin
ax_winding.text(0, 0, 'O', fontsize=12, ha='right', va='bottom')
ax_winding.set_xlim(-1.5, 1.5)
ax_winding.set_ylim(-1.5, 1.5)
ax_winding.set_aspect('equal')
ax_winding.grid(True)
ax_winding.legend()

plt.tight_layout()
plt.savefig('/home/ubuntu/MIT_Differential_Geometry_18.950_Textbook/supplementary_materials/visualizations/chapter5/winding_number_comparison.png', dpi=300)

# 2. No Retraction Theorem Visualization
fig_retraction = plt.figure(figsize=(10, 10))
ax_retraction = fig_retraction.add_subplot(111)
ax_retraction.set_title('No Retraction Theorem')

# Draw the disk and its boundary
theta = np.linspace(0, 2*np.pi, 100)
boundary_x = np.cos(theta)
boundary_y = np.sin(theta)
ax_retraction.plot(boundary_x, boundary_y, 'r-', linewidth=2, label='Boundary (S¹)')

# Fill the disk
r = np.linspace(0, 1, 20)
theta_grid, r_grid = np.meshgrid(theta, r)
x = r_grid * np.cos(theta_grid)
y = r_grid * np.sin(theta_grid)
ax_retraction.scatter(x, y, c='blue', s=1, alpha=0.3, label='Interior (D²)')

# Illustrate the impossibility of retraction
# Draw some radial lines that would need to be mapped to boundary points
for angle in np.linspace(0, 2*np.pi, 12, endpoint=False):
    x_line = np.linspace(0, np.cos(angle), 100)
    y_line = np.linspace(0, np.sin(angle), 100)
    ax_retraction.plot(x_line, y_line, 'g--', alpha=0.5)
    
    # Add a text to explain the contradiction
    if angle == 0:
        ax_retraction.text(0.5, 0.1, "These points must\nmap to boundary", 
                 fontsize=10, ha='center', rotation=angle*180/np.pi)

# Add a note about the contradiction
ax_retraction.text(0, 0, "Contradiction:\nOrigin must map to\na boundary point", 
         fontsize=12, ha='center', va='center', bbox=dict(facecolor='white', alpha=0.7))

ax_retraction.set_xlim(-1.5, 1.5)
ax_retraction.set_ylim(-1.5, 1.5)
ax_retraction.set_aspect('equal')
ax_retraction.grid(True)
ax_retraction.legend()

plt.tight_layout()
plt.savefig('/home/ubuntu/MIT_Differential_Geometry_18.950_Textbook/supplementary_materials/visualizations/chapter5/no_retraction_theorem.png', dpi=300)

# 3. Degree of Maps Between Spheres
fig_spheres = plt.figure(figsize=(12, 8))
ax_spheres = fig_spheres.add_subplot(111, projection='3d')
ax_spheres.set_title('Degree of Maps Between Spheres')

# Create two spheres
u = np.linspace(0, 2*np.pi, 30)
v = np.linspace(0, np.pi, 30)
x1 = 1 * np.outer(np.cos(u), np.sin(v)) - 2
y1 = 1 * np.outer(np.sin(u), np.sin(v))
z1 = 1 * np.outer(np.ones(np.size(u)), np.cos(v))

x2 = 1 * np.outer(np.cos(u), np.sin(v)) + 2
y2 = 1 * np.outer(np.sin(u), np.sin(v))
z2 = 1 * np.outer(np.ones(np.size(u)), np.cos(v))

# Plot the spheres
ax_spheres.plot_surface(x1, y1, z1, color='b', alpha=0.3)
ax_spheres.plot_surface(x2, y2, z2, color='r', alpha=0.3)

# Add labels
ax_spheres.text(-2, 0, 1.5, "Input Sphere (S²)", color='blue', fontsize=12)
ax_spheres.text(2, 0, 1.5, "Output Sphere (S²)", color='red', fontsize=12)

# Illustrate a map of degree 2
# Select some points on the input sphere
theta_points = np.linspace(0, 2*np.pi, 8)
phi_points = np.linspace(0, np.pi, 4)[1:-1]  # Exclude poles for clarity
theta_grid, phi_grid = np.meshgrid(theta_points, phi_points)
theta_grid = theta_grid.flatten()
phi_grid = phi_grid.flatten()

# Calculate coordinates on input sphere
x_in = np.sin(phi_grid) * np.cos(theta_grid) - 2
y_in = np.sin(phi_grid) * np.sin(theta_grid)
z_in = np.cos(phi_grid)

# Map to output sphere with degree 2 (double the longitude)
x_out = np.sin(phi_grid) * np.cos(2*theta_grid) + 2
y_out = np.sin(phi_grid) * np.sin(2*theta_grid)
z_out = np.cos(phi_grid)

# Plot points and connections
ax_spheres.scatter(x_in, y_in, z_in, color='blue', s=50)
ax_spheres.scatter(x_out, y_out, z_out, color='red', s=50)

for i in range(len(x_in)):
    ax_spheres.plot([x_in[i], x_out[i]], [y_in[i], y_out[i]], [z_in[i], z_out[i]], 
                   'k-', alpha=0.3)

# Add a note about the degree
ax_spheres.text(0, 0, 2, "Degree 2 Map:\nEach point on output sphere\nhas two preimages", 
               fontsize=12, ha='center', bbox=dict(facecolor='white', alpha=0.7))

ax_spheres.set_xlim(-3, 3)
ax_spheres.set_ylim(-1.5, 1.5)
ax_spheres.set_zlim(-1.5, 1.5)
ax_spheres.set_box_aspect([6, 3, 3])
ax_spheres.set_axis_off()

plt.tight_layout()
plt.savefig('/home/ubuntu/MIT_Differential_Geometry_18.950_Textbook/supplementary_materials/visualizations/chapter5/degree_of_maps_between_spheres.png', dpi=300)

print("All visualizations created successfully!")
