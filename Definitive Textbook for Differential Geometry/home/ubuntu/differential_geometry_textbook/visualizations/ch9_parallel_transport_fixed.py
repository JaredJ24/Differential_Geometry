import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create figure
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Create a simple surface to demonstrate parallel transport
def surface(u, v):
    # A curved surface (paraboloid)
    x = u
    y = v
    z = 0.5 * (u**2 + v**2)
    return x, y, z

# Create a grid of points on the surface
u = np.linspace(-1.5, 1.5, 20)
v = np.linspace(-1.5, 1.5, 20)
u_grid, v_grid = np.meshgrid(u, v)
x_grid, y_grid, z_grid = surface(u_grid, v_grid)

# Plot the surface
surf = ax.plot_surface(x_grid, y_grid, z_grid, color='lightblue', alpha=0.6, edgecolor='none')

# Define a path on the surface for parallel transport
t = np.linspace(0, 2*np.pi, 100)
radius = 1.0
path_u = radius * np.cos(t)
path_v = radius * np.sin(t)
path_x, path_y, path_z = surface(path_u, path_v)

# Plot the path
ax.plot(path_x, path_y, path_z, 'r-', linewidth=2, label='Path on Surface')

# Calculate tangent vectors to the surface
def tangent_vectors(u, v):
    # Partial derivatives with respect to u and v
    xu = 1
    yu = 0
    zu = u
    
    xv = 0
    yv = 1
    zv = v
    
    # Tangent vectors
    Tu = np.array([xu, yu, zu])
    Tv = np.array([xv, yv, zv])
    
    # Normal vector (cross product of tangent vectors)
    N = np.cross(Tu, Tv)
    N = N / np.linalg.norm(N)
    
    return Tu, Tv, N

# Sample points along the path for visualization
sample_indices = np.linspace(0, len(t)-1, 8, dtype=int)

# Create a vector to parallel transport (initially tangent to the path)
initial_vector = np.array([0, 1, 0])  # Start with a vector in the y-direction
initial_vector = initial_vector / np.linalg.norm(initial_vector)

# Simulate parallel transport (simplified for visualization)
transported_vectors = []
for i in sample_indices:
    u_val, v_val = path_u[i], path_v[i]
    Tu, Tv, N = tangent_vectors(u_val, v_val)
    
    # Project initial vector onto tangent plane
    dot_product_u = np.dot(initial_vector, Tu)
    dot_product_v = np.dot(initial_vector, Tv)
    
    # Create a vector in the tangent plane
    tangent_vector = dot_product_u * Tu + dot_product_v * Tv
    tangent_vector = tangent_vector / np.linalg.norm(tangent_vector)
    
    # Rotate the vector based on position (simulating parallel transport)
    angle = t[i]
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle), 0],
        [np.sin(angle), np.cos(angle), 0],
        [0, 0, 1]
    ])
    rotated_vector = np.dot(rotation_matrix, tangent_vector)
    
    # Project back to tangent plane
    projected_vector = rotated_vector - np.dot(rotated_vector, N) * N
    projected_vector = projected_vector / np.linalg.norm(projected_vector)
    
    transported_vectors.append(projected_vector)

# Draw the transported vectors using quiver instead of custom Arrow3D
scale = 0.3
for i, idx in enumerate(sample_indices):
    x, y, z = path_x[idx], path_y[idx], path_z[idx]
    vector = transported_vectors[i]
    
    # Draw the vector using quiver3D
    ax.quiver(x, y, z, 
              scale * vector[0], scale * vector[1], scale * vector[2],
              color='green', arrow_length_ratio=0.3, linewidth=2)
    
    # Add a point at the base of the vector
    ax.scatter([x], [y], [z], color='blue', s=50)

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Connections and Parallel Transport', fontsize=14)

# Add explanation text
explanation = """Parallel transport is a way to move vectors along a curve on a surface while keeping them "as parallel as possible".

Key concepts illustrated:
1. The green arrows represent a vector being parallel transported along the red circular path
2. Notice how the vector's direction changes as it moves around the surface
3. When the vector returns to its starting point, it may not point in the same direction - this is holonomy
4. The difference in orientation measures the curvature of the surface

A connection defines how to differentiate vector fields on a manifold, enabling:
- Parallel transport of vectors
- Definition of geodesics (paths of minimal length)
- Measurement of curvature

Applications include:
- General relativity (gravity as curvature of spacetime)
- Gauge theories in physics
- Computer graphics (texture mapping)
- Robotics (orientation control)"""

# Position the text explanation
ax.text2D(0.02, 0.02, explanation, transform=ax.transAxes, fontsize=10,
         bbox=dict(facecolor='white', alpha=0.7))

# Adjust view angle
ax.view_init(elev=30, azim=45)

# Save the figure
plt.tight_layout()
plt.savefig('/home/ubuntu/differential_geometry_textbook/visualizations/ch9_parallel_transport.png', dpi=300, bbox_inches='tight')
plt.close()

print("Visualization saved to: /home/ubuntu/differential_geometry_textbook/visualizations/ch9_parallel_transport.png")
