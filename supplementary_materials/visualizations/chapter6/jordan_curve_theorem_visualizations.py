import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d
import matplotlib.animation as animation
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Polygon

# Set up the figure with multiple subplots
fig = plt.figure(figsize=(20, 15))
fig.suptitle('Jordan Curve Theorem and Closed Curves Visualizations', fontsize=20)

# 1. Simple Closed Curves vs. Non-Simple Closed Curves
ax1 = fig.add_subplot(231)
ax1.set_title('Simple vs. Non-Simple Closed Curves')

# Draw a circle (simple closed curve)
theta = np.linspace(0, 2*np.pi, 100)
circle_x = np.cos(theta)
circle_y = np.sin(theta)
ax1.plot(circle_x, circle_y, 'b-', label='Circle (Simple)')

# Draw an ellipse (simple closed curve)
ellipse_x = 2 * np.cos(theta)
ellipse_y = np.sin(theta)
ax1.plot(ellipse_x, ellipse_y, 'g-', label='Ellipse (Simple)')

# Draw a figure-eight (non-simple closed curve)
figure_eight_x = np.sin(2*theta)
figure_eight_y = np.sin(theta)
ax1.plot(figure_eight_x, figure_eight_y, 'r-', label='Figure-Eight (Non-Simple)')

ax1.set_xlim(-2.5, 2.5)
ax1.set_ylim(-1.5, 1.5)
ax1.set_aspect('equal')
ax1.grid(True)
ax1.legend()

# 2. Jordan Curve Theorem Visualization
ax2 = fig.add_subplot(232)
ax2.set_title('Jordan Curve Theorem')

