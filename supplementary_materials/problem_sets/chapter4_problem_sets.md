# Chapter 4: Interleaved Problem Sets

## Problem Set 4.1: Frenet Frame and Curvature in Higher Dimensions

### Foundational Problems

**Problem 4.1.1:** For the curve r(t) = (t, t², t³) in ℝ³:
a) Find the arc length parameter s(t).
b) Calculate the unit tangent vector T(s).
c) Determine the curvature κ(s).
d) Find the unit normal vector N(s).

**Problem 4.1.2:** Prove that for any curve r(s) parametrized by arc length, the acceleration vector r''(s) is perpendicular to the velocity vector r'(s).

**Problem 4.1.3:** For a curve r(t) with arbitrary parameter t, show that the curvature can be computed using the formula:
κ = |r'(t) × r''(t)| / |r'(t)|³

**Problem 4.1.4:** For the helix r(t) = (a cos t, a sin t, bt), where a and b are positive constants:
a) Find the arc length parameter s(t).
b) Calculate the curvature κ and torsion τ.
c) Determine the Frenet frame {T, N, B} at any point.

### Exploratory Problems

**Problem 4.1.5:** Consider a curve r(s) in ℝ⁴ parametrized by arc length. Define the generalized curvatures κ₁, κ₂, and κ₃, and explain their geometric meaning.

**Problem 4.1.6:** For the curve r(t) = (cos t, sin t, cos 2t, sin 2t) in ℝ⁴:
a) Verify that this curve lies on the surface of a torus in ℝ⁴.
b) Calculate the first generalized curvature κ₁.
c) Sketch how the Frenet frame would evolve along this curve.

**Problem 4.1.7:** A curve r(s) in ℝⁿ is called a generalized helix if its tangent vector makes a constant angle with a fixed direction. Prove that a curve in ℝ³ is a generalized helix if and only if the ratio τ/κ is constant. Then generalize this result to higher dimensions.

### Proofcraft Problems

**Problem 4.1.8:** Prove the Higher-Dimensional Frenet-Serret Formulas: For a curve r(s) in ℝⁿ parametrized by arc length, the derivatives of the Frenet frame vectors satisfy:

e₁'(s) = κ₁(s)e₂(s)
e₂'(s) = -κ₁(s)e₁(s) + κ₂(s)e₃(s)
...
eₙ₋₁'(s) = -κₙ₋₂(s)eₙ₋₂(s) + κₙ₋₁(s)eₙ(s)
eₙ'(s) = -κₙ₋₁(s)eₙ₋₁(s)

**Problem 4.1.9:** Prove that a curve in ℝⁿ is completely determined, up to rigid motions, by its n-1 generalized curvatures. (Hint: Use the existence and uniqueness theorem for systems of ordinary differential equations.)

**Problem 4.1.10:** For a curve r(s) in ℝ³ parametrized by arc length, define the osculating sphere at r(s) as the sphere that has fourth-order contact with the curve at that point. Prove that the center of the osculating sphere is given by:

