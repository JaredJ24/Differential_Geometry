import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
from matplotlib import cm

# Set up figure for multiple visualizations
fig = plt.figure(figsize=(20, 15))
fig.suptitle('Frenet Theory and Higher-Dimensional Curves Visualizations', fontsize=20)

# 1. Helix with Frenet Frame
ax1 = fig.add_subplot(221, projection='3d')
ax1.set_title('Helix with Frenet Frame')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')

# Parameters for the helix
a = 1  # radius
b = 0.2  # pitch
t = np.linspace(0, 4*np.pi, 100)

# Helix parametrization
x = a * np.cos(t)
y = a * np.sin(t)
z = b * t

# Plot the helix
ax1.plot(x, y, z, 'b-', linewidth=2)

# Calculate Frenet frame at selected points
points = [10, 30, 50, 70, 90]  # Indices of points to show Frenet frame

for i in points:
    # Position
    pos = np.array([x[i], y[i], z[i]])
    
    # Tangent vector (normalized)
    dx = -a * np.sin(t[i])
    dy = a * np.cos(t[i])
    dz = b
    tangent = np.array([dx, dy, dz])
    tangent = tangent / np.linalg.norm(tangent)
    
    # Normal vector (normalized)
    d2x = -a * np.cos(t[i])
    d2y = -a * np.sin(t[i])
    d2z = 0
    normal = np.array([d2x, d2y, d2z])
    normal = normal / np.linalg.norm(normal)
    
    # Binormal vector (cross product of T and N)
    binormal = np.cross(tangent, normal)
    binormal = binormal / np.linalg.norm(binormal)
    
    # Scale for visualization
    scale = 0.3
    
    # Plot Frenet frame
    ax1.quiver(pos[0], pos[1], pos[2], scale*tangent[0], scale*tangent[1], scale*tangent[2], 
               color='r', arrow_length_ratio=0.2)
    ax1.quiver(pos[0], pos[1], pos[2], scale*normal[0], scale*normal[1], scale*normal[2], 
               color='g', arrow_length_ratio=0.2)
    ax1.quiver(pos[0], pos[1], pos[2], scale*binormal[0], scale*binormal[1], scale*binormal[2], 
               color='b', arrow_length_ratio=0.2)

# Add legend
ax1.text(1.5, 0, 2, 'Tangent (T)', color='r')
ax1.text(1.5, 0, 1.7, 'Normal (N)', color='g')
ax1.text(1.5, 0, 1.4, 'Binormal (B)', color='b')

# 2. Osculating, Normal, and Rectifying Planes
ax2 = fig.add_subplot(222, projection='3d')
ax2.set_title('Osculating, Normal, and Rectifying Planes')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')

# Plot the helix
ax2.plot(x, y, z, 'b-', linewidth=2)

# Choose a point to show the planes
i = 50
pos = np.array([x[i], y[i], z[i]])

# Calculate Frenet frame
dx = -a * np.sin(t[i])
dy = a * np.cos(t[i])
dz = b
tangent = np.array([dx, dy, dz])
tangent = tangent / np.linalg.norm(tangent)

d2x = -a * np.cos(t[i])
d2y = -a * np.sin(t[i])
d2z = 0
normal = np.array([d2x, d2y, d2z])
normal = normal / np.linalg.norm(normal)

binormal = np.cross(tangent, normal)
binormal = binormal / np.linalg.norm(binormal)

# Create grid for planes
grid_size = 0.5
xx, yy = np.meshgrid(np.linspace(-grid_size, grid_size, 10), 
                     np.linspace(-grid_size, grid_size, 10))

# Osculating plane (spanned by T and N)
zz_osc = np.zeros_like(xx)
for i in range(xx.shape[0]):
    for j in range(xx.shape[1]):
        point = pos + xx[i,j]*tangent + yy[i,j]*normal
        zz_osc[i,j] = point[2]

# Normal plane (spanned by N and B)
zz_norm = np.zeros_like(xx)
for i in range(xx.shape[0]):
    for j in range(xx.shape[1]):
        point = pos + xx[i,j]*normal + yy[i,j]*binormal
        zz_norm[i,j] = point[2]

# Rectifying plane (spanned by T and B)
zz_rect = np.zeros_like(xx)
for i in range(xx.shape[0]):
    for j in range(xx.shape[1]):
        point = pos + xx[i,j]*tangent + yy[i,j]*binormal
        zz_rect[i,j] = point[2]

