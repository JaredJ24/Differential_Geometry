# Additional Problem Sets for Chapter 5: Periodic Functions and Degree Theory

## Interleaved Problem Set 3: Fourier Series and Periodic Functions

### Foundational Problems

**Problem 5.21:** Calculate the Fourier coefficients for the following periodic functions with period 2π:
a) f(t) = |sin(t)|
b) f(t) = t for t ∈ [0, 2π)
c) f(t) = e^(cos(t))

*Hint:* Use the formulas aₙ = (1/π) ∫_{-π}^π f(t) cos(nt) dt and bₙ = (1/π) ∫_{-π}^π f(t) sin(nt) dt.

**Problem 5.22:** Prove that if f is an even function (i.e., f(-t) = f(t)), then all its sine coefficients bₙ are zero. Similarly, if f is an odd function (i.e., f(-t) = -f(t)), then all its cosine coefficients aₙ are zero.

*Hint:* Use the properties of even and odd functions under integration.

**Problem 5.23:** Let f(t) be a continuous periodic function with period 2π. Show that the Fourier series of the derivative f'(t) can be obtained by term-by-term differentiation of the Fourier series of f(t).

*Hint:* Use the formulas for the Fourier coefficients and integration by parts.

### Exploratory Problems

**Problem 5.24:** Consider the sawtooth function f(t) = t for t ∈ [0, 2π) and extended periodically.
a) Find its Fourier series.
b) Use the Fourier series to calculate the sum Σ_{n=1}^∞ 1/n².
c) Investigate the convergence of the Fourier series at the points of discontinuity.

*Hint:* For part (b), use Parseval's identity.

**Problem 5.25:** Let f(t) be a periodic function with period T. Show that if f is shifted by a constant c to get g(t) = f(t-c), then the Fourier coefficients of g are related to those of f by a phase shift.

*Hint:* Use the formula for the Fourier coefficients and the substitution u = t-c.

**Problem 5.26:** Investigate the Gibbs phenomenon for the Fourier series of the square wave function f(t) = sgn(sin(t)).
a) Plot the partial sums of the Fourier series for different numbers of terms.
b) Show that the overshoot near the discontinuities approaches approximately 9% of the jump as the number of terms increases.

*Hint:* The Gibbs phenomenon occurs because the Fourier series of a discontinuous function exhibits oscillations near the discontinuities.

### Proofcraft Problems

**Problem 5.27:** Prove Parseval's identity: If f is a periodic function with period 2π and Fourier coefficients aₙ and bₙ, then:

(1/2π) ∫_{-π}^π |f(t)|² dt = (a₀/2)² + Σ_{n=1}^∞ (aₙ² + bₙ²)

*Hint:* Use the orthogonality of the trigonometric functions and the definition of the Fourier coefficients.

**Problem 5.28:** Let f and g be periodic functions with period 2π and Fourier coefficients aₙ, bₙ and cₙ, dₙ, respectively. Prove that:

(1/2π) ∫_{-π}^π f(t)g(t) dt = (a₀c₀/2) + Σ_{n=1}^∞ (aₙcₙ + bₙdₙ)

*Hint:* Express f and g in terms of their Fourier series and use the orthogonality of the trigonometric functions.

**Problem 5.29:** Prove the Riemann-Lebesgue Lemma: If f is integrable on [-π, π], then its Fourier coefficients aₙ and bₙ approach 0 as n approaches infinity.

*Hint:* Approximate f by a step function and use the fact that the Fourier coefficients of a step function approach 0.

## Interleaved Problem Set 4: Applications of Degree Theory

### Foundational Problems

**Problem 5.30:** Use the Brouwer Fixed Point Theorem to prove that if A is an n×n matrix and b is an n-dimensional vector, then the system of equations Ax + b = x has a solution if all components of b are bounded by 1 in absolute value.

*Hint:* Consider the function f(x) = Ax + b and apply the Brouwer Fixed Point Theorem to a suitable ball.

**Problem 5.31:** Prove that any continuous function f: [a,b] → [a,b] has a fixed point.

*Hint:* Apply the one-dimensional version of the Brouwer Fixed Point Theorem directly.

**Problem 5.32:** Let f: S¹ → S¹ be a continuous map with deg(f) = d. Prove that for any point y ∈ S¹, the equation f(x) = y has exactly |d| solutions if d ≠ 0, and either 0 or infinitely many solutions if d = 0.

*Hint:* Use the fact that f can be written as f(e^(it)) = e^(ig(t)) where g(t + 2π) = g(t) + 2πd, and consider the solutions to g(t) = arg(y) + 2πk for integers k.

### Exploratory Problems

**Problem 5.33:** Consider the system of equations:
x² + y² = 1
(x-a)² + (y-b)² = 1
where a and b are constants. Use degree theory to determine for which values of a and b the system has a solution.

*Hint:* Interpret the system as the intersection of two circles and consider when the circles intersect.

