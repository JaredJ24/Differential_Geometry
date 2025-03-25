import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create figure for osculating circles visualization
fig1 = plt.figure(figsize=(12, 10))
ax1 = fig1.add_subplot(111)

# Generate an ellipse
a, b = 3.0, 1.5  # semi-major and semi-minor axes
t = np.linspace(0, 2*np.pi, 1000)
x = a * np.cos(t)
y = b * np.sin(t)

# Calculate curvature at each point
dx_dt = -a * np.sin(t)
dy_dt = b * np.cos(t)
d2x_dt2 = -a * np.cos(t)
d2y_dt2 = -b * np.sin(t)
curvature = np.abs(dx_dt * d2y_dt2 - dy_dt * d2x_dt2) / (dx_dt**2 + dy_dt**2)**(3/2)

# Plot the ellipse
ax1.plot(x, y, 'b-', linewidth=2, label='Ellipse')

# Sample points for osculating circles
sample_indices = [0, 250, 500, 750]  # at t = 0, π/2, π, 3π/2
colors = ['r', 'g', 'm', 'c']  # red, green, magenta, cyan

# Plot osculating circles at sample points
for i, idx in enumerate(sample_indices):
    # Get point on curve
    point_x, point_y = x[idx], y[idx]
    
    # Calculate radius of curvature (reciprocal of curvature)
    radius = 1 / curvature[idx]
    
    # Calculate normal vector (perpendicular to tangent)
    tangent_x, tangent_y = dx_dt[idx], dy_dt[idx]
    tangent_mag = np.sqrt(tangent_x**2 + tangent_y**2)
    tangent_x, tangent_y = tangent_x / tangent_mag, tangent_y / tangent_mag
    normal_x, normal_y = -tangent_y, tangent_x  # rotate 90 degrees
    
    # Calculate center of osculating circle
    center_x = point_x + radius * normal_x
    center_y = point_y + radius * normal_y
    
    # Plot the osculating circle
    circle = plt.Circle((center_x, center_y), radius, fill=False, color=colors[i], linestyle='--', linewidth=1.5)
    ax1.add_patch(circle)
    
    # Plot the center of the osculating circle
    ax1.plot(center_x, center_y, color=colors[i], marker='o', markersize=6)
    
    # Plot the radius line
    ax1.plot([point_x, center_x], [point_y, center_y], color=colors[i], linestyle='-', linewidth=1)
    
    # Annotate the point
    ax1.annotate(f't = {t[idx]:.2f}', (point_x, point_y), xytext=(point_x + 0.3, point_y + 0.3))

# Plot the evolute (locus of centers of osculating circles)
# Calculate centers of all osculating circles
normal_x = -dy_dt / np.sqrt(dx_dt**2 + dy_dt**2)
normal_y = dx_dt / np.sqrt(dx_dt**2 + dy_dt**2)
centers_x = x + normal_x / curvature
centers_y = y + normal_y / curvature

# Plot the evolute
ax1.plot(centers_x, centers_y, 'm-', linewidth=1.5, label='Evolute')

# Set labels and title
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_title('Ellipse with Osculating Circles and Evolute')
ax1.legend()
ax1.grid(True)
ax1.set_aspect('equal')

# Set axis limits with some padding
ax1.set_xlim(min(centers_x) - 1, max(centers_x) + 1)
ax1.set_ylim(min(centers_y) - 1, max(centers_y) + 1)

# Save the figure
plt.savefig('/home/ubuntu/MIT_Differential_Geometry_18.950_Textbook/supplementary_materials/visualizations/chapter2/osculating_circles_evolute.png', dpi=300, bbox_inches='tight')

# Create figure for curvature visualization
fig2 = plt.figure(figsize=(12, 6))
ax2 = fig2.add_subplot(111)

# Plot curvature as a function of parameter
ax2.plot(t, curvature, 'b-', linewidth=2)

# Mark the sample points
for i, idx in enumerate(sample_indices):
    ax2.plot(t[idx], curvature[idx], color=colors[i], marker='o', markersize=8)
    ax2.annotate(f't = {t[idx]:.2f}', (t[idx], curvature[idx]), 
                 xytext=(t[idx] + 0.1, curvature[idx] + 0.05))

# Set labels and title
ax2.set_xlabel('Parameter t')
ax2.set_ylabel('Curvature κ(t)')
ax2.set_title('Curvature of Ellipse as a Function of Parameter')
ax2.grid(True)

