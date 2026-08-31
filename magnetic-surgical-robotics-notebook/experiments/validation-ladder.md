# Experimental Validation Ladder

Do not claim “medical/surgical” based on a water tank alone.

## L0 — actuator characterization
- field map validated,
- gradient map validated,
- force/torque measurement,
- thermal behavior,
- calibration repeatability.

## L1 — free robot mechanics
- pose/trajectory control,
- workspace map,
- singularity/conditioning map,
- disturbance-free baseline.

## L2 — controlled fluid/contact
- viscosity sweep,
- known flow,
- surface friction/contact,
- repeatability.

## L3 — physiological phantom
- anatomical dimensions,
- clinically plausible depth,
- pulsatile/realistic flow,
- tissue-mimicking mechanical properties,
- clinical imaging or a justified surrogate.

## L4 — task experiment
Examples:
- puncture,
- grasp,
- biopsy,
- suction,
- suture,
- drug deposition,
- navigation through stenosis/bifurcation.

Must report success rate and failure mode, not only trajectory error.

## L5 — ex vivo
Preserved/fresh tissue with clinically meaningful geometry and tool interaction.

## L6 — in vivo large/small animal
Only when preceding failure modes are controlled and ethical/clinical rationale is clear.

## L7 — human feasibility / clinical trial

### Required metadata at every level
- actuator-to-target distance,
- robot dimensions,
- magnetic moment/material,
- field and gradient,
- sensing rate,
- controller update rate,
- task time,
- tracking error,
- number of trials,
- failures,
- retrieval method,
- safety limits.
