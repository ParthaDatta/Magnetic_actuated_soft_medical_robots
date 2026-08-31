# Idea Register

Status labels:
- `SEED` — interesting observation only.
- `NOVELTY-CHECK` — active prior-art search.
- `MODEL` — mathematical feasibility work.
- `BENCH` — hardware/experimental validation.
- `PAPER` — contribution is mature.

## I-001 — Singularity-aware path planning / NMPC
**Status:** NOVELTY-CHECK

**Observation:** magnetic actuation quality varies across workspace; planning and wrench allocation are often separated.

**Hypothesis:** include actuation-matrix conditioning / minimum singular value directly in trajectory optimization to avoid dynamically weak regions.

**Need to check:** prior magnetic robot planning papers, EPM path optimization, manipulator dexterity metrics.

**Possible evaluation:** same path length vs improved minimum controllability margin, current demand, tracking under disturbance.

---

## I-002 — Contact-aware magnetic surgical manipulation without distal force sensor
**Status:** SEED

**Observation:** tissue contact is a major hidden state.

**Hypothesis:** combine magnetic wrench model + robot motion residual + image-based deformation to infer contact onset/force class.

**Clinical relevance:** suturing, biopsy, retraction, suction positioning.

**Risks:** magnetic model error may be indistinguishable from contact.

---

## I-003 — Imaging-aware magnetic planning
**Status:** SEED

**Hypothesis:** optimize path for anatomy + magnetic controllability + visibility / imaging quality.

`J = J_path + λ J_magnetic + μ J_visibility`

**Potential impact:** directly addresses medical imaging constraint rather than treating localization as guaranteed.

---

## I-004 — Thermal-state-aware electromagnetic actuation control
**Status:** SEED

**Hypothesis:** embed coil thermal state in MPC to maximize sustained performance subject to safe temperature/current.

**Need:** determine novelty in magnetic robotics specifically; thermal-aware coil optimization likely exists elsewhere.

---

## I-005 — Navigation + temporary force amplification by modular docking
**Status:** SEED

**Observation:** small robots navigate well but often cannot deliver surgical-scale force.

**Hypothesis:** multiple units dock only at the target to form a stronger tool/mechanism, then undock for retrieval.

**Strong adjacency:** Bhattacharjee modular magnetic robotics + medical task direction.

**Critical prior-art check:** magnetic modular millirobots, swarm cooperative manipulation, local magnetic transmissions.

---

## I-006 — Physics + learned residual model for magnetically actuated soft surgical tools
**Status:** NOVELTY-CHECK

**Trigger:** 2026 Mechatronics soft suction paper uses RF/NN field-to-Bezier prediction.

**Hypothesis:** physics-informed backbone + learned residual gives better out-of-distribution accuracy and interpretable uncertainty than pure RF/NN.

**Meaningful experiment:** train on limited fields/distances, test unseen field strengths, distances, frequencies, material batches, and contact loads.
