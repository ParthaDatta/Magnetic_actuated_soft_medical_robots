# 8. Reading roadmap

This sequence is organized by decisions you need to make, not by publication date.

## Phase 1 — derive and verify the magnetic interaction

1. Griffiths, *Introduction to Electrodynamics*: magnetic dipoles, energy, torque, and force.
2. Furlani, *Permanent Magnet and Electromechanical Devices*: engineering models for permanent magnets.
3. Petruska & Abbott (2013): when a real permanent magnet behaves sufficiently like a point dipole.
4. Run Notebook 01 and reproduce the energy-gradient force check.

**Exit test:** You can state the source-to-receiver vector, derive \(\mathbf B\), \(\mathbf F\), \(\boldsymbol\tau\), explain \(r^{-3}\) versus \(r^{-4}\), and detect a sign/cross-term error numerically.

## Phase 2 — connect magnetics to robot kinematics

1. Siciliano *et al.* or Murray, Li & Sastry: spatial velocity, Jacobians, pseudoinverses, redundancy.
2. Mahoney & Abbott (2016): single-EPM magnetic manipulation.
3. Pittiglio *et al.* (2019): the supplied appendix and dynamic levitation controller.
4. Run Notebook 02 and verify translation and rotation blocks by finite difference.

**Exit test:** You can derive \(\dot{\mathbf w}=J_q\dot{\mathbf q}+J_\chi\dot{\boldsymbol\chi}\) from definitions and explain the feed-forward internal-motion term.

## Phase 3 — choose an actuator architecture

Read one source from each family:

- Kummer *et al.* (OctoMag) for coil arrays;
- Ryan & Diller for rotating permanent magnets;
- Pittiglio *et al.* (2023) for dual EPMs;
- Brockdorff *et al.* for dual-EPM transition planning;
- a human-scale/under-table system for clinical depth and access.

Run Notebook 03 and replace its example moments/distances with your proposed hardware.

**Exit test:** You have a quantitative field, gradient, force, torque, thermal, access, and collision comparison at the actual target depth.

## Phase 4 — select the surgical robot model

- Capsule/endoluminal: Pittiglio 2019; Taddese 2016/2018.
- Catheter/continuum: Edelmann 2017; BigMag; patient-specific magnetic catheter literature.
- Laparoscopic anchoring: MAGS human-feasibility and retraction literature.
- Endovascular micro/millirobot: clinically ready microrobot and image-guided control literature.
- Soft continuum body: Kim *et al.* 2019 and subsequent hard-magnetic soft-robot work.

**Exit test:** Your state includes the clinically important contact, tether, flow, shape, or payload variables—not only free-space pose.

## Phase 5 — close the observable and safe loop

1. Read the most clinically compatible localization paper for your anatomy.
2. Implement a constrained inverse or MPC with actuator and tissue limits.
3. Add estimator covariance, dropout handling, and an explicit recovery state.
4. Validate transitions as well as steady states.

**Exit test:** The robot enters a safe behavior when localization, actuation authority, or contact estimates become unreliable.

## Phase 6 — build the publication argument

A strong magnetic-surgery paper usually contributes at least one new item while measuring all the others:

- actuation hardware or human-scale workspace;
- calibrated field/wrench model;
- controllability or inverse-actuation method;
- clinically compatible state estimation;
- constrained feedback and recovery;
- task-level surgical intervention;
- stronger anatomical or in vivo validation.

Use the paper-dissection table in Chapter 4 to show precisely which interface your work advances and which layers are reused from prior work.

## Textbook shelf

| Book | Best chapters/topics for this notebook |
|---|---|
| Griffiths, *Introduction to Electrodynamics* | magnetostatics, magnetic dipoles, boundary conditions |
| Jackson, *Classical Electrodynamics* | advanced multipoles and field theory; use after Griffiths |
| Furlani, *Permanent Magnet and Electromechanical Devices* | finite permanent magnets, magnetic circuits, actuator engineering |
| Siciliano *et al.*, *Robotics: Modelling, Planning and Control* | manipulator kinematics, Jacobians, inverse kinematics, control |
| Murray, Li & Sastry, *A Mathematical Introduction to Robotic Manipulation* | rigid motions, twists, geometric Jacobians, nonlinear control |
| Khalil, *Nonlinear Systems* | Lyapunov stability, backstepping, robustness |
| Slotine & Li, *Applied Nonlinear Control* | robot/nonlinear control and adaptive methods |
| Nocedal & Wright, *Numerical Optimization* | constrained inverse actuation, SQP, numerical conditioning |

The textbooks supply reusable theory. Journal papers establish how that theory survives real actuator geometry, sensing, anatomy, and experimental constraints.