# Draw a simple closed curve (a rounded rectangle)
def rounded_rect(center, width, height, radius, num_points=100):
    # Generate the four corners
    corners = [
        [center[0] - width/2 + radius, center[1] - height/2 + radius],  # bottom-left
        [center[0] + width/2 - radius, center[1] - height/2 + radius],  # bottom-right
        [center[0] + width/2 - radius, center[1] + height/2 - radius],  # top-right
        [center[0] - width/2 + radius, center[1] + height/2 - radius]   # top-left
    ]
    
    # Generate the four arcs
    arcs = []
    for i, corner in enumerate(corners):
        if i == 0:  # bottom-left
            start_angle = np.pi
            end_angle = 3*np.pi/2
        elif i == 1:  # bottom-right
            start_angle = 3*np.pi/2
            end_angle = 2*np.pi
        elif i == 2:  # top-right
            start_angle = 0
            end_angle = np.pi/2
        else:  # top-left
            start_angle = np.pi/2
            end_angle = np.pi
        
        angles = np.linspace(start_angle, end_angle, num_points//4)
        arc_x = corner[0] + radius * np.cos(angles)
        arc_y = corner[1] + radius * np.sin(angles)
        arcs.append((arc_x, arc_y))
    
    # Generate the four straight segments
    segments = []
    for i in range(4):
        next_i = (i + 1) % 4
        if i == 0:  # bottom
            x = np.linspace(corners[i][0], corners[next_i][0], num_points//4)
            y = np.full_like(x, center[1] - height/2)
        elif i == 1:  # right
            y = np.linspace(corners[i][1], corners[next_i][1], num_points//4)
            x = np.full_like(y, center[0] + width/2)
        elif i == 2:  # top
            x = np.linspace(corners[i][0], corners[next_i][0], num_points//4)
            y = np.full_like(x, center[1] + height/2)
        else:  # left
            y = np.linspace(corners[i][1], corners[next_i][1], num_points//4)
            x = np.full_like(y, center[0] - width/2)
        segments.append((x, y))
    
    # Combine all parts to form the rounded rectangle
    x = np.concatenate([arcs[0][0], segments[0][0], arcs[1][0], segments[1][0], 
                        arcs[2][0], segments[2][0], arcs[3][0], segments[3][0]])
    y = np.concatenate([arcs[0][1], segments[0][1], arcs[1][1], segments[1][1], 
                        arcs[2][1], segments[2][1], arcs[3][1], segments[3][1]])
    
    return x, y

# Create a rounded rectangle
rect_x, rect_y = rounded_rect([0, 0], 3, 2, 0.5)
ax2.plot(rect_x, rect_y, 'b-', linewidth=2)

# Shade the interior
ax2.fill(rect_x, rect_y, 'lightblue', alpha=0.5, label='Interior')

# Add points in the interior and exterior
interior_points = [(0, 0), (1, 0.5), (-0.5, -0.5)]
exterior_points = [(2, 2), (-2, -2), (0, 2)]

for point in interior_points:
    ax2.plot(point[0], point[1], 'go', markersize=8)
    ax2.text(point[0]+0.1, point[1]+0.1, 'Interior Point', fontsize=8)

for point in exterior_points:
    ax2.plot(point[0], point[1], 'ro', markersize=8)
    ax2.text(point[0]+0.1, point[1]+0.1, 'Exterior Point', fontsize=8)

# Draw a path that connects interior and exterior points, crossing the curve
ax2.plot([interior_points[0][0], exterior_points[0][0]], 
         [interior_points[0][1], exterior_points[0][1]], 
         'k--', label='Path crosses curve')

ax2.set_xlim(-3, 3)
ax2.set_ylim(-3, 3)
ax2.set_aspect('equal')
ax2.grid(True)
ax2.legend()

# 3. Winding Number Visualization
ax3 = fig.add_subplot(233)
ax3.set_title('Winding Numbers')

# Draw a simple closed curve (circle)
circle_x = np.cos(theta)
circle_y = np.sin(theta)
ax3.plot(circle_x, circle_y, 'b-', linewidth=2, label='Simple Closed Curve')

# Add arrows to show direction
for i in range(0, 100, 20):
    ax3.arrow(circle_x[i], circle_y[i], 
              (circle_x[i+1]-circle_x[i])*20, (circle_y[i+1]-circle_y[i])*20, 
              head_width=0.05, head_length=0.1, fc='blue', ec='blue')

# Add points with different winding numbers
interior_point = (0, 0)
exterior_point = (2, 0)

ax3.plot(interior_point[0], interior_point[1], 'go', markersize=8)
ax3.text(interior_point[0]+0.1, interior_point[1]+0.1, 'W(γ,p) = 1', fontsize=10)

ax3.plot(exterior_point[0], exterior_point[1], 'ro', markersize=8)
ax3.text(exterior_point[0]+0.1, exterior_point[1]+0.1, 'W(γ,p) = 0', fontsize=10)

# Draw rays from points to infinity to illustrate winding number calculation
ray_theta = np.linspace(0, np.pi, 100)
ray_r = np.linspace(0, 3, 100)
ray_x = interior_point[0] + ray_r * np.cos(ray_theta)
ray_y = interior_point[1] + ray_r * np.sin(ray_theta)
ax3.plot(ray_x, ray_y, 'g--', alpha=0.5)

ray_x = exterior_point[0] + ray_r * np.cos(ray_theta)
ray_y = exterior_point[1] + ray_r * np.sin(ray_theta)
ax3.plot(ray_x, ray_y, 'r--', alpha=0.5)

ax3.set_xlim(-3, 3)
ax3.set_ylim(-2, 2)
ax3.set_aspect('equal')
ax3.grid(True)
ax3.legend()

# 4. Brouwer Fixed Point Theorem Visualization
ax4 = fig.add_subplot(234)
ax4.set_title('Brouwer Fixed Point Theorem')

# Draw the unit disk
circle_x = np.cos(theta)
circle_y = np.sin(theta)
ax4.plot(circle_x, circle_y, 'b-', linewidth=2, label='Unit Disk Boundary')

# Fill the disk
r = np.linspace(0, 1, 20)
theta_grid, r_grid = np.meshgrid(theta, r)
x = r_grid * np.cos(theta_grid)
y = r_grid * np.sin(theta_grid)
ax4.scatter(x, y, c='lightblue', s=1, alpha=0.5)

# Define a continuous function from disk to disk (a rotation + contraction)
def disk_map(x, y, angle=np.pi/4, contraction=0.7):
    # Rotate by angle and contract by factor
    x_new = contraction * (x * np.cos(angle) - y * np.sin(angle))
    y_new = contraction * (x * np.sin(angle) + y * np.cos(angle))
    return x_new, y_new

# Apply the function to points in the disk
x_mapped, y_mapped = disk_map(x, y)
ax4.scatter(x_mapped, y_mapped, c='lightgreen', s=1, alpha=0.5)

# Find a fixed point (where x_mapped ≈ x and y_mapped ≈ y)
distances = np.sqrt((x.flatten() - x_mapped.flatten())**2 + (y.flatten() - y_mapped.flatten())**2)
fixed_point_idx = np.argmin(distances)
fixed_point_x = x.flatten()[fixed_point_idx]
fixed_point_y = y.flatten()[fixed_point_idx]

ax4.plot(fixed_point_x, fixed_point_y, 'ro', markersize=8, label='Fixed Point')
ax4.text(fixed_point_x+0.1, fixed_point_y+0.1, 'f(x) = x', fontsize=10)

# Draw arrows from some points to their images
for i in range(0, 400, 80):
    ax4.arrow(x.flatten()[i], y.flatten()[i], 
              x_mapped.flatten()[i] - x.flatten()[i], 
              y_mapped.flatten()[i] - y.flatten()[i], 
              head_width=0.05, head_length=0.05, fc='green', ec='green', alpha=0.7)

ax4.set_xlim(-1.5, 1.5)
ax4.set_ylim(-1.5, 1.5)
ax4.set_aspect('equal')
ax4.grid(True)
ax4.legend()

# 5. Rotation Number Visualization
ax5 = fig.add_subplot(235)
ax5.set_title('Rotation Numbers')

# Draw curves with different rotation numbers
# Circle (rotation number 1)
circle_x = np.cos(theta)
circle_y = np.sin(theta)
ax5.plot(circle_x, circle_y, 'b-', linewidth=2, label='Circle (rot = 1)')

# Figure-eight (rotation number 0)
figure_eight_x = np.sin(2*theta)
figure_eight_y = np.sin(theta)
ax5.plot(figure_eight_x, figure_eight_y, 'r-', linewidth=2, label='Figure-Eight (rot = 0)')

# Trefoil projection (rotation number 3)
trefoil_x = np.sin(theta) + 2 * np.sin(2*theta)
trefoil_y = np.cos(theta) - 2 * np.cos(2*theta)
# Normalize to fit in the plot
max_val = max(np.max(np.abs(trefoil_x)), np.max(np.abs(trefoil_y)))
trefoil_x = trefoil_x / max_val * 1.5
trefoil_y = trefoil_y / max_val * 1.5
ax5.plot(trefoil_x, trefoil_y, 'g-', linewidth=2, label='Trefoil Proj. (rot = 3)')

# Add tangent vectors at selected points to illustrate rotation
for curve, color, points in [
    ((circle_x, circle_y), 'blue', [0, 25, 50, 75]),
    ((figure_eight_x, figure_eight_y), 'red', [0, 25, 50, 75]),
    ((trefoil_x, trefoil_y), 'green', [0, 25, 50, 75])
]:
    for i in points:
        # Calculate tangent vector
        if i < len(curve[0]) - 1:
            dx = curve[0][i+1] - curve[0][i]
            dy = curve[1][i+1] - curve[1][i]
        else:
            dx = curve[0][0] - curve[0][i]
            dy = curve[1][0] - curve[1][i]
        
        # Normalize
        length = np.sqrt(dx**2 + dy**2)
        if length > 0:
            dx = dx / length * 0.2
            dy = dy / length * 0.2
        
        ax5.arrow(curve[0][i], curve[1][i], dx, dy, 
                  head_width=0.05, head_length=0.05, fc=color, ec=color)

ax5.set_xlim(-2, 2)
ax5.set_ylim(-2, 2)
ax5.set_aspect('equal')
ax5.grid(True)
ax5.legend()

# 6. Isoperimetric Inequality Visualization
ax6 = fig.add_subplot(236)
ax6.set_title('Isoperimetric Inequality')

# Draw shapes with different isoperimetric ratios
# Circle (optimal ratio = 1)
circle_x = np.cos(theta)
circle_y = np.sin(theta)
ax6.plot(circle_x, circle_y, 'b-', linewidth=2, label='Circle (ratio = 1)')
ax6.fill(circle_x, circle_y, 'lightblue', alpha=0.3)

# Ellipse (suboptimal ratio)
a, b = 2, 0.5  # semi-major and semi-minor axes
ellipse_x = a * np.cos(theta)
ellipse_y = b * np.sin(theta)
ax6.plot(ellipse_x, ellipse_y, 'g-', linewidth=2, label=f'Ellipse (ratio ≈ {np.pi*a*b/(2*np.pi*np.sqrt((a**2+b**2)/2)):.3f})')
ax6.fill(ellipse_x, ellipse_y, 'lightgreen', alpha=0.3)

# Square (suboptimal ratio)
square_x = np.array([-1, 1, 1, -1, -1]) * np.sqrt(np.pi/4)  # Area = pi
square_y = np.array([-1, -1, 1, 1, -1]) * np.sqrt(np.pi/4)
ax6.plot(square_x, square_y, 'r-', linewidth=2, label=f'Square (ratio ≈ {np.pi/(4*np.sqrt(np.pi/4)):.3f})')
ax6.fill(square_x, square_y, 'lightcoral', alpha=0.3)

# Add text explaining the inequality
ax6.text(0, -2, "4πA ≤ L²", fontsize=12, ha='center')
ax6.text(0, -2.3, "Equality holds only for circles", fontsize=10, ha='center')

ax6.set_xlim(-2.5, 2.5)
ax6.set_ylim(-2.5, 2.5)
ax6.set_aspect('equal')
ax6.grid(True)
ax6.legend()

plt.tight_layout()
plt.savefig('/home/ubuntu/MIT_Differential_Geometry_18.950_Textbook/supplementary_materials/visualizations/chapter6/jordan_curve_theorem_visualizations.png', dpi=300)

# Create additional visualizations

# 1. Four Vertex Theorem Visualization
fig_vertex = plt.figure(figsize=(10, 10))
ax_vertex = fig_vertex.add_subplot(111)
ax_vertex.set_title('Four Vertex Theorem')

# Draw an ellipse
a, b = 2, 1  # semi-major and semi-minor axes
ellipse_x = a * np.cos(theta)
ellipse_y = b * np.sin(theta)
ax_vertex.plot(ellipse_x, ellipse_y, 'b-', linewidth=2, label='Ellipse')

# Calculate curvature of the ellipse
# κ(t) = ab / (a² sin²(t) + b² cos²(t))^(3/2)
curvature = a * b / ((a**2 * np.sin(theta)**2 + b**2 * np.cos(theta)**2)**(3/2))

# Find vertices (local extrema of curvature)
# For an ellipse, vertices are at t = 0, π/2, π, 3π/2
vertices_t = [0, np.pi/2, np.pi, 3*np.pi/2]
vertices_x = [a * np.cos(t) for t in vertices_t]
vertices_y = [b * np.sin(t) for t in vertices_t]
vertices_k = [a * b / ((a**2 * np.sin(t)**2 + b**2 * np.cos(t)**2)**(3/2)) for t in vertices_t]

# Mark vertices on the ellipse
ax_vertex.plot(vertices_x, vertices_y, 'ro', markersize=8, label='Vertices (Extrema of Curvature)')

# Add osculating circles at vertices
for i, t in enumerate(vertices_t):
    # Radius of osculating circle is 1/κ
    r = 1 / vertices_k[i]
    
    # Center of osculating circle is r units along the normal vector
    normal_x = -np.sin(t)
    normal_y = np.cos(t)
    if i == 0 or i == 2:  # At t = 0 or t = π
        center_x = vertices_x[i] - r * normal_x
        center_y = vertices_y[i] - r * normal_y
    else:  # At t = π/2 or t = 3π/2
        center_x = vertices_x[i] - r * normal_x
        center_y = vertices_y[i] - r * normal_y
    
    # Draw osculating circle
    osc_circle_x = center_x + r * np.cos(theta)
    osc_circle_y = center_y + r * np.sin(theta)
    ax_vertex.plot(osc_circle_x, osc_circle_y, '--', color='gray', alpha=0.5)

# Add a subplot showing curvature as a function of parameter
ax_curvature = fig_vertex.add_axes([0.2, 0.2, 0.3, 0.2])
ax_curvature.plot(theta, curvature, 'g-')
ax_curvature.set_title('Curvature vs. Parameter', fontsize=10)
ax_curvature.set_xlabel('t', fontsize=8)
ax_curvature.set_ylabel('κ(t)', fontsize=8)
ax_curvature.grid(True)

# Mark extrema on the curvature plot
for i, t in enumerate(vertices_t):
    ax_curvature.plot(t, vertices_k[i], 'ro', markersize=5)

ax_vertex.set_xlim(-3, 3)
ax_vertex.set_ylim(-2, 2)
ax_vertex.set_aspect('equal')
ax_vertex.grid(True)
ax_vertex.legend()

plt.savefig('/home/ubuntu/MIT_Differential_Geometry_18.950_Textbook/supplementary_materials/visualizations/chapter6/four_vertex_theorem.png', dpi=300)

# 2. Gauss-Bonnet Theorem Visualization
fig_gauss_bonnet = plt.figure(figsize=(10, 10))
ax_gauss_bonnet = fig_gauss_bonnet.add_subplot(111)
ax_gauss_bonnet.set_title('Gauss-Bonnet Theorem for Plane Curves')

# Draw different curves with the same total curvature
# Circle
circle_x = np.cos(theta)
circle_y = np.sin(theta)
ax_gauss_bonnet.plot(circle_x, circle_y, 'b-', linewidth=2, label='Circle')

# Ellipse
a, b = 2, 1
ellipse_x = a * np.cos(theta)
ellipse_y = b * np.sin(theta)
ax_gauss_bonnet.plot(ellipse_x, ellipse_y, 'g-', linewidth=2, label='Ellipse')

# Rounded square
square_x, square_y = rounded_rect([0, 0], 2, 2, 0.3)
ax_gauss_bonnet.plot(square_x, square_y, 'r-', linewidth=2, label='Rounded Square')

# Add tangent vectors to illustrate total rotation
for curve, color, points in [
    ((circle_x, circle_y), 'blue', [0, 25, 50, 75]),
    ((ellipse_x, ellipse_y), 'green', [0, 25, 50, 75]),
    ((square_x, square_y), 'red', [0, 25, 50, 75])
]:
    for i in points:
        # Calculate tangent vector
        if i < len(curve[0]) - 1:
            dx = curve[0][i+1] - curve[0][i]
            dy = curve[1][i+1] - curve[1][i]
        else:
            dx = curve[0][0] - curve[0][i]
            dy = curve[1][0] - curve[1][i]
        
        # Normalize
        length = np.sqrt(dx**2 + dy**2)
        if length > 0:
            dx = dx / length * 0.2
            dy = dy / length * 0.2
        
        ax_gauss_bonnet.arrow(curve[0][i], curve[1][i], dx, dy, 
                             head_width=0.05, head_length=0.05, fc=color, ec=color)

# Add text explaining the theorem
ax_gauss_bonnet.text(0, -2.5, "∫ κ(s) ds = 2π", fontsize=12, ha='center')
ax_gauss_bonnet.text(0, -2.8, "Total curvature = 2π for any simple closed curve", fontsize=10, ha='center')

ax_gauss_bonnet.set_xlim(-3, 3)
ax_gauss_bonnet.set_ylim(-3, 3)
ax_gauss_bonnet.set_aspect('equal')
ax_gauss_bonnet.grid(True)
ax_gauss_bonnet.legend()

plt.savefig('/home/ubuntu/MIT_Differential_Geometry_18.950_Textbook/supplementary_materials/visualizations/chapter6/gauss_bonnet_theorem.png', dpi=300)

# 3. Whitney-Graustein Theorem Visualization
fig_whitney = plt.figure(figsize=(15, 5))
fig_whitney.suptitle('Whitney-Graustein Theorem', fontsize=16)

# Create curves with different rotation numbers
# Rotation number 1 (circle)
ax1 = fig_whitney.add_subplot(131)
ax1.set_title('Rotation Number = 1')
circle_x = np.cos(theta)
circle_y = np.sin(theta)
ax1.plot(circle_x, circle_y, 'b-', linewidth=2)

# Add tangent vectors
for i in range(0, 100, 20):
    # Calculate tangent vector
    dx = circle_x[(i+1)%100] - circle_x[i]
    dy = circle_y[(i+1)%100] - circle_y[i]
    
    # Normalize
    length = np.sqrt(dx**2 + dy**2)
    if length > 0:
        dx = dx / length * 0.2
        dy = dy / length * 0.2
    
    ax1.arrow(circle_x[i], circle_y[i], dx, dy, 
              head_width=0.05, head_length=0.05, fc='blue', ec='blue')

# Rotation number 0 (figure-eight)
ax2 = fig_whitney.add_subplot(132)
ax2.set_title('Rotation Number = 0')
figure_eight_x = np.sin(2*theta)
figure_eight_y = np.sin(theta)
ax2.plot(figure_eight_x, figure_eight_y, 'r-', linewidth=2)

# Add tangent vectors
for i in range(0, 100, 20):
    # Calculate tangent vector
    dx = figure_eight_x[(i+1)%100] - figure_eight_x[i]
    dy = figure_eight_y[(i+1)%100] - figure_eight_y[i]
    
    # Normalize
    length = np.sqrt(dx**2 + dy**2)
    if length > 0:
        dx = dx / length * 0.2
        dy = dy / length * 0.2
    
    ax2.arrow(figure_eight_x[i], figure_eight_y[i], dx, dy, 
              head_width=0.05, head_length=0.05, fc='red', ec='red')

# Rotation number 2 (double circle)
ax3 = fig_whitney.add_subplot(133)
ax3.set_title('Rotation Number = 2')
double_circle_x = np.cos(2*theta)
double_circle_y = np.sin(2*theta)
ax3.plot(double_circle_x, double_circle_y, 'g-', linewidth=2)

# Add tangent vectors
for i in range(0, 100, 20):
    # Calculate tangent vector
    dx = double_circle_x[(i+1)%100] - double_circle_x[i]
    dy = double_circle_y[(i+1)%100] - double_circle_y[i]
    
    # Normalize
    length = np.sqrt(dx**2 + dy**2)
    if length > 0:
        dx = dx / length * 0.2
        dy = dy / length * 0.2
    
    ax3.arrow(double_circle_x[i], double_circle_y[i], dx, dy, 
              head_width=0.05, head_length=0.05, fc='green', ec='green')

# Set limits and properties for all subplots
for ax in [ax1, ax2, ax3]:
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.grid(True)

plt.tight_layout()
plt.savefig('/home/ubuntu/MIT_Differential_Geometry_18.950_Textbook/supplementary_materials/visualizations/chapter6/whitney_graustein_theorem.png', dpi=300)

print("All visualizations created successfully!")
