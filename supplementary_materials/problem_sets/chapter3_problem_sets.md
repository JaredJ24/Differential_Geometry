# Additional Interleaved Problem Sets for Chapter 3

## Problem Set 3.3: Minkowski Geometry and Special Relativity

### Foundational Problems

1. **Problem 3.3.1:** Consider the following events in the Minkowski plane:
   - Event A: (0, 0)
   - Event B: (3, 4)
   - Event C: (4, 3)
   - Event D: (5, 5)
   
   a) Calculate the Minkowski interval between each pair of events.
   b) Classify each interval as timelike, spacelike, or lightlike.
   c) Determine which events could have a cause-effect relationship with event A.
   
   *Hint:* The Minkowski interval between events (t₁, x₁) and (t₂, x₂) is (t₂ - t₁)² - (x₂ - x₁)².

2. **Problem 3.3.2:** A particle moves along the worldline r(τ) = (cosh τ, sinh τ) in the Minkowski plane, where τ is the proper time.
   
   a) Show that this worldline satisfies ⟨r'(τ), r'(τ)⟩ₘ = 1, confirming it is a timelike curve.
   b) Calculate the Minkowski curvature κₘ(τ).
   c) Interpret the physical meaning of this worldline in the context of special relativity.
   
   *Hint:* For a timelike curve parametrized by proper time, the Minkowski curvature measures the proper acceleration.

### Exploratory Problems

3. **Problem 3.3.3:** Investigate the "twin paradox" using the Minkowski plane.
   
   a) Draw the worldlines of two twins: one who stays on Earth and one who travels at 0.8c to a star 4 light-years away and then returns to Earth.
   b) Calculate the proper time experienced by each twin.
   c) Explain why the traveling twin ages less, using the geometry of the Minkowski plane.
   
   *Starting Point:* The worldline of the Earth-bound twin is a straight vertical line. The worldline of the traveling twin consists of two straight segments with different slopes.

4. **Problem 3.3.4:** Explore the concept of simultaneity in special relativity using the Minkowski plane.
   
   a) In the rest frame of observer A, events at (1, 0) and (1, 2) occur simultaneously. Find the coordinates of these events in the frame of observer B, who moves at speed v = 0.6c relative to A.
   b) Are these events simultaneous in observer B's frame? If not, which one occurs first?
   c) Illustrate this scenario in the Minkowski plane, showing the lines of simultaneity for both observers.
   
   *Starting Point:* Apply a Lorentz transformation with rapidity φ = tanh⁻¹(0.6) to the coordinates of the events.

### Proofcraft Problems

5. **Problem 3.3.5:** Prove that the proper time along a timelike curve between two events is maximized when the curve is a geodesic (straight line in the Minkowski plane).
   
   *Milestone 1:* Set up the proper time functional for a timelike curve r(t) = (t, x(t)) between events (t₁, x₁) and (t₂, x₂).
   
   *Milestone 2:* Apply the Euler-Lagrange equation to find the curve that extremizes this functional.
   
   *Milestone 3:* Show that the extremal curve is a straight line, and verify that it maximizes (not minimizes) the proper time.

6. **Problem 3.3.6:** Prove that the composition of two Lorentz transformations with rapidities φ₁ and φ₂ is another Lorentz transformation with rapidity φ₁ + φ₂.
   
   *Milestone 1:* Write out the matrices for Lorentz transformations with rapidities φ₁ and φ₂.
   
   *Milestone 2:* Multiply these matrices to find their composition.
   
   *Milestone 3:* Show that the resulting matrix has the form of a Lorentz transformation with rapidity φ₁ + φ₂, using the addition formulas for hyperbolic functions.

## Problem Set 3.4: Hyperboloid Model and Hyperbolic Geometry

### Foundational Problems

1. **Problem 3.4.1:** Consider the hyperboloid model of the hyperbolic plane:
   
   H = {(t, x, y) ∈ ℝ¹⁺² : t² - x² - y² = 1, t > 0}
   
   a) Show that the curve γ(s) = (cosh s, sinh s, 0) lies on H.
   b) Calculate the tangent vector γ'(s) and verify that it is a unit vector with respect to the induced metric.
   c) Find the geodesic curvature of γ(s) in H.
   
   *Hint:* The induced metric on H is ds² = dt² - dx² - dy², restricted to tangent vectors of H.

2. **Problem 3.4.2:** In the hyperboloid model of the hyperbolic plane:
   
   a) Find the distance between the points (1, 0, 0) and (cosh d, sinh d, 0) on H.
   b) Show that the distance formula in the hyperbolic plane is d(p, q) = cosh⁻¹(-⟨p, q⟩ₘ), where p and q are points on H and ⟨·,·⟩ₘ is the Minkowski inner product.
   c) Compare this with the distance formula in Euclidean geometry.
   
   *Hint:* The distance between two points on H is measured along a geodesic connecting them.

### Exploratory Problems

3. **Problem 3.4.3:** Investigate the concept of "parallel" geodesics in the hyperbolic plane.
   
   a) In the hyperboloid model, find two geodesics that never intersect.
   b) Calculate the minimum distance between these geodesics.
   c) How does this differ from parallel lines in Euclidean geometry?
   
   *Starting Point:* Geodesics in the hyperboloid model are the intersections of H with planes through the origin in ℝ¹⁺².