# Plot planes
xx_osc = pos[0] + xx*tangent[0] + yy*normal[0]
yy_osc = pos[1] + xx*tangent[1] + yy*normal[1]
ax2.plot_surface(xx_osc, yy_osc, zz_osc, alpha=0.3, color='r')

xx_norm = pos[0] + xx*normal[0] + yy*binormal[0]
yy_norm = pos[1] + xx*normal[1] + yy*binormal[1]
ax2.plot_surface(xx_norm, yy_norm, zz_norm, alpha=0.3, color='g')

xx_rect = pos[0] + xx*tangent[0] + yy*binormal[0]
yy_rect = pos[1] + xx*tangent[1] + yy*binormal[1]
ax2.plot_surface(xx_rect, yy_rect, zz_rect, alpha=0.3, color='b')

# Add legend
ax2.text(1.5, 0, 2, 'Osculating Plane (T,N)', color='r')
ax2.text(1.5, 0, 1.7, 'Normal Plane (N,B)', color='g')
ax2.text(1.5, 0, 1.4, 'Rectifying Plane (T,B)', color='b')

# 3. Curvature and Torsion of Different Curves
ax3 = fig.add_subplot(223, projection='3d')
ax3.set_title('Curvature and Torsion of Different Curves')
ax3.set_xlabel('X')
ax3.set_ylabel('Y')
ax3.set_zlabel('Z')

# Straight line
t_line = np.linspace(0, 2, 100)
x_line = t_line
y_line = np.zeros_like(t_line)
z_line = np.zeros_like(t_line)
ax3.plot(x_line, y_line, z_line, 'k-', linewidth=2, label='Line (κ=0, τ undefined)')

# Circle
t_circle = np.linspace(0, 2*np.pi, 100)
x_circle = np.cos(t_circle)
y_circle = np.sin(t_circle)
z_circle = np.zeros_like(t_circle)
ax3.plot(x_circle, y_circle, z_circle, 'r-', linewidth=2, label='Circle (κ=1, τ=0)')

# Helix
t_helix = np.linspace(0, 4*np.pi, 100)
x_helix = np.cos(t_helix)
y_helix = np.sin(t_helix)
z_helix = 0.5 * t_helix
ax3.plot(x_helix, y_helix, z_helix, 'g-', linewidth=2, label='Helix (κ,τ constant)')

# General curve (trefoil knot)
t_trefoil = np.linspace(0, 2*np.pi, 100)
x_trefoil = np.sin(t_trefoil) + 2*np.sin(2*t_trefoil)
y_trefoil = np.cos(t_trefoil) - 2*np.cos(2*t_trefoil)
z_trefoil = -np.sin(3*t_trefoil)
ax3.plot(x_trefoil, y_trefoil, z_trefoil, 'b-', linewidth=2, label='Trefoil (κ,τ varying)')

ax3.legend(loc='upper left')

# 4. Fundamental Theorem Visualization
ax4 = fig.add_subplot(224, projection='3d')
ax4.set_title('Fundamental Theorem: Curves with Prescribed Curvature and Torsion')
ax4.set_xlabel('X')
ax4.set_ylabel('Y')
ax4.set_zlabel('Z')

# Function to generate curve from curvature and torsion
def generate_curve(kappa, tau, s_values):
    # Initial Frenet frame
    T = np.array([1.0, 0.0, 0.0])
    N = np.array([0.0, 1.0, 0.0])
    B = np.array([0.0, 0.0, 1.0])
    
    # Initial position
    r = np.array([0.0, 0.0, 0.0])
    
    # Arrays to store curve points and frames
    curve = [r.copy()]
    
    # Step size
    ds = s_values[1] - s_values[0]
    
    # Generate curve using Frenet-Serret formulas
    for i in range(1, len(s_values)):
        s = s_values[i-1]
        
        # Update Frenet frame using Frenet-Serret formulas
        T_new = T + ds * (kappa(s) * N)
        N_new = N + ds * (-kappa(s) * T + tau(s) * B)
        B_new = B + ds * (-tau(s) * N)
        
        # Normalize to prevent drift
        T = T_new / np.linalg.norm(T_new)
        N = N_new / np.linalg.norm(N_new)
        B = B_new / np.linalg.norm(B_new)
        
        # Ensure orthogonality
        N = np.cross(B, T)
        B = np.cross(T, N)
        
        # Update position
        r = r + ds * T
        
        # Store curve point
        curve.append(r.copy())
    
    return np.array(curve)

