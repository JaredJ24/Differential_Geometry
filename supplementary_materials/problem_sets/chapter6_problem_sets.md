# Additional Problem Sets for Chapter 6: Closed Curves and the Jordan Curve Theorem

## Interleaved Problem Set 3: Winding Numbers and the Jordan Curve Theorem

### Foundational Problems

**Problem 6.19:** Let γ be a simple closed curve in the plane, and let p be a point not on γ. Prove that if p is in the interior of γ, then any ray from p to infinity intersects γ an odd number of times, and if p is in the exterior of γ, then any ray from p to infinity intersects γ an even number of times (possibly zero).

*Hint:* Consider how the parity of intersection points relates to the winding number.

**Problem 6.20:** Let γ₁ and γ₂ be simple closed curves such that γ₁ lies entirely in the interior of γ₂. If p is a point in the interior of γ₁, compute W(γ₁, p) + W(γ₂, p).

*Hint:* Use the fact that the winding number is 1 for points in the interior of a simple closed curve and 0 for points in the exterior.

**Problem 6.21:** Let γ be a simple closed curve, and let f: γ → ℝ² be a continuous function such that f(γ) is also a simple closed curve. If p is in the interior of γ and f(p) is in the interior of f(γ), prove that the degree of the map f|γ: γ → f(γ) is odd.

*Hint:* Consider the relationship between the degree of the map and the winding numbers.

### Exploratory Problems

**Problem 6.22:** Let γ be a closed curve (not necessarily simple) in the plane, and let p be a point not on γ. Prove that the winding number W(γ, p) can be computed as:

W(γ, p) = (1/2π) ∫ dθ

where θ is the angle between the vector from p to a point on γ and the positive x-axis, and the integral is taken along the curve γ.

*Hint:* Express the curve in polar coordinates centered at p.

**Problem 6.23:** Let γ be a simple closed curve, and let T be a continuous transformation of the plane that maps γ to another simple closed curve T(γ). If T preserves the orientation of the plane (i.e., it doesn't reflect), prove that for any point p in the interior of γ, the point T(p) is in the interior of T(γ).

*Hint:* Consider how T affects the winding number.

**Problem 6.24:** Let γ be a simple closed curve, and let p and q be two points in the interior of γ. Prove that there exists a continuous path from p to q that lies entirely within the interior of γ.

*Hint:* Use the fact that the interior of a simple closed curve is path-connected.

### Proofcraft Problems

**Problem 6.25:** Prove that the Jordan Curve Theorem implies the Brouwer Fixed Point Theorem for the disk: any continuous function f: D² → D² has a fixed point.

*Hint:* Assume f has no fixed points and construct a retraction from the disk to its boundary, which contradicts the No Retraction Theorem.

**Problem 6.26:** Prove the Schoenflies Theorem: If γ is a simple closed curve in the plane, then there exists a homeomorphism h: ℝ² → ℝ² such that h(γ) is the unit circle.

*Hint:* First show that the interior of γ is homeomorphic to the open unit disk using the Riemann Mapping Theorem, then extend this homeomorphism to the boundary and the exterior.

**Problem 6.27:** Prove that the Jordan Curve Theorem fails in higher dimensions: there exists a simple closed curve in ℝ³ whose complement is connected.

*Hint:* Consider a trefoil knot in ℝ³ and show that any point in ℝ³ not on the knot can be connected to any other such point by a path that doesn't intersect the knot.

## Interleaved Problem Set 4: Rotation Numbers and the Whitney-Graustein Theorem

### Foundational Problems

**Problem 6.28:** Calculate the rotation number for the following regular closed curves:
a) γ(t) = (cos t, sin t) for t ∈ [0, 2π]
b) γ(t) = (cos 2t, sin 2t) for t ∈ [0, 2π]
c) γ(t) = (sin 2t, sin t) for t ∈ [0, 2π]

*Hint:* Track how the tangent vector rotates as you traverse the curve.

**Problem 6.29:** Prove that the rotation number of a regular closed curve is always an integer.

*Hint:* Consider the total change in angle of the tangent vector as you traverse the curve.

