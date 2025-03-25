# Additional Problem Sets for Chapter 7: Total Curvature and the Hopf Umlaufsatz

## Interleaved Problem Set 3: Total Curvature and Turning Angles

### Foundational Problems

**Problem 7.21:** Calculate the total curvature of the following curves:
a) A parabola y = x² from x = -1 to x = 1
b) A logarithmic spiral r = e^(aθ) for one complete turn
c) A cardioid r = 1 + cos θ

*Hint:* For the parabola, use the formula κ = |y''|/(1 + (y')²)^(3/2).

**Problem 7.22:** Let γ be a curve consisting of two semicircles of radius 1 connected by straight line segments of length 2. Calculate the total curvature of γ.

*Hint:* Break the calculation into parts and use the additivity of total curvature.

**Problem 7.23:** Prove that the total curvature of a convex closed curve equals 2π.

*Hint:* Use the fact that the tangent vector makes one complete revolution.

### Exploratory Problems

**Problem 7.24:** Let γ₁ and γ₂ be two curves with the same endpoints and the same tangent vectors at those endpoints. If K₁ and K₂ are their total curvatures, prove that |K₁ - K₂| ≤ π.

*Hint:* Consider the turning angles of the two curves.

**Problem 7.25:** Let γ be a simple closed curve in the plane. Define the "average curvature" of γ as K/L, where K is the total curvature and L is the length of γ. Prove that the average curvature is minimized when γ is a circle.

*Hint:* Use the isoperimetric inequality and the Hopf Umlaufsatz.

**Problem 7.26:** Let γ be a curve in the plane with curvature κ(s) ≥ 0 for all s. Prove that if the total curvature of γ is less than π, then γ is a simple curve (i.e., it has no self-intersections).

*Hint:* Consider what happens to the tangent vector as you traverse the curve.

### Proofcraft Problems

**Problem 7.27:** Prove the Hopf Umlaufsatz: If γ is a simple closed curve in the plane, then the total curvature of γ is 2π.

*Hint:* Use the winding number of the tangent vector around the origin.

**Problem 7.28:** Let γ be a closed curve in the plane with exactly one self-intersection. Prove that the total curvature of γ is at least 2π.

*Hint:* Consider the winding numbers of the two simple closed curves formed by the self-intersection.

**Problem 7.29:** Prove that if γ is a closed curve in the plane with total curvature less than 4π, then γ has at most one self-intersection.

*Hint:* Use the relationship between total curvature and winding number.

## Interleaved Problem Set 4: Winding Numbers and the Gauss-Bonnet Theorem

### Foundational Problems

**Problem 7.30:** Calculate the winding number of the following curves around the origin:
a) A circle centered at (2, 0) with radius 1
b) A figure-eight curve given by x(t) = sin(2t), y(t) = sin(t) for t ∈ [0, 2π]
c) A limacon r = 2 + cos θ

*Hint:* For the figure-eight, consider the winding of the tangent vector.

**Problem 7.31:** Let γ be a closed curve in the plane, and let p and q be two points in the same connected component of the complement of γ. Prove that W(γ, p) = W(γ, q).

*Hint:* Consider a path connecting p and q, and how the winding number changes along this path.

**Problem 7.32:** Let γ be a closed curve in the plane with winding number W(γ, p) = 2 around some point p. Calculate the total curvature of γ.

*Hint:* Use the relationship between total curvature and winding number.

### Exploratory Problems

**Problem 7.33:** Let γ be a closed curve in the plane with total curvature 6π. What can you say about the possible winding numbers of γ around points in the plane?

*Hint:* Use the relationship between total curvature and the absolute value of the winding number.

**Problem 7.34:** Let γ₁ and γ₂ be two closed curves in the plane, and let γ be the curve obtained by first traversing γ₁ and then traversing γ₂. Prove that W(γ, p) = W(γ₁, p) + W(γ₂, p) for any point p not on γ₁ or γ₂.

*Hint:* Consider the definition of winding number in terms of the turning of the position vector.

**Problem 7.35:** Let γ be a closed curve in the plane with winding number 0 around every point not on γ. What can you say about γ?

*Hint:* Consider the relationship between winding number and total curvature.

### Proofcraft Problems

**Problem 7.36:** Prove the Gauss-Bonnet Theorem for plane curves: If γ is a simple closed curve in the plane, oriented counterclockwise, then ∫γ κ(s) ds = 2π, where κ(s) is the signed curvature.

*Hint:* Use the relationship between signed curvature and the turning angle of the tangent vector.

**Problem 7.37:** Let γ be a simple closed curve in the plane, and let D be the region enclosed by γ. Let γ₁, γ₂, ..., γₙ be simple closed curves inside D, oriented clockwise, and let D' be the region obtained by removing the interiors of γ₁, γ₂, ..., γₙ from D. Prove that ∫∂D' κ(s) ds = 2π(1-n), where ∂D' is the boundary of D' with the orientation induced from D.

