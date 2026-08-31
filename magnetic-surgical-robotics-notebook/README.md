# Magnetic Actuation–Based Surgical Robotics — Research Notebook

**Purpose:** living research repository for magnetic surgical robots, medical microrobots/millirobots, magnetic continuum devices, capsule systems, untethered tools, image-guided navigation, state estimation, and task-level autonomy.

This is **not a course notebook**. Every entry should answer one or more research questions, preserve evidence, and record what we did/learned so the work can be reconstructed months or years later.

## Research north star

> Develop clinically meaningful miniature robotic systems in which magnetic actuation, sensing/localization, estimation, planning, and control work together under realistic anatomical and physiological constraints.

Primary adjacency: Anuruddha Bhattacharjee's work on magnetic miniature robots, closed-loop manipulation, magnetic surgical tools, image-constrained control, physiological-flow navigation, modularity, and targeted delivery.

## Repository map

- `daily/` — dated research logs. This is the chronological source of truth.
- `literature/` — paper database, priority reading queues, review maps, paper notes.
- `labs/` — PI/lab intelligence: what they build, their technical moat, latest work, useful hardware/methods.
- `methods/` — reusable models, algorithms, equations, control/estimation approaches.
- `tools-materials/` — magnets, coils, sensors, imaging, fabrication, software, materials, vendors/specs when verified.
- `resources/` — *high-signal* videos, seminars, theses, code, CAD, datasets, protocols. Avoid generic learning links.
- `experiments/` — procedures, test rigs, metrics, calibration and validation protocols.
- `ideas/` — hypotheses and novelty checks. Ideas stay here until evidence supports them.
- `decisions/` — why we selected/rejected a design, method, tool, material, controller, or experiment.
- `templates/` — repeatable paper note, experiment note, and idea evaluation formats.

## Rules for this notebook

1. **Evidence first.** Claims from papers must retain DOI/stable source.
2. **Numbers matter.** Record dimensions, field/gradient, actuator distance, force/torque, errors, frame rate, flow rate, sample size, etc.
3. **Separate fact from inference.** Use `Evidence`, `Interpretation`, `Hypothesis`.
4. **Record failure modes.** They are often more valuable than headline performance.
5. **Never write “learn X” without a research reason.** A resource belongs here only if it unlocks a concrete model, experiment, method, or design decision.
6. **Every deep-read paper produces at least one question:** “What assumption would fail in vivo?”
7. **Every candidate idea gets a novelty audit** before hardware effort.
8. **Do not silently overwrite decisions.** Create a dated decision note when direction changes.

## Current high-value questions

- Can controllability/singularity metrics be incorporated directly into path planning or NMPC?
- How should magnetic robots be controlled when medical imaging is low-rate, intermittent, occluded, or delayed?
- Can tool–tissue contact be estimated without a distal force sensor?
- Can local/hybrid magnetic actuation deliver surgical forces at clinically realistic depth?
- Can modular robots temporarily dock to amplify force/function and still retain safe navigation/retrieval?
- What validation ladder is sufficient to move from water-tank demonstration to clinically meaningful evidence?
