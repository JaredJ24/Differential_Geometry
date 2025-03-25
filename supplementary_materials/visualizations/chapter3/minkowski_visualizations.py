import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Set up figure and subplots
fig = plt.figure(figsize=(20, 15))
fig.suptitle('Minkowski Plane Visualizations', fontsize=20)

# 1. Light Cone and Vector Classification
ax1 = fig.add_subplot(221)
ax1.set_title('Light Cone and Vector Classification')
ax1.set_xlabel('x (space)')
ax1.set_ylabel('t (time)')
ax1.grid(True)
ax1.axhline(y=0, color='k', linestyle='-', alpha=0.3)
ax1.axvline(x=0, color='k', linestyle='-', alpha=0.3)
ax1.set_xlim(-5, 5)
ax1.set_ylim(-5, 5)

# Draw light cone
x = np.linspace(-5, 5, 100)
ax1.plot(x, x, 'r--', label='Lightlike (slope = 1)')
ax1.plot(x, -x, 'r--', label='Lightlike (slope = -1)')

# Fill regions
ax1.fill_between(x, x, 5, alpha=0.2, color='blue', label='Timelike (future)')
ax1.fill_between(x, -x, -5, alpha=0.2, color='blue', label='Timelike (past)')
ax1.fill_between(x, x, -x, where=(x > 0), alpha=0.2, color='green', label='Spacelike')
ax1.fill_between(x, -x, x, where=(x < 0), alpha=0.2, color='green')

# Example vectors
vectors = [
    ((0, 0), (3, 4), 'Timelike'),
    ((0, 0), (4, 3), 'Spacelike'),
    ((0, 0), (2, 2), 'Lightlike')
]

for start, end, label in vectors:
    ax1.annotate('', xy=end, xytext=start,
                arrowprops=dict(facecolor='black', shrink=0.05, width=1.5, headwidth=8))
    ax1.text(end[0]*1.1, end[1]*1.1, label)

ax1.legend(loc='upper left')

# 2. Lorentz Transformation (Hyperbolic Rotation)
ax2 = fig.add_subplot(222)
ax2.set_title('Lorentz Transformation (Hyperbolic Rotation)')
ax2.set_xlabel('x (space)')
ax2.set_ylabel('t (time)')
ax2.grid(True)
ax2.axhline(y=0, color='k', linestyle='-', alpha=0.3)
ax2.axvline(x=0, color='k', linestyle='-', alpha=0.3)
ax2.set_xlim(-5, 5)
ax2.set_ylim(-5, 5)

# Draw light cone
ax2.plot(x, x, 'r--', alpha=0.5)
ax2.plot(x, -x, 'r--', alpha=0.5)

# Draw hyperbolas (curves of constant Minkowski norm)
t = np.linspace(-5, 5, 1000)
for norm in [1, 2, 3]:
    # Timelike hyperbolas (t² - x² = norm²)
    valid_t = t[np.abs(t) >= norm]
    x_pos = np.sqrt(valid_t**2 - norm**2)
    x_neg = -np.sqrt(valid_t**2 - norm**2)
    ax2.plot(x_pos, valid_t, 'b-', alpha=0.7)
    ax2.plot(x_neg, valid_t, 'b-', alpha=0.7)
    
    # Spacelike hyperbolas (x² - t² = norm²)
    valid_x = t[np.abs(t) >= norm]
    t_pos = np.sqrt(valid_x**2 - norm**2)
    t_neg = -np.sqrt(valid_x**2 - norm**2)
    ax2.plot(valid_x, t_pos, 'g-', alpha=0.7)
    ax2.plot(valid_x, t_neg, 'g-', alpha=0.7)

# Original vector
original = (2, 1)  # Timelike vector
ax2.annotate('', xy=original, xytext=(0, 0),
            arrowprops=dict(facecolor='black', shrink=0.05, width=1.5, headwidth=8))
ax2.text(original[0]*1.1, original[1]*1.1, 'Original')

# Apply Lorentz transformations with different rapidities
rapidities = [0.5, 1.0, 1.5]
colors = ['purple', 'orange', 'brown']

