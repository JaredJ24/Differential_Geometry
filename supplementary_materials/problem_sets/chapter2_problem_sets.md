# Additional Interleaved Problem Sets for Chapter 2

## Problem Set 2.3: Osculating Circles and Evolutes

### Foundational Problems

1. **Problem 2.3.1:** For the parabola r(t) = (t, t²):
   a) Calculate the curvature κ(t).
   b) Find the center of the osculating circle at the point t = 1.
   c) Sketch the parabola and the osculating circle at t = 1.
   
   *Hint:* Use the formula for the center of the osculating circle: r(t) + (1/κ(t))N(t).

2. **Problem 2.3.2:** For the ellipse r(t) = (a cos t, b sin t) where a > b > 0:
   a) Find the points of maximum and minimum curvature.
   b) Calculate the centers of the osculating circles at these points.
   c) What is the relationship between these centers and the foci of the ellipse?
   
   *Hint:* To find extrema of curvature, set the derivative of κ(t) equal to zero.

### Exploratory Problems

3. **Problem 2.3.3:** Investigate the evolute of the ellipse r(t) = (a cos t, b sin t).
   a) Derive a parametric equation for the evolute.
   b) Show that the evolute is an astroid (a star-shaped curve) with parametric equations x = (a² - b²)cos³t/a and y = (a² - b²)sin³t/b.
   c) How does the shape of the evolute change as the ratio a/b varies?
   
   *Starting Point:* Use the formula for the center of the osculating circle and express it parametrically.

4. **Problem 2.3.4:** For the logarithmic spiral r(t) = (e^t cos t, e^t sin t):
   a) Calculate the curvature κ(t).
   b) Find the evolute of the spiral.
   c) Show that the evolute is another logarithmic spiral, rotated and scaled from the original.
   
   *Starting Point:* Calculate the first and second derivatives, then use the formula for curvature.

### Proofcraft Problems

5. **Problem 2.3.5:** Prove that the evolute of a curve has cusps at points corresponding to extrema of curvature on the original curve.
   
   *Milestone 1:* Express the evolute parametrically as e(s) = r(s) + (1/κ(s))N(s).
   
   *Milestone 2:* Calculate the derivative e'(s) and express it in terms of the Frenet frame.
   
   *Milestone 3:* Show that e'(s) = 0 precisely when κ'(s) = 0.

6. **Problem 2.3.6:** Prove that the length of an arc of the evolute equals the difference in the radii of curvature at the endpoints of the corresponding arc on the original curve.
   
   *Milestone 1:* Express the differential of arc length on the evolute in terms of |e'(s)|ds.
   
   *Milestone 2:* Show that |e'(s)| = |d(1/κ(s))/ds|.
   
   *Milestone 3:* Integrate to find the total length and interpret the result.

## Problem Set 2.4: Global Properties of Curvature

### Foundational Problems

1. **Problem 2.4.1:** For a simple closed curve in the plane:
   a) Define what it means for a point on the curve to be a vertex.
   b) State the Four Vertex Theorem.
   c) Verify that an ellipse has exactly four vertices.
   
   *Hint:* A vertex is a point where the curvature reaches a local extremum.

2. **Problem 2.4.2:** Consider a curve evolving under the curve shortening flow, where each point moves in the normal direction with speed proportional to the curvature.
   a) Write the evolution equation for the curve.
   b) Explain why a circle evolves by shrinking uniformly.
   c) What happens to a non-circular closed curve under this flow?
   
   *Hint:* The evolution equation is ∂r/∂t = κN.

### Exploratory Problems

3. **Problem 2.4.3:** Investigate the total curvature of closed curves.
   a) Calculate the total curvature ∫κ(s)ds for a circle.
   b) Show that the total curvature of any simple closed curve in the plane is 2π.
   c) What is the total curvature of a figure-eight curve? How does this relate to the turning number of the curve?
   
   *Starting Point:* For a plane curve, relate the curvature to the rate of change of the tangent angle.

4. **Problem 2.4.4:** Explore the isoperimetric inequality, which states that among all closed curves with a fixed perimeter, the circle encloses the maximum area.
   a) Verify the inequality for some simple cases (e.g., compare a circle and a square with the same perimeter).
   b) Research how the isoperimetric inequality relates to curvature.
   c) Investigate how the isoperimetric inequality generalizes to higher dimensions.
   
   *Starting Point:* The isoperimetric inequality can be stated as L² ≥ 4πA, where L is the perimeter and A is the area.

### Proofcraft Problems

5. **Problem 2.4.5:** Prove that a simple closed curve with constant curvature in the plane must be a circle.
   
   *Milestone 1:* Use the fact that for a plane curve parametrized by arc length, κ(s) = dφ/ds, where φ is the angle the tangent makes with the x-axis.
   
   *Milestone 2:* If κ is constant, then φ(s) = κs + φ₀ for some constant φ₀.
   
   *Milestone 3:* Use this to show that the curve must be a circle with radius 1/κ.