**Problem 5.34:** Let f: D² → D² be a continuous function from the unit disk to itself. Prove that if f has no fixed points on the boundary S¹, then the number of fixed points of f (counted with multiplicity) is equal to the degree of the map g: S¹ → S¹ defined by g(x) = (x - f(x))/|x - f(x)| for x ∈ S¹.

*Hint:* Use the properties of degree and the fact that the fixed points of f correspond to the zeros of the function h(x) = x - f(x).

**Problem 5.35:** Prove the Borsuk-Ulam Theorem for n = 2: For any continuous function f: S² → ℝ², there exists a point x ∈ S² such that f(x) = f(-x).

*Hint:* Consider the function g(x) = f(x) - f(-x) and use the properties of degree to show that g must have a zero.

### Proofcraft Problems

**Problem 5.36:** Prove the Fundamental Theorem of Algebra using degree theory: Any non-constant polynomial p(z) with complex coefficients has at least one root in ℂ.

*Hint:* For a polynomial of degree n, consider the map f(z) = p(z)/|p(z)| defined on a large circle. Compute the degree of this map and use the properties of degree to show that p must have a root inside the circle.

**Problem 5.37:** Prove the Jordan Curve Theorem using degree theory: Any simple closed curve in the plane divides the plane into exactly two regions, an "inside" and an "outside."

*Hint:* Use the winding number to distinguish between points inside and outside the curve.

**Problem 5.38:** Let f: S^n → S^n be a continuous map. Prove that if f has no fixed points, then deg(f) = (-1)^(n+1).

*Hint:* Consider the map g(x) = -f(-x) and compute its degree. Then use the fact that f has no fixed points to establish a relationship between f and the antipodal map.

## Interleaved Problem Set 5: Degree Theory in Higher Dimensions

### Foundational Problems

**Problem 5.39:** Calculate the degree of the following maps:
a) f: S¹ → S¹ given by f(e^(it)) = e^(i4t)
b) g: S¹ → S¹ given by g(e^(it)) = e^(-i3t)
c) h: S² → S² given by h(x,y,z) = (-x,-y,-z) (the antipodal map)

*Hint:* For parts (a) and (b), use the definition of degree for circle maps. For part (c), use the fact that the antipodal map on S^n has degree (-1)^(n+1).

**Problem 5.40:** Let f: S^n → S^n be a continuous map. Prove that if f is homotopic to the identity map, then deg(f) = 1.

*Hint:* Use the fact that degree is invariant under homotopy and that the degree of the identity map is 1.

**Problem 5.41:** Let f, g: S^n → S^n be continuous maps. Prove that deg(f ∘ g) = deg(f) · deg(g).

*Hint:* Use the definition of degree in terms of the induced map on the top homology group.

### Exploratory Problems

**Problem 5.42:** Let f: S² → S² be a continuous map with deg(f) = 0. Prove that there exist antipodal points x and -x on S² such that f(x) = f(-x).

*Hint:* Consider the function g(x) = f(x) - f(-x) and use the properties of degree to show that g must have a zero.

**Problem 5.43:** Investigate the Hopf fibration h: S³ → S². Show that each point in S² has a circle in S³ as its preimage, and these circles are linked in a specific way.

*Hint:* Represent S³ as the unit sphere in ℂ² and S² as the Riemann sphere (ℂ ∪ {∞}). Define h(z₁, z₂) = z₁/z₂ for (z₁, z₂) ∈ S³ ⊂ ℂ².

**Problem 5.44:** Let f: S^n → S^n be a continuous map with deg(f) ≠ 0. Prove that f is surjective (i.e., f(S^n) = S^n).

*Hint:* Suppose f is not surjective. Then there exists a point p ∈ S^n such that p ∉ f(S^n). Use this to show that f is homotopic to a constant map.

### Proofcraft Problems

**Problem 5.45:** Prove the Brouwer Degree Theorem: If U is a bounded open subset of ℝ^n, f: U̅ → ℝ^n is continuous, p ∉ f(∂U), and f^(-1)(p) is finite, then the degree of f at p, denoted deg(f, U, p), is well-defined and satisfies:

deg(f, U, p) = Σ_{x ∈ f^(-1)(p)} sign(det(Df(x)))

if f is differentiable at each x ∈ f^(-1)(p) and det(Df(x)) ≠ 0.

*Hint:* Use the properties of degree and the fact that the degree can be defined in terms of the winding number for n = 2 and generalized to higher dimensions.

**Problem 5.46:** Prove the Hopf Theorem: Two maps f, g: S^n → S^n are homotopic if and only if deg(f) = deg(g).

*Hint:* The "only if" part follows from the invariance of degree under homotopy. For the "if" part, use the fact that S^n is (n-1)-connected and construct an explicit homotopy.

**Problem 5.47:** Let f: S^n → S^n be a continuous map. Prove that f is homotopic to a constant map if and only if deg(f) = 0.

*Hint:* Use the Hopf Theorem and the fact that a constant map has degree 0.