# Set x-axis ticks to show multiples of π/2
ax2.set_xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
ax2.set_xticklabels(['0', 'π/2', 'π', '3π/2', '2π'])

# Save the figure
plt.savefig('/home/ubuntu/MIT_Differential_Geometry_18.950_Textbook/supplementary_materials/visualizations/chapter2/ellipse_curvature.png', dpi=300, bbox_inches='tight')

# Create figure for comparing curves with different curvatures
fig3 = plt.figure(figsize=(15, 5))

# Create three subplots
ax3 = fig3.add_subplot(131)
ax4 = fig3.add_subplot(132)
ax5 = fig3.add_subplot(133)

# 1. Circle (constant curvature)
radius = 1.0
t_circle = np.linspace(0, 2*np.pi, 1000)
x_circle = radius * np.cos(t_circle)
y_circle = radius * np.sin(t_circle)
curvature_circle = np.ones_like(t_circle) / radius

ax3.plot(x_circle, y_circle, 'b-', linewidth=2)
ax3.set_title(f'Circle\nConstant Curvature κ = {1/radius:.2f}')
ax3.set_xlabel('X')
ax3.set_ylabel('Y')
ax3.grid(True)
ax3.set_aspect('equal')

# 2. Parabola (variable curvature)
t_parabola = np.linspace(-2, 2, 1000)
x_parabola = t_parabola
y_parabola = t_parabola**2
dx_dt = np.ones_like(t_parabola)
dy_dt = 2 * t_parabola
d2x_dt2 = np.zeros_like(t_parabola)
d2y_dt2 = 2 * np.ones_like(t_parabola)
curvature_parabola = np.abs(dx_dt * d2y_dt2 - dy_dt * d2x_dt2) / (dx_dt**2 + dy_dt**2)**(3/2)

ax4.plot(x_parabola, y_parabola, 'g-', linewidth=2)
ax4.set_title('Parabola\nVariable Curvature')
ax4.set_xlabel('X')
ax4.set_ylabel('Y')
ax4.grid(True)
ax4.set_aspect('equal')

# 3. Sine curve (oscillating curvature)
t_sine = np.linspace(-2*np.pi, 2*np.pi, 1000)
x_sine = t_sine
y_sine = np.sin(t_sine)
dx_dt = np.ones_like(t_sine)
dy_dt = np.cos(t_sine)
d2x_dt2 = np.zeros_like(t_sine)
d2y_dt2 = -np.sin(t_sine)
curvature_sine = np.abs(dx_dt * d2y_dt2 - dy_dt * d2x_dt2) / (dx_dt**2 + dy_dt**2)**(3/2)

ax5.plot(x_sine, y_sine, 'r-', linewidth=2)
ax5.set_title('Sine Curve\nOscillating Curvature')
ax5.set_xlabel('X')
ax5.set_ylabel('Y')
ax5.grid(True)
ax5.set_aspect('equal')

plt.tight_layout()
plt.savefig('/home/ubuntu/MIT_Differential_Geometry_18.950_Textbook/supplementary_materials/visualizations/chapter2/curve_comparison.png', dpi=300, bbox_inches='tight')

# Create figure for curvature comparison
fig4 = plt.figure(figsize=(15, 5))

# Create three subplots
ax6 = fig4.add_subplot(131)
ax7 = fig4.add_subplot(132)
ax8 = fig4.add_subplot(133)

# Plot curvature functions
ax6.plot(t_circle, curvature_circle, 'b-', linewidth=2)
ax6.set_title('Circle Curvature')
ax6.set_xlabel('Parameter t')
ax6.set_ylabel('Curvature κ(t)')
ax6.grid(True)
ax6.set_ylim(0, 2)

ax7.plot(t_parabola, curvature_parabola, 'g-', linewidth=2)
ax7.set_title('Parabola Curvature')
ax7.set_xlabel('Parameter t')
ax7.set_ylabel('Curvature κ(t)')
ax7.grid(True)
ax7.set_ylim(0, 2)

ax8.plot(t_sine, curvature_sine, 'r-', linewidth=2)
ax8.set_title('Sine Curve Curvature')
ax8.set_xlabel('Parameter t')
ax8.set_ylabel('Curvature κ(t)')
ax8.grid(True)
ax8.set_ylim(0, 2)

