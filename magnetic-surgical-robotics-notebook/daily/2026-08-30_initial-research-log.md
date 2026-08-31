# Daily Research Log — 2026-08-30

## Objective

Establish the notebook/repository, define the evidence-capture workflow, and perform a first targeted search for **high-value current papers and research resources** rather than generic coursework.

## Search coverage

Sources searched in this pass:
- PubMed / biomedical literature
- Nature / npj Robotics
- Science-family pages
- Robotics: Science and Systems proceedings
- ScienceDirect / Mechatronics / Robotics and Autonomous Systems
- university/lab seminar pages
- targeted video/lecture indexes

Target concepts:
- magnetic surgical mechatronics
- magnetic microrobots/millirobots
- continuum / catheter / guidewire systems
- magnetic localization
- soft magnetic surgical tools
- clinical translation
- recent 2025–2026 work
- high-signal seminars and microrobotics lectures

## Findings that materially changed the map

### F-001 — A new 10-year surgical magnetic-mechatronics systematic review is now available

**Source:** Cornejo et al., *Journal of Robotic Surgery*, 2026.  
**DOI:** `10.1007/s11701-026-03679-w`  
**Published:** 2026-08-04.

**Evidence**
- Review covers 2016–2026.
- Clinical areas include HPB, bariatrics, OB-GYN, urology and neurosurgery.
- Search began with 68,956 records and retained 187 studies after screening.
- Emphasis: magnetic actuation, robot design, actuator-sensor fusion, experimental validation and clinical translation.

**Why this matters**
This should become a **backbone citation-mining source**. Instead of searching the field from scratch, extract all 187 included studies, tag them by clinical application + actuation + sensing + validation level, then forward-cite the strongest systems.

**Action**
- Obtain full text/supplementary list.
- Build `literature/surgical-magnetic-mechatronics-2016-2026-map.md`.
- Cross-reference included authors against the lab map.

---

### F-002 — Magnetic microrobotics has reached “clinically-ready system integration” territory

**Source:** Nature Reviews Materials research highlight (2025) discussing Landers et al., *Science* 390, 710–715 (2025), “Clinically ready magnetic microrobots for targeted therapies.”  
**DOI of highlight:** `10.1038/s41578-025-00867-2`.

**Evidence**
The highlighted platform combines:
- magnetic navigation,
- therapeutic payload,
- clinical imaging,
- multiple locomotion modes (rolling, gradient pulling, in-flow navigation),
- triggered drug release.

**Interpretation**
The translational bar is no longer “robot moves in a channel.” High-impact work increasingly demands a **full clinical task chain**: deploy → localize → navigate → act → verify/retrieve.

**Action**
Use this as a benchmark against every proposed project idea.

---

### F-003 — Full 6-DoF localization remains a central bottleneck, and SMOL is a strong reference architecture

**Source:** Fischer et al., *npj Robotics* 2, 1 (2024), “Magneto-oscillatory localization for small-scale robots.”

**Evidence**
- Full six-DoF wireless localization.
- Deep biological tissue claim up to 12 cm.
- Sub-millimeter translational accuracy reported.
- Uses a resonant magnetic cantilever to break rotational symmetry.
- Demonstrated integration with closed-loop robots/tools.

**Why this matters**
This is directly relevant to the “same magnet for actuation + sensing” problem and to alternatives to fluoroscopy/vision.

**Question**
Can magnetic actuation and SMOL-like localization coexist without unacceptable mutual interference in a surgical workspace?

---

### F-004 — Magnetic soft surgical tools are moving toward sensing + learned shape models

**Source:** “Learning-based modeling of a magnetically steerable soft suction device for endoscopic endonasal interventions,” *Mechatronics* 116 (2026), 103468.  
**DOI:** `10.1016/j.mechatronics.2026.103468`.

**Evidence**
- 4 mm OD, 2 mm ID, 40 mm long.
- Biocompatible SIL 30.
- Embedded FBG shape sensors.
- Data: 5,097 experimental samples.
- Magnetic field inputs: 0–14 mT; frequency 0.2–1.0 Hz.
- Test tip distance: 90–100 mm.
- Random Forest outperformed NN.
- Mean Bezier control-point RMSE: 0.087 mm.
- Mean shape reconstruction error: 0.064 mm.
- Concept: map magnetic field parameters → low-dimensional Bezier shape representation.

**Research significance**
This is an excellent reference for a hybrid direction:
`magnetic actuation + continuum mechanics + embedded sensing + low-dimensional learned model + closed-loop surgery`.

**Open extension**
Replace pure data-driven prediction with a physics-informed residual model and evaluate out-of-distribution anatomy/field conditions.

---

### F-005 — Local / hybrid actuation should be treated as a first-class design axis, not an implementation detail

**Source:** “A hybrid force-magnetic control scheme for flexible medical device steering,” *Mechatronics* 95 (2023), 103072.

**Evidence**
- Jacobian-based inverse kinematics for magnetic steering.
- Admittance-based force control for safe magnet/body interaction.
- Reported catheter-tip RMS error 0.43 ± 0.22 mm in one condition.
- Hybrid scheme RMS error 0.52 ± 0.41 mm.
- External contact maintained below 15 N.

**Interpretation**
External actuator motion relative to the patient is itself a safety/control problem. This suggests a broader system model:
`robot state + external magnet robot state + patient/contact state`.

---