for i, phi in enumerate(rapidities):
    # Lorentz transformation matrix
    L = np.array([
        [np.cosh(phi), np.sinh(phi)],
        [np.sinh(phi), np.cosh(phi)]
    ])
    
    # Apply transformation
    transformed = L @ np.array(original)
    
    # Draw transformed vector
    ax2.annotate('', xy=transformed, xytext=(0, 0),
                arrowprops=dict(facecolor=colors[i], shrink=0.05, width=1.5, headwidth=8))
    ax2.text(transformed[0]*1.1, transformed[1]*1.1, f'φ = {phi}')

# Add legend
ax2.text(3.5, 4, 'Timelike hyperbolas\n(t² - x² = const > 0)', color='blue')
ax2.text(-4.8, 4, 'Spacelike hyperbolas\n(x² - t² = const > 0)', color='green')

# 3. Timelike, Spacelike, and Lightlike Curves
ax3 = fig.add_subplot(223)
ax3.set_title('Timelike, Spacelike, and Lightlike Curves')
ax3.set_xlabel('x (space)')
ax3.set_ylabel('t (time)')
ax3.grid(True)
ax3.axhline(y=0, color='k', linestyle='-', alpha=0.3)
ax3.axvline(x=0, color='k', linestyle='-', alpha=0.3)
ax3.set_xlim(-5, 5)
ax3.set_ylim(-5, 5)

# Draw light cone
ax3.plot(x, x, 'r--', alpha=0.5)
ax3.plot(x, -x, 'r--', alpha=0.5)

# Timelike curve (vertical-ish)
t_timelike = np.linspace(0, 4, 100)
x_timelike = 0.5 * np.sin(t_timelike)
ax3.plot(x_timelike, t_timelike, 'b-', linewidth=2, label='Timelike curve')

# Spacelike curve (horizontal-ish)
x_spacelike = np.linspace(-3, 3, 100)
t_spacelike = 0.5 * np.sin(x_spacelike)
ax3.plot(x_spacelike, t_spacelike, 'g-', linewidth=2, label='Spacelike curve')

# Lightlike curve
t_lightlike = np.linspace(0, 4, 100)
x_lightlike = t_lightlike
ax3.plot(x_lightlike, t_lightlike, 'r-', linewidth=2, label='Lightlike curve')

# Draw tangent vectors
# Fixed: Using string identifiers instead of comparing arrays
curve_points = [
    ("timelike", 'blue', [20, 50, 80]),
    ("spacelike", 'green', [20, 50, 80]),
    ("lightlike", 'red', [20, 50, 80])
]

for curve_type, color, points in curve_points:
    for i in points:
        # Calculate tangent vector
        if curve_type == "timelike":
            x_point = x_timelike[i]
            t_point = t_timelike[i]
            dx = np.cos(t_timelike[i]) * 0.5
            dt = 1
        elif curve_type == "spacelike":
            x_point = x_spacelike[i]
            t_point = t_spacelike[i]
            dx = 1
            dt = np.cos(x_spacelike[i]) * 0.5
        else:  # lightlike
            x_point = x_lightlike[i]
            t_point = t_lightlike[i]
            dx = 1
            dt = 1
            
        # Normalize
        mag = np.sqrt(abs(dt**2 - dx**2)) if abs(dt**2 - dx**2) > 1e-10 else 1
        dx, dt = dx/mag, dt/mag
        
        # Draw tangent vector
        ax3.annotate('', 
                    xy=(x_point + dx, t_point + dt), 
                    xytext=(x_point, t_point),
                    arrowprops=dict(facecolor=color, shrink=0.05, width=1.5, headwidth=8))

ax3.legend(loc='upper left')

# 4. Hyperboloid Model of Hyperbolic Geometry
ax4 = fig.add_subplot(224, projection='3d')
ax4.set_title('Hyperboloid Model of Hyperbolic Geometry')
ax4.set_xlabel('x')
ax4.set_ylabel('y')
ax4.set_zlabel('t')
ax4.view_init(elev=30, azim=30)

# Generate hyperboloid
u = np.linspace(-2, 2, 30)
v = np.linspace(0, 2*np.pi, 30)
u, v = np.meshgrid(u, v)
x = np.sinh(u) * np.cos(v)
y = np.sinh(u) * np.sin(v)
t = np.cosh(u)

# Plot hyperboloid
ax4.plot_surface(x, y, t, alpha=0.3, color='blue')

