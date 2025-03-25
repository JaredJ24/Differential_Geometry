# Chapter 6: Closed Curves and the Jordan Curve Theorem

## Connections to Previous Material

In our journey through differential geometry, we've built a foundation that now allows us to explore the fascinating global properties of closed curves. Let's connect this chapter's content with what we've learned previously:

**From Chapter 1:** We began with the fundamental concepts of parametrized curves and their properties. The regular curves we studied—where r'(t) ≠ 0—form the building blocks for the closed curves we'll examine in this chapter. The arc length parametrization we developed will be particularly useful when we discuss the isoperimetric inequality.

**From Chapter 2:** Our exploration of curvature as a local property measuring how quickly a curve turns now extends to global results. The total curvature of a simple closed curve being 2π (which we'll revisit in the Gauss-Bonnet Theorem) connects local differential properties to global topological ones.

**From Chapters 3-4:** The Frenet frame and torsion concepts, while primarily focused on space curves, provide important context for understanding plane curves as a special case where torsion vanishes. The Fundamental Theorem of Curves from Chapter 4 gives us existence and uniqueness results that complement the classification theorems we'll encounter in this chapter.

**From Chapter 5:** Our work with periodic functions and degree theory directly supports this chapter's exploration of winding numbers and the Jordan Curve Theorem. The Brouwer Fixed Point Theorem we studied will reappear as both an application of and a tool for proving the Jordan Curve Theorem.

This chapter represents a significant shift in perspective—from studying local differential properties to examining global topological properties. We'll see how seemingly intuitive results like "a simple closed curve divides the plane into inside and outside regions" require sophisticated mathematics to prove rigorously, highlighting the deep connection between differential geometry and topology.

## Launch Pad

Imagine tracing your finger along the outline of a leaf. You start at a point, follow the edge, and eventually return to where you began. This simple act—following a closed path that doesn't intersect itself—embodies one of the most intuitive yet profound concepts in mathematics: a simple closed curve.

**Big Picture Concept:** In this chapter, we explore the remarkable properties of closed curves, culminating in the Jordan Curve Theorem—a result so seemingly obvious that it was once accepted without proof, yet so subtle that its rigorous demonstration requires sophisticated mathematics. The theorem states that a simple closed curve in the plane divides the plane into exactly two regions: an "inside" and an "outside." While this may seem self-evident from everyday experience, proving it rigorously reveals deep connections between geometry, topology, and analysis. The Jordan Curve Theorem serves as a gateway to understanding how curves organize space, a fundamental question that resonates throughout mathematics from algebraic topology to complex analysis and beyond.

## Prerequisite Bridge

Before we delve into closed curves and the Jordan Curve Theorem, let's ensure we have the necessary tools from previous chapters and prerequisite subjects.

### Key Prerequisites

**From Chapter 1:** Recall our work with parametrized curves r(t) = (x(t), y(t)) and the concept of regular curves, where the derivative r'(t) is non-zero for all t.

**From Chapter 2:** We explored curvature κ as a measure of how quickly a curve turns, and we saw that the total curvature of a simple closed curve in the plane is 2π.

**From Chapter 5:** We studied periodic functions, degree theory, and winding numbers. Remember that the winding number counts how many times a closed curve winds around a point, with counterclockwise loops contributing positively and clockwise loops contributing negatively.

**From Topology:** We'll need basic concepts of point-set topology, including open and closed sets, connectedness, and compactness. We'll also use the concept of a homeomorphism—a continuous bijection with a continuous inverse.

**From Complex Analysis:** We'll occasionally use the language of complex numbers to simplify our discussion of plane curves. Recall that a complex number z = x + iy can be identified with the point (x, y) in the plane.

**Notation Alert:** In this chapter, we'll use γ: [a, b] → ℝ² to denote a curve in the plane, and we'll often identify ℝ² with the complex plane ℂ. We'll use int(γ) to denote the interior of a simple closed curve γ, and ext(γ) to denote its exterior.

## Narrative Spine

### The Historical Quest

The Jordan Curve Theorem is named after the French mathematician Camille Jordan, who first stated and attempted to prove it in his 1887 work "Cours d'analyse." However, Jordan's proof was later found to be incomplete, highlighting the surprising depth of this seemingly intuitive result.

The quest for a rigorous proof of the Jordan Curve Theorem spans more than a century and involves some of the most brilliant mathematicians of their time. It touches on fundamental questions about the nature of curves, the structure of the plane, and the foundations of topology.

### The Key Insight

The breakthrough insight came with the realization that the Jordan Curve Theorem is fundamentally a topological result, not a geometric one. It doesn't depend on the smoothness or regularity of the curve, but only on its continuity and the fact that it doesn't intersect itself.

This shift in perspective—from seeing curves as geometric objects defined by equations to viewing them as topological entities defined by their connectivity properties—opened the door to powerful new techniques. It also revealed connections to other areas of mathematics, including algebraic topology, where tools like the Brouwer Fixed Point Theorem (which we encountered in Chapter 5) play a crucial role.

### The Modern Perspective

Today, the Jordan Curve Theorem is understood as a special case of more general results in dimension theory and algebraic topology. It exemplifies the power of topological thinking, where properties that are invariant under continuous deformations reveal deep truths about the structure of space.

The theorem has been generalized to higher dimensions (the Jordan-Brouwer Separation Theorem) and to more general spaces (the Schoenflies Theorem). It continues to inspire research in areas ranging from computational geometry to dynamical systems, demonstrating how a seemingly simple question about curves can lead to profound mathematical insights.

## Core Content

### Section 1: Simple Closed Curves

We begin by formalizing the concept of a simple closed curve, which is the main object of study in this chapter.

**Definition 6.1 (Simple Closed Curve):** A simple closed curve in the plane is a continuous function γ: [a, b] → ℝ² such that:
1. γ(a) = γ(b) (closed)
2. γ is injective on [a, b) (simple, i.e., no self-intersections)

Alternatively, a simple closed curve can be defined as a continuous bijection from the unit circle S¹ to a subset of the plane.

**Example 6.2:** The unit circle γ(t) = (cos t, sin t) for t ∈ [0, 2π] is a simple closed curve. The figure-eight curve γ(t) = (sin 2t, sin t) for t ∈ [0, 2π] is closed but not simple, as it has a self-intersection at the origin.

**Theorem 6.3 (Invariance of Domain):** If U is an open subset of ℝⁿ and f: U → ℝⁿ is a continuous injective function, then f(U) is open in ℝⁿ and f is a homeomorphism onto its image.

*Proof:* The complete proof is beyond our scope, but it relies on the Brouwer Fixed Point Theorem and the fact that a continuous bijection from a compact space to a Hausdorff space is a homeomorphism. ■

This theorem has an important corollary for our study of curves:

**Corollary 6.4:** A simple closed curve in the plane is homeomorphic to the unit circle S¹.

*Proof:* By definition, a simple closed curve is the image of a continuous bijection from S¹ to the plane. Since S¹ is compact and the plane is Hausdorff, this bijection is a homeomorphism onto its image. ■

This corollary tells us that, from a topological perspective, all simple closed curves are the same—they're just deformed circles. This is a powerful insight that allows us to transfer properties from the circle to arbitrary simple closed curves.

### Section 2: The Jordan Curve Theorem

We now state and prove the central result of this chapter.

**Theorem 6.5 (Jordan Curve Theorem):** A simple closed curve γ in the plane divides the plane into exactly two connected components: a bounded component (the interior) and an unbounded component (the exterior). The curve γ is the boundary of each component.

*Proof:* The complete proof is quite involved, but we'll outline the main steps:

1. First, we prove the theorem for polygonal curves (curves consisting of finitely many line segments). This case can be handled by induction on the number of segments.

2. Next, we approximate an arbitrary simple closed curve by polygonal curves. By the Invariance of Domain, the approximation can be made arbitrarily close to the original curve.

3. We show that the number of connected components of the complement of a simple closed curve is invariant under small perturbations of the curve.

4. Finally, we prove that the complement has exactly two connected components by showing that any point not on the curve can be connected by a path to either a point very close to the curve (which must be in the same component as the exterior of a sufficiently close polygonal approximation) or to a point very far from the curve (which must be in the exterior).

The details of this proof require techniques from algebraic topology, including the concept of the winding number, which we studied in Chapter 5. ■

**Corollary 6.6:** If γ is a simple closed curve in the plane, then the interior of γ is homeomorphic to the open unit disk, and the closure of the interior is homeomorphic to the closed unit disk.

*Proof:* This is the Schoenflies Theorem, which strengthens the Jordan Curve Theorem. The proof uses techniques from complex analysis, including the Riemann Mapping Theorem. ■

The Jordan Curve Theorem and its corollary tell us that, from a topological perspective, the interior of any simple closed curve is just a deformed disk. This is a remarkable result that highlights the power of topological thinking.

### Section 3: Winding Number and the Jordan Curve Theorem

The winding number, which we introduced in Chapter 5, provides an alternative approach to understanding the Jordan Curve Theorem.

**Definition 6.7 (Winding Number):** Let γ: [a, b] → ℝ² \ {p} be a closed curve that doesn't pass through the point p. The winding number of γ around p, denoted W(γ, p), is the number of times γ winds around p, counted with sign (positive for counterclockwise, negative for clockwise).

**Theorem 6.8:** If γ is a simple closed curve in the plane, then W(γ, p) = 1 for all points p in the interior of γ, and W(γ, p) = 0 for all points p in the exterior of γ.

*Proof:* For a simple closed curve, the winding number is constant on each connected component of the complement of the curve (by the continuity of the winding number). Since the winding number is 0 for points sufficiently far from the curve, it must be 0 for all points in the unbounded component (the exterior).

For points in the bounded component (the interior), we can show that the winding number is ±1 by considering a ray from p to infinity, counting the number of times the curve crosses this ray, and determining the direction of each crossing. For a simple closed curve, the net count is ±1, and by convention, we orient the curve so that the winding number is +1 for interior points. ■

This theorem provides an alternative characterization of the interior and exterior of a simple closed curve in terms of the winding number. It also connects the Jordan Curve Theorem to complex analysis, where the winding number appears in the Cauchy Integral Formula and the Argument Principle.

### Section 4: Applications of the Jordan Curve Theorem

The Jordan Curve Theorem has numerous applications in mathematics and beyond. Here, we explore a few of them.

**Theorem 6.9 (Brouwer Fixed Point Theorem for the Disk):** Any continuous function f: D² → D² from the closed unit disk to itself has a fixed point.

*Proof:* We proved this theorem in Chapter 5 using degree theory. Here, we give an alternative proof using the Jordan Curve Theorem:

Suppose f has no fixed point. Then for each x ∈ D², we can define a ray from f(x) through x, extending to the boundary of the disk. Let g(x) be the point where this ray intersects the boundary. This defines a continuous function g: D² → S¹ such that g(x) = x for all x ∈ S¹.

But this contradicts the No Retraction Theorem, which states that there is no continuous map from the disk to its boundary that fixes every point on the boundary. The No Retraction Theorem, in turn, can be proved using the Jordan Curve Theorem. ■

**Theorem 6.10 (Fundamental Theorem of Algebra):** Every non-constant polynomial with complex coefficients has at least one complex root.

*Proof:* Let p(z) = aₙzⁿ + aₙ₋₁zⁿ⁻¹ + ... + a₁z + a₀ be a polynomial of degree n ≥ 1. For sufficiently large |z|, the term aₙzⁿ dominates, so p(z) ≈ aₙzⁿ. This means that for a large circle γ centered at the origin, the image p(γ) winds n times around the origin.

If p has no roots, then p(z) ≠ 0 for all z, so we can define a continuous function f(z) = p(z)/|p(z)| from the complex plane to the unit circle. But this means that the winding number of p(γ) around the origin is 0, which contradicts our earlier observation that it should be n. Therefore, p must have at least one root. ■

### Section 5: The Rotation Number and the Whitney-Graustein Theorem

For regular closed curves, we can define the rotation number, which measures how many times the tangent vector rotates as we traverse the curve.

**Definition 6.11 (Rotation Number):** Let γ: [a, b] → ℝ² be a regular closed curve. The rotation number of γ, denoted rot(γ), is the number of complete counterclockwise rotations made by the tangent vector as we traverse the curve from t = a to t = b.

**Theorem 6.12 (Whitney-Graustein Theorem):** Two regular closed curves in the plane are regularly homotopic (i.e., can be continuously deformed into each other through regular curves) if and only if they have the same rotation number.

*Proof:* The complete proof is beyond our scope, but the key idea is to show that the rotation number is invariant under regular homotopy, and that any two regular closed curves with the same rotation number can be deformed into each other through a specific construction. ■

This theorem provides a complete classification of regular closed curves in the plane up to regular homotopy. It tells us that the rotation number is the only invariant that matters for this classification.

### Section 6: The Isoperimetric Inequality

One of the most beautiful results in the theory of curves is the isoperimetric inequality, which relates the length of a simple closed curve to the area it encloses.

**Theorem 6.13 (Isoperimetric Inequality):** If γ is a simple closed curve in the plane with length L and enclosed area A, then 4πA ≤ L², with equality if and only if γ is a circle.

*Proof:* There are many proofs of this result, but one elegant approach uses Fourier series. We can parametrize γ by arc length and express it in terms of its Fourier coefficients. The isoperimetric inequality then follows from the Cauchy-Schwarz inequality applied to these coefficients. ■

The isoperimetric inequality has a beautiful physical interpretation: among all simple closed curves with a fixed length, the circle encloses the maximum area. Equivalently, among all simple closed curves enclosing a fixed area, the circle has the minimum length.

This result explains why soap bubbles form spheres (the three-dimensional analog of circles) and why many natural structures, from cells to planets, tend toward spherical shapes when external forces are minimized.

### Section 7: The Gauss-Bonnet Theorem for Plane Curves

The Gauss-Bonnet Theorem, which we'll explore more fully in later chapters, has a special case for simple closed curves in the plane.

**Theorem 6.14 (Gauss-Bonnet for Plane Curves):** If γ is a simple closed curve in the plane, oriented counterclockwise, then the total curvature of γ is 2π:

∫ κ(s) ds = 2π

where κ(s) is the curvature of γ at the point γ(s), and the integral is taken over the entire curve.

*Proof:* This follows from the fact that the tangent vector makes one complete counterclockwise rotation as we traverse the curve. ■

This theorem connects the local property of curvature to the global topological property of being a simple closed curve. It's a special case of the more general Gauss-Bonnet Theorem, which relates the curvature of a surface to its Euler characteristic.

### Section 8: The Four Vertex Theorem

We conclude our exploration of closed curves with the Four Vertex Theorem, which places constraints on the curvature of simple closed curves.

**Theorem 6.15 (Four Vertex Theorem):** Any simple closed curve in the plane, other than a circle, has at least four vertices, where a vertex is a local extremum of the curvature.

*Proof:* There are several proofs of this theorem, but one approach uses the fact that the derivative of the curvature with respect to arc length must have at least four zeros on the curve. This follows from the Gauss-Bonnet Theorem and the intermediate value theorem. ■

The Four Vertex Theorem tells us that the curvature of a simple closed curve must oscillate at least four times, unless the curve is a circle (in which case the curvature is constant). This places a strong constraint on the possible shapes of simple closed curves.

## Summary of Key Concepts

As we conclude our exploration of closed curves and the Jordan Curve Theorem, let's summarize the key concepts and results:

1. **Simple Closed Curves**: A simple closed curve is a continuous function γ: [a, b] → ℝ² that is closed (γ(a) = γ(b)) and simple (no self-intersections). From a topological perspective, all simple closed curves are homeomorphic to the unit circle.

2. **The Jordan Curve Theorem**: A simple closed curve divides the plane into exactly two connected components: a bounded interior and an unbounded exterior. This seemingly intuitive result requires sophisticated mathematics to prove rigorously.

3. **Winding Number**: For a simple closed curve, the winding number is 1 for points in the interior and 0 for points in the exterior. This provides an alternative characterization of the interior and exterior.

4. **Applications**: The Jordan Curve Theorem has numerous applications, including proofs of the Brouwer Fixed Point Theorem and the Fundamental Theorem of Algebra.

5. **Rotation Number**: The rotation number counts how many times the tangent vector rotates as we traverse a regular closed curve. The Whitney-Graustein Theorem tells us that two regular closed curves are regularly homotopic if and only if they have the same rotation number.

6. **Isoperimetric Inequality**: Among all simple closed curves with a fixed length, the circle encloses the maximum area. This explains why many natural structures tend toward circular or spherical shapes.

7. **Gauss-Bonnet Theorem**: The total curvature of a simple closed curve in the plane is 2π, connecting local differential properties to global topological ones.

8. **Four Vertex Theorem**: Any simple closed curve, other than a circle, has at least four vertices (local extrema of curvature). This places constraints on the possible shapes of simple closed curves.

These results demonstrate the rich interplay between differential geometry, topology, and analysis in the study of closed curves. They also highlight how seemingly simple questions about curves can lead to deep mathematical insights.

## Visualization Pipeline

To better understand the concepts in this chapter, let's visualize some key ideas:

**Figure 6.1: Simple Closed Curves vs. Non-Simple Closed Curves**
- A circle, an ellipse, and a rounded triangle are examples of simple closed curves.
- A figure-eight and a trefoil knot projection are examples of closed curves that are not simple due to self-intersections.

**Figure 6.2: The Jordan Curve Theorem**
- A simple closed curve divides the plane into an interior (shaded) and an exterior.
- Points in the interior cannot be connected to points in the exterior without crossing the curve.

**Figure 6.3: Winding Numbers**
- For a simple closed curve, the winding number is 1 for points in the interior and 0 for points in the exterior.
- For more complex curves with self-intersections, the winding number can take other integer values.

**Figure 6.4: The Brouwer Fixed Point Theorem**
- Any continuous function from the disk to itself has at least one fixed point.
- Illustration of the proof by contradiction, showing how the absence of a fixed point would lead to a retraction of the disk onto its boundary.

**Figure 6.5: Rotation Numbers**
- A circle has rotation number 1.
- A figure-eight has rotation number 0.
- A trefoil knot projection has rotation number 3.

**Figure 6.6: The Isoperimetric Inequality**
- Among all simple closed curves with a fixed length, the circle encloses the maximum area.
- Comparison of the area-to-perimeter ratio for various shapes.

**Figure 6.7: The Four Vertex Theorem**
- An ellipse has exactly four vertices (two points of maximum curvature and two points of minimum curvature).
- More complex curves have at least four vertices, often more.

## Interleaved Problem Set 1: Simple Closed Curves and the Jordan Curve Theorem

### Foundational Problems

**Problem 6.1:** Prove that the unit circle S¹ = {(x, y) ∈ ℝ² : x² + y² = 1} is a simple closed curve.

**Problem 6.2:** Show that the curve γ(t) = (sin 2t, sin t) for t ∈ [0, 2π] is closed but not simple. Identify the self-intersection points.

**Problem 6.3:** Let γ be a simple closed curve in the plane. Prove that γ is compact (i.e., closed and bounded).

### Exploratory Problems

**Problem 6.4:** Let γ be a simple closed curve in the plane, and let p be a point in the interior of γ. Prove that any ray from p intersects γ at least once.

**Problem 6.5:** Prove that the interior of a simple closed curve is path-connected. That is, show that any two points in the interior can be connected by a continuous path that stays entirely within the interior.

**Problem 6.6:** Let γ₁ and γ₂ be simple closed curves such that γ₁ lies entirely within the interior of γ₂. Prove that the interior of γ₁ is contained within the interior of γ₂.

### Proofcraft Problems

**Problem 6.7:** Prove that the Jordan Curve Theorem holds for polygonal curves (curves consisting of finitely many line segments).

**Problem 6.8:** Use the Jordan Curve Theorem to prove the Brouwer Fixed Point Theorem for the disk: any continuous function f: D² → D² has a fixed point.

**Problem 6.9:** Prove that the Jordan Curve Theorem implies the Fundamental Theorem of Algebra: every non-constant polynomial with complex coefficients has at least one complex root.

## Visualization Pipeline (Continued)

Let's explore some more advanced visualizations:

**Figure 6.8: The Winding Number Integral**
- The winding number can be computed as a contour integral: W(γ, p) = (1/2πi) ∫ dz/(z-p), where the integral is taken along the curve γ.
- Visualization of how this integral counts the number of times γ winds around p.

**Figure 6.9: The Whitney-Graustein Theorem**
- Animation showing how two curves with the same rotation number can be continuously deformed into each other.
- Examples of curves with different rotation numbers that cannot be deformed into each other through regular curves.

**Figure 6.10: The Isoperimetric Inequality**
- Interactive demonstration of how the area-to-perimeter ratio changes as we deform a curve.
- Visualization of the calculus of variations approach to proving the isoperimetric inequality.

**Figure 6.11: The Gauss-Bonnet Theorem**
- Visualization of how the total curvature of a simple closed curve equals 2π.
- Comparison of curves with different curvature distributions but the same total curvature.

**Figure 6.12: The Four Vertex Theorem**
- Animation showing the curvature function of a simple closed curve and its vertices.
- Examples of curves with exactly four vertices and curves with more than four vertices.

## Interleaved Problem Set 2: Applications and Extensions

### Foundational Problems

**Problem 6.10:** Calculate the winding number of the curve γ(t) = (2 cos t, sin t) for t ∈ [0, 2π] around the points (0, 0), (1, 0), and (3, 0).

**Problem 6.11:** Compute the rotation number of the curve γ(t) = (cos t, sin t) for t ∈ [0, 2π]. Verify that it equals the winding number of the curve around the origin.

**Problem 6.12:** Prove that the isoperimetric inequality 4πA ≤ L² holds for a circle, with equality.

### Exploratory Problems

**Problem 6.13:** Let γ be a simple closed curve with length L and enclosed area A. Define the isoperimetric ratio as 4πA/L². Investigate how this ratio changes when γ is:
a) An ellipse with semi-axes a and b.
b) A rectangle with sides a and b.
c) A regular n-gon with side length s.

