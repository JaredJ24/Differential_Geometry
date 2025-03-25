# Additional Interleaved Problem Sets for Chapter 1

## Problem Set 1.2: Reparametrization and Arc Length

### Foundational Problems

1. **Problem 1.2.1:** Consider the curve r(t) = (t, t², t³) for t ∈ [0, 1].
   a) Show that this curve is regular.
   b) Calculate the arc length function s(t).
   c) Find the arc length parametrization of this curve.
   
   *Hint:* For part (c), you'll need to express t as a function of s, then substitute.

2. **Problem 1.2.2:** For the ellipse with parametrization r(t) = (a cos t, b sin t, 0) where a > b > 0:
   a) Calculate the speed |r'(t)| at each point.
   b) Identify the points of maximum and minimum speed.
   c) Explain geometrically why the speed varies along the ellipse.
   
   *Hint:* Consider the geometric meaning of the parameter t.

### Exploratory Problems

3. **Problem 1.2.3:** Investigate how the arc length of a helix r(t) = (a cos t, a sin t, bt) changes as the parameters a and b vary.
   a) Derive a formula for the arc length of one complete turn as a function of a and b.
   b) What happens to the arc length as b approaches 0? Interpret this geometrically.
   c) For a fixed arc length L, describe the family of helices that have arc length L for one complete turn.
   
   *Starting Point:* Calculate the arc length for specific values of a and b, then generalize.

4. **Problem 1.2.4:** Consider a curve with the property that its arc length parametrization is r(s) = (f(s), g(s), h(s)) where f, g, and h are all periodic functions with the same period.
   a) What can you say about the shape of this curve?
   b) Give an example of such a curve.
   c) How would the curve change if the periods of f, g, and h were different but related by rational ratios?
   
   *Starting Point:* Think about what it means for a vector-valued function to be periodic.

### Proofcraft Problems

5. **Problem 1.2.5:** Prove that if two regular curves have the same trace and the same orientation, then one is a reparametrization of the other.
   
   *Milestone 1:* Define what it means for two curves to have the same trace and orientation.
   
   *Milestone 2:* For a point p on the trace, consider the parameters t₁ and t₂ such that r₁(t₁) = r₂(t₂) = p.
   
   *Milestone 3:* Construct a function φ such that r₂ = r₁ ∘ φ and verify that it satisfies the conditions for a reparametrization.

6. **Problem 1.2.6:** Prove that the arc length of a curve is invariant under rigid motions (translations and rotations).
   
   *Milestone 1:* Express a rigid motion mathematically as r̃(t) = Ar(t) + b, where A is an orthogonal matrix and b is a constant vector.
   
   *Milestone 2:* Calculate the derivative r̃'(t) and its magnitude.
   
   *Milestone 3:* Show that |r̃'(t)| = |r'(t)| and use this to prove that the arc length is preserved.

## Problem Set 1.3: Curvature and the Frenet Frame

### Foundational Problems

1. **Problem 1.3.1:** Calculate the curvature of the following curves:
   a) The parabola r(t) = (t, t², 0)
   b) The logarithmic spiral r(t) = (e^t cos t, e^t sin t, 0)
   c) The circular helix r(t) = (cos t, sin t, t)
   
   *Hint:* Use the formula κ = |r' × r''|/|r'|³ for curves not parametrized by arc length.

2. **Problem 1.3.2:** For the curve r(t) = (t, t², t³), t ∈ [0, 1]:
   a) Calculate the unit tangent vector T(t).
   b) Calculate the curvature κ(t).
   c) Find the unit normal vector N(t) and the binormal vector B(t).
   d) Verify that {T(t), N(t), B(t)} forms an orthonormal basis for each t.
   
   *Hint:* Remember that T(t) = r'(t)/|r'(t)| and N(t) = T'(t)/|T'(t)|.

### Exploratory Problems

3. **Problem 1.3.3:** Explore the relationship between the curvature of a curve and its visual appearance.
   a) Design a curve with regions of high curvature and regions of low curvature.
   b) How does the curvature relate to the "tightness" of the curve's turns?
   c) Can you create a curve with constant curvature that is not a circle? What about a curve with linearly increasing curvature?
   
   *Starting Point:* Consider curves like r(t) = (t, t^n, 0) for different values of n.