# Draw some geodesics (intersections with planes through origin)
theta = np.linspace(0, 2*np.pi, 100)
for angle in [0, np.pi/4, np.pi/2, 3*np.pi/4]:
    r = np.linspace(1, 2, 100)
    x_geo = r * np.cos(angle)
    y_geo = r * np.sin(angle)
    t_geo = np.sqrt(1 + x_geo**2 + y_geo**2)
    ax4.plot(x_geo, y_geo, t_geo, 'r-', linewidth=2)

# Add text
ax4.text(0, 0, 3, "Upper sheet of hyperboloid\nt² - x² - y² = 1, t > 0", 
         color='blue', ha='center')
ax4.text(2, 2, 3, "Geodesics\n(intersections with planes\nthrough origin)", 
         color='red', ha='center')

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig('/home/ubuntu/MIT_Differential_Geometry_18.950_Textbook/supplementary_materials/visualizations/chapter3/minkowski_plane_visualizations.png', dpi=300)

# Create additional visualizations

# 1. Lorentz Transformation Animation
fig_lorentz = plt.figure(figsize=(10, 10))
ax_lorentz = fig_lorentz.add_subplot(111)
ax_lorentz.set_title('Lorentz Transformation Animation')
ax_lorentz.set_xlabel('x (space)')
ax_lorentz.set_ylabel('t (time)')
ax_lorentz.grid(True)
ax_lorentz.axhline(y=0, color='k', linestyle='-', alpha=0.3)
ax_lorentz.axvline(x=0, color='k', linestyle='-', alpha=0.3)
ax_lorentz.set_xlim(-5, 5)
ax_lorentz.set_ylim(-5, 5)

# Draw light cone
ax_lorentz.plot(x, x, 'r--', alpha=0.5)
ax_lorentz.plot(x, -x, 'r--', alpha=0.5)

# Draw grid in original frame
grid_size = 1
for i in range(-4, 5):
    ax_lorentz.plot([i*grid_size, i*grid_size], [-5, 5], 'b-', alpha=0.2)
    ax_lorentz.plot([-5, 5], [i*grid_size, i*grid_size], 'b-', alpha=0.2)

# Apply Lorentz transformation with rapidity 1.0
phi = 1.0
L = np.array([
    [np.cosh(phi), np.sinh(phi)],
    [np.sinh(phi), np.cosh(phi)]
])

# Draw transformed grid
for i in range(-4, 5):
    # Vertical lines
    points = np.array([[i*grid_size, -5], [i*grid_size, 5]]).T
    transformed = L @ points
    ax_lorentz.plot(transformed[0], transformed[1], 'r-', alpha=0.2)
    
    # Horizontal lines
    points = np.array([[-5, i*grid_size], [5, i*grid_size]]).T
    transformed = L @ points
    ax_lorentz.plot(transformed[0], transformed[1], 'r-', alpha=0.2)

# Add legend
ax_lorentz.text(3, 4, 'Original frame', color='blue')
ax_lorentz.text(3, 3, 'Transformed frame\n(rapidity φ = 1.0)', color='red')

plt.tight_layout()
plt.savefig('/home/ubuntu/MIT_Differential_Geometry_18.950_Textbook/supplementary_materials/visualizations/chapter3/lorentz_transformation_grid.png', dpi=300)

# 2. Minkowski Curvature Visualization
fig_curv = plt.figure(figsize=(10, 10))
ax_curv = fig_curv.add_subplot(111)
ax_curv.set_title('Minkowski Curvature of Hyperbola')
ax_curv.set_xlabel('x (space)')
ax_curv.set_ylabel('t (time)')
ax_curv.grid(True)
ax_curv.axhline(y=0, color='k', linestyle='-', alpha=0.3)
ax_curv.axvline(x=0, color='k', linestyle='-', alpha=0.3)
ax_curv.set_xlim(-5, 5)
ax_curv.set_ylim(-5, 5)

# Draw light cone
ax_curv.plot(x, x, 'r--', alpha=0.5)
ax_curv.plot(x, -x, 'r--', alpha=0.5)

# Draw hyperbola t² - x² = 1
t_hyp = np.linspace(1, 5, 1000)
x_pos = np.sqrt(t_hyp**2 - 1)
x_neg = -np.sqrt(t_hyp**2 - 1)
ax_curv.plot(x_pos, t_hyp, 'b-', linewidth=2, label='Hyperbola t² - x² = 1')
ax_curv.plot(x_neg, t_hyp, 'b-', linewidth=2)