# Generate curves with different curvature and torsion functions
s = np.linspace(0, 10, 500)

# Constant curvature and torsion (helix)
kappa1 = lambda s: 1.0
tau1 = lambda s: 0.5
curve1 = generate_curve(kappa1, tau1, s)

# Varying curvature, constant torsion
kappa2 = lambda s: 1.0 + 0.5*np.sin(s)
tau2 = lambda s: 0.5
curve2 = generate_curve(kappa2, tau2, s)

# Constant curvature, varying torsion
kappa3 = lambda s: 1.0
tau3 = lambda s: 0.5 + 0.3*np.cos(s)
curve3 = generate_curve(kappa3, tau3, s)

# Both varying
kappa4 = lambda s: 1.0 + 0.5*np.sin(s)
tau4 = lambda s: 0.5 + 0.3*np.cos(s)
curve4 = generate_curve(kappa4, tau4, s)

# Plot curves
ax4.plot(curve1[:,0], curve1[:,1], curve1[:,2], 'r-', linewidth=2, 
         label='κ=1, τ=0.5')
ax4.plot(curve2[:,0], curve2[:,1], curve2[:,2], 'g-', linewidth=2, 
         label='κ=1+0.5sin(s), τ=0.5')
ax4.plot(curve3[:,0], curve3[:,1], curve3[:,2], 'b-', linewidth=2, 
         label='κ=1, τ=0.5+0.3cos(s)')
ax4.plot(curve4[:,0], curve4[:,1], curve4[:,2], 'y-', linewidth=2, 
         label='κ=1+0.5sin(s), τ=0.5+0.3cos(s)')

ax4.legend(loc='upper left')

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig('/home/ubuntu/MIT_Differential_Geometry_18.950_Textbook/supplementary_materials/visualizations/chapter4/frenet_theory_visualizations.png', dpi=300)

# Create additional visualizations

# 1. Bertrand and Mannheim Curves
fig_special = plt.figure(figsize=(20, 10))
fig_special.suptitle('Special Curves in Differential Geometry', fontsize=20)

# Bertrand Curves
ax_bertrand = fig_special.add_subplot(121, projection='3d')
ax_bertrand.set_title('Bertrand Curves')
ax_bertrand.set_xlabel('X')
ax_bertrand.set_ylabel('Y')
ax_bertrand.set_zlabel('Z')

# Parameters for Bertrand curve
a = 1.0  # constant in the relation aκ + bτ = 1
b = 0.5  # constant in the relation aκ + bτ = 1

# Generate a curve with curvature and torsion satisfying aκ + bτ = 1
def kappa_bertrand(s):
    return 0.5 + 0.2*np.sin(s)

def tau_bertrand(s):
    # From aκ + bτ = 1, we get τ = (1 - aκ)/b
    return (1 - a*kappa_bertrand(s))/b

# Generate Bertrand curve
s_bertrand = np.linspace(0, 10, 500)
bertrand_curve = generate_curve(kappa_bertrand, tau_bertrand, s_bertrand)

# Generate Bertrand mate
bertrand_mate = []
for i in range(len(s_bertrand)):
    s = s_bertrand[i]
    
    # Calculate Frenet frame at this point
    if i > 0:
        T = (bertrand_curve[i] - bertrand_curve[i-1]) / np.linalg.norm(bertrand_curve[i] - bertrand_curve[i-1])
        
        # Approximate curvature and torsion
        kappa = kappa_bertrand(s)
        tau = tau_bertrand(s)
        
        # Calculate normal and binormal
        if i > 1:
            # Use finite differences to approximate derivatives
            T_prev = (bertrand_curve[i-1] - bertrand_curve[i-2]) / np.linalg.norm(bertrand_curve[i-1] - bertrand_curve[i-2])
            dT = (T - T_prev) / (s_bertrand[i] - s_bertrand[i-1])
            
            # Normal vector
            N = dT / np.linalg.norm(dT) if np.linalg.norm(dT) > 1e-10 else np.array([0, 1, 0])
            
            # Binormal vector
            B = np.cross(T, N)
            B = B / np.linalg.norm(B)
            
            # Ensure orthogonality
            N = np.cross(B, T)
            
            # Bertrand mate is at a constant distance along the normal
            c = a / np.sqrt(a*a + b*b)  # constant distance
            mate_point = bertrand_curve[i] + c * N
            bertrand_mate.append(mate_point)

