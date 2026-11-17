# ⏳ Phases 01–02 — Time, cosmology, and feedback

_Status: Mathematical candidates | Physical interpretation unproven_

Back: [[README]] · Next: [[03_06_TIME_ENTROPY_AND_STRUCTURE]] · Audit: [[PHASE_07_FINAL_AUDIT]]

## 🧭 Research question

Could a temporal parameter exist independently of spatial geometry? **Assumption:** introduce (T\in(-\infty,\infty)). Its unbounded domain and physical fundamentality are **not observations**.

### Phase 01 — Two competing models

**Model A: eternal spatial geometry.** Choose
$$
a(T)=a_{\min}+Ae^{\lambda T},\quad a_{\min},A,\lambda>0.
$$
Then
$$
H(T)=\frac{\dot a}{a}=\frac{\lambda Ae^{\lambda T}}{a_{\min}+Ae^{\lambda T}},
\qquad
\dot H=\frac{\lambda^2a_{\min}Ae^{\lambda T}}{(a_{\min}+Ae^{\lambda T})^2}>0.
$$
**Assumed** flat FLRW metric:
$$ds^2=-c^2dT^2+a(T)^2(dx^2+dy^2+dz^2).$$
In ordinary flat GR, `\dot H=-4\pi G(\rho+p/c^2)` (with conventional mass-density units), so this model requires an effective null-energy-condition violation unless gravitational assumptions change. Flat 3D slices were **inserted**, not derived. A positive minimum scale factor alone does not prove geodesic completeness.

**Model B: spatial emergence.** Define an order parameter
$$
\phi(T)=0\ (T\le T_c),\qquad \phi(T)>0\ (T>T_c).
$$
The interpretation that `\phi=0` means no spatial geometry is **speculative**. For a post-transition illustration choose
$$a(T)=a_*e^{H_*(T-T_c)},\quad T\ge T_c.$$
Its flat de Sitter phase can satisfy GR with `\Lambda=3H_*^2/c^2`, but neither the transition nor a pre-spatial mechanism is derived. The metric is degenerate if `h_{ij}=\phi^2\bar h_{ij}` at zero.

### Candidate temporal action

$$
S_T=\int dT\left[\frac\mu2\dot\phi^2-V(\phi)\right],
\qquad \mu\ddot\phi+V'(\phi)=0.
$$
For `V=\lambda(\phi^2-v^2)^2/4`, zero is unstable to perturbations but an exactly zero classical initial state can remain there. The potential does not explain a unique `T_c`.

## 🔄 Phase 02 — Coupled scale and internal oscillations

**Chosen phenomenological equations:**
$$
\dot a=a(H_0+gq),\qquad
\dot q=-\omega(a)p,\qquad
\dot p=\omega(a)q,
$$
$$\omega(a)=\omega_0(a/a_0)^{-s}.$$

**Derived:** `I=q^2+p^2=r^2` is constant. If `H_0>|g|r`, expansion is monotonic. Writing `q=r\cos\theta,p=r\sin\theta` gives
$$\dot\theta=\omega_0(a/a_0)^{-s}.$$
For `s>0` with asymptotically exponential expansion, total future phase can converge: **infinite time does not imply infinitely many oscillations**. `s=0` gives constant frequency, while `s<0` increases frequency as expansion proceeds.

A first-order oscillator Lagrangian can reproduce its internal equations, but it does **not** automatically reproduce the phase-dependent scale equation. A fully consistent shared action remains unconstructed.

## ⚖️ Phase 01–02 verdict

- **Derived:** explicit expansion-rate behavior; oscillator invariant and conditional monotonic expansion.
- **Assumed:** eternal (T), flat 3D geometry in Model A, emergence threshold in Model B, phenomenological coupling.
- **Not derived:** independent physical time, transition mechanism, geodesic completeness, or observed cosmology.

Related: [[THEORY_LAYER]] · [[GEOMETRY_AS_CONSEQUENCE]].