# Draw tangent and normal vectors at selected points
s_values = [0.5, 1.0, 1.5, 2.0]
colors = ['purple', 'orange', 'green', 'brown']

for i, s in enumerate(s_values):
    # Parametric point on hyperbola
    t = np.cosh(s)
    x = np.sinh(s)
    
    # Tangent vector (normalized)
    dt = np.sinh(s)
    dx = np.cosh(s)
    
    # Normal vector (normalized)
    nt = np.cosh(s)
    nx = np.sinh(s)
    
    # Draw tangent vector
    ax_curv.annotate('', 
                    xy=(x + dx*0.5, t + dt*0.5), 
                    xytext=(x, t),
                    arrowprops=dict(facecolor=colors[i], shrink=0.05, width=1.5, headwidth=8))
    
    # Draw normal vector
    ax_curv.annotate('', 
                    xy=(x + nx*0.5, t + nt*0.5), 
                    xytext=(x, t),
                    arrowprops=dict(facecolor=colors[i], shrink=0.05, width=1.5, headwidth=8, alpha=0.5))
    
    # Label the point
    ax_curv.plot(x, t, 'o', color=colors[i])
    ax_curv.text(x+0.2, t+0.2, f's = {s}', color=colors[i])

# Add legend
ax_curv.text(3, 4, 'Tangent vectors (solid)', ha='center')
ax_curv.text(3, 3.5, 'Normal vectors (transparent)', ha='center')
ax_curv.text(3, 3, 'Minkowski curvature = 1\nat all points', ha='center')

plt.tight_layout()
plt.savefig('/home/ubuntu/MIT_Differential_Geometry_18.950_Textbook/supplementary_materials/visualizations/chapter3/minkowski_curvature.png', dpi=300)

# 3. Causal Structure Visualization
fig_causal = plt.figure(figsize=(10, 10))
ax_causal = fig_causal.add_subplot(111)
ax_causal.set_title('Causal Structure in Minkowski Plane')
ax_causal.set_xlabel('x (space)')
ax_causal.set_ylabel('t (time)')
ax_causal.grid(True)
ax_causal.axhline(y=0, color='k', linestyle='-', alpha=0.3)
ax_causal.axvline(x=0, color='k', linestyle='-', alpha=0.3)
ax_causal.set_xlim(-5, 5)
ax_causal.set_ylim(-5, 5)

# Draw light cone from origin
ax_causal.plot(x, x, 'r--', alpha=0.5)
ax_causal.plot(x, -x, 'r--', alpha=0.5)

# Mark origin as event A
ax_causal.plot(0, 0, 'ro', markersize=10)
ax_causal.text(0.2, 0.2, 'Event A', fontsize=12)

# Mark other events
events = [
    (1, 2, 'B', 'Can be influenced by A\nCan influence C'),
    (3, 1, 'C', 'Cannot be influenced by A\nCan influence D'),
    (2, 4, 'D', 'Can be influenced by A, B, and C'),
    (-2, 1, 'E', 'Cannot be influenced by A\nCannot influence A'),
    (-1, -2, 'F', 'Can influence A\nCannot be influenced by A')
]

for x_pos, t_pos, label, desc in events:
    ax_causal.plot(x_pos, t_pos, 'bo', markersize=8)
    ax_causal.text(x_pos+0.2, t_pos+0.2, label, fontsize=12)
    
    # Draw light cone from this event
    ax_causal.plot(x + x_pos, x + t_pos, 'r:', alpha=0.3)
    ax_causal.plot(x + x_pos, -x + t_pos, 'r:', alpha=0.3)
    
    # Add description
    if t_pos > 0:
        ax_causal.text(x_pos, t_pos+0.5, desc, fontsize=8, ha='center')
    else:
        ax_causal.text(x_pos, t_pos-0.8, desc, fontsize=8, ha='center')

# Add legend
ax_causal.text(-4.5, 4, 'Future light cone', color='red')
ax_causal.text(-4.5, 3.5, 'Past light cone', color='red')
ax_causal.text(-4.5, 3, 'Events', color='blue')

plt.tight_layout()
plt.savefig('/home/ubuntu/MIT_Differential_Geometry_18.950_Textbook/supplementary_materials/visualizations/chapter3/causal_structure.png', dpi=300)

print("Visualizations for Chapter 3 created successfully!")
