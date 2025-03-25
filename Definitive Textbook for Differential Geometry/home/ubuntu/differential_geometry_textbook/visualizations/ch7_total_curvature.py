import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Arc, Arrow

# Create figure
fig, ax = plt.figure(figsize=(10, 8)), plt.subplot(111)

# Function to create a curve with varying curvature
def curve_with_total_curvature(t):
    # Parametric equation for a curve
    x = 2 * np.cos(t) + np.cos(2 * t)
    y = 2 * np.sin(t) - np.sin(2 * t)
    return x, y

# Generate the curve
t = np.linspace(0, 2*np.pi, 1000)
x, y = curve_with_total_curvature(t)

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

# Calculate total curvature (absolute value of curvature integrated over the curve)
total_curvature = np.sum(np.abs(curvature) * np.sqrt(dx_dt**2 + dy_dt**2)) * dt
total_turning_angle = total_curvature * 180 / np.pi  # Convert to degrees

# Points to highlight curvature
points_to_show = [100, 300, 500, 700, 900]
colors = ['r', 'g', 'purple', 'orange', 'brown']

for i, point_idx in enumerate(points_to_show):
    # Get point on curve
    point_x, point_y = x[point_idx], y[point_idx]
    
    # Calculate tangent direction
    tangent_x, tangent_y = dx_dt[point_idx], dy_dt[point_idx]
    tangent_length = np.sqrt(tangent_x**2 + tangent_y**2)
    tangent_x, tangent_y = tangent_x/tangent_length, tangent_y/tangent_length
    
    # Calculate normal direction
    normal_x, normal_y = -tangent_y, tangent_x
    if curvature[point_idx] < 0:
        normal_x, normal_y = -normal_x, -normal_y
    
    # Draw tangent vector
    ax.arrow(point_x, point_y, tangent_x*0.3, tangent_y*0.3, 
             head_width=0.1, head_length=0.15, fc=colors[i], ec=colors[i])
    
    # Draw curvature indicator (circle with radius proportional to 1/|curvature|)
    k = curvature[point_idx]
    if abs(k) > 1e-10:  # Avoid division by zero
        radius = min(0.5, 1 / abs(k))  # Limit radius for visualization
        center_x = point_x + radius * normal_x
        center_y = point_y + radius * normal_y
        
        # Draw a small arc to indicate curvature
        angle = np.arctan2(tangent_y, tangent_x) * 180 / np.pi
        arc = Arc((center_x, center_y), 2*radius, 2*radius, 
                 angle=angle, theta1=-30, theta2=30, 
                 linewidth=1.5, color=colors[i], linestyle='--')
        ax.add_patch(arc)
        
        # Add text showing curvature value
        ax.text(point_x + 0.4*normal_x, point_y + 0.4*normal_y, 
                f'κ = {k:.2f}', color=colors[i], fontsize=9,
                bbox=dict(facecolor='white', alpha=0.7))

# Add arrows to show direction of traversal
arrow_positions = [50, 250, 450, 650, 850]
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
ax.set_title('Total Curvature and the Hopf Umlaufsatz', fontsize=14)

# Add explanation text
explanation = f"""The total curvature of a closed curve measures the total amount of turning:

Total Curvature = ∫|κ(s)|ds ≈ {total_curvature:.2f} radians ≈ {total_turning_angle:.1f}°

The Hopf Umlaufsatz (Turning Theorem) states:
- For a simple closed curve traversed counterclockwise, the total curvature is exactly 2π (360°)
- The sign of the curvature κ at each point indicates whether the curve is turning left (κ > 0) or right (κ < 0)
- For curves with self-intersections, the total curvature equals 2πn, where n is the rotation number

This connects local differential properties (curvature) with global topological properties (winding number).

Applications include:
- The Four Vertex Theorem (a simple closed curve has at least 4 points where curvature is locally extremal)
- The Fary-Milnor Theorem (a knotted curve has total curvature > 4π)
- The isoperimetric inequality (relating perimeter and area)"""

# Add a box for the explanation
ax.text(0.02, 0.02, explanation, transform=ax.transAxes, fontsize=10,
        bbox=dict(facecolor='white', alpha=0.7))

# Set limits with some padding
ax.set_xlim(-3.5, 3.5)
ax.set_ylim(-3.5, 3.5)

# Adjust layout and save
plt.tight_layout()
plt.savefig('/home/ubuntu/differential_geometry_textbook/visualizations/ch7_total_curvature.png', dpi=300, bbox_inches='tight')
plt.close()

print("Visualization saved to: /home/ubuntu/differential_geometry_textbook/visualizations/ch7_total_curvature.png")
