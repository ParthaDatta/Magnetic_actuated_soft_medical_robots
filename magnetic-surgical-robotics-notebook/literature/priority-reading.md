# Priority Reading Queue

## Tier 0 — map the field

### P0-01
Cornejo et al. (2026), **Multi-centric international 10-year review of surgical magnetic mechatronics in HPB, bariatrics, OB-GYN, urology and neurosurgery: minimally invasive technology, robot design & actuator-sensor fusion**. *Journal of Robotic Surgery*.

DOI: `10.1007/s11701-026-03679-w`

**Use:** extract the 187-study corpus and tag it.

### P0-02
Iacovacci, Diller, Ahmed, Menciassi, **Medical Microrobots**, *Annual Review of Biomedical Engineering* (2024).

**Use:** modern taxonomy across physiology, actuation, localization and control.

### P0-03
Abbott, Diller, Petruska, **Magnetic Methods in Robotics**, *Annual Review of Control, Robotics, and Autonomous Systems* (2020).

**Use:** actuation mathematics and architecture vocabulary.

### P0-04
Li et al., **A survey on magnetically driven continuum robots for biomedical application**, *Robotics and Autonomous Systems* (2026), DOI `10.1016/j.robot.2025.105316`.

**Use:** continuum branch map.

---

## Tier 1 — direct technical benchmarks

### P1-01 — localization
Fischer et al., **Magneto-oscillatory localization for small-scale robots**, *npj Robotics* (2024).

Reason: full 6-DoF, deep-tissue wireless tracking, closed-loop integration.

### P1-02 — magnetic DoF design
Diller et al., **Six-Degrees-of-Freedom Remote Actuation of Magnetic Microrobots**, RSS 2014.

DOI: `10.15607/RSS.2014.X.013`

Reason: fundamental limitation of uniform magnetization and a constructive solution.

### P1-03 — surgical soft robot + sensing
**Learning-based modeling of a magnetically steerable soft suction device for endoscopic endonasal interventions**, *Mechatronics* (2026).

DOI: `10.1016/j.mechatronics.2026.103468`

Reason: 4-mm surgical device, FBG sensing, field-to-shape learning, sub-mm prediction.

### P1-04 — magnetic + contact safety
**A hybrid force-magnetic control scheme for flexible medical device steering**, *Mechatronics* (2023).

DOI: `10.1016/j.mechatronics.2023.103072`

Reason: patient-contact safety of external magnet motion + catheter steering.

### P1-05 — capsule intervention architecture
Masjosthusmann & Misra, **Inductively triggered capsule robot for needle-based drug delivery**, *npj Robotics* (2026).

Reason: navigation and task actuation deliberately separated.

### P1-06 — translation benchmark
Landers et al., **Clinically ready magnetic microrobots for targeted therapies**, *Science* 390, 710–715 (2025).

Reason: integrated deployment + magnetic navigation + imaging + therapy.

---

## Tier 2 — mechanism / swarm / historical but reusable

- Floyd, Pawashe, Sitti, **Dynamic Modeling of Stick Slip Motion in an Untethered Magnetic Micro-Robot**, RSS 2008.
- Dong & Sitti, **Collective Formation and Cooperative Function of a Magnetic Microrobotic Swarm**, RSS 2019.
- Recent step-out-frequency characterization papers for soft magnetic swimmers.