# Convert to numpy array
bertrand_mate = np.array(bertrand_mate)

# Plot Bertrand curve and its mate
ax_bertrand.plot(bertrand_curve[:,0], bertrand_curve[:,1], bertrand_curve[:,2], 'r-', linewidth=2, 
                 label='Bertrand Curve')
if len(bertrand_mate) > 0:
    ax_bertrand.plot(bertrand_mate[:,0], bertrand_mate[:,1], bertrand_mate[:,2], 'g-', linewidth=2, 
                     label='Bertrand Mate')

    # Draw some connecting lines
    for i in range(0, len(bertrand_mate), 50):
        if i < len(bertrand_curve):
            ax_bertrand.plot([bertrand_curve[i,0], bertrand_mate[i,0]], 
                             [bertrand_curve[i,1], bertrand_mate[i,1]], 
                             [bertrand_curve[i,2], bertrand_mate[i,2]], 'k--', alpha=0.3)

ax_bertrand.legend()

# Mannheim Curves
ax_mannheim = fig_special.add_subplot(122, projection='3d')
ax_mannheim.set_title('Mannheim Curves')
ax_mannheim.set_xlabel('X')
ax_mannheim.set_ylabel('Y')
ax_mannheim.set_zlabel('Z')

# Parameters for Mannheim curve
c = 0.5  # constant in the relation κ = c(κ² + τ²)

# Generate a curve with curvature and torsion satisfying κ = c(κ² + τ²)
def tau_mannheim(s):
    return 0.5 + 0.2*np.sin(s)

def kappa_mannheim(s):
    # From κ = c(κ² + τ²), we get κ(1 - cκ) = cτ²
    # This is a quadratic equation in κ: cκ² - κ + cτ² = 0
    # Using quadratic formula: κ = (1 ± √(1 - 4c²τ²))/(2c)
    # We take the positive root for physical relevance
    tau = tau_mannheim(s)
    discriminant = 1 - 4*c*c*tau*tau
    if discriminant < 0:
        return 1/(2*c)  # Limiting value when discriminant approaches 0
    else:
        return (1 + np.sqrt(discriminant))/(2*c)

# Generate Mannheim curve
s_mannheim = np.linspace(0, 10, 500)
mannheim_curve = generate_curve(kappa_mannheim, tau_mannheim, s_mannheim)

# Generate Mannheim partner
mannheim_partner = []
for i in range(len(s_mannheim)):
    s = s_mannheim[i]
    
    # Calculate Frenet frame at this point
    if i > 0:
        T = (mannheim_curve[i] - mannheim_curve[i-1]) / np.linalg.norm(mannheim_curve[i] - mannheim_curve[i-1])
        
        # Approximate curvature and torsion
        kappa = kappa_mannheim(s)
        tau = tau_mannheim(s)
        
        # Calculate normal and binormal
        if i > 1:
            # Use finite differences to approximate derivatives
            T_prev = (mannheim_curve[i-1] - mannheim_curve[i-2]) / np.linalg.norm(mannheim_curve[i-1] - mannheim_curve[i-2])
            dT = (T - T_prev) / (s_mannheim[i] - s_mannheim[i-1])
            
            # Normal vector
            N = dT / np.linalg.norm(dT) if np.linalg.norm(dT) > 1e-10 else np.array([0, 1, 0])
            
            # Binormal vector
            B = np.cross(T, N)
            B = B / np.linalg.norm(B)
            
            # Ensure orthogonality
            N = np.cross(B, T)
            
            # Mannheim partner has its binormal parallel to the normal of the original curve
            # We place it at a constant distance along the normal
            d = 1.0  # constant distance
            partner_point = mannheim_curve[i] + d * N
            mannheim_partner.append(partner_point)

# Convert to numpy array
mannheim_partner = np.array(mannheim_partner)

# Plot Mannheim curve and its partner
ax_mannheim.plot(mannheim_curve[:,0], mannheim_curve[:,1], mannheim_curve[:,2], 'b-', linewidth=2, 
                 label='Mannheim Curve')
if len(mannheim_partner) > 0:
    ax_mannheim.plot(mannheim_partner[:,0], mannheim_partner[:,1], mannheim_partner[:,2], 'm-', linewidth=2, 
                     label='Mannheim Partner')

    # Draw some connecting lines
    for i in range(0, len(mannheim_partner), 50):
        if i < len(mannheim_curve):
            ax_mannheim.plot([mannheim_curve[i,0], mannheim_partner[i,0]], 
                             [mannheim_curve[i,1], mannheim_partner[i,1]], 
                             [mannheim_curve[i,2], mannheim_partner[i,2]], 'k--', alpha=0.3)

