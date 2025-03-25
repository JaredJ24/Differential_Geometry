import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# Create figure
fig, ax = plt.figure(figsize=(10, 8)), plt.subplot(111)

# Function to create a circle with given center and radius
def create_circle(center_x, center_y, radius, **kwargs):
    return Circle((center_x, center_y), radius, **kwargs)

# Create a point to calculate winding numbers around
center_x, center_y = 0, 0

# Create curves with different winding numbers
theta = np.linspace(0, 2*np.pi, 100)  # Reduced number of points

# Curve with winding number 1 (circle)
r1 = 2
x1 = center_x + r1 * np.cos(theta)
y1 = center_y + r1 * np.sin(theta)

# Curve with winding number 2 (circle traversed twice)
x2 = center_x + r1 * np.cos(2*theta)
y2 = center_y + r1 * np.sin(2*theta)

# Curve with winding number 0 (figure-8)
r3 = 3
x3 = r3 * np.sin(theta)
y3 = r3 * np.sin(theta) * np.cos(theta)

# Curve with winding number -1 (circle in opposite direction)
x4 = center_x + r1 * np.cos(-theta)
y4 = center_y + r1 * np.sin(-theta)

# Plot the curves
ax.plot(x1, y1, 'b-', linewidth=2, label='Circle (winding number = 1)')
ax.plot(x2, y2, 'g-', linewidth=2, label='Double loop (winding number = 2)')
ax.plot(x3, y3, 'r-', linewidth=2, label='Figure-8 (winding number = 0)')
ax.plot(x4, y4, 'c-', linewidth=2, label='Reverse circle (winding number = -1)')

# Mark the center point
ax.plot(center_x, center_y, 'ko', markersize=8)
ax.text(center_x + 0.2, center_y + 0.2, 'Point p', fontsize=12)

# Add arrows to show direction
arrow_positions = [25, 50, 75]  # Indices for arrow positions

for curve_x, curve_y, color in [(x1, y1, 'b'), (x2, y2, 'g'), (x3, y3, 'r'), (x4, y4, 'c')]:
    for pos in arrow_positions:
        # Calculate direction at this position
        dx = curve_x[(pos+1) % len(curve_x)] - curve_x[pos]
        dy = curve_y[(pos+1) % len(curve_y)] - curve_y[pos]
        # Normalize
        length = np.sqrt(dx**2 + dy**2)
        if length > 0:
            dx, dy = dx/length, dy/length
            # Add arrow
            ax.arrow(curve_x[pos], curve_y[pos], dx*0.3, dy*0.3, 
                    head_width=0.15, head_length=0.2, fc=color, ec=color)

# Set equal aspect ratio
ax.set_aspect('equal')

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Winding Numbers of Different Curves', fontsize=14)

# Add a legend
ax.legend(loc='upper right')

# Add explanation text
explanation = """The winding number of a closed curve around a point p measures how many times 
the curve wraps around the point (positive for counterclockwise, negative for clockwise):

- Winding number = 1: The curve wraps once counterclockwise around p
- Winding number = 2: The curve wraps twice counterclockwise around p
- Winding number = 0: The curve doesn't fully wrap around p (or wraps equally in both directions)
- Winding number = -1: The curve wraps once clockwise around p

Mathematical definition: If γ(t) is a closed curve and p is a point not on γ, then the winding number is:
    w(γ, p) = (1/2π) ∫ dθ
where θ is the angle between the vector from p to γ(t) and the positive x-axis.

Applications: Winding numbers are used in complex analysis, topology, and vector field theory."""

# Add a box for the explanation
ax.text(0.02, 0.02, explanation, transform=ax.transAxes, fontsize=10,
        bbox=dict(facecolor='white', alpha=0.7))

# Set limits
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)

# Adjust layout and save
plt.tight_layout()
plt.savefig('/home/ubuntu/differential_geometry_textbook/visualizations/ch5_winding_numbers.png', dpi=300, bbox_inches='tight')
plt.close()

print("Visualization saved to: /home/ubuntu/differential_geometry_textbook/visualizations/ch5_winding_numbers.png")
