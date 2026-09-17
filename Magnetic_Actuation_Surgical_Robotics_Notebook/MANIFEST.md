# Repository manifest

## Learning artifacts

- Eight linked chapters covering fundamentals through reading strategy.
- Three executable Jupyter notebooks:
  - dipole field/force/torque and printed-formula check;
  - wrench Jacobian, sign convention, and damped inverse;
  - surgical-depth scaling and architecture selection.
- Reusable Python source for dipole magnetics and twist-to-wrench Jacobians.
- Five regression tests covering energy, torque, axis kinematics, and translation invariance.
- BibTeX database covering textbooks, foundational systems, capsule/endoscope control, catheters, dual EPMs, coil/rotating-magnet systems, laparoscopic magnetic anchoring, and clinical translation.
- MkDocs configuration and GitHub Actions validation workflow.

## Verification performed for version 1.0.0

- All Python source compiled successfully.
- All five regression tests passed.
- All code cells in all three notebooks executed successfully in sequence.
- The energy-gradient force and standard closed form agreed to numerical precision at a nonsymmetric test pose.
- Source- and receiver-translation Jacobian blocks were equal and opposite.
- Relative Markdown links were checked against the repository tree.

The notebooks intentionally retain clear parameter placeholders. Replace example magnet moments, anatomy distances, actuator scores, and safety bounds with measurements from the target system before using the calculations for design decisions.