*Hint:* Apply the Gauss-Bonnet Theorem to each component of the boundary.

**Problem 7.38:** Prove that the winding number of a closed curve γ around a point p not on γ can be computed as W(γ, p) = (1/2π) ∫γ (x-p₁) dy - (y-p₂) dx / (x-p₁)² + (y-p₂)², where p = (p₁, p₂).

*Hint:* Express the winding number in terms of the change in angle of the vector from p to a point on γ.

## Interleaved Problem Set 5: The Four Vertex Theorem and the Isoperimetric Inequality

### Foundational Problems

**Problem 7.39:** Prove that an ellipse has exactly four vertices: two points of maximum curvature at the ends of the minor axis, and two points of minimum curvature at the ends of the major axis.

*Hint:* Calculate the curvature of the ellipse and find its critical points.

**Problem 7.40:** Let γ be a simple closed curve with constant curvature. Prove that γ is a circle.

*Hint:* Use the Four Vertex Theorem.

**Problem 7.41:** Verify that the isoperimetric inequality L² ≥ 4πA holds with equality for a circle of radius r, where L = 2πr and A = πr².

*Hint:* Substitute the values of L and A into the inequality.

### Exploratory Problems

**Problem 7.42:** Let γ be a simple closed curve in the plane with length L and enclosed area A. Define the isoperimetric ratio as L²/4πA. Calculate this ratio for:
a) A square with side length s
b) An equilateral triangle with side length s
c) An ellipse with semi-major axis a and semi-minor axis b

*Hint:* For the ellipse, you can use the approximation L ≈ 2π√((a²+b²)/2).

**Problem 7.43:** Prove that among all rectangles with a fixed perimeter, the square has the maximum area.

*Hint:* Use calculus to find the dimensions that maximize the area for a fixed perimeter.

**Problem 7.44:** Prove that among all triangles with a fixed perimeter, the equilateral triangle has the maximum area.

*Hint:* Use calculus of variations or the method of Lagrange multipliers.

### Proofcraft Problems

**Problem 7.45:** Prove the Four Vertex Theorem: Any simple closed curve in the plane, other than a circle, has at least four vertices (points where the curvature reaches a local maximum or minimum).

*Hint:* Use the fact that the derivative of the curvature with respect to arc length must have at least four zeros on the curve.

**Problem 7.46:** Prove the isoperimetric inequality: Among all simple closed curves in the plane with a fixed length, the circle encloses the maximum area.

*Hint:* Use calculus of variations and the Euler-Lagrange equation.

**Problem 7.47:** Let γ be a simple closed curve in the plane with length L and enclosed area A. Prove that if the isoperimetric ratio L²/4πA is close to 1, then γ is close to a circle in the Hausdorff metric.

*Hint:* Use the concept of the Hausdorff distance between sets and the properties of the isoperimetric ratio.

## Interleaved Problem Set 6: The Fary-Milnor Theorem and Knot Theory

### Foundational Problems

**Problem 7.48:** Calculate the total curvature of a helix with parametrization r(t) = (cos t, sin t, bt) for t ∈ [0, 2π], where b is a constant.

*Hint:* Use the formula for the curvature of a space curve.

**Problem 7.49:** Prove that the total curvature of any closed curve in space is at least 2π.

*Hint:* Project the curve onto a plane and use the properties of total curvature.

**Problem 7.50:** Let γ be a simple closed curve in space with total curvature 2π. Prove that γ lies in a plane and is convex.

*Hint:* Use the Fenchel Theorem and its equality case.

### Exploratory Problems

**Problem 7.51:** Research and explain the concept of the "bridge number" of a knot and its relationship to the total curvature.

*Hint:* The bridge number is the minimum number of local maxima of the height function over all projections of the knot.

**Problem 7.52:** Let γ be a trefoil knot in space. Prove that the total curvature of γ is at least 4π.

*Hint:* Use the Fary-Milnor Theorem and the fact that the trefoil is a non-trivial knot.

**Problem 7.53:** Investigate the relationship between the total curvature of a knot and its crossing number (the minimum number of crossings in any projection of the knot).

*Hint:* Consider how crossings in a projection relate to the turning of the tangent vector.

### Proofcraft Problems

**Problem 7.54:** State and prove the Fenchel Theorem: The total curvature of any closed curve in space is at least 2π, with equality if and only if the curve is a convex plane curve.

*Hint:* Consider the tantrix (the curve traced by the unit tangent vector) on the unit sphere.

**Problem 7.55:** Research and write a short essay on the Fary-Milnor Theorem, which states that the total curvature of any knotted curve in space is at least 4π.

*Hint:* Explore the connection between total curvature and the bridge number of a knot.

**Problem 7.56:** Prove that if a curve in space has total curvature less than 4π, then it is unknotted (i.e., it can be continuously deformed to a circle without self-intersections).

*Hint:* Use the contrapositive of the Fary-Milnor Theorem.
