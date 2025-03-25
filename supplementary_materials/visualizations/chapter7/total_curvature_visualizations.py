import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d
import matplotlib.animation as animation
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Polygon

# Set up the figure with multiple subplots
fig = plt.figure(figsize=(20, 15))
fig.suptitle('Total Curvature and the Hopf Umlaufsatz Visualizations', fontsize=20)

# 1. Total Curvature of Simple Curves
ax1 = fig.add_subplot(231)
ax1.set_title('Total Curvature of Simple Curves')

# Draw a straight line
line_x = np.linspace(-1, 1, 100)
line_y = np.zeros_like(line_x)
ax1.plot(line_x, line_y, 'b-', linewidth=2, label='Line (K = 0)')

# Draw a circle
theta = np.linspace(0, 2*np.pi, 100)
circle_x = np.cos(theta)
circle_y = np.sin(theta)
ax1.plot(circle_x, circle_y, 'g-', linewidth=2, label='Circle (K = 2π)')

# Draw a semicircle
semicircle_theta = np.linspace(0, np.pi, 50)
semicircle_x = np.cos(semicircle_theta)
semicircle_y = np.sin(semicircle_theta)
ax1.plot(semicircle_x, semicircle_y, 'r-', linewidth=2, label='Semicircle (K = π)')

