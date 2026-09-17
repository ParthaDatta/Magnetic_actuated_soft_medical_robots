# Magnetic Actuation for Surgical Robotics

This notebook develops magnetic actuation as a complete surgical-robotics stack: magnetic physics, actuator hardware, robot kinematics, image-based state estimation, feedback control, anatomy-aware planning, and safety validation.

The central chain is

$$
\mathbf q
\xrightarrow{\text{robot kinematics}}
(\mathbf p_E,\hat{\mathbf m}_E)
\xrightarrow{\text{magnetostatics}}
(\mathbf B,\nabla\mathbf B)
\xrightarrow{\text{IPM}}
\mathbf w_m
\xrightarrow{\text{robot+tissue dynamics}}
\boldsymbol\chi
\xrightarrow{\text{imaging}}
\hat{\boldsymbol\chi}.
$$

The controller closes the loop from the estimated internal state $\hat{\boldsymbol\chi}$ to external actuator command $\dot{\mathbf q}$, coil current, or permanent-magnet motion.

## Four questions to ask of every paper

1. **What is controlled?** Field, gradient, force, torque, pose, shape, contact, or a surgical task?
2. **What is measured?** Magnet pose, robot pose, endoscopic image, fluoroscopy, ultrasound, force, temperature, or only the commanded input?
3. **What closes the loop?** A geometric inverse, PID, Jacobian control, optimization, MPC, learning, or the operator?
4. **What establishes surgical relevance?** Benchtop workspace, anatomical phantom, ex vivo tissue, acute animal, survival animal, or human study?

## Notation

| Symbol | Meaning | SI unit |
|---|---|---|
| $\mathbf p_E,\mathbf p_I$ | EPM and IPM positions | m |
| $\mathbf r=\mathbf p_I-\mathbf p_E$ | source-to-receiver relative vector used here | m |
| $\hat{\mathbf e}_E,\hat{\mathbf e}_I$ | unit magnetization axes | 1 |
| $\mathbf m_E=m_E\hat{\mathbf e}_E$ | EPM dipole moment | A·m² |
| $\mathbf m_I=m_I\hat{\mathbf e}_I$ | IPM dipole moment | A·m² |
| $\mathbf B$ | magnetic flux density | T |
| $\nabla\mathbf B$ | spatial field gradient | T/m |
| $\mathbf F_m$ | magnetic force on the IPM | N |
| $\boldsymbol\tau_m$ | magnetic torque on the IPM | N·m |
| $\mathbf w_m=[\mathbf F_m;\boldsymbol\tau_m]$ | magnetic wrench | N, N·m |
| $\mathbf q$ | external robot joints or actuator coordinates | mixed |
| $\boldsymbol\chi$ | internal device coordinates | mixed |

All derivations declare which point the field is evaluated at and which body receives the wrench. This avoids the most common sign error in two-magnet implementations.
