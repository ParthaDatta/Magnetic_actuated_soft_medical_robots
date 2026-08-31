# Failure-Mode Register

This is a living research-idea generator.

| Failure mode | Why it matters | Evidence needed | Possible research direction |
|---|---|---|---|
| Force decays at patient depth | benchtop geometry may not translate | force vs distance curves | local/hybrid actuator optimization |
| Magnetic singularity / poor conditioning | desired wrench unavailable | condition map over workspace | singularity-aware planning/NMPC |
| Coil heating | limits sustained force | current/temp/time curves | thermal-state MPC |
| Image dropout | robot can become effectively open-loop | dropout tests | belief-space / predictor-based control |
| Low fluoroscopy frame rate | latency + radiation constraints | closed-loop tests at clinical rates | asynchronous estimation/control |
| Tool-tissue contact unknown | tissue injury or task failure | force/contact ground truth | sensorless contact observer |
| Pulsatile flow | model mismatch/disturbance | physiological waveform tests | robust/adaptive control |
| Magnet–patient collision | EPM robotic arm safety | contact force tests | admittance + constrained planning |
| Soft robot hysteresis | shape model drifts | cyclic field tests | hysteresis/viscoelastic model |
| Multi-robot global-field coupling | agents cannot act independently | controllability analysis | heterogeneous/modular control |
| Lost robot / failed retrieval | critical clinical safety issue | recovery protocol | retrieval-aware design/planning |
| Magnetic tracking-actuation interference | sensing degrades during actuation | SNR vs actuation field | time/frequency multiplexing |
