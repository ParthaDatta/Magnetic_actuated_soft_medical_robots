# 5. Control and planning

## 5.1 Separate three inverse problems

Magnetic surgical systems often conflate three mappings:

1. **task inverse:** desired surgical state change $\rightarrow$ desired wrench;
2. **magnetic inverse:** desired wrench $\rightarrow$ desired field/gradient or actuator pose;
3. **robot inverse:** desired actuator motion $\rightarrow$ joints or currents.

Keeping them separate makes infeasibility visible. For example, a requested wrench may be anatomically appropriate but magnetically impossible at the current position.

## 5.2 Differential wrench control

Given

$$
\dot{\mathbf w}_m=J_q\dot{\mathbf q}+J_\chi\dot{\boldsymbol\chi},
$$

define $\tilde{\mathbf w}=\mathbf w_d-\mathbf w_m$ and target

$$
\dot{\mathbf w}_m^*=\dot{\mathbf w}_d+K_w\tilde{\mathbf w}.
$$

The least-squares joint-rate command is

$$
\dot{\mathbf q}=J_q^\dagger
\left(\dot{\mathbf w}_m^*-J_\chi\dot{\boldsymbol\chi}\right).
$$

Use a damped inverse near singularity:

$$
J_q^\#=J_q^T(J_qJ_q^T+\rho^2I)^{-1}.
$$

Damping limits joint speed but introduces task error. Make $\rho$ state dependent and report both error and actuator saturation.

## 5.3 Weighted units and achievable tasks

Because wrench rows mix N and N·m, define characteristic length $\ell_c$ or explicit performance weights:

$$
\bar{\mathbf w}=
\begin{bmatrix}
W_F&0\\0&W_\tau
\end{bmatrix}\mathbf w.
$$

Similarly scale metres and radians in actuator twists. Rank and conditioning should be computed on the scaled matrix that represents the clinical task, not on raw mixed-unit numbers.

Not every application needs all six wrench components. Introduce a selection matrix $S_t$:

$$
\dot{\mathbf w}_{task}=S_t\dot{\mathbf w}_m=S_tJ_q\dot{\mathbf q}+S_tJ_\chi\dot{\boldsymbol\chi}.
$$

A capsule with unconstrained spin about its dipole axis may require five task coordinates. A catheter may care more about distal bending torque and insertion force than lateral wrench components.

## 5.4 Redundancy and null-space behavior

For redundant actuation,

$$
\dot{\mathbf q}=J_q^\#\mathbf y+left(I-J_q^\#J_q\right)\mathbf z,
$$

where $\mathbf y=\dot{\mathbf w}_m^*-J_\chi\dot{\boldsymbol\chi}$. Choose $\mathbf z$ from a secondary objective:

$$
\mathbf z=-k\nabla_{\mathbf q}H(\mathbf q).
$$

Useful surgical costs include distance from patient and clinicians, robot manipulability, EPM–EPM separation, joint limits, calibrated-field confidence, imaging visibility, and available emergency withdrawal direction.

Null-space projection is local. It does not prove collision-free global motion and can behave poorly near rank changes.

## 5.5 Constrained inverse actuation

A velocity-level quadratic program is often safer than a bare pseudoinverse:

$$
\begin{aligned}
\min_{\dot{\mathbf q},\mathbf s}\quad &
\|W(J_q\dot{\mathbf q}-\mathbf y-\mathbf s)\|_2^2
+\rho_q\|\dot{\mathbf q}\|_2^2+\rho_s\|\mathbf s\|_2^2\\
\text{s.t.}\quad &
\dot{\mathbf q}_{min}\le\dot{\mathbf q}\le\dot{\mathbf q}_{max},\\
&\mathbf q_{min}\le\mathbf q+\Delta t\dot{\mathbf q}\le\mathbf q_{max},\\
&d_{patient}(\mathbf q)+\Delta t\dot d_{patient}\ge d_{safe},\\
&\mathbf w_m\in\mathcal W_{safe}(\hat{\boldsymbol\chi},\Sigma_\chi).
\end{aligned}
$$

Slack $\mathbf s$ makes loss of authority explicit. Logging slack is more informative than silently clipping joint commands.

## 5.6 Model predictive control

MPC/NMPC is useful when actuator motion, field transients, internal dynamics, delay, and anatomy must be predicted together:

$$
\min_{\mathbf u_{0:N-1}}
\sum_{k=0}^{N-1}
\left(
\|\mathbf x_k-\mathbf x_{d,k}\|_Q^2
+\|\mathbf u_k\|_R^2
+\|\Delta\mathbf u_k\|_S^2
\right)
+\|\mathbf x_N-\mathbf x_{d,N}\|_P^2.
$$

Constraints should cover EPM/arm collisions, coil current and temperature, field/gradient exposure, internal contact force, anatomical regions, localization uncertainty, and visibility. Whole-body MPC is particularly relevant because the actuator arm itself is part of the safety problem.

## 5.7 Hybrid actuator-space trajectory planning

For dual EPMs, a planner should penalize both external motion and transient internal wrench:

$$
J=\int_0^T
\left[
\|\mathbf w_m(t)-\mathbf w_d(t)\|_{Q_w}^2
+\|\dot{\mathbf q}(t)\|_{R_q}^2
+\Phi_{collision}(\mathbf q(t))
\right]dt.
$$

A hybrid strategy can search discrete homotopy/motion classes, then optimize the continuous trajectory. This addresses a failure of endpoint-only inverse actuation: a feasible start and goal do not imply a safe interpolation.

## 5.8 Estimation-aware control

The state estimate should include covariance $\Sigma_\chi$. A simple confidence gate is

$$
\lambda_{max}(\Sigma_\chi)\le\sigma_{task}^2;
$$

if violated, the system enters a lower-energy hold, re-localization, or withdrawal mode instead of continuing the intervention.

For delayed imaging with delay $d$, propagate the estimate to controller time:

$$
\hat{\mathbf x}_{k|k-d}=f^d(\hat{\mathbf x}_{k-d},\mathbf u_{k-d:k-1}).
$$

Report end-to-end latency—not only inference time—and test occlusion, dropouts, and disagreement between sensing modalities.

## 5.9 Recovery is part of autonomy

A minimally useful state machine includes:

- normal navigation;
- contact-limited or low-wrench motion;
- loss-of-localization hold;
- actuator-singularity escape;
- coupling-loss recovery;
- emergency withdrawal or passive-safe state;
- clinician takeover.

Success rate without recovery trials overstates autonomy. Benchmark recovery trigger accuracy, peak wrench during recovery, time to regain localization, and success after repeated failures.