ax_mannheim.legend()

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig('/home/ubuntu/MIT_Differential_Geometry_18.950_Textbook/supplementary_materials/visualizations/chapter4/special_curves_visualizations.png', dpi=300)

# 2. Evolutes and Involutes
fig_evolute = plt.figure(figsize=(20, 10))
fig_evolute.suptitle('Evolutes and Involutes', fontsize=20)

# Evolute of a curve
ax_evolute = fig_evolute.add_subplot(121, projection='3d')
ax_evolute.set_title('Evolute of a Curve')
ax_evolute.set_xlabel('X')
ax_evolute.set_ylabel('Y')
ax_evolute.set_zlabel('Z')

# Generate a curve (ellipse)
t_ellipse = np.linspace(0, 2*np.pi, 200)
a, b = 2.0, 1.0  # semi-major and semi-minor axes
x_ellipse = a * np.cos(t_ellipse)
y_ellipse = b * np.sin(t_ellipse)
z_ellipse = np.zeros_like(t_ellipse)

# Calculate evolute
# For an ellipse with semi-axes a and b, the evolute is:
# x = (a-b)²/a * cos³(t)/a
# y = (a-b)²/b * sin³(t)/b
x_evolute = (a-b)**2/a * np.cos(t_ellipse)**3/a
y_evolute = (a-b)**2/b * np.sin(t_ellipse)**3/b
z_evolute = np.zeros_like(t_ellipse)

# Plot ellipse and its evolute
ax_evolute.plot(x_ellipse, y_ellipse, z_ellipse, 'b-', linewidth=2, label='Ellipse')
ax_evolute.plot(x_evolute, y_evolute, z_evolute, 'r-', linewidth=2, label='Evolute')

# Draw some osculating circles
for t in [0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi]:
    # Point on ellipse
    x = a * np.cos(t)
    y = b * np.sin(t)
    z = 0
    
    # Curvature at this point
    kappa = (a*b) / ((a*np.sin(t))**2 + (b*np.cos(t))**2)**(3/2)
    
    # Center of osculating circle (point on evolute)
    x_center = (a-b)**2/a * np.cos(t)**3/a
    y_center = (a-b)**2/b * np.sin(t)**3/b
    z_center = 0
    
    # Draw osculating circle
    radius = 1/kappa
    theta = np.linspace(0, 2*np.pi, 100)
    
    # Normal vector to ellipse at this point
    nx = b * np.cos(t) / np.sqrt((a*np.sin(t))**2 + (b*np.cos(t))**2)
    ny = a * np.sin(t) / np.sqrt((a*np.sin(t))**2 + (b*np.cos(t))**2)
    
    # Tangent vector (perpendicular to normal)
    tx = -ny
    ty = nx
    
    # Points on osculating circle
    x_circle = x_center + radius * (nx*np.cos(theta) + tx*np.sin(theta))
    y_circle = y_center + radius * (ny*np.cos(theta) + ty*np.sin(theta))
    z_circle = np.zeros_like(theta)
    
    ax_evolute.plot(x_circle, y_circle, z_circle, 'g-', alpha=0.3)
    
    # Draw line from curve to evolute
    ax_evolute.plot([x, x_center], [y, y_center], [z, z_center], 'k--', alpha=0.5)

ax_evolute.legend()

# Involute of a curve
ax_involute = fig_evolute.add_subplot(122, projection='3d')
ax_involute.set_title('Involute of a Circle')
ax_involute.set_xlabel('X')
ax_involute.set_ylabel('Y')
ax_involute.set_zlabel('Z')

# Generate a circle
t_circle = np.linspace(0, 2*np.pi, 200)
radius = 1.0
x_circle = radius * np.cos(t_circle)
y_circle = radius * np.sin(t_circle)
z_circle = np.zeros_like(t_circle)

# Calculate involute
# For a circle with radius r, the involute is:
# x = r(cos(t) + t*sin(t))
# y = r(sin(t) - t*cos(t))
t_involute = np.linspace(0, 4*np.pi, 400)
x_involute = radius * (np.cos(t_involute) + t_involute*np.sin(t_involute))
y_involute = radius * (np.sin(t_involute) - t_involute*np.cos(t_involute))
z_involute = np.zeros_like(t_involute)