### F-006 — Full 6-DoF magnetic actuation is fundamentally linked to robot magnetization design

**Source:** Diller, Giltinan, Lum, Ye, Sitti, RSS 2014, “Six-Degrees-of-Freedom Remote Actuation of Magnetic Microrobots.”  
**DOI:** `10.15607/RSS.2014.X.013`.

**Evidence**
Uniformly magnetized dipoles have a fundamental missing torque about the magnetization axis. Non-uniform magnetization can create additional rigid-body torques through force moment arms.

**Why keep this old paper active**
This is not “historical trivia”; it is a **design theorem**. If a future surgical task truly needs full orientation control, magnetization architecture may be more important than adding more coils.

---

### F-007 — A 2026 capsule robot separates navigation from high-force intervention

**Source:** Masjosthusmann & Misra, *npj Robotics* 4, 39 (2026), “Inductively triggered capsule robot for needle-based drug delivery.”

**Evidence**
- Magnetic steering handles navigation.
- Inductive heating triggers a thermally controlled magnetic-spring sequence.
- Sequence includes needle ejection → liquid payload release → needle retraction.
- Design motivation explicitly addresses need for multi-newton intervention forces in a millimeter-scale untethered capsule.

**Interpretation**
Important architecture pattern:
> do not force one actuator modality to solve both locomotion and high-force task execution.

This pattern may generalize to suturing, biopsy, penetration, cutting, clamping, or anchoring.

---

## High-signal resources found

These are included because they directly overlap the current project, not because they are generic courses.

### R-001 — User reference video
https://www.youtube.com/watch?v=dyPp_GUTjrE&t=6s

Status: supplied as a strong relevance benchmark by the researcher. Metadata/title could not be reliably resolved in this web pass, so do **not** guess it. Use its content/style as the standard for future video curation.

### R-002 — Eric Diller seminar: “Micro-Scale Surgery: Using Magnetic Fields to Control Tiny Robots in the Gut and Brain”
Toronto Metropolitan University / IEEE RAS speaker event, 26 May 2026.

Why high-value:
- exact topic match,
- tiny robot design + production,
- external magnetic field generation,
- surgical use in body cavities/brain/GI,
- PI-level synthesis from one of the strongest labs in the area.

Source:
https://www.torontomu.ca/engineering-architectural-science/stories-events/events/2026/05/tmu-robotics-council-speaker-series-featuring-eric-diller/

### R-003 — Veronica Iacovacci seminar: “Coping with medical microrobotics challenges: novel fabrication, control and imaging paradigms”
Robotics at Leeds, 8 Jan 2026.

Why high-value:
- explicitly contrasts laboratory optical-microscope demonstrations with clinical conditions,
- focuses on fabrication + control + imaging in tissue,
- directly addresses the translational gap we care about.

Source:
https://robotics.leeds.ac.uk/events/seminar-coping-with-medical-microrobotics-challenges-novel-fabrication-control-and-imaging-paradigms-dr-veronica-iacovacci/

### R-004 — NPTEL Microactuation and Micromanipulation — magnetic actuation module
~27 min, focused on magnetic actuation configurations, micromanipulation and biomedical microrobots.

Source index:
https://www.classcentral.com/course/youtube-w4l17-microactuation-and-micromanipulation-module-02-474420

### R-005 — NPTEL Microsystems for Microrobots — Actuators Module 05
~39 min, helical magnetic micromachines, modes of motion, medical/endoscopic integration.

Source index:
https://www.classcentral.com/course/youtube-w8l40-microsystems-for-microrobots-actuators-module-05-481131

### R-006 — Bio-inspired micro-robot propulsion modules
Useful specifically for flagellar/ciliary propulsion and magnetic field-driven locomotion.

Source:
https://www.classcentral.com/course/youtube-w11l51-bio-inspired-micro-robots-propulsion-and-locomotion-module-01-482989

---

## Procedures adopted today

1. Daily search must separate:
   - peer-reviewed papers,
   - preprints,
   - lab/seminar updates,
   - clinical/regulatory translation.
2. For every paper capture:
   - dimensions,
   - magnetic material/magnetization,
   - actuator type,
   - field/gradient,
   - actuator distance,
   - sensing,
   - controller,
   - environment,
   - quantitative result,
   - failure mode,
   - validation level.
3. Do not add generic education resources unless they solve a current modeling/design/experimental need.
4. Maintain a `failure-mode` view of the literature.
5. Candidate ideas are hypotheses until a novelty search is complete.

## Key learning today

The strongest opportunity is increasingly **system-level integration under realistic constraints**, not another locomotion demonstration. Three recurring levers appeared in this first pass:

1. decouple navigation from high-force intervention,
2. fuse sensing/modeling with magnetic control,
3. make controllability, imaging, patient interaction and safety part of the optimization problem rather than afterthoughts.

## Next research actions

- Extract the 187-paper corpus from the 2026 systematic review.
- Build a “clinical validation ladder” taxonomy.
- Deep-read the 2026 soft suction / FBG paper.
- Deep-read SMOL localization and identify compatibility constraints with actuation fields.
- Search specifically for:
  - force-sensing magnetic surgical tools,
  - local magnetic actuation,
  - magnetic suturing and biopsy,
  - clinically realistic actuator-to-target distances,
  - low-frame-rate fluoroscopy / ultrasound control,
  - thermal-aware electromagnetic control.
