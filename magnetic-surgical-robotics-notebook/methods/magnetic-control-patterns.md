# Magnetic Control Patterns

## Pattern 1 — Wrench allocation

Typical structure:

`desired robot wrench → magnetic wrench map → actuator command`

Research variables:
- rank / condition number of actuation matrix,
- coil current constraints,
- field/gradient constraints,
- EPM pose constraints,
- thermal penalty,
- anatomical collision constraints.

**Research question:** should path planning avoid states with poor magnetic controllability?

---

## Pattern 2 — Navigation + intervention decoupling

Observed in modern capsule/therapeutic systems:

`magnetic locomotion` + `secondary high-force / release actuator`

Examples:
- magnetic steering + inductively triggered needle mechanism,
- magnetic navigation + thermally triggered dissolution/release.

**Why important:** magnetic navigation may be excellent for position/orientation yet inefficient for multi-newton puncture/cutting.

---

## Pattern 3 — Magnetic steering + patient-contact control

External permanent magnets/electromagnets mounted on robot arms create a second robot-control problem.

Possible architecture:
- catheter/tool tip tracking loop,
- external magnet pose loop,
- admittance/force safety loop for patient contact.

---

## Pattern 4 — Sensor/model hybrid continuum estimation

Recent example:
- FBG senses shape,
- magnetic field parameters are known,
- low-dimensional Bezier representation,
- learned model predicts configuration.

Potential upgrade:
`physics model + learned residual + uncertainty estimate`

This is more attractive than an opaque end-to-end network if safety/interpretability matter.

---

## Pattern 5 — Low-rate medical imaging control

Likely architecture:
`medical image → segmentation/pose → estimator/predictor → constrained controller`

Key variables to log:
- imaging rate,
- total latency,
- dropout duration,
- estimator covariance,
- control update rate,
- magnet command saturation,
- recovery logic.
