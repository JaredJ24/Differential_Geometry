# Chapter 8: Four Vertex Theorem and Applications

## Launch Pad

Imagine tracing your finger along the rim of an oval-shaped plate. As you move, you'll notice that the curve bends more sharply at some points and more gently at others. If you pay careful attention, you'll find exactly four special points where the bending reaches a local maximum or minimum—two points of maximum curvature at the narrow ends, and two points of minimum curvature at the wider sides.

**Big Picture Concept:** In this chapter, we explore the Four Vertex Theorem—a profound result that guarantees any simple closed curve in the plane (other than a circle) must have at least four "vertices" where the curvature reaches a local extreme value. This seemingly simple statement reveals deep connections between local differential properties and global topological constraints. The theorem exemplifies how the requirement that a curve closes smoothly upon itself forces certain patterns in its curvature distribution. As we'll discover, this fundamental result extends to various settings and has far-reaching applications across mathematics and beyond, from computer vision to celestial mechanics. The Four Vertex Theorem serves as a beautiful illustration of how global constraints shape local geometry, a recurring theme throughout differential geometry.

## Prerequisite Bridge

Before we delve into the Four Vertex Theorem and its applications, let's ensure we have the necessary tools from previous chapters and prerequisite subjects.

### Key Prerequisites

**From Chapter 1:** Recall our work with parametrized curves r(t) = (x(t), y(t)) and the concept of regular curves, where the derivative r'(t) is non-zero for all t.

**From Chapter 2:** We explored curvature κ as a measure of how quickly a curve turns at each point. For a curve parametrized by arc length, κ(s) = |T'(s)|, where T(s) is the unit tangent vector.

**From Chapter 7:** We studied total curvature and the Hopf Umlaufsatz, which states that the total curvature of a simple closed curve in the plane is always 2π.

**From Calculus:** We'll need concepts from differential calculus, particularly the analysis of critical points of functions. We'll also use the Mean Value Theorem and related results.

**From Analysis:** We'll use properties of continuous functions on compact intervals, including the existence of maximum and minimum values.

**Notation Alert:** In this chapter, we'll use γ: [a, b] → ℝ² to denote a curve in the plane, and κ(s) to denote the curvature at the point γ(s). We'll use κ'(s) to denote the derivative of curvature with respect to arc length.

## Narrative Spine

### The Historical Quest

The Four Vertex Theorem has a rich history dating back to the early 20th century. It was first proved by Syamadas Mukhopadhyaya in 1909 for convex curves, and later extended to general simple closed curves by Adolf Kneser in 1912.

The theorem emerged during a period of intense interest in the global properties of curves and surfaces. Mathematicians were beginning to understand that local differential properties (like curvature) are often constrained by global topological requirements (like being a closed curve). The Four Vertex Theorem was one of the first and most elegant results in this direction.

### The Key Insight

