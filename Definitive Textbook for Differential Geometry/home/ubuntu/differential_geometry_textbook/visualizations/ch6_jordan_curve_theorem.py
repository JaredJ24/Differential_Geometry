import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# Create figure
fig, ax = plt.figure(figsize=(10, 8)), plt.subplot(111)

# Function to create a simple closed curve
def create_simple_closed_curve(n_points=100, radius=1, center=(0, 0), noise=0.1):
    theta = np.linspace(0, 2*np.pi, n_points, endpoint=False)
    # Add some noise to make it less circular
    r = radius + noise * np.sin(3*theta) + noise/2 * np.cos(5*theta)
    x = center[0] + r * np.cos(theta)
    y = center[1] + r * np.sin(theta)
    return np.column_stack((x, y))

# Create a simple closed curve
curve = create_simple_closed_curve(n_points=100, radius=2, center=(0, 0), noise=0.5)

# Plot the curve
ax.plot(curve[:, 0], curve[:, 1], 'b-', linewidth=2, label='Simple Closed Curve')

# Fill the interior with a light color
interior_polygon = Polygon(curve, closed=True, alpha=0.2, color='blue')
ax.add_patch(interior_polygon)

# Mark some points inside and outside
inside_points = [(0, 0), (0.5, 0.5), (-0.7, 0.3)]
outside_points = [(3, 3), (-3, 2), (0, -3)]

# Plot inside points
for i, point in enumerate(inside_points):
    ax.plot(point[0], point[1], 'go', markersize=8)
    ax.text(point[0]+0.1, point[1]+0.1, f'Inside Point {i+1}', fontsize=10)

# Plot outside points
for i, point in enumerate(outside_points):
    ax.plot(point[0], point[1], 'ro', markersize=8)
    ax.text(point[0]+0.1, point[1]+0.1, f'Outside Point {i+1}', fontsize=10)

# Add arrows to show the orientation of the curve
arrow_positions = [10, 30, 50, 70, 90]  # Indices for arrow positions
for pos in arrow_positions:
    # Calculate direction at this position
    next_pos = (pos + 1) % len(curve)
    dx = curve[next_pos, 0] - curve[pos, 0]
    dy = curve[next_pos, 1] - curve[pos, 1]
    # Normalize
    length = np.sqrt(dx**2 + dy**2)
    if length > 0:
        dx, dy = dx/length, dy/length
        # Add arrow
        ax.arrow(curve[pos, 0], curve[pos, 1], dx*0.3, dy*0.3, 
                head_width=0.15, head_length=0.2, fc='blue', ec='blue')

# Set equal aspect ratio
ax.set_aspect('equal')

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Jordan Curve Theorem Visualization', fontsize=14)

# Add explanation text
explanation = """The Jordan Curve Theorem states that every simple closed curve in the plane 
divides the plane into exactly two regions: an "inside" and an "outside".

Key properties:
1. A simple closed curve is a continuous loop that doesn't intersect itself
2. Any path from an inside point to an outside point must cross the curve
3. The inside region is bounded, while the outside region is unbounded
4. The theorem seems intuitively obvious but is surprisingly difficult to prove rigorously

Applications:
- Computer graphics (determining if a point is inside or outside a polygon)
- Topology (fundamental result about plane separation)
- Winding number theory (inside points have non-zero winding numbers)
- Computer vision (object recognition and boundary detection)"""

# Add a box for the explanation
ax.text(0.02, 0.02, explanation, transform=ax.transAxes, fontsize=10,
        bbox=dict(facecolor='white', alpha=0.7))

# Set limits with some padding
ax.set_xlim(-3.5, 3.5)
ax.set_ylim(-3.5, 3.5)

# Adjust layout and save
plt.tight_layout()
plt.savefig('/home/ubuntu/differential_geometry_textbook/visualizations/ch6_jordan_curve_theorem.png', dpi=300, bbox_inches='tight')
plt.close()

print("Visualization saved to: /home/ubuntu/differential_geometry_textbook/visualizations/ch6_jordan_curve_theorem.png")
