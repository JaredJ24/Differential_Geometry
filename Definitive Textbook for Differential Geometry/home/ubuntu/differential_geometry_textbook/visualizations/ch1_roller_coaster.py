import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        FancyArrowPatch.draw(self, renderer)

# Create a helix curve (like a roller coaster)
t = np.linspace(0, 4*np.pi, 100)
radius = 1
height_scale = 0.5

# Parametric equation of a helix
x = radius * np.cos(t)
y = radius * np.sin(t)
z = height_scale * t

# Create figure and 3D axis
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the curve
ax.plot(x, y, z, 'b-', linewidth=2, label='Roller Coaster Track')

# Calculate tangent, normal, and binormal vectors at selected points
points_to_show = [10, 30, 50, 70, 90]  # Indices of points to show Frenet frame

for i in points_to_show:
    # Calculate derivatives
    dt = t[1] - t[0]
    dx_dt = np.gradient(x, dt)[i]
    dy_dt = np.gradient(y, dt)[i]
    dz_dt = np.gradient(z, dt)[i]
    
    # Tangent vector (T)
    tangent = np.array([dx_dt, dy_dt, dz_dt])
    tangent = tangent / np.linalg.norm(tangent)
    
    # Second derivatives
    d2x_dt2 = np.gradient(np.gradient(x, dt), dt)[i]
    d2y_dt2 = np.gradient(np.gradient(y, dt), dt)[i]
    d2z_dt2 = np.gradient(np.gradient(z, dt), dt)[i]
    
    second_deriv = np.array([d2x_dt2, d2y_dt2, d2z_dt2])
    
    # Normal vector (N)
    curvature_vector = second_deriv - np.dot(second_deriv, tangent) * tangent
    normal = curvature_vector / np.linalg.norm(curvature_vector)
    
    # Binormal vector (B)
    binormal = np.cross(tangent, normal)
    
    # Scale vectors for visualization
    scale = 0.3
    
    # Draw Frenet frame at the selected point
    point = np.array([x[i], y[i], z[i]])
    
    # Tangent vector (red)
    a = Arrow3D([point[0], point[0] + scale * tangent[0]],
                [point[1], point[1] + scale * tangent[1]],
                [point[2], point[2] + scale * tangent[2]],
                mutation_scale=15, lw=2, arrowstyle='->', color='r')
    ax.add_artist(a)
    
    # Normal vector (green)
    a = Arrow3D([point[0], point[0] + scale * normal[0]],
                [point[1], point[1] + scale * normal[1]],
                [point[2], point[2] + scale * normal[2]],
                mutation_scale=15, lw=2, arrowstyle='->', color='g')
    ax.add_artist(a)
    
    # Binormal vector (blue)
    a = Arrow3D([point[0], point[0] + scale * binormal[0]],
                [point[1], point[1] + scale * binormal[1]],
                [point[2], point[2] + scale * binormal[2]],
                mutation_scale=15, lw=2, arrowstyle='->', color='b')
    ax.add_artist(a)

# Add a legend
from matplotlib.lines import Line2D
custom_lines = [Line2D([0], [0], color='r', lw=2),
                Line2D([0], [0], color='g', lw=2),
                Line2D([0], [0], color='b', lw=2)]
ax.legend(custom_lines, ['Tangent (T)', 'Normal (N)', 'Binormal (B)'], loc='upper right')

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Roller Coaster Parametrization with Frenet Frame', fontsize=14)

# Add text annotation explaining the Frenet frame
ax.text2D(0.05, 0.95, "The Frenet Frame provides a natural moving reference frame along a curve:\n" +
          "- Tangent vector (T): Points in the direction of motion\n" +
          "- Normal vector (N): Points toward the center of curvature\n" +
          "- Binormal vector (B): Perpendicular to both T and N",
          transform=ax.transAxes, fontsize=10, bbox=dict(facecolor='white', alpha=0.7))

# Set equal aspect ratio
ax.set_box_aspect([1,1,0.5])

# Save the figure
plt.savefig('/home/ubuntu/differential_geometry_textbook/visualizations/ch1_roller_coaster_frenet_frame.png', dpi=300, bbox_inches='tight')
plt.close()

print("Visualization saved to: /home/ubuntu/differential_geometry_textbook/visualizations/ch1_roller_coaster_frenet_frame.png")