**Problem 6.30:** Let γ be a regular closed curve with rotation number n. If γ is traversed in the opposite direction to obtain a new curve γ', what is the rotation number of γ'?

*Hint:* Consider how reversing the direction affects the tangent vector.

### Exploratory Problems

**Problem 6.31:** Let γ₁ and γ₂ be two regular closed curves with rotation numbers n₁ and n₂, respectively. Define a new curve γ by first traversing γ₁ and then traversing γ₂. What is the rotation number of γ?

*Hint:* Consider how the tangent vector changes as you traverse each curve.

**Problem 6.32:** Construct a regular closed curve with rotation number 3. Can you find a simple closed curve with rotation number 3?

*Hint:* Consider curves that wind around multiple times.

**Problem 6.33:** Let γ be a regular closed curve with rotation number n. Prove that γ can be continuously deformed through regular closed curves to a circle traversed n times.

*Hint:* Use the Whitney-Graustein Theorem.

### Proofcraft Problems

**Problem 6.34:** Prove the Whitney-Graustein Theorem: Two regular closed curves in the plane are regularly homotopic if and only if they have the same rotation number.

*Hint:* First show that the rotation number is invariant under regular homotopy. Then construct an explicit regular homotopy between any curve with rotation number n and a circle traversed n times.

**Problem 6.35:** Let γ be a regular closed curve with rotation number n. Prove that γ has at least |n| + 1 inflection points (points where the curvature is zero).

*Hint:* Use the fact that the tangent vector must make n complete rotations, and consider how the curvature changes sign.

**Problem 6.36:** Prove that any regular closed curve with rotation number 0 must have at least 4 inflection points.

*Hint:* Consider the changes in the sign of the curvature as the tangent vector makes a complete cycle.

## Interleaved Problem Set 5: The Isoperimetric Inequality and the Four Vertex Theorem

### Foundational Problems

**Problem 6.37:** Verify that the isoperimetric inequality 4πA ≤ L² holds with equality for a circle of radius r, where A = πr² and L = 2πr.

*Hint:* Substitute the values of A and L into the inequality.

**Problem 6.38:** Let γ be a square with side length s. Calculate the area A, perimeter L, and the isoperimetric ratio 4πA/L². How does this compare to the optimal ratio for a circle?

*Hint:* For a square, A = s² and L = 4s.

**Problem 6.39:** Let γ be a regular hexagon with side length s. Calculate the area A, perimeter L, and the isoperimetric ratio 4πA/L². How does this compare to the square and the circle?

*Hint:* For a regular hexagon, A = (3√3/2)s² and L = 6s.

### Exploratory Problems

**Problem 6.40:** Investigate how the isoperimetric ratio 4πA/L² changes for a family of ellipses with semi-major axis a and semi-minor axis b, where a/b varies from 1 to 10.

*Hint:* For an ellipse, A = πab and L ≈ 2π√((a²+b²)/2) (this is an approximation).

**Problem 6.41:** Prove that among all rectangles with a fixed perimeter, the square has the maximum area.

*Hint:* Use calculus to find the dimensions that maximize the area for a fixed perimeter.

**Problem 6.42:** Investigate the isoperimetric inequality on the sphere: among all simple closed curves on the sphere with a fixed length, which one encloses the maximum area?

*Hint:* Consider small circles on the sphere and use calculus of variations.

### Proofcraft Problems

**Problem 6.43:** Prove the isoperimetric inequality using Fourier series: if γ is a simple closed curve in the plane with length L and enclosed area A, then 4πA ≤ L², with equality if and only if γ is a circle.

*Hint:* Parametrize γ by arc length and express it in terms of its Fourier coefficients. Then apply the Cauchy-Schwarz inequality.

**Problem 6.44:** Prove the Four Vertex Theorem: any simple closed curve in the plane, other than a circle, has at least four vertices (local extrema of curvature).

*Hint:* Use the fact that the derivative of the curvature with respect to arc length must have at least four zeros on the curve.

**Problem 6.45:** Prove that the Four Vertex Theorem is sharp: there exists a simple closed curve with exactly four vertices.

*Hint:* Consider an ellipse and show that it has exactly four vertices.