# Plot circle and its involute
ax_involute.plot(x_circle, y_circle, z_circle, 'b-', linewidth=2, label='Circle')
ax_involute.plot(x_involute, y_involute, z_involute, 'r-', linewidth=2, label='Involute')

# Draw some "unwinding string" lines
for t in np.linspace(0, 4*np.pi, 20):
    # Point on circle
    x_c = radius * np.cos(t)
    y_c = radius * np.sin(t)
    z_c = 0
    
    # Point on involute
    x_i = radius * (np.cos(t) + t*np.sin(t))
    y_i = radius * (np.sin(t) - t*np.cos(t))
    z_i = 0
    
    # Draw line (the "string")
    ax_involute.plot([x_c, x_i], [y_c, y_i], [z_c, z_i], 'g-', alpha=0.3)

ax_involute.legend()

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig('/home/ubuntu/MIT_Differential_Geometry_18.950_Textbook/supplementary_materials/visualizations/chapter4/evolute_involute_visualizations.png', dpi=300)

# 3. Higher-Dimensional Frenet Frame
fig_higher = plt.figure(figsize=(15, 15))
fig_higher.suptitle('Higher-Dimensional Frenet Frame', fontsize=20)

ax_higher = fig_higher.add_subplot(111, projection='3d')
ax_higher.set_title('Frenet Frame in 4D (Projected to 3D)')
ax_higher.set_xlabel('X')
ax_higher.set_ylabel('Y')
ax_higher.set_zlabel('Z')

# Generate a curve in 4D
t_4d = np.linspace(0, 4*np.pi, 200)
x_4d = np.cos(t_4d)
y_4d = np.sin(t_4d)
z_4d = np.cos(2*t_4d)/2
w_4d = np.sin(2*t_4d)/2  # 4th dimension

# Project to 3D for visualization (simple projection ignoring w)
ax_higher.plot(x_4d, y_4d, z_4d, 'b-', linewidth=2, label='4D Curve (3D Projection)')

# Calculate Frenet frame at selected points
points_4d = [0, 25, 50, 75, 100, 125, 150, 175]