**Problem 6.14:** Prove that the rotation number of a regular closed curve is an integer. Give examples of curves with rotation numbers 0, 1, and 2.

**Problem 6.15:** Investigate the relationship between the winding number and the rotation number for simple closed curves. Prove that for a simple closed curve, the rotation number equals the winding number of the curve around any interior point.

### Proofcraft Problems

**Problem 6.16:** Prove the Gauss-Bonnet Theorem for simple closed curves: if γ is a simple closed curve in the plane, oriented counterclockwise, then the total curvature of γ is 2π.

**Problem 6.17:** Prove the Four Vertex Theorem: any simple closed curve in the plane, other than a circle, has at least four vertices (local extrema of curvature).

**Problem 6.18:** Prove the Tennis Ball Theorem: any smooth simple closed curve on the sphere that divides the sphere into two equal-area regions must have at least four points where the geodesic curvature vanishes.

## Easter Eggs for Experts

**The Schoenflies Theorem:** The Jordan Curve Theorem tells us that a simple closed curve divides the plane into two regions. The Schoenflies Theorem goes further, stating that the closure of the bounded region is homeomorphic to the closed unit disk. This means that, topologically, the interior of any simple closed curve is just a deformed disk. The proof of this stronger result requires techniques from complex analysis, including the Riemann Mapping Theorem.