4. **Problem 3.4.4:** Explore the concept of a "circle" in the hyperbolic plane.
   
   a) Define what a circle of radius r centered at point p means in the hyperbolic plane.
   b) In the hyperboloid model, find the equation of a circle of radius 1 centered at the point (1, 0, 0).
   c) Calculate the circumference and area of this circle, and compare with the formulas for a circle in Euclidean geometry.
   
   *Starting Point:* A circle in the hyperbolic plane is the set of all points at a fixed distance from a given center point.

### Proofcraft Problems

5. **Problem 3.4.5:** Prove that the area of a triangle in the hyperbolic plane is A = π - (α + β + γ), where α, β, and γ are the interior angles of the triangle.
   
   *Milestone 1:* Use the Gauss-Bonnet theorem, which relates the integral of the Gaussian curvature over a region to the boundary behavior.
   
   *Milestone 2:* Show that the Gaussian curvature of the hyperbolic plane is constant and equal to -1.
   
   *Milestone 3:* Apply the theorem to a triangle and interpret the result.

6. **Problem 3.4.6:** Prove that there are infinitely many distinct parallel geodesics to a given geodesic through a point not on the geodesic in the hyperbolic plane.
   
   *Milestone 1:* In the hyperboloid model, represent a geodesic as the intersection of H with a plane through the origin.
   
   *Milestone 2:* For a point p not on this geodesic, characterize the set of all geodesics through p that do not intersect the given geodesic.
   
   *Milestone 3:* Show that this set has infinitely many elements, and explain how this violates Euclid's fifth postulate.

## Problem Set 3.5: Applications of Minkowski Geometry

### Foundational Problems

1. **Problem 3.5.1:** In special relativity, the energy E and momentum p of a particle with rest mass m₀ moving at velocity v are given by:
   
   E = γm₀c²
   p = γm₀v
   
   where γ = 1/√(1-v²/c²) is the Lorentz factor and c is the speed of light.
   
   a) Show that these quantities satisfy the relation E² - (pc)² = (m₀c²)².
   b) Interpret this relation in terms of the Minkowski norm of the four-momentum vector (E/c, p).
   c) What does this relation tell us about massless particles like photons?
   
   *Hint:* The four-momentum of a particle is a timelike vector for massive particles and a lightlike vector for massless particles.

2. **Problem 3.5.2:** The Doppler effect in special relativity describes how the frequency of light changes when observed from different reference frames.
   
   a) Derive the relativistic Doppler shift formula: f' = f√((1+v/c)/(1-v/c)) for light emitted along the direction of motion.
   b) Express this formula in terms of the rapidity φ of the Lorentz transformation.
   c) Compare this with the classical Doppler effect formula and explain the differences.
   
   *Hint:* Consider a light wave with four-wavevector k = (ω/c, k) in one frame, and apply a Lorentz transformation.

### Exploratory Problems

3. **Problem 3.5.3:** Investigate the concept of "proper acceleration" in the Minkowski plane.
   
   a) For a particle moving along a timelike curve r(τ) parametrized by proper time, define the proper acceleration as a(τ) = r''(τ).
   b) Show that ⟨a(τ), r'(τ)⟩ₘ = 0, meaning the proper acceleration is always orthogonal to the four-velocity.
   c) For a particle moving with constant proper acceleration α in the x-direction, find its worldline r(τ).
   
   *Starting Point:* The condition of constant proper acceleration means |⟨a(τ), a(τ)⟩ₘ| = α².

4. **Problem 3.5.4:** Explore the "Rindler coordinates" in the Minkowski plane, which describe the perspective of a constantly accelerating observer.
   
   a) The Rindler coordinates (η, ξ) are related to Minkowski coordinates (t, x) by t = ξ sinh η and x = ξ cosh η. Show that lines of constant ξ represent worldlines of constantly accelerating observers.
   b) Calculate the proper acceleration of an observer at constant ξ.
   c) Investigate the "Rindler horizon" at x = t and explain its significance for accelerating observers.
   
   *Starting Point:* The Minkowski metric in Rindler coordinates takes the form ds² = ξ²dη² - dξ².

### Proofcraft Problems

5. **Problem 3.5.5:** Prove the "clock hypothesis" in special relativity, which states that the proper time measured by an accelerating clock depends only on its instantaneous velocity, not on its acceleration.
   
   *Milestone 1:* For a clock moving along a timelike curve r(t) = (t, x(t)), express the proper time in terms of the coordinate time t.
   
   *Milestone 2:* Show that this expression depends only on the velocity dx/dt, not on the acceleration d²x/dt².
   
   *Milestone 3:* Discuss the implications of this result for the twin paradox and for gravitational time dilation in general relativity.

6. **Problem 3.5.6:** Prove that the set of all events that can be influenced by a given event (its future light cone) forms a convex set in the Minkowski plane.
   
   *Milestone 1:* Define precisely what it means for an event to be in the future light cone of another event.
   
   *Milestone 2:* For any two events in the future light cone of a given event, show that any convex combination of these events is also in the future light cone.
   
   *Milestone 3:* Discuss the physical interpretation of this result in terms of causality in special relativity.