# Add tangent vectors to illustrate turning
for curve, color, points in [
    ((line_x, line_y), 'blue', [0, 50, 99]),
    ((circle_x, circle_y), 'green', [0, 25, 50, 75]),
    ((semicircle_x, semicircle_y), 'red', [0, 25, 49])
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
        
        ax1.arrow(curve[0][i], curve[1][i], dx, dy, 
                  head_width=0.05, head_length=0.05, fc=color, ec=color)

ax1.set_xlim(-1.5, 1.5)
ax1.set_ylim(-1.5, 1.5)
ax1.set_aspect('equal')
ax1.grid(True)
ax1.legend()

# 2. The Hopf Umlaufsatz for Simple Closed Curves
ax2 = fig.add_subplot(232)
ax2.set_title('Hopf Umlaufsatz: Simple Closed Curves')

# Draw different simple closed curves
# Circle
circle_x = np.cos(theta)
circle_y = np.sin(theta)
ax2.plot(circle_x, circle_y, 'b-', linewidth=2, label='Circle')

# Ellipse
a, b = 1.5, 0.8
ellipse_x = a * np.cos(theta)
ellipse_y = b * np.sin(theta)
ax2.plot(ellipse_x, ellipse_y, 'g-', linewidth=2, label='Ellipse')

# Rounded square
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

square_x, square_y = rounded_rect([0, 0], 1.5, 1.5, 0.3)
ax2.plot(square_x, square_y, 'r-', linewidth=2, label='Rounded Square')

# Add text explaining the theorem
ax2.text(0, -1.8, "Hopf Umlaufsatz: Total Curvature = 2π", fontsize=12, ha='center')
ax2.text(0, -2.1, "for any simple closed curve", fontsize=10, ha='center')

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
        
        ax2.arrow(curve[0][i], curve[1][i], dx, dy, 
                  head_width=0.05, head_length=0.05, fc=color, ec=color)

ax2.set_xlim(-2.5, 2.5)
ax2.set_ylim(-2.5, 2.5)
ax2.set_aspect('equal')
ax2.grid(True)
ax2.legend()

# 3. Winding Numbers and Total Curvature
ax3 = fig.add_subplot(233)
ax3.set_title('Winding Numbers and Total Curvature')

# Draw a figure-eight curve
t = np.linspace(0, 2*np.pi, 100)
figure_eight_x = np.sin(t)
figure_eight_y = np.sin(2*t) / 2
ax3.plot(figure_eight_x, figure_eight_y, 'b-', linewidth=2, label='Figure-Eight (K = 2π)')

# Draw a double circle (circle traversed twice)
double_circle_t = np.linspace(0, 4*np.pi, 200)
double_circle_x = np.cos(double_circle_t)
double_circle_y = np.sin(double_circle_t)
ax3.plot(double_circle_x, double_circle_y, 'g-', linewidth=2, label='Double Circle (K = 4π)')

# Add points with different winding numbers
points = [
    (0.5, 0.2, 'Figure-Eight: W = 1'),
    (-0.5, -0.2, 'Figure-Eight: W = -1'),
    (0, 0, 'Double Circle: W = 2')
]

for x, y, label in points:
    ax3.plot(x, y, 'ro', markersize=8)
    ax3.text(x+0.1, y+0.1, label, fontsize=8)

# Add tangent vectors to illustrate winding
for curve, color, points in [
    ((figure_eight_x, figure_eight_y), 'blue', [0, 25, 50, 75]),
    ((double_circle_x, double_circle_y), 'green', [0, 50, 100, 150])
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
        
        ax3.arrow(curve[0][i], curve[1][i], dx, dy, 
                  head_width=0.05, head_length=0.05, fc=color, ec=color)

# Add text explaining the relationship
ax3.text(0, -1.8, "Total Curvature = 2π · |Winding Number|", fontsize=12, ha='center')

ax3.set_xlim(-2, 2)
ax3.set_ylim(-2, 2)
ax3.set_aspect('equal')
ax3.grid(True)
ax3.legend()

# 4. The Four Vertex Theorem
ax4 = fig.add_subplot(234)
ax4.set_title('Four Vertex Theorem')

# Draw an ellipse
a, b = 2, 1
ellipse_t = np.linspace(0, 2*np.pi, 100)
ellipse_x = a * np.cos(ellipse_t)
ellipse_y = b * np.sin(ellipse_t)
ax4.plot(ellipse_x, ellipse_y, 'b-', linewidth=2, label='Ellipse')

# Calculate curvature of the ellipse
# κ(t) = ab / (a² sin²(t) + b² cos²(t))^(3/2)
curvature = a * b / ((a**2 * np.sin(ellipse_t)**2 + b**2 * np.cos(ellipse_t)**2)**(3/2))

# Find vertices (local extrema of curvature)
# For an ellipse, vertices are at t = 0, π/2, π, 3π/2
vertices_t = [0, np.pi/2, np.pi, 3*np.pi/2]
vertices_x = [a * np.cos(t) for t in vertices_t]
vertices_y = [b * np.sin(t) for t in vertices_t]
vertices_k = [a * b / ((a**2 * np.sin(t)**2 + b**2 * np.cos(t)**2)**(3/2)) for t in vertices_t]

# Mark vertices on the ellipse
ax4.plot(vertices_x, vertices_y, 'ro', markersize=8, label='Vertices (Extrema of Curvature)')

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
    osc_circle_t = np.linspace(0, 2*np.pi, 100)
    osc_circle_x = center_x + r * np.cos(osc_circle_t)
    osc_circle_y = center_y + r * np.sin(osc_circle_t)
    ax4.plot(osc_circle_x, osc_circle_y, '--', color='gray', alpha=0.5)

# Add a subplot showing curvature as a function of parameter
ax_curvature = fig.add_axes([0.2, 0.2, 0.2, 0.1])
ax_curvature.plot(ellipse_t, curvature, 'g-')
ax_curvature.set_title('Curvature vs. Parameter', fontsize=10)
ax_curvature.set_xlabel('t', fontsize=8)
ax_curvature.set_ylabel('κ(t)', fontsize=8)
ax_curvature.grid(True)

# Mark extrema on the curvature plot
for i, t in enumerate(vertices_t):
    ax_curvature.plot(t, vertices_k[i], 'ro', markersize=5)

# Add text explaining the theorem
ax4.text(0, -2.5, "Four Vertex Theorem: Any simple closed curve", fontsize=12, ha='center')
ax4.text(0, -2.8, "has at least four vertices (extrema of curvature)", fontsize=10, ha='center')

ax4.set_xlim(-3, 3)
ax4.set_ylim(-3, 3)
ax4.set_aspect('equal')
ax4.grid(True)
ax4.legend()

# 5. The Isoperimetric Inequality
ax5 = fig.add_subplot(235)
ax5.set_title('Isoperimetric Inequality')

# Draw shapes with different isoperimetric ratios
# Circle (optimal ratio = 1)
circle_t = np.linspace(0, 2*np.pi, 100)
circle_x = np.cos(circle_t)
circle_y = np.sin(circle_t)
ax5.plot(circle_x, circle_y, 'b-', linewidth=2, label='Circle (L²/4πA = 1)')
ax5.fill(circle_x, circle_y, 'lightblue', alpha=0.3)

# Ellipse (suboptimal ratio)
a, b = 2, 0.5  # semi-major and semi-minor axes
ellipse_x = a * np.cos(circle_t)
ellipse_y = b * np.sin(circle_t)
# Calculate perimeter (approximation)
perimeter_ellipse = 2 * np.pi * np.sqrt((a**2 + b**2) / 2)
area_ellipse = np.pi * a * b
ratio_ellipse = perimeter_ellipse**2 / (4 * np.pi * area_ellipse)
ax5.plot(ellipse_x, ellipse_y, 'g-', linewidth=2, label=f'Ellipse (L²/4πA ≈ {ratio_ellipse:.3f})')
ax5.fill(ellipse_x, ellipse_y, 'lightgreen', alpha=0.3)

# Square (suboptimal ratio)
square_side = np.sqrt(np.pi)  # Area = pi
square_x = np.array([-1, 1, 1, -1, -1]) * square_side/2
square_y = np.array([-1, -1, 1, 1, -1]) * square_side/2
perimeter_square = 4 * square_side
area_square = square_side**2
ratio_square = perimeter_square**2 / (4 * np.pi * area_square)
ax5.plot(square_x, square_y, 'r-', linewidth=2, label=f'Square (L²/4πA ≈ {ratio_square:.3f})')
ax5.fill(square_x, square_y, 'lightcoral', alpha=0.3)

# Add text explaining the inequality
ax5.text(0, -2.5, "Isoperimetric Inequality: L² ≥ 4πA", fontsize=12, ha='center')
ax5.text(0, -2.8, "Equality holds only for circles", fontsize=10, ha='center')

ax5.set_xlim(-2.5, 2.5)
ax5.set_ylim(-3, 3)
ax5.set_aspect('equal')
ax5.grid(True)
ax5.legend()

# 6. The Fary-Milnor Theorem
ax6 = fig.add_subplot(236)
ax6.set_title('Fary-Milnor Theorem')

# Draw an unknot (circle)
circle_t = np.linspace(0, 2*np.pi, 100)
circle_x = np.cos(circle_t)
circle_y = np.sin(circle_t)
circle_z = np.zeros_like(circle_t)
ax6.plot(circle_x, circle_y, 'b-', linewidth=2, label='Unknot (K = 2π)')

# Draw a trefoil knot projection
trefoil_t = np.linspace(0, 2*np.pi, 100)
trefoil_x = np.sin(trefoil_t) + 2 * np.sin(2*trefoil_t)
trefoil_y = np.cos(trefoil_t) - 2 * np.cos(2*trefoil_t)
# Normalize to fit in the plot
max_val = max(np.max(np.abs(trefoil_x)), np.max(np.abs(trefoil_y)))
trefoil_x = trefoil_x / max_val * 1.5
trefoil_y = trefoil_y / max_val * 1.5
ax6.plot(trefoil_x, trefoil_y, 'g-', linewidth=2, label='Trefoil Knot (K > 4π)')

# Add text explaining the theorem
ax6.text(0, -2.5, "Fary-Milnor Theorem: If a curve is knotted,", fontsize=12, ha='center')
ax6.text(0, -2.8, "its total curvature is at least 4π", fontsize=10, ha='center')

ax6.set_xlim(-2.5, 2.5)
ax6.set_ylim(-3, 3)
ax6.set_aspect('equal')
ax6.grid(True)
ax6.legend()

plt.tight_layout()
plt.savefig('/home/ubuntu/MIT_Differential_Geometry_18.950_Textbook/supplementary_materials/visualizations/chapter7/total_curvature_visualizations.png', dpi=300)

# Create additional visualizations

# 1. Turning Angle Visualization
fig_turning = plt.figure(figsize=(15, 5))
fig_turning.suptitle('Turning Angle and Total Curvature', fontsize=16)

# Create curves with different turning angles
# Straight line (turning angle = 0)
ax1 = fig_turning.add_subplot(131)
ax1.set_title('Straight Line (Δθ = 0)')
line_t = np.linspace(0, 1, 100)
line_x = line_t
line_y = np.zeros_like(line_t)
ax1.plot(line_x, line_y, 'b-', linewidth=2)

# Add tangent vectors
for i in range(0, 100, 20):
    ax1.arrow(line_x[i], line_y[i], 0.1, 0, 
              head_width=0.05, head_length=0.05, fc='blue', ec='blue')

# Semicircle (turning angle = π)
ax2 = fig_turning.add_subplot(132)
ax2.set_title('Semicircle (Δθ = π)')
semicircle_t = np.linspace(0, np.pi, 100)
semicircle_x = np.cos(semicircle_t)
semicircle_y = np.sin(semicircle_t)
ax2.plot(semicircle_x, semicircle_y, 'g-', linewidth=2)

# Add tangent vectors
for i in range(0, 100, 20):
    # Calculate tangent vector
    dx = -np.sin(semicircle_t[i])
    dy = np.cos(semicircle_t[i])
    
    # Normalize
    length = np.sqrt(dx**2 + dy**2)
    if length > 0:
        dx = dx / length * 0.2
        dy = dy / length * 0.2
    
    ax2.arrow(semicircle_x[i], semicircle_y[i], dx, dy, 
              head_width=0.05, head_length=0.05, fc='green', ec='green')

# Full circle (turning angle = 2π)
ax3 = fig_turning.add_subplot(133)
ax3.set_title('Full Circle (Δθ = 2π)')
circle_t = np.linspace(0, 2*np.pi, 100)
circle_x = np.cos(circle_t)
circle_y = np.sin(circle_t)
ax3.plot(circle_x, circle_y, 'r-', linewidth=2)

# Add tangent vectors
for i in range(0, 100, 20):
    # Calculate tangent vector
    dx = -np.sin(circle_t[i])
    dy = np.cos(circle_t[i])
    
    # Normalize
    length = np.sqrt(dx**2 + dy**2)
    if length > 0:
        dx = dx / length * 0.2
        dy = dy / length * 0.2
    
    ax3.arrow(circle_x[i], circle_y[i], dx, dy, 
              head_width=0.05, head_length=0.05, fc='red', ec='red')

# Set limits and properties for all subplots
for ax in [ax1, ax2, ax3]:
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.grid(True)

plt.tight_layout()
plt.savefig('/home/ubuntu/MIT_Differential_Geometry_18.950_Textbook/supplementary_materials/visualizations/chapter7/turning_angle_visualization.png', dpi=300)

# 2. Gauss-Bonnet Theorem Visualization
fig_gauss_bonnet = plt.figure(figsize=(10, 10))
ax_gauss_bonnet = fig_gauss_bonnet.add_subplot(111)
ax_gauss_bonnet.set_title('Gauss-Bonnet Theorem for Plane Curves')

# Draw different curves with the same total curvature
# Circle
circle_t = np.linspace(0, 2*np.pi, 100)
circle_x = np.cos(circle_t)
circle_y = np.sin(circle_t)
ax_gauss_bonnet.plot(circle_x, circle_y, 'b-', linewidth=2, label='Circle')

# Ellipse
a, b = 2, 1
ellipse_x = a * np.cos(circle_t)
ellipse_y = b * np.sin(circle_t)
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
ax_gauss_bonnet.text(0, -2.5, "Gauss-Bonnet Theorem: ∫ κ(s) ds = 2π", fontsize=12, ha='center')
ax_gauss_bonnet.text(0, -2.8, "for any simple closed curve", fontsize=10, ha='center')

ax_gauss_bonnet.set_xlim(-3, 3)
ax_gauss_bonnet.set_ylim(-3, 3)
ax_gauss_bonnet.set_aspect('equal')
ax_gauss_bonnet.grid(True)
ax_gauss_bonnet.legend()

plt.savefig('/home/ubuntu/MIT_Differential_Geometry_18.950_Textbook/supplementary_materials/visualizations/chapter7/gauss_bonnet_theorem.png', dpi=300)

print("All visualizations created successfully!")