**The Jordan-Brouwer Separation Theorem:** The Jordan Curve Theorem generalizes to higher dimensions: an (n-1)-dimensional sphere embedded in n-dimensional space divides the space into two connected components. The proof of this generalization is even more involved than the proof of the original theorem and requires sophisticated tools from algebraic topology, including homology theory.

**The Hopf Umlaufsatz:** This theorem, which we'll explore in the next chapter, relates the total curvature of a closed curve to its rotation number. Specifically, it states that the total curvature of a regular closed curve equals 2π times its rotation number. This provides a beautiful connection between differential geometry (curvature) and topology (rotation number).

## Cross-Pollination

**Computer Graphics:** The Jordan Curve Theorem is fundamental in computer graphics, particularly in algorithms for determining whether a point is inside or outside a polygon. The "even-odd rule" and the "non-zero winding rule" are based on the winding number concept we've studied in this chapter.

**Medical Imaging:** In medical image analysis, the detection and characterization of closed curves (representing boundaries of organs or tumors) is a crucial task. Algorithms based on the isoperimetric inequality and the Four Vertex Theorem can help identify abnormalities in these boundaries.

**Fluid Dynamics:** The study of vortex rings in fluid dynamics relies on the theory of closed curves. The winding number concept appears in the circulation of a fluid around a closed path, which is related to the vorticity of the fluid.

