# 📏 Phase 07.04–07.06 — Statistical metric, response, and locality

_Status: Mathematical metric obtained | Physical distance not obtained_

Back: [[07_01_07_03_DYNAMICS]] · Next: [[07_07_DYNAMICAL_COUPLINGS]]

## 📊 07.04 — Correlation-derived distance

For a stable quadratic system,
$$
K=\begin{pmatrix}k_1&g\\g&k_2\end{pmatrix},
\qquad k_1,k_2>0,\quad g^2<k_1k_2.
$$
**Additional assumption:** a canonical equilibrium ensemble at temperature `\Theta>0`:
$$P(X)\propto e^{-X^TKX/(2k_B\Theta)}.$$
Then covariance is
$$
C=k_B\Theta K^{-1},\quad
K^{-1}=\frac1{k_1k_2-g^2}
\begin{pmatrix}k_2&-g\\-g&k_1\end{pmatrix}.
$$
Therefore
$$\rho_{12}=-\frac{g}{\sqrt{k_1k_2}}.$$
For standardized variables (Z_i), define
$$
d_{\mathrm{stat}}(i,j)=\sqrt{\langle(Z_i-Z_j)^2\rangle}
=\sqrt{2(1-\rho_{ij})}.
$$
For the two-variable model,
$$d_{\mathrm{stat}}(1,2)=\sqrt{2\left(1+\frac g{\sqrt{k_1k_2}}\right)}.$$
This is the (L^2) metric on standardized random variables **modulo equality almost surely**; without that identification it is a pseudometric. It is **not physical distance**. Correlation depends on variable conventions and can reflect indirect or common influences.

## 📡 07.05 — Disturbance response

For an initial velocity impulse at variable 1,
$$
X_1(0)=X_2(0)=0,\quad \dot X_1(0)=v,\quad\dot X_2(0)=0,
$$
the linear coupled equations give
$$X_1(T)=vT+O(T^3),$$
$$X_2(T)=-\frac{gv}{6m_2}T^3+O(T^5).$$
For nonzero (g), response occurs for arbitrarily small positive (T). There is no strictly positive first-response time.

For a nearest-neighbor chain with equal masses and coupling magnitude (g), a node (n) edges away has leading response of order
$$X_{n+1}(T)\sim\left(-\frac gm\right)^n\frac{vT^{2n+1}}{(2n+1)!},$$
assuming no cancellations and the specified chain stiffness. The suppression is strong, but no exact causal front follows from the finite-dimensional ODE.

A continuum wave equation
$$\partial_T^2u=c_*^2\partial_x^2u,\quad c_*=a\sqrt{\kappa/m}$$
can arise from a chain continuum limit, but the chain neighborhood and lattice spacing (a) were **imposed**.

## 🕸️ 07.06 — Graph growth and dimensionality

For symmetric stiffness matrix (K), define `A_{ij}=1` for nonzero off-diagonal couplings, and graph distance (d_G(i,j)) as shortest path length on a connected graph. Then
$$
N_i(r)=|\{j:d_G(i,j)\le r\}|,\quad
D_{\mathrm{eff}}\simeq\frac{d\ln N_i(r)}{d\ln r}
$$
in a suitable scaling regime. A chain behaves approximately 1D; square and cubic lattices approximately 2D and 3D; trees can grow exponentially; complete graphs lack an ordinary large-radius Euclidean scaling regime.

**All examples supply connectivity beforehand.** A graph metric is not automatically a physical spatial metric. No unique dimension, preferred neighborhood, or relativistic speed is derived.

## 🧾 Failure register

- Statistical distance `\ne` physical distance.
- Nonzero coupling `\ne` strictly finite signal speed.
- Effective graph dimension `\ne` observed spatial dimension.
- The interaction matrix remains an unexplained input.

Next: [[07_07_DYNAMICAL_COUPLINGS]] · [[PHASE_07_FINAL_AUDIT]].