4. **Problem 1.3.4:** Investigate the Frenet frame along a circular helix.
   a) Calculate the Frenet frame {T(t), N(t), B(t)} for the helix r(t) = (a cos t, a sin t, bt).
   b) Show that the binormal vector makes a constant angle with the z-axis.
   c) What happens to the Frenet frame as the ratio b/a changes?
   
   *Starting Point:* Calculate the derivatives r'(t) and r''(t), then normalize to find T(t) and N(t).

### Proofcraft Problems

5. **Problem 1.3.5:** Prove that a curve with zero torsion lies in a plane.
   
   *Milestone 1:* Recall that the torsion τ appears in the Frenet formula B'(s) = -τ(s)N(s).
   
   *Milestone 2:* If τ = 0, what does this tell you about B(s)?
   
   *Milestone 3:* Use the fact that B(s) is constant to show that the curve lies in a plane.

6. **Problem 1.3.6:** Prove that a curve with constant non-zero curvature and zero torsion is a circle.
   
   *Milestone 1:* From the previous problem, we know the curve lies in a plane. Choose coordinates so that this is the xy-plane.
   
   *Milestone 2:* Use the Frenet formula T'(s) = κN(s) with constant κ to set up a differential equation.
   
   *Milestone 3:* Solve the differential equation to show that the curve has the form r(s) = (R cos(s/R + φ), R sin(s/R + φ), 0) for some constants R and φ.

## Problem Set 1.4: Applications and Connections

### Foundational Problems

1. **Problem 1.4.1:** A particle moves along a curve r(t) with position at time t. Its velocity is v(t) = r'(t) and its acceleration is a(t) = r''(t).
   a) Express the acceleration in terms of the Frenet frame {T, N, B}.
   b) Identify the tangential and normal components of acceleration.
   c) How does the curvature of the path relate to the normal component of acceleration?
   
   *Hint:* Use the chain rule to relate derivatives with respect to t and derivatives with respect to arc length s.

2. **Problem 1.4.2:** In computer graphics, Bézier curves are commonly used. A cubic Bézier curve has the form:
   r(t) = (1-t)³P₀ + 3(1-t)²tP₁ + 3(1-t)t²P₂ + t³P₃ for t ∈ [0, 1]
   where P₀, P₁, P₂, and P₃ are control points.
   
   a) Show that the curve starts at P₀ and ends at P₃.
   b) Calculate the tangent vectors at the endpoints.
   c) How do the control points P₁ and P₂ influence the shape of the curve?
   
   *Hint:* Calculate r'(0) and r'(1) to find the initial and final tangent directions.

### Exploratory Problems

3. **Problem 1.4.3:** In relativity theory, the path of a particle in spacetime is called its world line. For a particle moving in one spatial dimension, we can represent its world line as a curve (t, x(t)) in the tx-plane.
   
   a) What does the tangent vector to this curve represent physically?
   b) If the particle moves at constant velocity v, what is the curvature of its world line?
   c) For a particle with constant acceleration a, describe its world line and calculate its curvature.
   
   *Starting Point:* For constant velocity, x(t) = vt + x₀. For constant acceleration, x(t) = ½at² + v₀t + x₀.

4. **Problem 1.4.4:** The "curve shortening flow" is a process where each point on a curve moves in the normal direction with speed proportional to the curvature: ∂r/∂t = κN.
   
   a) Explain why this process tends to smooth out irregularities in a curve.
   b) What happens to a circle under this flow?
   c) Research and describe one application of curve shortening flow in image processing or computer vision.
   
   *Starting Point:* Consider what happens at points of high curvature versus points of low curvature.

### Proofcraft Problems

5. **Problem 1.4.5:** The total curvature of a closed curve is defined as ∫κ(s)ds, where the integral is taken over the entire curve. Prove that the total curvature of a simple closed curve in the plane is 2π.
   
   *Milestone 1:* Recall that for a curve parametrized by arc length, T'(s) = κ(s)N(s).
   
   *Milestone 2:* Express the total curvature in terms of the change in the tangent vector as you go around the curve.
   
   *Milestone 3:* Use the fact that the tangent vector makes one complete revolution as you traverse a simple closed curve.

6. **Problem 1.4.6:** The evolute of a curve is the locus of its centers of curvature. For a plane curve r(s) parametrized by arc length, the evolute is given by e(s) = r(s) + (1/κ(s))N(s).
   
   Prove that the tangent to the evolute at e(s) is parallel to the normal N(s) of the original curve.
   
   *Milestone 1:* Calculate the derivative e'(s).
   
   *Milestone 2:* Use the Frenet formulas to simplify this expression.
   
   *Milestone 3:* Show that e'(s) is parallel to N(s).