**Quantum Mechanics:** In quantum mechanics, the winding number appears in the study of topological phases of matter, where it characterizes the robustness of certain quantum states against perturbations. This connection has led to the development of topological quantum computing.

**Architecture:** The isoperimetric inequality has influenced architectural design, particularly in structures that need to maximize enclosed space while minimizing material usage. Domes and arches, which approximate circular shapes, are efficient solutions to this optimization problem.

## Metacognitive Checklists

### Self-Assessment

Can you:
- State and explain the Jordan Curve Theorem?
- Calculate the winding number of a curve around a point?
- Apply the isoperimetric inequality to specific curves?
- Determine the rotation number of a regular closed curve?
- Explain the relationship between the Jordan Curve Theorem and the Brouwer Fixed Point Theorem?

### Conceptual Red Flags

Watch out if:
- You think the Jordan Curve Theorem applies to all closed curves—it specifically applies to simple closed curves (no self-intersections)—revisit Section 6.1.
- You confuse the winding number with the rotation number—the winding number counts how many times a curve winds around a point, while the rotation number counts how many times the tangent vector rotates as we traverse the curve—revisit Sections 6.3 and 6.8.
- You believe the isoperimetric inequality states that the circle has the minimum perimeter for a fixed area—it actually states that the circle has the maximum area for a fixed perimeter (or equivalently, the minimum perimeter for a fixed area)—revisit Section 6.6.
- You think the Jordan Curve Theorem requires the curve to be smooth—it applies to any simple closed curve, even those with corners or other non-smooth features—revisit Section 6.2.

