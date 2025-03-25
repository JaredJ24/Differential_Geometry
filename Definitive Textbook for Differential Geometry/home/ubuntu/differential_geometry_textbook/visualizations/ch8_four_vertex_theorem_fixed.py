import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# Create figure
fig, ax = plt.figure(figsize=(10, 8)), plt.subplot(111)

# Function to create a curve with exactly four vertices
def curve_with_four_vertices(t):
    # Parametric equation for a curve with exactly four vertices
    r = 2 + 0.3 * np.cos(2*t)
    x = r * np.cos(t)
    y = r * np.sin(t)
    return x, y

# Generate the curve
t = np.linspace(0, 2*np.pi, 1000)
x, y = curve_with_four_vertices(t)

# Plot the curve
ax.plot(x, y, 'b-', linewidth=2, label='Closed Curve')

# Calculate curvature at each point
dt = t[1] - t[0]
dx_dt = np.gradient(x, dt)
dy_dt = np.gradient(y, dt)
d2x_dt2 = np.gradient(dx_dt, dt)
d2y_dt2 = np.gradient(dy_dt, dt)

# Curvature formula: κ = (x'y'' - y'x'') / (x'^2 + y'^2)^(3/2)
numerator = dx_dt * d2y_dt2 - dy_dt * d2x_dt2
denominator = (dx_dt**2 + dy_dt**2)**(3/2)
curvature = numerator / denominator

# Find vertices (local extrema of curvature)
vertices = []
for i in range(1, len(curvature)-1):
    if (curvature[i] > curvature[i-1] and curvature[i] > curvature[i+1]) or \
       (curvature[i] < curvature[i-1] and curvature[i] < curvature[i+1]):
        vertices.append(i)

# Ensure we have exactly 4 vertices for visualization
if len(vertices) > 4:
    # Find the 4 most extreme vertices
    vertex_values = [abs(curvature[i]) for i in vertices]
    vertices = [vertices[i] for i in np.argsort(vertex_values)[-4:]]

# Plot vertices
colors = ['red', 'green', 'purple', 'orange']
for i, vertex_idx in enumerate(vertices):
    # Get point on curve
    point_x, point_y = x[vertex_idx], y[vertex_idx]
    
    # Plot vertex
    ax.plot(point_x, point_y, 'o', color=colors[i], markersize=10)
    
    # Add label
    if curvature[vertex_idx] > 0:
        label = f"Vertex {i+1}: κ = {curvature[vertex_idx]:.3f} (max)"
    else:
        label = f"Vertex {i+1}: κ = {curvature[vertex_idx]:.3f} (min)"
    
    ax.text(point_x + 0.1, point_y + 0.1, label, fontsize=10, 
            bbox=dict(facecolor='white', alpha=0.7))
    
    # Draw osculating circle
    k = curvature[vertex_idx]
    if abs(k) > 1e-10:  # Avoid division by zero
        radius = 1 / abs(k)
        
        # Calculate normal direction
        tangent_x, tangent_y = dx_dt[vertex_idx], dy_dt[vertex_idx]
        tangent_length = np.sqrt(tangent_x**2 + tangent_y**2)
        tangent_x, tangent_y = tangent_x/tangent_length, tangent_y/tangent_length
        normal_x, normal_y = -tangent_y, tangent_x
        if k < 0:
            normal_x, normal_y = -normal_x, -normal_y
        
        # Calculate center of osculating circle
        center_x = point_x + radius * normal_x
        center_y = point_y + radius * normal_y
        
        # Draw osculating circle
        circle = Circle((center_x, center_y), radius, fill=False, 
                        linestyle='--', color=colors[i], alpha=0.5)
        ax.add_patch(circle)

# Add arrows to show direction of traversal
arrow_positions = [100, 350, 600, 850]
for pos in arrow_positions:
    # Calculate direction at this position
    dx = x[(pos+10) % len(x)] - x[pos]
    dy = y[(pos+10) % len(y)] - y[pos]
    # Normalize
    length = np.sqrt(dx**2 + dy**2)
    if length > 0:
        dx, dy = dx/length, dy/length
        # Add arrow
        ax.arrow(x[pos], y[pos], dx*0.2, dy*0.2, 
                head_width=0.1, head_length=0.15, fc='blue', ec='blue')

# Set equal aspect ratio
ax.set_aspect('equal')

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Four Vertex Theorem Visualization', fontsize=14)

# Add explanation text
explanation = """The Four Vertex Theorem states that any simple closed curve in the plane has at least 
four vertices, where a vertex is a point of locally extreme curvature.

Key insights:
1. A vertex occurs where the curvature reaches a local maximum or minimum
2. The osculating circles at vertices (dashed circles) are either:
   - Locally largest (at minimum curvature points)
   - Locally smallest (at maximum curvature points)
3. The theorem holds for all simple closed curves, regardless of shape

This result connects to:
- The Tennis Ball Theorem (a smooth closed surface in R³ must have at least four umbilical points)
- Sturm's oscillation theorem in differential equations
- The isoperimetric inequality

Applications include:
- Computer-aided geometric design
- Optical systems design
- Shape analysis in computer vision"""

# Add a box for the explanation
ax.text(0.02, 0.02, explanation, transform=ax.transAxes, fontsize=10,
        bbox=dict(facecolor='white', alpha=0.7))

# Set limits with some padding
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)

# Adjust layout and save
plt.tight_layout()
plt.savefig('/home/ubuntu/differential_geometry_textbook/visualizations/ch8_four_vertex_theorem.png', dpi=300, bbox_inches='tight')
plt.close()

print("Visualization saved to: /home/ubuntu/differential_geometry_textbook/visualizations/ch8_four_vertex_theorem.png")