for i in points_4d:
    # Position
    pos = np.array([x_4d[i], y_4d[i], z_4d[i]])
    
    # Approximate Frenet frame using finite differences
    if i > 0 and i < len(t_4d) - 1:
        # First derivative (e₁ = T)
        dt = t_4d[i+1] - t_4d[i-1]
        dx = (x_4d[i+1] - x_4d[i-1]) / dt
        dy = (y_4d[i+1] - y_4d[i-1]) / dt
        dz = (z_4d[i+1] - z_4d[i-1]) / dt
        dw = (w_4d[i+1] - w_4d[i-1]) / dt
        
        e1_4d = np.array([dx, dy, dz, dw])
        e1_4d = e1_4d / np.linalg.norm(e1_4d)
        
        # Second derivative
        d2x = (x_4d[i+1] - 2*x_4d[i] + x_4d[i-1]) / (dt/2)**2
        d2y = (y_4d[i+1] - 2*y_4d[i] + y_4d[i-1]) / (dt/2)**2
        d2z = (z_4d[i+1] - 2*z_4d[i] + z_4d[i-1]) / (dt/2)**2
        d2w = (w_4d[i+1] - 2*w_4d[i] + w_4d[i-1]) / (dt/2)**2
        
        d2r = np.array([d2x, d2y, d2z, d2w])
        
        # e₂ is the component of d2r orthogonal to e₁
        e2_4d = d2r - np.dot(d2r, e1_4d) * e1_4d
        if np.linalg.norm(e2_4d) > 1e-10:
            e2_4d = e2_4d / np.linalg.norm(e2_4d)
        else:
            # If e2 is too small, choose an arbitrary vector orthogonal to e1
            e2_4d = np.array([0, 0, 0, 0])
            if abs(e1_4d[0]) > 1e-10:
                e2_4d[1] = 1.0
            else:
                e2_4d[0] = 1.0
            e2_4d = e2_4d - np.dot(e2_4d, e1_4d) * e1_4d
            e2_4d = e2_4d / np.linalg.norm(e2_4d)
        
        # Third derivative (approximate)
        if i > 1 and i < len(t_4d) - 2:
            d3x = (x_4d[i+2] - 2*x_4d[i+1] + 2*x_4d[i-1] - x_4d[i-2]) / (dt)**3
            d3y = (y_4d[i+2] - 2*y_4d[i+1] + 2*y_4d[i-1] - y_4d[i-2]) / (dt)**3
            d3z = (z_4d[i+2] - 2*z_4d[i+1] + 2*z_4d[i-1] - z_4d[i-2]) / (dt)**3
            d3w = (w_4d[i+2] - 2*w_4d[i+1] + 2*w_4d[i-1] - w_4d[i-2]) / (dt)**3
            
            d3r = np.array([d3x, d3y, d3z, d3w])
            
            # e₃ is the component of d3r orthogonal to e₁ and e₂
            e3_4d = d3r - np.dot(d3r, e1_4d) * e1_4d - np.dot(d3r, e2_4d) * e2_4d
            if np.linalg.norm(e3_4d) > 1e-10:
                e3_4d = e3_4d / np.linalg.norm(e3_4d)
            else:
                # If e3 is too small, choose an arbitrary vector orthogonal to e1 and e2
                e3_4d = np.array([0, 0, 0, 0])
                if abs(e1_4d[0]*e2_4d[1] - e1_4d[1]*e2_4d[0]) > 1e-10:
                    e3_4d[0] = e2_4d[1]
                    e3_4d[1] = -e2_4d[0]
                else:
                    e3_4d[0] = e2_4d[2]
                    e3_4d[2] = -e2_4d[0]
                e3_4d = e3_4d - np.dot(e3_4d, e1_4d) * e1_4d - np.dot(e3_4d, e2_4d) * e2_4d
                e3_4d = e3_4d / np.linalg.norm(e3_4d)
            
            # e₄ is determined by the cross product in 4D (using determinant)
            # For simplicity, we'll just ensure it's orthogonal to e₁, e₂, and e₃
            e4_4d = np.array([0, 0, 0, 0])
            if abs(e1_4d[0]) > 1e-10:
                e4_4d[1] = e3_4d[2]
                e4_4d[2] = -e3_4d[1]
            else:
                e4_4d[0] = e3_4d[2]
                e4_4d[2] = -e3_4d[0]
            e4_4d = e4_4d - np.dot(e4_4d, e1_4d) * e1_4d - np.dot(e4_4d, e2_4d) * e2_4d - np.dot(e4_4d, e3_4d) * e3_4d
            e4_4d = e4_4d / np.linalg.norm(e4_4d)
            
            # Project 4D vectors to 3D for visualization
            e1_3d = np.array([e1_4d[0], e1_4d[1], e1_4d[2]])
            e2_3d = np.array([e2_4d[0], e2_4d[1], e2_4d[2]])
            e3_3d = np.array([e3_4d[0], e3_4d[1], e3_4d[2]])
            e4_3d = np.array([e4_4d[0], e4_4d[1], e4_4d[2]])
            
            # Scale for visualization
            scale = 0.3
            
            # Plot Frenet frame
            ax_higher.quiver(pos[0], pos[1], pos[2], scale*e1_3d[0], scale*e1_3d[1], scale*e1_3d[2], 
                           color='r', arrow_length_ratio=0.2)
            ax_higher.quiver(pos[0], pos[1], pos[2], scale*e2_3d[0], scale*e2_3d[1], scale*e2_3d[2], 
                           color='g', arrow_length_ratio=0.2)
            ax_higher.quiver(pos[0], pos[1], pos[2], scale*e3_3d[0], scale*e3_3d[1], scale*e3_3d[2], 
                           color='b', arrow_length_ratio=0.2)
            ax_higher.quiver(pos[0], pos[1], pos[2], scale*e4_3d[0], scale*e4_3d[1], scale*e4_3d[2], 
                           color='m', arrow_length_ratio=0.2)

# Add legend
ax_higher.text(1.5, 0, 0, 'e₁ (Tangent)', color='r')
ax_higher.text(1.5, 0, -0.3, 'e₂ (Normal)', color='g')
ax_higher.text(1.5, 0, -0.6, 'e₃ (Binormal)', color='b')
ax_higher.text(1.5, 0, -0.9, 'e₄ (Trinormal)', color='m')

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig('/home/ubuntu/MIT_Differential_Geometry_18.950_Textbook/supplementary_materials/visualizations/chapter4/higher_dimensional_frenet_frame.png', dpi=300)

print("Visualizations for Chapter 4 created successfully!")
