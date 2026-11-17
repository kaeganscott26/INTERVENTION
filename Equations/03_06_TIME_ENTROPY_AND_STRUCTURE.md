# 🌀 Phases 03–06 — Nonlinearity, proper time, and entropy

_Status: Mathematical constructions | No physical space derived_

Back: [[01_FOUNDATIONS_AND_COSMOLOGY]] · Next: [[07_01_07_03_DYNAMICS]]

## 🌊 Phase 03 — Nonlinear interactions and candidate geometry

A standard Duffing oscillator:
$$m\ddot X+kX+\lambda X^3=0.$$
For weak positive cubic stiffness, its approximate frequency is
$$
\omega(A)\approx\sqrt{k/m}\left(1+\frac{3\lambda A^2}{8k}\right).
$$
This is an amplitude-dependent **internal** oscillation, not a derivation of physical spatial shape.

For internal variables `X_i`, a potential may contain pair couplings `g_{ij}X_iX_j`. Defining `w_{ij}=|g_{ij}|` and edge length `\ell_{ij}=\kappa/w_{ij}` gives a graph shortest-path distance **if** connectivity and positive edge lengths are specified. The mapping from coupling to length is **chosen**, not discovered. Graph volume growth can define a conditional effective dimension.

## ⌛ Phase 04 — Coordinate time versus proper time

ADM decomposition in established GR:
$$
ds^2=-N^2c^2dT^2+h_{ij}(dx^i+N^i dT)(dx^j+N^j dT).
$$
For comoving observers in a homogeneous zero-shift setting,
$$d\tau=N(T)dT.$$
**Important:** ADM `T` ordinarily labels slices of already-existing spacetime; writing this equation does not prove a physically separate fundamental time. An order-parameter metric `h_{ij}=\phi(T)^2\bar h_{ij}` is degenerate at `\phi=0`, beyond ordinary nondegenerate GR without additional theory.

## ↔️ Phase 05 — Reversibility and the arrow of time

For `V(\phi)=\lambda(\phi^2-v^2)^2/4`, linearizing about zero gives
$$\mu\ddot\phi-\lambda v^2\phi=0,$$
$$\phi(T)=Ae^{\gamma T}+Be^{-\gamma T},\qquad \gamma=\sqrt{\lambda v^2/\mu}.$$
The equations are invariant under `T\to-T` (with transformed initial data). Growing modes do **not** identify an intrinsic forward direction.

Gibbs entropy:
$$S_G=-k_B\sum_i p_i\ln p_i.$$
Microscopic reversible Hamiltonian evolution preserves fine-grained Gibbs entropy; thermodynamic increase requires statistical conditions, coarse-graining, and/or special boundaries. A low-entropy boundary can yield a conditional arrow, not one derived solely from (T).

## 🎲 Phase 06 — Entropy without spatial volume

Take (N) labeled binary internal variables. There are (2^N) microstates. For (m) ones,
$$\Omega(m)=\binom Nm,\qquad S_B(m)=k_B\ln\Omega(m).$$
No spatial positions are required for this combinatorial definition.

For an effective symmetric continuous-time master equation with `W_{ij}=W_{ji}\ge0`,
$$
\dot p_i=\sum_jW_{ij}(p_j-p_i),
$$
the Gibbs entropy production is
$$
\frac{dS_G}{dT}=\frac{k_B}{2}\sum_{ij}W_{ij}(p_i-p_j)\ln\frac{p_i}{p_j}\ge0
$$
for positive probabilities, with limiting interpretation at zeros. **This is an effective stochastic model, not a derivation of fundamental irreversibility.**

An illustrative Janus-like profile `S(T)\simeq S_{\min}+\alpha|T|` represents two opposite entropy arrows from a low-entropy boundary; it is not observational evidence.

A speculative coupling `V(\phi,S)=\lambda\phi^4/4-r(S)\phi^2/2` can shift the preferred order parameter when `r(S)` changes sign, but the function `r(S)` is externally selected. A conservative `\phi` equation coupled to an irreversible entropy law requires a consistent larger-system treatment.

## 🧾 Verdict

- **Yes, mathematically:** distinguishable internal states and statistical entropy need not be assigned spatial coordinates.
- **No:** entropy increase, a preferred time direction, physical clock time, or spatial emergence does not follow automatically.
- **Caution:** a graph, a statistical state space, and physical space are different concepts.

Related: [[THEORY_LAYER]] · [[GEOMETRY_AS_CONSEQUENCE]].