plt.tight_layout()
plt.savefig('/home/ubuntu/MIT_Differential_Geometry_18.950_Textbook/supplementary_materials/visualizations/chapter2/curvature_comparison.png', dpi=300, bbox_inches='tight')

# Create figure for the Four Vertex Theorem
fig5 = plt.figure(figsize=(10, 10))
ax9 = fig5.add_subplot(111)

# Create a non-circular closed curve (perturbed ellipse)
t_perturbed = np.linspace(0, 2*np.pi, 1000)
r = 2 + 0.5 * np.cos(3*t_perturbed)  # radius varies with angle
x_perturbed = r * np.cos(t_perturbed)
y_perturbed = r * np.sin(t_perturbed)

# Calculate curvature (this is more complex for polar form)
# First convert to parametric form and calculate derivatives
dx_dt = -r * np.sin(t_perturbed) + np.cos(t_perturbed) * (-1.5 * np.sin(3*t_perturbed))
dy_dt = r * np.cos(t_perturbed) + np.sin(t_perturbed) * (-1.5 * np.sin(3*t_perturbed))
d2x_dt2 = -r * np.cos(t_perturbed) - np.sin(t_perturbed) * (-1.5 * np.sin(3*t_perturbed)) + np.cos(t_perturbed) * (-4.5 * np.cos(3*t_perturbed))
d2y_dt2 = -r * np.sin(t_perturbed) + np.cos(t_perturbed) * (-1.5 * np.sin(3*t_perturbed)) + np.sin(t_perturbed) * (-4.5 * np.cos(3*t_perturbed))

curvature_perturbed = np.abs(dx_dt * d2y_dt2 - dy_dt * d2x_dt2) / (dx_dt**2 + dy_dt**2)**(3/2)

# Find local extrema of curvature (vertices)
vertices = []
for i in range(1, len(curvature_perturbed)-1):
    if (curvature_perturbed[i] > curvature_perturbed[i-1] and 
        curvature_perturbed[i] > curvature_perturbed[i+1]) or \
       (curvature_perturbed[i] < curvature_perturbed[i-1] and 
        curvature_perturbed[i] < curvature_perturbed[i+1]):
        vertices.append(i)

# Plot the curve
ax9.plot(x_perturbed, y_perturbed, 'b-', linewidth=2, label='Closed Curve')

# Mark the vertices
for idx in vertices:
    ax9.plot(x_perturbed[idx], y_perturbed[idx], 'ro', markersize=8)
    
    # Calculate osculating circle at vertex
    radius = 1 / curvature_perturbed[idx]
    
    # Calculate normal vector
    tangent_x, tangent_y = dx_dt[idx], dy_dt[idx]
    tangent_mag = np.sqrt(tangent_x**2 + tangent_y**2)
    tangent_x, tangent_y = tangent_x / tangent_mag, tangent_y / tangent_mag
    normal_x, normal_y = -tangent_y, tangent_x
    
    # Calculate center of osculating circle
    center_x = x_perturbed[idx] + radius * normal_x
    center_y = y_perturbed[idx] + radius * normal_y
    
    # Plot the osculating circle
    circle = plt.Circle((center_x, center_y), radius, fill=False, color='r', linestyle='--', linewidth=1)
    ax9.add_patch(circle)
    
    # Annotate the vertex
    if len(vertices) >= 4:  # Only label if we have at least 4 vertices
        ax9.annotate(f'Vertex {vertices.index(idx)+1}', 
                     (x_perturbed[idx], y_perturbed[idx]), 
                     xytext=(x_perturbed[idx] + 0.5, y_perturbed[idx] + 0.5))

# Set labels and title
ax9.set_xlabel('X')
ax9.set_ylabel('Y')
ax9.set_title('Four Vertex Theorem Illustration')
ax9.grid(True)
ax9.set_aspect('equal')

# Add explanation text
if len(vertices) >= 4:
    ax9.text(0.05, 0.05, f'This closed curve has {len(vertices)} vertices\n(points where curvature reaches a local extremum).\nThe Four Vertex Theorem guarantees at least 4 vertices\nfor any simple closed curve in the plane.',
             transform=ax9.transAxes, bbox=dict(facecolor='white', alpha=0.8))

plt.savefig('/home/ubuntu/MIT_Differential_Geometry_18.950_Textbook/supplementary_materials/visualizations/chapter2/four_vertex_theorem.png', dpi=300, bbox_inches='tight')

print("Visualizations for Chapter 2 created successfully!")