## Chapter Summary

### Key Takeaways

1. The Jordan Curve Theorem states that a simple closed curve in the plane divides the plane into exactly two connected components: a bounded interior and an unbounded exterior.

2. The winding number provides a way to determine whether a point is inside or outside a simple closed curve: the winding number is 1 for points inside and 0 for points outside.

3. The isoperimetric inequality relates the length of a simple closed curve to the area it encloses, with equality holding only for circles.

4. The Gauss-Bonnet Theorem for simple closed curves states that the total curvature is always 2π, regardless of the specific shape of the curve.

5. The Whitney-Graustein Theorem classifies regular closed curves in the plane up to regular homotopy, with the rotation number being the complete invariant.

### Looking Ahead

In the next chapter, we'll explore the total curvature of curves and the Hopf Umlaufsatz, which relates the total curvature of a closed curve to its winding number. This will deepen our understanding of the global properties of curves and their relationship to differential geometry.

## Preview of Next Steps

As we move forward in our exploration of differential geometry, we'll build on the foundations established in this chapter to study more advanced topics:

**In Chapter 7:** We'll delve deeper into the isoperimetric inequality, exploring its generalizations to other settings and its connections to the calculus of variations. We'll see how this fundamental result has inspired a whole field of geometric inequalities.

**In Chapter 8:** We'll study the Four Vertex Theorem in more detail, including its generalizations and applications. We'll also explore other results that constrain the possible shapes of curves, such as the Tennis Ball Theorem and the Converse to the Four Vertex Theorem.

**In Chapter 9:** We'll extend our study of curves to different geometric settings, including spherical geometry and hyperbolic geometry. We'll see how the concepts we've developed—such as curvature, winding number, and the Gauss-Bonnet Theorem—generalize to these non-Euclidean contexts.

**In Chapter 10:** We'll make the transition from curves to surfaces, where many of the ideas we've explored—particularly the Gauss-Bonnet Theorem—find their full expression. We'll see how the study of curves provides a foundation for understanding the more complex geometry of surfaces.

These upcoming chapters will continue to reveal the beautiful interplay between local differential properties and global topological features that is characteristic of differential geometry. The Jordan Curve Theorem, which we've explored in this chapter, is just the beginning of a rich tapestry of results that connect geometry, topology, and analysis.
