# 7. Paper-to-equation and method map

Use this page to move from a concept to the most useful primary source. The “use it for” column is intentionally specific.

## 7.1 Foundations and models

| Concept | Source | Use it for | Important limit |
|---|---|---|---|
| Dipole field, energy, force, torque | Griffiths, *Introduction to Electrodynamics*; Furlani, *Permanent Magnet and Electromechanical Devices* | Derive $\mathbf B$, $U$, $\mathbf F$, $\boldsymbol\tau$; check units | Not a surgical-system model |
| Dipole approximation quality | Petruska & Abbott, 2013 | Select magnet geometries and quantify where dipole modelling is credible | Geometry-specific; still validate assembled hardware |
| Robot Jacobians and pseudoinverse | Siciliano *et al.*; Murray, Li & Sastry | Map EPM twist to joint rates; frame conventions; redundancy | Does not supply magnetic or tissue dynamics |
| Nonlinear/robust control | Khalil; Slotine & Li | Lyapunov, backstepping, adaptive and robust-control tools | Stability assumptions must match sensing and saturation |

## 7.2 Permanent-magnet manipulation

| Method | Primary source | What to extract | Why it matters surgically |
|---|---|---|---|
| Single-EPM 5-DOF manipulation | Mahoney & Abbott, 2016 | Dipole inverse, controllable DOF, stomach-capsule experiments | Canonical single external magnet architecture |
| Dynamic levitation of soft-tethered capsule | Pittiglio *et al.*, 2019 | Dynamic model, wrench-rate Jacobian, feedback law | Direct source of the supplied appendix |
| Dual robotically actuated EPMs | Pittiglio *et al.*, 2023 | Collaborative magnetic map and dual-arm control | More field/gradient authority at cost of planning complexity |
| Dual-EPM hybrid trajectory planning | Brockdorff *et al.*, 2025 | Restricted-area motion planning and transient field/gradient suppression | Shows why actuator transition paths are safety-critical |
| Rotating-PM full dexterity | Ryan & Diller, 2017 | Rotor-phase actuation and 3D tracking | Permanent-magnet alternative to coil arrays |

## 7.3 Electromagnetic actuation

| Method | Primary source | What to extract | Why it matters surgically |
|---|---|---|---|
| OctoMag | Kummer *et al.*, 2010 | Eight-coil field/gradient control and wireless micromanipulation | Canonical multi-coil architecture |
| Minimum electromagnet count | Petruska & Nelson, 2015 | Maxwell-constrained actuation rank and lower bounds | Prevents overclaiming independent magnetic DOF |
| BigMag | Sikorski *et al.*, 2017 | Large-workspace actuation of flexible surgical manipulators | Links coil-system design with continuum surgery |
| Unobtrusive under-table coils | Pancaldi *et al.*, 2023 preprint | Human access, working depth, under-table geometry | OR integration and patient access become design variables |
| Human-scale rotating field | Le *et al.*, 2026 | Permanent-magnet RMF at anatomical scale | Scaling and practical delivery at clinically relevant depth |

## 7.4 Devices, perception, and autonomy

| System | Primary source | What to extract | Missing interface to study |
|---|---|---|---|
| Magnetic continuum devices | Edelmann, Petruska & Nelson, 2017 | Mechanics and magnetic control of continuum bodies | Full-shape and contact estimation |
| Capsule pose estimation | Taddese *et al.*, 2018 | Real-time pose estimator and closed-loop integration | Translation to opaque clinical anatomy |
| Nonholonomic soft-tethered capsule control | Taddese *et al.*, 2016 | Velocity control and rolling/tether constraints | Robustness to tissue contact and variable lumen geometry |
| Whole-body MPC endoscope | IEEE T-RO, 2025 | Joint optimization of external actuator and internal endoscope behavior | Clinical sensing, delay, and uncertainty validation |
| Ultrasound-guided magnetic robot | Guo *et al.*, 2025 | Ultrasound state feedback for actuation | Occlusion, confidence and anatomical registration |
| Clinically ready therapeutic microrobots | Landers *et al.*, 2025 | End-to-end navigation, therapy, imaging and translation workflow | Generalization across anatomy and clinical centers |
| Ferromagnetic soft continuum robots | Kim *et al.*, 2019 | Programmed magnetization and large deformation | Patient-scale localization and safe contact control |

## 7.5 Laparoscopic magnetic anchoring

Historical magnetic anchoring and guidance system (MAGS) literature should be used for trocar reduction, camera/retractor deployment, transabdominal coupling, and early human feasibility. It should not be treated as equivalent to closed-loop robotic magnetic navigation.

| Source | Evidence to extract | Proper interpretation |
|---|---|---|
| Cadeddu *et al.*, 2009 | Two initial human cases using an externally controlled magnetically anchored camera | Early clinical feasibility and workflow; not autonomous robotic control |
| Best & Cadeddu, 2010 | MAGS device taxonomy and minimally invasive applications | System-design entry point and historical references |
| Leong *et al.*, 2018 preprint | Insufflated abdominal-wall dynamics under magnetically anchored instruments | Why the abdominal wall is part of the plant, not a rigid fixture |

When reviewing a MAGS paper, extract abdominal-wall thickness, anchoring force, contact footprint, deployment/retrieval, and whether the external magnet was manual or robotic.

## 7.6 Source hierarchy

Prefer evidence in this order:

1. full primary paper and supplement;
2. accepted manuscript or author repository;
3. official publisher abstract/metadata;
4. standards, regulatory databases, trial registries, or manufacturer specifications for relevant factual claims;
5. reviews only for discovery and taxonomy.

Do not derive quantitative claims from a review when the primary paper is available. Mark preprints, conference papers, simulations, ex vivo work, and in vivo work distinctly.
