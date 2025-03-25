import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d

# Create figure
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

# Create a helix (space curve)
t = np.linspace(0, 4*np.pi, 200)
a, b = 1.0, 0.3  # radius and pitch
x = a*np.cos(t)
y = a*np.sin(t)
z = b*t

# Plot the curve
ax.plot(x, y, z, 'b-', linewidth=2, label='Space Curve')

# Calculate Frenet frame at selected points
points_to_show = [25, 75, 125, 175]  # Indices of points to show Frenet frame
colors = ['r', 'g', 'b']  # Colors for T, N, B

for i in points_to_show:
    # Calculate derivatives
    dt = t[1] - t[0]
    
    # First derivatives (velocity vector)
    dx_dt = np.gradient(x, dt)[i]
    dy_dt = np.gradient(y, dt)[i]
    dz_dt = np.gradient(z, dt)[i]
    
    # Tangent vector (T)
    velocity = np.array([dx_dt, dy_dt, dz_dt])
    speed = np.linalg.norm(velocity)
    tangent = velocity / speed
    
    # Second derivatives (acceleration vector)
    d2x_dt2 = np.gradient(np.gradient(x, dt), dt)[i]
    d2y_dt2 = np.gradient(np.gradient(y, dt), dt)[i]
    d2z_dt2 = np.gradient(np.gradient(z, dt), dt)[i]
    
    acceleration = np.array([d2x_dt2, d2y_dt2, d2z_dt2])
    
    # Normal component of acceleration
    acc_parallel = np.dot(acceleration, tangent) * tangent
    acc_normal = acceleration - acc_parallel
    
    # Normal vector (N)
    normal_magnitude = np.linalg.norm(acc_normal)
    if normal_magnitude < 1e-10:  # Avoid division by zero
        normal = np.array([0, 0, 0])
    else:
        normal = acc_normal / normal_magnitude
    
    # Binormal vector (B)
    binormal = np.cross(tangent, normal)
    
    # Calculate curvature and torsion
    curvature = np.linalg.norm(acc_normal) / (speed**2)
    
    # For torsion, we need third derivatives
    d3x_dt3 = np.gradient(np.gradient(np.gradient(x, dt), dt), dt)[i]
    d3y_dt3 = np.gradient(np.gradient(np.gradient(y, dt), dt), dt)[i]
    d3z_dt3 = np.gradient(np.gradient(np.gradient(z, dt), dt), dt)[i]
    
    jerk = np.array([d3x_dt3, d3y_dt3, d3z_dt3])
    
    # Torsion formula: τ = (v × a) · j / |v × a|²
    v_cross_a = np.cross(velocity, acceleration)
    v_cross_a_magnitude_squared = np.dot(v_cross_a, v_cross_a)
    
    if v_cross_a_magnitude_squared < 1e-10:  # Avoid division by zero
        torsion = 0
    else:
        torsion = np.dot(v_cross_a, jerk) / v_cross_a_magnitude_squared
    
    # Scale vectors for visualization
    scale = 0.3
    
    # Draw Frenet frame at the selected point
    point = np.array([x[i], y[i], z[i]])
    
    # Vectors of the Frenet frame
    vectors = [tangent, normal, binormal]
    vector_names = ['T', 'N', 'B']
    
    # Draw each vector
    for j, (vector, name, color) in enumerate(zip(vectors, vector_names, colors)):
        end_point = point + scale * vector
        ax.quiver(point[0], point[1], point[2], 
                  scale * vector[0], scale * vector[1], scale * vector[2],
                  color=color, arrow_length_ratio=0.2)
        
        # Add text label for each vector
        text_pos = point + 1.2 * scale * vector
        ax.text(text_pos[0], text_pos[1], text_pos[2], name, color=color, fontsize=12)
    
    # Add text showing curvature and torsion
    ax.text(point[0], point[1], point[2] + 0.2, 
            f'κ = {curvature:.2f}\nτ = {torsion:.2f}', 
            color='black', fontsize=10,
            bbox=dict(facecolor='white', alpha=0.7))

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
ax.set_title('Frenet Frame for Space Curves', fontsize=14)

# Add explanation text
explanation = """The Frenet Frame for a space curve consists of three orthonormal vectors:

1. Tangent vector (T): Points in the direction of motion
   - T = v/|v| where v is the velocity vector

2. Normal vector (N): Points toward the center of curvature
   - N = a⊥/|a⊥| where a⊥ is the normal component of acceleration

3. Binormal vector (B): Perpendicular to both T and N
   - B = T × N

Curvature (κ) measures how sharply the curve bends:
   - κ = |a⊥|/|v|²

Torsion (τ) measures how much the curve twists out of the osculating plane:
   - τ = ((v × a) · j) / |v × a|² where j is the jerk vector (third derivative)"""

# Add the explanation as a text box in the figure
plt.figtext(0.5, 0.01, explanation, ha='center', fontsize=10, 
            bbox=dict(facecolor='white', alpha=0.8), 
            wrap=True)

# Adjust the view
ax.view_init(elev=20, azim=30)
ax.set_box_aspect([1,1,0.5])

# Adjust layout and save
plt.tight_layout(rect=[0, 0.15, 1, 1])  # Make room for the explanation text
plt.savefig('/home/ubuntu/differential_geometry_textbook/visualizations/ch4_frenet_frame_space_curve.png', dpi=300, bbox_inches='tight')
plt.close()

print("Visualization saved to: /home/ubuntu/differential_geometry_textbook/visualizations/ch4_frenet_frame_space_curve.png")
