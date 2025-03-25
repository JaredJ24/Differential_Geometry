import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Create figure
fig, ax = plt.figure(figsize=(10, 8)), plt.subplot(111)

# Set up the Minkowski plane
x_range = np.linspace(-3, 3, 1000)
y_range = np.linspace(-3, 3, 1000)
X, Y = np.meshgrid(x_range, y_range)

# Light cone equation: x^2 - y^2 = 0 (45-degree lines)
# We'll color the regions based on their classification

# Create a mask for different regions
timelike_future = Y > np.abs(X)  # Above the light cone
timelike_past = Y < -np.abs(X)   # Below the light cone
spacelike = np.abs(Y) < np.abs(X)  # Left and right of the light cone

# Create a colored background
background = np.zeros((len(y_range), len(x_range), 3))
background[timelike_future] = [0.9, 0.7, 0.7]  # Light red for future timelike
background[timelike_past] = [0.7, 0.7, 0.9]    # Light blue for past timelike
background[spacelike] = [0.7, 0.9, 0.7]        # Light green for spacelike

# Plot the background
ax.imshow(background, extent=[-3, 3, -3, 3], origin='lower', aspect='auto', alpha=0.5)

# Draw the light cone lines
ax.plot(x_range, x_range, 'k-', linewidth=2)  # Upper right
ax.plot(x_range, -x_range, 'k-', linewidth=2)  # Lower right
ax.plot(-x_range, x_range, 'k-', linewidth=2)  # Upper left
ax.plot(-x_range, -x_range, 'k-', linewidth=2)  # Lower left

# Draw the axes
ax.axhline(y=0, color='k', linestyle='-', alpha=0.3)
ax.axvline(x=0, color='k', linestyle='-', alpha=0.3)

# Add labels for the regions
ax.text(0, 2, "Future Timelike\n(causally connected to future)", 
        ha='center', va='center', fontsize=10, bbox=dict(facecolor='white', alpha=0.7))
ax.text(0, -2, "Past Timelike\n(causally connected to past)", 
        ha='center', va='center', fontsize=10, bbox=dict(facecolor='white', alpha=0.7))
ax.text(2, 0, "Spacelike\n(causally disconnected)", 
        ha='center', va='center', fontsize=10, bbox=dict(facecolor='white', alpha=0.7))
ax.text(-2, 0, "Spacelike\n(causally disconnected)", 
        ha='center', va='center', fontsize=10, bbox=dict(facecolor='white', alpha=0.7))

# Add vectors to illustrate different types
# Timelike vector (future-directed)
ax.arrow(0, 0, 0, 1.5, head_width=0.1, head_length=0.2, fc='red', ec='red', linewidth=2)
ax.text(0.2, 0.75, "Timelike\nvector", color='red')

# Spacelike vector
ax.arrow(0, 0, 1.5, 0, head_width=0.1, head_length=0.2, fc='green', ec='green', linewidth=2)
ax.text(0.75, 0.2, "Spacelike\nvector", color='green')

# Lightlike/null vector
ax.arrow(0, 0, 1, 1, head_width=0.1, head_length=0.2, fc='blue', ec='blue', linewidth=2)
ax.text(0.6, 0.6, "Lightlike\nvector", color='blue')

# Set labels and title
ax.set_xlabel('x (space)')
ax.set_ylabel('t (time)')
ax.set_title('Light Cone in Minkowski Space', fontsize=14)

# Add explanation text
explanation = """In Minkowski spacetime:
- Timelike vectors (inside the light cone) have ds² < 0
- Spacelike vectors (outside the light cone) have ds² > 0
- Lightlike vectors (on the light cone) have ds² = 0

Where ds² = -dt² + dx² is the spacetime interval.

Events in the future light cone can be causally influenced by the origin.
Events in the past light cone can causally influence the origin.
Events in spacelike regions cannot have causal relationships with the origin."""

# Add a box for the explanation
ax.text(0.02, 0.02, explanation, transform=ax.transAxes, fontsize=10,
        bbox=dict(facecolor='white', alpha=0.7))

# Set equal aspect ratio and limits
ax.set_aspect('equal')
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)

# Adjust layout and save
plt.tight_layout()
plt.savefig('/home/ubuntu/differential_geometry_textbook/visualizations/ch3_light_cone.png', dpi=300, bbox_inches='tight')
plt.close()

print("Visualization saved to: /home/ubuntu/differential_geometry_textbook/visualizations/ch3_light_cone.png")