6. **Problem 2.4.6:** Prove the Tennis Ball Theorem: Any smooth curve on a sphere that divides the sphere into two equal areas must have at least four points where the geodesic curvature vanishes.
   
   *Milestone 1:* Understand what geodesic curvature measures (the deviation of a curve from being a great circle).
   
   *Milestone 2:* Use the fact that the curve must cross each great circle at least twice.
   
   *Milestone 3:* Apply a variant of the Four Vertex Theorem to complete the proof.

## Problem Set 2.5: Applications of Curvature

### Foundational Problems

1. **Problem 2.5.1:** In computer graphics, Bézier curves are commonly used to model smooth curves. A cubic Bézier curve has the form:
   r(t) = (1-t)³P₀ + 3(1-t)²tP₁ + 3(1-t)t²P₂ + t³P₃ for t ∈ [0, 1]
   where P₀, P₁, P₂, and P₃ are control points.
   
   a) Calculate the curvature of a Bézier curve at t = 0 and t = 1.
   b) How do the positions of the control points affect the curvature at the endpoints?
   c) Design a Bézier curve with specified curvatures at its endpoints.
   
   *Hint:* Calculate the first and second derivatives at t = 0 and t = 1 in terms of the control points.

2. **Problem 2.5.2:** In optics, the shape of a lens surface determines how it refracts light. The relationship between the radius of curvature ρ of a lens surface and its focal length f is given by the lensmaker's equation:
   1/f = (n-1)(1/ρ₁ - 1/ρ₂)
   where n is the refractive index of the lens material, and ρ₁ and ρ₂ are the radii of curvature of the two surfaces.
   
   a) Design a biconvex lens (both surfaces curved outward) with a focal length of 10 cm, using glass with n = 1.5.
   b) How does the shape of the lens change if you want to minimize spherical aberration?
   c) Research how aspherical lenses (with non-constant curvature) improve optical performance.
   
   *Hint:* For a biconvex lens, ρ₁ > 0 and ρ₂ < 0.

### Exploratory Problems

3. **Problem 2.5.3:** In general relativity, the curvature of spacetime is related to the distribution of mass and energy. The simplest solution to Einstein's field equations is the Schwarzschild metric, which describes the spacetime around a non-rotating spherical mass.
   
   a) Research how the geodesics (paths of free-falling particles) in Schwarzschild spacetime relate to the orbits of planets.
   b) Investigate how the curvature of spacetime leads to the bending of light around massive objects.
   c) Explore how the concept of curvature in differential geometry provides the mathematical framework for general relativity.
   
   *Starting Point:* In Newtonian gravity, the force is inversely proportional to the square of the distance. In general relativity, gravity is not a force but a manifestation of spacetime curvature.

4. **Problem 2.5.4:** In computer-aided design (CAD), curvature analysis is used to ensure smooth transitions between different surfaces.
   
   a) Research how curvature continuity (G₁, G₂, etc.) is defined in CAD systems.
   b) Investigate how automotive designers use curvature plots to create aesthetically pleasing car bodies.
   c) Design a simple 3D object with G₂ continuity (continuous curvature) across all surface transitions.
   
   *Starting Point:* G₁ continuity means the tangent directions match at a junction, while G₂ continuity means both the tangent directions and the curvatures match.

### Proofcraft Problems

5. **Problem 2.5.5:** In differential geometry, the Gauss-Bonnet theorem relates the total curvature of a surface to its topology. For a compact surface without boundary, it states that:
   ∫∫K dA = 2πχ(S)
   where K is the Gaussian curvature and χ(S) is the Euler characteristic of the surface.
   
   Prove that for a sphere, the total curvature is 4π.
   
   *Milestone 1:* Calculate the Gaussian curvature K of a sphere of radius R.
   
   *Milestone 2:* Calculate the surface area of the sphere.
   
   *Milestone 3:* Compute the integral and verify that it equals 2πχ(S) = 4π, since χ(S) = 2 for a sphere.

6. **Problem 2.5.6:** In the study of elastic rods, the curvature and torsion determine the shape of the rod under various loading conditions. The total energy of a bent rod is proportional to the integral of the square of the curvature along the rod.
   
   Prove that among all curves of fixed length connecting two points, the one that minimizes the integral of the square of the curvature is a segment of a circle if the tangent directions at the endpoints are specified.
   
   *Milestone 1:* Set up the variational problem with the appropriate constraints.
   
   *Milestone 2:* Derive the Euler-Lagrange equation for this problem.
   
   *Milestone 3:* Show that the solution is a segment of a circle passing through the two points with the specified tangent directions.