The breakthrough insight came from recognizing that the curvature function of a closed curve must be periodic, and a continuous periodic function must have at least two local maxima and two local minima (unless it's constant). This simple observation, combined with the fact that a circle is the only curve with constant curvature, leads to the Four Vertex Theorem.

But the deeper insight is that the Four Vertex Theorem is intimately connected to the Hopf Umlaufsatz, which we studied in Chapter 7. The requirement that the total curvature of a simple closed curve is 2π constrains the possible variations of curvature along the curve, forcing the existence of at least four vertices.

### The Modern Perspective

Today, the Four Vertex Theorem is understood as part of a broader family of results in differential geometry that relate local differential properties to global topological constraints. It has been generalized to various settings, including curves on surfaces, curves in higher-dimensional spaces, and even to discrete curves.

The theorem has also found applications in diverse areas, from computer vision and pattern recognition to celestial mechanics and the theory of billiards. It exemplifies the power of differential geometry to reveal deep connections between seemingly disparate fields.

## Core Content

### Section 1: Vertices of Plane Curves

We begin by formalizing the concept of a vertex, which is the central object of study in this chapter.

**Definition 8.1 (Vertex):** A vertex of a plane curve is a point where the derivative of the curvature with respect to arc length is zero: κ'(s) = 0.

Vertices are points where the curvature reaches a local maximum or minimum, or an inflection point where the curvature transitions from increasing to decreasing or vice versa.

**Example 8.2:** For a circle of radius r, the curvature is constant: κ(s) = 1/r. Since κ'(s) = 0 for all s, every point on a circle is a vertex. This is a degenerate case, and it's the only curve where every point is a vertex.

**Example 8.3:** For an ellipse with semi-major axis a and semi-minor axis b, the curvature varies along the curve. The curvature is maximum at the ends of the minor axis and minimum at the ends of the major axis. Therefore, an ellipse has exactly four vertices.

**Theorem 8.4:** If γ is a simple closed curve in the plane with constant curvature, then γ is a circle.

*Proof:* If the curvature is constant, say κ(s) = c, then the total curvature is K = c · L, where L is the length of the curve. By the Hopf Umlaufsatz, K = 2π, so c · L = 2π, which means c = 2π/L.

Now, a curve with constant curvature c is either a circle of radius 1/c or a straight line (if c = 0). Since γ is closed, it can't be a straight line, so it must be a circle of radius 1/c = L/(2π). ■

This theorem tells us that the circle is the only simple closed curve with constant curvature. For any other simple closed curve, the curvature must vary along the curve, which means there must be points where the curvature reaches local extreme values—these are the vertices.

### Section 2: The Four Vertex Theorem

We now state and prove the central result of this chapter.

**Theorem 8.5 (Four Vertex Theorem):** Any simple closed curve in the plane, other than a circle, has at least four vertices.

*Proof:* Let γ be a simple closed curve in the plane, parametrized by arc length, with curvature function κ(s). Since γ is closed, κ(s) is a periodic function with period L, the length of the curve.

If κ(s) is constant, then by Theorem 8.4, γ is a circle. Otherwise, κ(s) is a non-constant continuous periodic function. By calculus, such a function must have at least two local maxima and two local minima on any interval of length equal to its period. At each of these local extrema, κ'(s) = 0, so these points are vertices of γ.

Therefore, γ has at least four vertices. ■

This proof is elegant in its simplicity, relying only on basic properties of continuous periodic functions. But it hides some subtleties. For instance, it assumes that the local extrema of κ(s) are isolated points, which is true for analytic curves but requires more careful analysis for general smooth curves.

**Example 8.6:** As we saw in Example 8.3, an ellipse has exactly four vertices: two at the ends of the minor axis (where the curvature is maximum) and two at the ends of the major axis (where the curvature is minimum).

**Example 8.7:** A limaçon is a curve given in polar coordinates by r = a + b cos θ, where a > b > 0. This curve has exactly four vertices, corresponding to the values of θ where the curvature reaches local extrema.

The Four Vertex Theorem provides a beautiful example of how global topological constraints (being a simple closed curve) impose restrictions on local differential properties (the distribution of curvature). It tells us that no matter how we deform a circle into a non-circular simple closed curve, we'll always create at least four special points where the curvature reaches local extreme values.

### Section 3: Generalizations of the Four Vertex Theorem

The Four Vertex Theorem has been generalized in various ways, extending its insights to different settings.

**Theorem 8.8 (Four Vertex Theorem for Curves on Surfaces):** Let γ be a simple closed curve on a surface, and let κg be the geodesic curvature of γ. If γ is not a geodesic circle (a curve with constant geodesic curvature), then γ has at least four vertices (points where κg'(s) = 0).

*Proof:* The proof is similar to that of the original Four Vertex Theorem, using the fact that the geodesic curvature function κg(s) is periodic and applying the properties of continuous periodic functions. ■

This generalization shows that the Four Vertex Theorem is not just a result about curves in the plane, but a more general phenomenon that applies to curves on arbitrary surfaces.

**Theorem 8.9 (Four Vertex Theorem for Space Curves):** Let γ be a simple closed curve in ℝ³ that lies on a convex surface. Then the curvature function κ(s) of γ has at least four local extrema.

*Proof:* The proof uses techniques from the theory of convex surfaces and the properties of the curvature function of a space curve. ■

This generalization extends the Four Vertex Theorem to curves in three-dimensional space, provided they lie on a convex surface. It shows that the phenomenon of vertices is not restricted to plane curves, but appears in more general settings.

**Theorem 8.10 (Discrete Four Vertex Theorem):** Let P be a simple closed polygon in the plane with n vertices. Then P has at least four "vertices" in the sense of local extrema of the discrete curvature (the exterior angle at each vertex of the polygon).

*Proof:* The proof uses properties of the discrete curvature function and the fact that the sum of the exterior angles of a simple closed polygon is 2π. ■

This generalization shows that the Four Vertex Theorem has a discrete analogue for polygons, where the role of curvature is played by the exterior angle at each vertex. It's another example of how the insights of differential geometry can be extended to discrete settings.

### Section 4: The Tennis Ball Theorem

A beautiful application of the Four Vertex Theorem is the Tennis Ball Theorem, which concerns the curves formed by the seam of a tennis ball.

**Theorem 8.11 (Tennis Ball Theorem):** Any smooth curve on a sphere that divides the sphere into two regions of equal area must have at least four vertices (points where the geodesic curvature has a local extremum).

*Proof:* The proof uses the Four Vertex Theorem for curves on surfaces, along with properties of curves that divide a sphere into regions of equal area. ■

The Tennis Ball Theorem explains why the seam of a tennis ball, which divides the ball into two equal halves, must have at least four points where it bends most sharply. This is a beautiful example of how differential geometry can explain everyday phenomena.

**Example 8.12:** The equator of a sphere has constant geodesic curvature (in fact, zero geodesic curvature), so it doesn't have vertices in the sense of the Tennis Ball Theorem. But any other curve that divides the sphere into two equal halves must have at least four vertices.

### Section 5: The Four Vertex Theorem and Isoperimetric Inequalities

The Four Vertex Theorem has implications for isoperimetric inequalities, which relate the length of a curve to the area it encloses.

**Theorem 8.13 (Isoperimetric Inequality):** If γ is a simple closed curve in the plane with length L and enclosing an area A, then:

4πA ≤ L²

with equality if and only if γ is a circle.

*Proof:* We proved this theorem in Chapter 7 using techniques from the calculus of variations. Here, we note that the Four Vertex Theorem provides an alternative approach: if γ is not a circle, it has at least four vertices, which constrains its shape and leads to the isoperimetric inequality. ■

The isoperimetric inequality tells us that among all simple closed curves with a fixed length, the circle encloses the maximum area. Equivalently, among all simple closed curves enclosing a fixed area, the circle has the minimum length.

**Theorem 8.14 (Bonnesen's Inequality):** If γ is a simple closed curve in the plane with length L and enclosing an area A, and if r and R are the inradius and circumradius of γ, respectively, then:

L² - 4πA ≥ π²(R - r)²

*Proof:* The proof uses the Four Vertex Theorem and properties of the inradius and circumradius. ■

Bonnesen's inequality provides a stronger version of the isoperimetric inequality, giving a lower bound on the "isoperimetric deficit" L² - 4πA in terms of the difference between the circumradius and inradius. This inequality is sharp, with equality holding for a circle (where R = r).

### Section 6: The Four Vertex Theorem and Billiards

The Four Vertex Theorem has applications in the theory of billiards, which studies the motion of a particle bouncing inside a closed curve.

**Theorem 8.15 (Mather's Theorem):** If γ is a simple closed curve in the plane with at least four vertices, then there exists a billiard trajectory inside γ that is not periodic.

*Proof:* The proof uses techniques from dynamical systems theory and the properties of billiard trajectories. ■

Mather's theorem connects the Four Vertex Theorem to the theory of billiards, showing that the existence of vertices in a curve has implications for the dynamics of particles bouncing inside the curve. It's a beautiful example of how differential geometry can inform our understanding of physical systems.

**Example 8.16:** For an elliptical billiard table, which has exactly four vertices, there are both periodic and non-periodic trajectories. The periodic trajectories include those that pass through the foci of the ellipse.

## Visualization Pipeline

### Geometric Sketch: Vertices of an Ellipse

[*Imagine a hand-drawn ellipse with its four vertices marked: two at the ends of the major axis (where the curvature is minimum) and two at the ends of the minor axis (where the curvature is maximum). Arrows indicate the direction of increasing and decreasing curvature along the ellipse.*]

**What to Notice:** The Four Vertex Theorem guarantees that any simple closed curve in the plane, other than a circle, has at least four vertices—points where the curvature reaches a local maximum or minimum. For an ellipse, these vertices are located at the ends of the major and minor axes. The curvature is maximum at the ends of the minor axis, where the ellipse bends most sharply, and minimum at the ends of the major axis, where the ellipse is flattest.

### Dynamic Analogy: The Roller Coaster

Imagine a roller coaster track that forms a closed loop. As you ride the roller coaster, you experience varying levels of "tightness" in the turns—this corresponds to the curvature of the track. The Four Vertex Theorem tells us that there must be at least four points along the track where the tightness reaches a local maximum or minimum.

Think of it this way: as you traverse the loop, you must encounter at least two points where the turns are locally the tightest (local maxima of curvature) and at least two points where the turns are locally the gentlest (local minima of curvature). This is true regardless of the specific shape of the roller coaster loop, as long as it's not a perfect circle.

**Why This Works:** This analogy captures the essence of the Four Vertex Theorem in a visceral way. The varying tightness of the roller coaster turns corresponds to the varying curvature along a closed curve. The theorem guarantees that there must be at least four points where this tightness reaches a local extreme value.

### Coordinate-Free Mnemonic: "Four Extremes for Every Closed Curve"

Any simple closed curve in the plane, other than a circle, must have at least four points where the curvature reaches a local maximum or minimum.

**Remember This Because:** This mnemonic emphasizes the key content of the Four Vertex Theorem in a way that doesn't depend on coordinates or specific geometric properties. It focuses on the topological essence of the result: the constraint that a simple closed curve must have at least four vertices.

## Interleaved Problem Set 1: The Four Vertex Theorem and Its Generalizations

### Foundational Problems

1. **Problem 8.1.1:** Verify that an ellipse with semi-major axis a and semi-minor axis b has exactly four vertices, located at the ends of the major and minor axes.
   
   *Hint:* Find the curvature of the ellipse as a function of the parameter, and determine where its derivative is zero.

2. **Problem 8.1.2:** Prove that a circle is the only simple closed curve in the plane with constant curvature.
   
   *Hint:* Use the Hopf Umlaufsatz and the fact that the total curvature of a simple closed curve is 2π.

### Exploratory Problem

**Problem 8.1.3:** Investigate the vertices of the limaçon curve given in polar coordinates by r = a + b cos θ, where a > b > 0. How many vertices does this curve have, and where are they located?

*Starting Point:* Find the curvature of the limaçon as a function of θ, and determine where its derivative is zero.

### Proofcraft Problem

**Problem 8.1.4:** Prove that any simple closed curve in the plane that has reflective symmetry across a line has at least six vertices, unless it's a circle.

*Milestone 1:* Show that if a curve has reflective symmetry across a line, then the curvature function has a corresponding symmetry.

*Milestone 2:* Use the symmetry of the curvature function to show that if there's a local extremum of curvature at a point, there's a corresponding local extremum at the reflected point.

*Milestone 3:* Apply the Four Vertex Theorem to show that there must be at least six vertices in total.

## Core Content (Continued)

### Section 7: The Four Vertex Theorem and Celestial Mechanics

The Four Vertex Theorem has surprising applications in celestial mechanics, particularly in the study of planetary orbits.

**Theorem 8.17 (Bertrand's Theorem):** The only central force fields that allow all bounded orbits to be closed are the inverse-square field (like gravity) and the linear field (like a spring).

*Proof:* The complete proof is beyond our scope, but it involves analyzing the conditions under which a central force field produces closed orbits. The Four Vertex Theorem plays a role in constraining the possible shapes of these orbits. ■

Bertrand's theorem is a remarkable result in celestial mechanics that explains why planetary orbits are ellipses (a consequence of the inverse-square nature of gravity). The connection to the Four Vertex Theorem comes through the analysis of the curvature of these orbits.

**Example 8.18:** In an inverse-square force field (like gravity), the orbits are conic sections: ellipses, parabolas, or hyperbolas. For elliptical orbits, the Four Vertex Theorem guarantees at least four vertices, which correspond to the points of maximum and minimum distance from the focus (the perihelion and aphelion) and the points of maximum and minimum angular velocity.

### Section 8: The Four Vertex Theorem and Computer Vision

The Four Vertex Theorem has applications in computer vision and pattern recognition, particularly in the analysis of shape.

**Definition 8.19 (Curvature Scale Space):** The curvature scale space of a curve is a multi-scale representation that tracks the evolution of the curve's vertices as the curve is progressively smoothed.

The curvature scale space provides a way to analyze the shape of a curve at different levels of detail. The Four Vertex Theorem guarantees that any simple closed curve (other than a circle) has at least four vertices, which appear as features in the curvature scale space.

**Theorem 8.20:** The curvature scale space of a simple closed curve in the plane, other than a circle, contains at least four branches corresponding to the evolution of the curve's vertices under smoothing.

*Proof:* The proof uses the Four Vertex Theorem and properties of the heat equation, which governs the smoothing process. ■

This theorem shows how the Four Vertex Theorem informs the analysis of shape in computer vision. The vertices of a curve serve as landmark points that can be tracked across different scales, providing a robust representation of the curve's shape.

**Example 8.21:** In object recognition, the curvature scale space is used to match shapes across different views and scales. The Four Vertex Theorem guarantees that any simple closed contour has at least four distinctive features (vertices) that can serve as reference points for matching.

### Section 9: The Four Vertex Theorem and the Evolute

The Four Vertex Theorem has implications for the evolute of a curve, which is the locus of its centers of curvature.

**Definition 8.22 (Evolute):** The evolute of a curve γ is the curve formed by the centers of curvature of γ. If γ is parametrized by arc length, with unit tangent T(s) and unit normal N(s), then the evolute is given by:

E(s) = γ(s) + (1/κ(s)) · N(s)

where κ(s) is the curvature at γ(s).

**Theorem 8.23:** The evolute of a simple closed curve in the plane, other than a circle, has at least four cusps, corresponding to the vertices of the original curve.

*Proof:* At a vertex of γ, where κ'(s) = 0, the evolute has a cusp. By the Four Vertex Theorem, γ has at least four vertices, so the evolute has at least four cusps. ■

This theorem connects the Four Vertex Theorem to the geometry of the evolute, showing that the vertices of a curve correspond to distinctive features (cusps) in its evolute.

**Example 8.24:** The evolute of an ellipse is an astroid, a curve with exactly four cusps. These cusps correspond to the four vertices of the ellipse.

## Visualization Pipeline (Continued)

### Geometric Sketch: The Evolute of an Ellipse

[*Imagine a hand-drawn ellipse with its evolute (an astroid) inside it. The four cusps of the astroid are marked, corresponding to the four vertices of the ellipse. Arrows connect each vertex of the ellipse to the corresponding cusp of the evolute.*]

**What to Notice:** The evolute of a curve is the locus of its centers of curvature. For an ellipse, the evolute is an astroid—a curve with exactly four cusps. These cusps correspond to the four vertices of the ellipse, where the curvature reaches a local maximum or minimum. The Four Vertex Theorem guarantees that any simple closed curve (other than a circle) has at least four vertices, so its evolute has at least four cusps.

### Dynamic Analogy: The Shadow Puppet

Imagine creating a shadow puppet of a rabbit on the wall. As you move your hands to change the shape of the rabbit's outline, the shadow forms a simple closed curve. The Four Vertex Theorem tells us that no matter how you shape your hands, as long as the shadow forms a simple closed curve (and not a perfect circle), there will always be at least four points along the outline where the curvature reaches a local maximum or minimum.

These four (or more) special points might correspond to the tips of the rabbit's ears, the curve of its back, or the roundness of its belly. But the key insight is that you cannot create a simple closed shadow without having at least four such distinctive points—it's a mathematical impossibility!

**Why This Works:** This analogy captures the universality of the Four Vertex Theorem. No matter how we deform a simple closed curve, as long as it's not a perfect circle, it must have at least four vertices. The shadow puppet provides a tangible way to visualize this constraint on the possible shapes of simple closed curves.

## Interleaved Problem Set 2: Applications of the Four Vertex Theorem

### Foundational Problems

1. **Problem 8.2.1:** Find the evolute of the ellipse x²/a² + y²/b² = 1, and verify that it has exactly four cusps corresponding to the four vertices of the ellipse.
   
   *Hint:* Use the formula for the evolute in terms of the curve's parametrization and its curvature.

2. **Problem 8.2.2:** Verify Bonnesen's inequality for a rectangle with length a and width b.
   
   *Hint:* Calculate the length, area, inradius, and circumradius of the rectangle, and check whether the inequality holds.

### Exploratory Problem

**Problem 8.2.3:** Investigate the relationship between the Four Vertex Theorem and the isoperimetric quotient of a curve. The isoperimetric quotient is defined as 4πA/L², where A is the area enclosed by the curve and L is its length.

*Starting Point:* Consider how the isoperimetric quotient varies as a curve is deformed, and how the vertices of the curve relate to this variation.

### Proofcraft Problem

**Problem 8.2.4:** Prove that if a simple closed curve in the plane has exactly four vertices, then it has reflective symmetry across at least one line.

*Milestone 1:* Show that if a curve has exactly four vertices, then the curvature function has exactly two local maxima and two local minima.

*Milestone 2:* Use properties of continuous periodic functions to show that the two local maxima must have the same value, and the two local minima must have the same value.

*Milestone 3:* Use the equality of the extreme values to establish the reflective symmetry of the curve.

## Easter Eggs for Experts

**For Dynamical Systems Enthusiasts:** The Four Vertex Theorem has connections to the theory of integrable billiards. A billiard inside an ellipse is integrable, meaning that the motion of the billiard ball can be described in terms of conserved quantities. This integrability is related to the fact that an ellipse has exactly four vertices. More generally, the number and location of vertices of a curve influence the dynamics of a billiard inside the curve, with implications for chaos theory and the study of ergodic systems.

**Historical Depth:** The Four Vertex Theorem was first proved by Syamadas Mukhopadhyaya in 1909, but only for convex curves. The extension to general simple closed curves was accomplished by Adolf Kneser in 1912. The theorem has since been generalized in various directions, including to curves on surfaces (by Jackson), to space curves (by Sedykh), and to discrete curves (by Fuchs and Tabachnikov). Each generalization reveals new connections between differential geometry and other areas of mathematics.

**Advanced Perspective:** In modern differential geometry, the Four Vertex Theorem is understood as a special case of more general results about the topology of the space of immersions of the circle into the plane. The space of immersions has a rich structure, and the Four Vertex Theorem constrains the possible paths through this space. This perspective connects the theorem to the study of moduli spaces and the calculus of variations.

## Cross-Pollination

### Real-World Application: Computer-Aided Design and Manufacturing

The Four Vertex Theorem has applications in computer-aided design (CAD) and manufacturing, particularly in the design of curves and surfaces. When designing a curve for aesthetic or functional purposes, engineers often need to control the distribution of curvature along the curve. The Four Vertex Theorem provides constraints on what's possible: any simple closed curve (other than a circle) must have at least four points where the curvature reaches a local extreme value.

For example, in automotive design, the silhouette of a car is a simple closed curve. The Four Vertex Theorem guarantees that this silhouette must have at least four points where the curvature reaches a local maximum or minimum. These points often correspond to distinctive features of the car's design, such as the curve of the hood, the slope of the windshield, the line of the roof, and the shape of the trunk. Understanding these constraints helps designers create aesthetically pleasing and aerodynamically efficient shapes.

### Interdisciplinary Connection: Optics and Caustics

In optics, the Four Vertex Theorem has implications for the study of caustics—the envelopes of light rays reflected or refracted by a curved surface. The caustic of a curve is closely related to its evolute, and the Four Vertex Theorem constrains the possible shapes of caustics.

For instance, when light reflects off the inside of a coffee cup, it forms a caustic on the surface of the coffee. The shape of this caustic depends on the curvature of the cup, and the Four Vertex Theorem guarantees that the caustic has at least four distinctive features (cusps) if the cup's cross-section is not a perfect circle. This connection between differential geometry and optics helps explain the beautiful patterns of light we observe in everyday phenomena.

### Modern Research Direction: Quantum Billiards and Quantum Chaos

The Four Vertex Theorem has connections to the study of quantum billiards and quantum chaos. In quantum mechanics, a particle confined to a region (like a billiard inside a curve) is described by a wave function that satisfies the Schrödinger equation with appropriate boundary conditions. The behavior of this wave function—specifically, the distribution of its energy levels—depends on the shape of the boundary.

Recent research has explored how the vertices of the boundary curve influence the quantum properties of the system. The Four Vertex Theorem constrains the possible shapes of the boundary, which in turn constrains the possible quantum behaviors. This connection between classical differential geometry and quantum physics provides insights into the quantum-classical correspondence and the emergence of chaos in quantum systems.

## Metacognitive Checklists

### Self-Assessment

Can you:
- State and explain the Four Vertex Theorem?
- Identify the vertices of specific curves, like ellipses and limaçons?
- Explain the connection between the Four Vertex Theorem and the evolute of a curve?
- Apply the Four Vertex Theorem to problems in isoperimetric inequalities, billiards, and computer vision?
- Generalize the Four Vertex Theorem to curves on surfaces and space curves?

### Conceptual Red Flags

Watch out if:
- You think the Four Vertex Theorem applies to all curves—it specifically applies to simple closed curves in the plane—revisit Section 8.2.
- You confuse vertices (where κ'(s) = 0) with points of zero curvature (where κ(s) = 0)—these are different concepts—revisit Section 8.1.
- You believe the Four Vertex Theorem implies that a curve has exactly four vertices—it guarantees at least four vertices, but a curve can have more—revisit Section 8.2.
- You think the vertices of a curve must be evenly spaced or symmetrically arranged—the theorem only constrains the number of vertices, not their distribution—revisit Section 8.2.

## Chapter Summary

### Key Takeaways

1. The Four Vertex Theorem states that any simple closed curve in the plane, other than a circle, has at least four vertices—points where the curvature reaches a local maximum or minimum.

2. The theorem is a consequence of the fact that the curvature function of a closed curve is periodic, and a continuous periodic function must have at least two local maxima and two local minima (unless it's constant).

3. The Four Vertex Theorem has been generalized to curves on surfaces, space curves, and discrete curves, showing that the phenomenon of vertices is not restricted to plane curves.

4. The theorem has applications in diverse areas, including isoperimetric inequalities, billiards, celestial mechanics, computer vision, and the study of evolutes and caustics.

5. The Four Vertex Theorem exemplifies how global topological constraints (being a simple closed curve) impose restrictions on local differential properties (the distribution of curvature).

### Looking Ahead

In the next chapter, we'll explore connections and parallel transport, which provide a framework for comparing vectors at different points on a manifold. This will deepen our understanding of curvature and prepare us for the study of curvature tensors in Chapter 10.
