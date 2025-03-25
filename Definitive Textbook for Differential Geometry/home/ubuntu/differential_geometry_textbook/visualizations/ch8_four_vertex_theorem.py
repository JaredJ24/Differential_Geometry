import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d

# Create a 3D plotting class for arrows
class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0, 0), (0, 0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, self.axes.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        FancyArrowPatch.draw(self, renderer)

# Create figure
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

# Create an ellipsoid
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 50)
a, b, c = 2, 1.5, 1  # Semi-axes lengths
x = a * np.outer(np.cos(u), np.sin(v))
y = b * np.outer(np.sin(u), np.sin(v))
z = c * np.outer(np.ones_like(u), np.cos(v))

# Plot the ellipsoid surface
surf = ax.plot_surface(x, y, z, color='lightblue', alpha=0.7, edgecolor='none')

# Create a grid of points on the surface for principal curvature directions
u_sample = np.linspace(0, 2 * np.pi, 12)
v_sample = np.linspace(0, np.pi, 6)
u_grid, v_grid = np.meshgrid(u_sample, v_sample)
u_grid = u_grid.flatten()
v_grid = v_grid.flatten()

# Calculate points on the ellipsoid
x_grid = a * np.cos(u_grid) * np.sin(v_grid)
y_grid = b * np.sin(u_grid) * np.sin(v_grid)
z_grid = c * np.cos(v_grid)

# Calculate normal vectors at each point
normal_x = x_grid / a**2
normal_y = y_grid / b**2
normal_z = z_grid / c**2
norm = np.sqrt(normal_x**2 + normal_y**2 + normal_z**2)
normal_x /= norm
normal_y /= norm
normal_z /= norm

# Calculate principal curvature directions (simplified for visualization)
# For an ellipsoid, the principal directions are approximately along the parametric lines
k1_x = -a * np.sin(u_grid) * np.sin(v_grid)
k1_y = b * np.cos(u_grid) * np.sin(v_grid)
k1_z = np.zeros_like(u_grid)
norm_k1 = np.sqrt(k1_x**2 + k1_y**2 + k1_z**2)
k1_x = np.where(norm_k1 > 0, k1_x / norm_k1, 0)
k1_y = np.where(norm_k1 > 0, k1_y / norm_k1, 0)
k1_z = np.where(norm_k1 > 0, k1_z / norm_k1, 0)

k2_x = a * np.cos(u_grid) * np.cos(v_grid)
k2_y = b * np.sin(u_grid) * np.cos(v_grid)
k2_z = -c * np.sin(v_grid)
norm_k2 = np.sqrt(k2_x**2 + k2_y**2 + k2_z**2)
k2_x = np.where(norm_k2 > 0, k2_x / norm_k2, 0)
k2_y = np.where(norm_k2 > 0, k2_y / norm_k2, 0)
k2_z = np.where(norm_k2 > 0, k2_z / norm_k2, 0)

# Draw principal curvature directions at sample points
scale = 0.2
for i in range(len(u_grid)):
    # Skip some points for clarity
    if i % 3 != 0:
        continue
        
    # Draw normal vector
    normal_arrow = Arrow3D([x_grid[i], x_grid[i] + scale * normal_x[i]],
                          [y_grid[i], y_grid[i] + scale * normal_y[i]],
                          [z_grid[i], z_grid[i] + scale * normal_z[i]],
                          mutation_scale=10, lw=1, arrowstyle='-|>', color='black')
    ax.add_artist(normal_arrow)
    
    # Draw first principal direction
    k1_arrow = Arrow3D([x_grid[i], x_grid[i] + scale * k1_x[i]],
                       [y_grid[i], y_grid[i] + scale * k1_y[i]],
                       [z_grid[i], z_grid[i] + scale * k1_z[i]],
                       mutation_scale=10, lw=1, arrowstyle='-|>', color='red')
    ax.add_artist(k1_arrow)
    
    # Draw second principal direction
    k2_arrow = Arrow3D([x_grid[i], x_grid[i] + scale * k2_x[i]],
                       [y_grid[i], y_grid[i] + scale * k2_y[i]],
                       [z_grid[i], z_grid[i] + scale * k2_z[i]],
                       mutation_scale=10, lw=1, arrowstyle='-|>', color='blue')
    ax.add_artist(k2_arrow)

# Highlight points of extreme curvature
# Top and bottom points (maximum curvature)
ax.scatter([0], [0], [c], color='purple', s=100, label='Maximum Curvature')
ax.scatter([0], [0], [-c], color='purple', s=100)

# Points on the equator (minimum and saddle points)
ax.scatter([a], [0], [0], color='green', s=100, label='Minimum Curvature')
ax.scatter([-a], [0], [0], color='green', s=100)
ax.scatter([0], [b], [0], color='orange', s=100, label='Saddle Point')
ax.scatter([0], [-b], [0], color='orange', s=100)

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Four Vertex Theorem and Principal Curvatures', fontsize=14)

# Add a legend
ax.legend(loc='upper right')

# Add text explanation
explanation = """The Four Vertex Theorem states that any simple closed curve in the plane has at least four vertices,
where a vertex is a point of locally extreme curvature.

On a surface, curvature becomes more complex:
- Principal curvatures (κ₁, κ₂) are the maximum and minimum curvatures at each point
- Principal directions (shown as red and blue arrows) are perpendicular directions of principal curvature
- Normal vectors (black arrows) are perpendicular to the surface

Special points on this ellipsoid:
- Purple points: Maximum curvature (both principal curvatures have the same sign)
- Green points: Minimum curvature (both principal curvatures have the same sign)
- Orange points: Saddle points (principal curvatures have opposite signs)

The Gaussian curvature K = κ₁·κ₂ is:
- Positive at elliptic points (purple and green)
- Negative at hyperbolic points (orange)
- Zero at parabolic points (not highlighted)

This generalizes to the Tennis Ball Theorem: a smooth closed surface in R³ must have at least
four umbilical points, where the principal curvatures are equal."""

# Position the text explanation
ax.text2D(0.02, 0.02, explanation, transform=ax.transAxes, fontsize=10,
         bbox=dict(facecolor='white', alpha=0.7))

# Set equal aspect ratio
ax.set_box_aspect([1, 1, 1])

# Adjust view angle
ax.view_init(elev=20, azim=30)

# Save the figure
plt.tight_layout()
plt.savefig('/home/ubuntu/differential_geometry_textbook/visualizations/ch8_four_vertex_theorem.png', dpi=300, bbox_inches='tight')
plt.close()

print("Visualization saved to: /home/ubuntu/differential_geometry_textbook/visualizations/ch8_four_vertex_theorem.png")
