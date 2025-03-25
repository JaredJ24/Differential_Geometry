import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# Create figure
fig, ax = plt.figure(figsize=(10, 8)), plt.subplot(111)

# Function to create a curve with varying curvature
def curve_with_osculating_circles(t):
    # Parametric equation for a curve with varying curvature
    x = 2 * np.cos(t) + np.cos(2 * t)
    y = 2 * np.sin(t) - np.sin(2 * t)
    return x, y

# Generate the curve
t = np.linspace(0, 2*np.pi, 1000)
x, y = curve_with_osculating_circles(t)

# Plot the curve
ax.plot(x, y, 'b-', linewidth=2, label='Curve')

# Points to show osculating circles
points_to_show = [100, 300, 500, 700, 900]
colors = ['r', 'g', 'purple', 'orange', 'brown']

for i, point_idx in enumerate(points_to_show):
    # Get point on curve
    point_x, point_y = x[point_idx], y[point_idx]
    
    # Calculate derivatives
    dt = t[1] - t[0]
    dx_dt = np.gradient(x, dt)[point_idx]
    dy_dt = np.gradient(y, dt)[point_idx]
    
    # Second derivatives
    d2x_dt2 = np.gradient(np.gradient(x, dt), dt)[point_idx]
    d2y_dt2 = np.gradient(np.gradient(y, dt), dt)[point_idx]
    
    # Calculate curvature
    numerator = dx_dt * d2y_dt2 - dy_dt * d2x_dt2
    denominator = (dx_dt**2 + dy_dt**2)**(3/2)
    curvature = numerator / denominator
    
    # Radius of osculating circle
    radius = 1 / abs(curvature)
    
    # Unit tangent vector
    speed = np.sqrt(dx_dt**2 + dy_dt**2)
    tangent_x, tangent_y = dx_dt / speed, dy_dt / speed
    
    # Unit normal vector (rotate tangent 90 degrees in direction of curvature)
    normal_x = -tangent_y
    normal_y = tangent_x
    if curvature < 0:
        normal_x, normal_y = -normal_x, -normal_y
    
    # Center of osculating circle
    center_x = point_x + radius * normal_x
    center_y = point_y + radius * normal_y
    
    # Draw osculating circle
    circle = Circle((center_x, center_y), radius, fill=False, color=colors[i], linestyle='--', linewidth=1.5)
    ax.add_patch(circle)
    
    # Mark the point on the curve
    ax.plot(point_x, point_y, 'o', color=colors[i], markersize=6)
    
    # Draw radius line from point to center
    ax.plot([point_x, center_x], [point_y, center_y], '-', color=colors[i], linewidth=1)
    
    # Add text showing curvature value
    ax.annotate(f'κ = {curvature:.2f}\nR = {radius:.2f}', 
                xy=(point_x, point_y), 
                xytext=(point_x + 0.5, point_y + 0.5),
                color=colors[i],
                bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=colors[i], alpha=0.7))

# Set equal aspect ratio
ax.set_aspect('equal')

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Osculating Circles and Curvature', fontsize=14)

# Add explanation text
explanation = """The osculating circle at a point on a curve is the circle that:
1. Passes through the point
2. Has the same tangent as the curve at that point
3. Has the same curvature as the curve at that point

The radius of the osculating circle is R = 1/|κ|, where κ is the curvature.
- Smaller circles (larger curvature) indicate sharper turns
- Larger circles (smaller curvature) indicate gentler turns
- The sign of κ indicates the direction of turning"""

ax.text(0.02, 0.02, explanation, transform=ax.transAxes, fontsize=10,
        bbox=dict(facecolor='white', alpha=0.7))

# Adjust layout and save
plt.tight_layout()
plt.savefig('/home/ubuntu/differential_geometry_textbook/visualizations/ch2_osculating_circles.png', dpi=300, bbox_inches='tight')
plt.close()

print("Visualization saved to: /home/ubuntu/differential_geometry_textbook/visualizations/ch2_osculating_circles.png")
