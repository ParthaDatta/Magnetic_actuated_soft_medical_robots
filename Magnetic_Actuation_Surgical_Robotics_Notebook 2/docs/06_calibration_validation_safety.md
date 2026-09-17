# 6. Calibration, validation, and safety

## 6.1 Calibration hierarchy

### Level 1 — individual magnet

Estimate dipole direction, moment magnitude, and offset from the mechanical reference frame. Fit measured field data to

$$
\hat{\boldsymbol\theta}
=\arg\min_{\boldsymbol\theta}
\sum_k\|\mathbf B_{meas,k}-\mathbf B_{model}(\mathbf p_k;\boldsymbol\theta)\|_2^2.
$$

Use measurements distributed in 3D; a single axial scan cannot reliably identify lateral offset and tilt.

### Level 2 — actuator/robot hand–eye calibration

Identify the transform from robot end effector to EPM magnetic frame. Small angular errors can produce large force errors because force depends on both direction and spatial gradient.

### Level 3 — field and force map

Compare predicted and measured $\mathbf B$, $\nabla\mathbf B$, force, and torque across the full surgical workspace. A model can fit field magnitude but still predict gradient poorly.

### Level 4 — integrated state estimation

Register imaging, robot, patient, and magnetic frames. Report target registration error, latency, drift, and the effect of patient motion.

## 6.2 Dipole-validity experiment

1. Measure the EPM field on a 3D grid spanning the intended distances and orientations.
2. Fit dipole moment and pose on a training subset.
3. Report held-out vector-field RMSE and angular error.
4. Differentiate the fitted/empirical map or directly measure force to assess gradient error.
5. Define the smallest separation at which both field and force error meet task tolerances.

Do not select the validity threshold from field error alone if the controller regulates force.

## 6.3 Control validation ladder

| Stage | Minimum evidence |
|---|---|
| Simulation | model perturbation, delay, noise, saturation, singularity and collision cases |
| Free-space bench | pose/wrench tracking, full workspace, repeated initial conditions |
| Structured phantom | lumen/abdominal/vessel geometry, realistic distance and access |
| Dynamic phantom | flow, respiration/peristalsis, moving target, deformable contact |
| Ex vivo | tissue friction, compliance, visibility, thermal/contact measurements |
| In vivo acute | procedural feasibility and immediate safety |
| Survival animal | recovery, delayed injury, retention/clearance, device reliability |
| Human study | protocol-defined safety and clinical endpoints |

Moving up this ladder changes the model and the workflow; it is not merely a more realistic visualization.

## 6.4 Metrics that support comparison

### Magnetic model

- field-vector RMSE and maximum error;
- gradient-tensor error;
- force and torque RMSE under multiple orientations;
- valid-separation region;
- calibration drift after sterilization or repeated use.

### Control

- internal position/orientation/shape error;
- wrench error and overshoot;
- settling time, bandwidth, latency, and jitter;
- actuator saturation and slack usage;
- singularity distance/condition metric;
- performance under disturbance and localization dropout.

### Surgical task

- task completion and duration;
- target-to-intervention offset;
- tissue contact force/pressure and duration;
- visualization coverage and image usability;
- intervention success, dose/biopsy accuracy, or treatment margin;
- deployment, retrieval, and recovery success.

Report distributions and number of independent devices/tissues/animals—not just the best trial.

## 6.5 Hazard-to-control map

| Hazard | Initiating mechanism | Online indicator | Prevention/mitigation | Required validation |
|---|---|---|---|---|
| Excess tissue force | model error, small separation, actuator transient | force estimate, distance, image/contact cue | wrench limit, barrier constraint, compliant/passive-safe mode | tissue phantom and ex vivo pressure/force |
| EPM–patient collision | inverse solution or arm motion | robot geometry, proximity sensing | whole-body collision constraint, speed limit, guarded workspace | realistic table/patient/manikin trials |
| Magnet–tool attraction | ferromagnetic instrument enters field | instrument inventory/proximity | compatibility protocol, exclusion zone | worst-case tool tests |
| Device decoupling/loss | excessive gap, disturbance, saturation | field/pose estimate, slip cue | capture-region constraint, recovery field, retrieval plan | repeated loss-and-recovery trials |
| Localization failure | occlusion, artifact, latency | covariance, innovation, modality disagreement | confidence gate, low-energy hold, re-localize | programmed dropout/occlusion tests |
| Coil overheating | high RMS current, cooling failure | winding/core/skin temperature | thermal model, current derating, shutdown | worst-case duty cycle |
| Unintended transient actuation | unsafe actuator path | predicted field/gradient/wrench | trajectory-level field penalty | start-to-goal transition tests |
| Uncontrolled spin | dipole-axis unobservability | image/IMU feature confidence | mechanical asymmetry, second field mode, accept as free DOF | task-specific spin sensitivity |

## 6.6 Surgical integration questions

Before moving to animal or human work, answer:

- Where are the actuator, patient, surgeon, anesthetic equipment, and imaging devices?
- Which instruments are ferromagnetic or field sensitive?
- How is the sterile field maintained while moving an external magnet?
- What happens during power loss, robot e-stop, network delay, or loss of tracking?
- Can the internal device be retrieved endoscopically or laparoscopically?
- What peak and cumulative contact/thermal exposure is acceptable?
- Does the field distort fluoroscopy, ultrasound, endoscopy, electromagnetic tracking, or implanted devices?
- Which decisions remain with the surgeon, and how is takeover performed?

## 6.7 Minimum reproducible report

A paper or thesis should publish enough to reconstruct:

1. magnet dimensions, grade, moment estimate, and magnetic-frame calibration;
2. actuator geometry, robot model, coil constants, current limits, or EPM limits;
3. field/wrench equations and coordinate conventions;
4. controller update rate, imaging rate, latency, and gains/optimization weights;
5. workspace and distance distribution;
6. complete metrics, trial counts, failure criteria, and excluded trials;
7. code or pseudocode for the inverse actuation and safety logic;
8. geometry/CAD or a dimensioned schematic sufficient for independent replication.