c(s) = r(s) + (1/κ)N(s) + (κ'/κ² + τ²/κ²)B(s)

and its radius is:

R = √[(1/κ)² + (κ'/κ² + τ²/κ²)²]

## Problem Set 4.2: Torsion and the Frenet-Serret Formulas

### Foundational Problems

**Problem 4.2.1:** Calculate the torsion of the curve r(t) = (t, t², t³) using the formula:
τ = (r' × r'') · r''' / |r' × r''|²

**Problem 4.2.2:** Prove that a curve lies in a plane if and only if its torsion is identically zero.

**Problem 4.2.3:** For a curve r(s) in ℝ³ parametrized by arc length, show that:
r''(s) = κ(s)N(s)
r'''(s) = -κ(s)²T(s) + κ'(s)N(s) + κ(s)τ(s)B(s)

**Problem 4.2.4:** For the curve r(t) = (e^t cos t, e^t sin t, e^t):
a) Find the curvature κ(t) and torsion τ(t).
b) Determine whether this curve is a generalized helix.

### Exploratory Problems

**Problem 4.2.5:** For a curve r(s) in ℝ³ parametrized by arc length, define the Darboux vector:
Ω(s) = τ(s)T(s) + κ(s)B(s)

Show that:
a) The Frenet-Serret formulas can be written as e'ᵢ(s) = Ω(s) × eᵢ(s) for i = 1, 2, 3, where e₁ = T, e₂ = N, e₃ = B.
b) The magnitude of the Darboux vector is |Ω(s)| = √(κ(s)² + τ(s)²).
c) The Darboux vector points along the instantaneous axis of rotation of the Frenet frame.

**Problem 4.2.6:** A curve r(s) in ℝ³ is called a slant helix if its principal normal makes a constant angle with a fixed direction. Show that a curve is a slant helix if and only if:
κ²/(κ² + τ²)³/² · d/ds(τ/κ) = constant

**Problem 4.2.7:** For a curve r(s) in ℝ³ parametrized by arc length, define the rectifying plane at r(s) as the plane spanned by T(s) and B(s). Show that:
a) The rectifying plane is perpendicular to the normal vector N(s).
b) A curve is a cylindrical helix if and only if all its rectifying planes pass through a fixed line.
c) A curve is a spherical curve if and only if all its rectifying planes pass through a fixed point.

### Proofcraft Problems

**Problem 4.2.8:** Prove that a curve r(s) in ℝ³ lies on a sphere if and only if:
(κ'/κ)² + κ² + τ² = constant

**Problem 4.2.9:** A curve r(s) in ℝ³ is called a Salkowski curve if it has constant curvature but non-constant torsion. Prove that:
a) The torsion of a Salkowski curve must satisfy a specific differential equation.
b) The binormal vector of a Salkowski curve traces a curve on a sphere.

**Problem 4.2.10:** The total curvature of a curve r(s) in ℝ³ parametrized by arc length from s = a to s = b is defined as:
K = ∫ₐᵇ κ(s) ds

Prove that:
a) The total curvature of a closed curve is at least 2π.
b) The total curvature equals 2π if and only if the curve is a convex plane curve.

## Problem Set 4.3: Special Curves and Applications

### Foundational Problems

**Problem 4.3.1:** A Bertrand curve is a curve that shares its principal normal with another curve at each point. Show that a curve is a Bertrand curve if and only if there exist constants a and b, not both zero, such that aκ + bτ = 1, where κ is the curvature and τ is the torsion.

**Problem 4.3.2:** A Mannheim curve is a curve whose principal normal at each point is parallel to the binormal of another curve (called its Mannheim partner) at the corresponding point. Show that a curve is a Mannheim curve if and only if its curvature κ and torsion τ satisfy the relation κ = c(κ² + τ²) for some constant c.

**Problem 4.3.3:** The evolute of a curve r(s) is the locus of centers of its osculating circles, given by e(s) = r(s) + (1/κ(s))N(s). Show that:
a) The tangent to the evolute at e(s) is parallel to the binormal vector B(s) of the original curve.
b) The arc length element of the evolute is |τ(s)/κ(s)| ds.

**Problem 4.3.4:** For an ellipse with semi-major axis a and semi-minor axis b, show that the evolute is a 4-cusped hypocycloid with parametric equation:
e(t) = ((a-b)cos³t/a, (a-b)sin³t/b)

### Exploratory Problems

**Problem 4.3.5:** In computer graphics, the Frenet frame can lead to abrupt changes in orientation when the curvature changes rapidly (the "Frenet frame flip" problem). Research and explain the Bishop frame (or parallel transport frame) as an alternative, and discuss its advantages for applications in computer animation and robotics.

**Problem 4.3.6:** In the theory of relativity, the path of a particle in a gravitational field is a geodesic. Explain how the Frenet-Serret formulas, generalized to curved spacetime, help in analyzing these paths. Discuss the physical interpretation of curvature and torsion in this context.

**Problem 4.3.7:** DNA molecules can be modeled as elastic rods with intrinsic curvature and torsion. Research and explain how the Frenet theory helps in understanding DNA supercoiling. What is the relationship between the torsion of the DNA axis and the biological concept of supercoiling?

### Proofcraft Problems

**Problem 4.3.8:** The Bishop frame {T, M₁, M₂} consists of the tangent vector T and two normal vectors M₁ and M₂ that span the normal plane. The evolution of the Bishop frame is given by:

T'(s) = k₁(s)M₁(s) + k₂(s)M₂(s)
M₁'(s) = -k₁(s)T(s)
M₂'(s) = -k₂(s)T(s)

where k₁ and k₂ are the Bishop curvatures. Prove that:
a) The Bishop frame is well-defined even when the Frenet curvature vanishes.
b) The Bishop curvatures relate to the Frenet curvature and torsion by:
   κ = √(k₁² + k₂²)
   τ = (k₁k₂' - k₂k₁')/κ²

**Problem 4.3.9:** For a curve r(s) in ℝ³ parametrized by arc length, the writhing number is defined as:
Wr = (1/2π) ∫∫ ((r'(s) × r'(t)) · (r(s) - r(t))) / |r(s) - r(t)|³ ds dt

Prove that for a closed curve, the writhing number is related to the total torsion by:
Wr = (1/2π) ∫ τ(s) ds + n

where n is an integer representing the linking number of the curve with its axis.

**Problem 4.3.10:** In the study of knot theory, the Frenet frame plays a crucial role. For a knot represented as a closed curve in ℝ³, prove that the total torsion ∫ τ(s) ds is invariant under ambient isotopy (continuous deformations that don't allow the curve to pass through itself). Discuss the implications of this result for knot classification.
