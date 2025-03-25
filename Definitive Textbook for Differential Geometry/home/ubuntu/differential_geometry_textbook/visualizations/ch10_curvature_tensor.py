import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

# Create figure
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

# Create a grid for the manifold
u = np.linspace(-1, 1, 30)
v = np.linspace(0, 2*np.pi, 30)
u_grid, v_grid = np.meshgrid(u, v)

# Define a 2D manifold embedded in 3D (a torus)
def torus(u, v, R=1.5, r=0.5):
    x = (R + r*np.cos(v)) * np.cos(u*np.pi)
    y = (R + r*np.cos(v)) * np.sin(u*np.pi)
    z = r * np.sin(v)
    return x, y, z

# Calculate the torus coordinates
x_grid, y_grid, z_grid = torus(u_grid, v_grid)

# Plot the torus surface
surf = ax.plot_surface(x_grid, y_grid, z_grid, cmap=cm.viridis, alpha=0.7, 
                       linewidth=0, antialiased=True)

# Define a function to compute Gaussian curvature on the torus
def gaussian_curvature(u, v, R=1.5, r=0.5):
    # For a torus, the Gaussian curvature is:
    # K = cos(v) / (r * (R + r*cos(v)))
    return np.cos(v) / (r * (R + r*np.cos(v)))

# Calculate curvature values
K_values = gaussian_curvature(u_grid, v_grid)

# Create a second plot for the curvature visualization
fig2 = plt.figure(figsize=(12, 10))
ax2 = fig2.add_subplot(111, projection='3d')

# Plot the torus with color representing curvature
surf2 = ax2.plot_surface(x_grid, y_grid, z_grid, facecolors=cm.coolwarm(plt.Normalize(-1, 1)(K_values)),
                        linewidth=0, antialiased=True)

# Add a colorbar
m = cm.ScalarMappable(cmap=cm.coolwarm, norm=plt.Normalize(-1, 1))
m.set_array(K_values)
cbar = fig2.colorbar(m, ax=ax2, shrink=0.6, aspect=10)
cbar.set_label('Gaussian Curvature', fontsize=12)

# Set labels and title
ax2.set_xlabel('X', fontsize=12)
ax2.set_ylabel('Y', fontsize=12)
ax2.set_zlabel('Z', fontsize=12)
ax2.set_title('Curvature Tensor Visualization: Gaussian Curvature on a Torus', fontsize=14)

# Add explanation text
explanation = """Curvature Tensors in Differential Geometry

The Riemann curvature tensor measures how parallel transport around an infinitesimal loop fails to return a vector to its original orientation.

Key concepts illustrated:
1. The torus surface is colored according to its Gaussian curvature (K = κ₁κ₂)
2. Red regions have positive curvature (like a sphere)
3. Blue regions have negative curvature (like a saddle)
4. Green regions have near-zero curvature (like a plane)

The Gaussian curvature is an intrinsic property of the surface - it can be measured by beings living on the surface without reference to the embedding space.

Related tensors:
- Riemann tensor: The full curvature tensor with components Rᵢⱼₖₗ
- Ricci tensor: A contraction of the Riemann tensor (Rᵢⱼ = Rᵏᵢₖⱼ)
- Scalar curvature: A further contraction (R = gᵢʲRᵢⱼ)

Applications include:
- General relativity (Einstein field equations)
- Differential topology (Gauss-Bonnet theorem)
- Computer graphics (mesh processing)
- Machine learning (manifold learning)"""

# Position the text explanation
ax2.text2D(0.02, 0.02, explanation, transform=ax2.transAxes, fontsize=10,
         bbox=dict(facecolor='white', alpha=0.7))

# Adjust view angle
ax2.view_init(elev=30, azim=45)

# Save the figure
plt.tight_layout()
plt.savefig('/home/ubuntu/differential_geometry_textbook/visualizations/ch10_curvature_tensor.png', dpi=300, bbox_inches='tight')
plt.close(fig)
plt.close(fig2)

print("Visualization saved to: /home/ubuntu/differential_geometry_textbook/visualizations/ch10_curvature_tensor.png")
