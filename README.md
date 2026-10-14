[README_MagRobot_Linux_Installation.md](https://github.com/user-attachments/files/33450942/README_MagRobot_Linux_Installation.md)
# MagRobot on Ubuntu / Linux — reproducible research fork

**Personal research guide | 2026-10-14 | status: three local scene families visually operational**  
**Original project:** <https://github.com/MagRobotics/MagRobot>  
**Associated manuscript:** Wang, Song, Zheng, Han & Wang, *MagRobot: An Open Simulator for Magnetically Navigated Robots*, arXiv:2603.05992 (2026), <https://arxiv.org/abs/2603.05992>.

> **Provenance.** This document is for a *local Linux adaptation*; it does not purport to be an upstream-supported Linux release. The checked-in upstream scene files, the user's verified working configurations, and our independently modified dual-arm scene are three distinct artifacts. Successful rendering does **not** by itself establish magnetic tracking performance, closed-loop actuation, or reproduction of the paper's quantitative results. The local filesystem paths below are the ones used in the successful installation; exact package versions beyond the observed SOFA/Python installation should be captured with the commands in §3.

## 1. What is already working

| Local experiment | Mechanism | Proven configuration/launcher | Confirmed status | Qualification |
|---|---|---|---|---|
| Case 1: bronchoscopy | Flexible magnetic catheter/bronchoscope; robot-mounted PM | `demo_c/GUI_interface/info_wire_rob_hard_bronchus_nc.txt` | Scene displayed in Linux SOFA | Keyboard/physical insertion needs its own instrumented test. |
| Case 2: endovascular | Aortic anatomy, catheter and stationary coil array | `demo_c/GUI_interface/case2_working_backup.txt` | Scene displayed in Linux SOFA | Working backup is authoritative; do not replace with an upstream `info_wire_elc_soft_arc*` configuration without an isolated test. |
| Case 3A: single robotic EPM/capsule | One manipulator, one capsule | `demo_c/GUI_interface/info_capsule_rob.txt`, or saved scene | Rendered successfully | Scene rendering is distinct from validated closed-loop tracking. |
| Case 3 dual: 2 EPMs, one or two capsules | Two manipulators + capsule(s) | `./run_scene_case3_2arms_1capsule.sh`; `./run_scene_case3_2arms_2capsules.sh` | Linux dual-arm scene displayed; user reports the three principal versions working | Our generated extension: geometric collision screening, prescribed joint motion, point-dipole capsule dynamics; **not upstream paper's validated Case III**. |
| Case 4: cardiac EP | Eight coils + magnetized ablation catheter | `Config_Scene/Case4/info_wire_elc_hard_heart_dual_EN.md` | Not reproduced | Upstream specification, missing referenced heart mesh and specialized dual-tip magnet controller. |

## 2. The installation directory — do not mix with `~/Downloads`

```text
/home/partha/research/magnetic_robotics/MagRobot/
├── demo_c/
│   ├── main.py                          # Main SOFA entry; locally supports MAGROBOT_SCENE_CONFIG
│   ├── case3_dual_aligned.py            # Independent Linux two-arm extension, manager-generated
│   ├── GUI_interface/
│   │   ├── ceshi.txt                    # Legacy default, mutable — do not treat as a baseline
│   │   ├── case2_working_backup.txt     # User-verified preservation of Case 2
│   │   ├── info_wire_rob_hard_bronchus_nc.txt
│   │   ├── info_capsule_rob.txt
│   │   └── saved_scenes/                 # Immutable-by-convention case snapshots
│   │       ├── case1_bronchoscopy.json
│   │       ├── case2_endovascular.json
│   │       └── case3a.json
│   ├── Module_Package/                 # SOFA element creators, controller implementations
│   ├── Magnetic_Engine/                # Analytical field and gradient models
│   ├── Manipulator_Kinematics/         # 6-axis FK, Jacobian, nonlinear IK
│   ├── Control_Package/               # PID
│   ├── State_Estimation/              # EKF, gradient, LM
│   ├── Trajectory_Package/            # Polynomial/spline-related trajectory utilities
│   └── post_processing/               # Centerline and trajectory datasets
├── run_magrobot_gui.sh                # Locally tested SOFA launcher
├── run_scene_case1.sh
├── run_scene_case2.sh
├── run_scene_case3a.sh
├── run_scene_case3_2arms_1capsule.sh
└── run_scene_case3_2arms_2capsules.sh

/home/partha/manage_magrobot_scenes.py     # Single master manager; update IN PLACE
/home/partha/magrobot_sofa25_migrate.py    # Earlier migration script; archive, do not rerun blindly
/home/partha/magrobot_case2_runtime_fix.py # Earlier diagnostic script; archive, do not rerun blindly
```

**Rule:** All new iterations of the manager must retain the filename `manage_magrobot_scenes.py`. Do not accumulate `fix_1.py`, `(1).py`, or alternate launchers unless deliberately starting a new experiment branch. **Keep a Git commit for each validated milestone**; the filename stays stable but revision history remains recoverable.

## 3. Record the *actual* software stack

The user's console output establishes SOFA running from conda environment `magrobot`, Python **3.10.22**, and the installed BeamAdapter/SofaPython3/SOFA component libraries under `/home/partha/miniconda3/envs/magrobot/`. This is not enough to pin all transitive dependencies. Run:

```bash
conda activate magrobot
cd ~/research/magnetic_robotics/MagRobot
mkdir -p docs/linux/env
python --version | tee docs/linux/env/python_version.txt
conda list --explicit > docs/linux/env/conda-explicit-linux-64.txt
conda env export --no-builds > docs/linux/env/environment-from-working-machine.yml
conda list | grep -Ei 'sofa|beamadapter|numpy|scipy|pyqt|opengl' > docs/linux/env/critical-packages.txt
git status --short > docs/linux/env/git-status.txt
git rev-parse HEAD > docs/linux/env/upstream-base-commit.txt
sha256sum demo_c/GUI_interface/case2_working_backup.txt \
  demo_c/GUI_interface/info_wire_rob_hard_bronchus_nc.txt \
  demo_c/main.py run_magrobot_gui.sh \
  > docs/linux/env/worked-file-checksums.txt
```

If the project contains absolute paths, machine-specific caches or credentials, redact these before pushing the environment files publicly. `conda list --explicit` is typically architecture/platform-specific and may not reproduce on another distro or CPU.

The known working system is **SOFA 25.06-era conda packages** with the `BeamAdapter` plugin; confirm exact package builds from the exported manifest rather than guessing versions in an installation recipe. SOFA launchers must run from the expected `demo_c` working directory because the upstream code resolves meshes and JSON using relative paths.

## 4. Restore a scene without destroying another

### Preferred isolated launchers

```bash
conda activate magrobot
cd ~/research/magnetic_robotics/MagRobot
./run_scene_case1.sh
# Close SOFA before starting the next scene:
./run_scene_case2.sh
./run_scene_case3a.sh
./run_scene_case3_2arms_1capsule.sh
./run_scene_case3_2arms_2capsules.sh
```

These commands rely on having run the manager successfully:

```bash
python ~/manage_magrobot_scenes.py --repo "$PWD"
```

The manager modifies `demo_c/main.py` *once* to support the environment variable `MAGROBOT_SCENE_CONFIG`, generates scene snapshot files and the isolated dual-arm scene, and preserves `ceshi.txt`. It creates backups if replacing a generated scene. Inspect changes with `git diff` before committing.

### Legacy manual switch (fallback, independently user-verified)

```bash
cd ~/research/magnetic_robotics/MagRobot
cp demo_c/GUI_interface/info_wire_rob_hard_bronchus_nc.txt \
   demo_c/GUI_interface/ceshi.txt
./run_magrobot_gui.sh

# To return to the visually working endovascular setup:
cp demo_c/GUI_interface/case2_working_backup.txt \
   demo_c/GUI_interface/ceshi.txt
./run_magrobot_gui.sh
```

**Never** overwrite `case2_working_backup.txt` with a freshly downloaded or upstream `ceshi.txt`. For reproducible experiments, use the saved scenes, not a mutable `ceshi.txt`.

## 5. Operational workflow and logs

```bash
conda activate magrobot
cd ~/research/magnetic_robotics/MagRobot
mkdir -p logs
PYTHONUNBUFFERED=1 PYTHONFAULTHANDLER=1 \
  ./run_scene_case3_2arms_1capsule.sh \
  2>&1 | tee "logs/case3-dual-$(date +%F_%H%M%S).log"
```

1. Launch SOFA; ensure anatomical geometry and both manipulators render.
2. Check for scene-loader exceptions and SOFA plugin warnings.
3. Verify simulation time increases when **Play** is pressed.
4. Confirm motion in 3D and **numeric state** in stdout/recording; a frame moving is not proof of closed-loop control.
5. For capsule tracking, record time, capsule pose, EPM poses, magnetic field/force/torque, target, commanded joint angles, and safety-guard status.
6. Archive a screenshot and log under the same run ID, together with the full scene JSON and Git commit SHA.

### Controls

Upstream Windows README documents `Ctrl+Up/Down` for insertion/retraction and `Ctrl+I/J/K/L` for steering. **Do not assume these map identically to SOFA ImGui/Linux.** Earlier Ctrl+Shift combinations closed the window on the user machine. To debug, click viewport for focus, try a disposable test scene, inspect `KeyBoardController.onKeypressedEvent` and BeamAdapter's `InterventionalRadiologyController`, and log event keycodes. There are *two different input paths*: Python updates the desired magnet/tip orientation; BeamAdapter handles physical catheter insertion. Automated `planning` scenes are not necessarily keyboard-driven.

## 6. Failure ledger — problems encountered and meaning

| Symptom | Source | Observed cause | Verified response / open issue |
|---|---|---|---|
| SOFA opens white window | Scene initialization or visual camera | Changing `ceshi.txt` to a different Case 2 coil representation led to failure/blank display | Restore `case2_working_backup.txt` first; inspect stderr before changing camera |
| `TypeError ... list and int` in `Create_Electromagnet` | `create_scene.py`, magnetic source construction | Nested arrays in one coil source were appended as whole lists, yielding `radius[i] ** 2` on a list | Normalize a coil group to flat scalar radii/turns; preserve `ceshi` while testing |
| Duplicated `RequiredPlugin` | SOFA root | Repeated plugin objects sharing default names | One unique `RequiredPlugin` with all required modules, in each isolated scene root |
| SceneChecker missing plugin warnings | SOFA root | Libraries are preloaded but not declared in scene | Explicit scene-level dependency manifest; avoid hiding the warning |
| Duplicated `sphere_visu1` | `Create_Magnetic_sphere` | Upstream creates two children with identical `sphere_visu1` name | Give distinct node names; do not rely on permissive SOFA behavior |
| `UncoupledConstraintCorrection ... Can't find any odeSolver` | Capsule scene tree | Solver/correction placement is invalid for that node or component initialization order | Investigate corrected node placement; do not claim physical contact is solved by suppressing it |
| `fsolve` poor progress | EPM inverse positioning/IK | Nonlinear solver did not reliably converge from initial guess | Use multi-start IK and **report FK residual plus whole-arm clearance** |
| One arm passes through pedestal | Dual-arm preview | End-effector FK error was near zero while intermediate links intersected the table | Numerical link/pedestal collision screening now in local extension; mesh-resolved SOFA contact still missing |
| Black-looking robot models | Custom dual-arm preview | Missing original illumination rig | Restore the original three `DirectionalLight` sources, retain neutral gray mesh materials |
| `MousePosition` invalid `vOp` | SOFA ImGui | GUI interaction state/error, not proven to arise from surgical model | Collect isolated minimal repro; don't conflate with capsule physics |
| No motion on Play | Old two-arm preview | Explicitly `COUPLED CONTROL DISABLED` | Updated local open-loop joint motion; not a reproduction of upstream coupled feedback |
| Coil simulation looks correct but doesn't navigate | Visual-only `ceshi.txt` | Path, pose estimation, controller config are empty | Need separate navigation test with valid pipeline and quantitative motion logs |
| Linux compatibility of `Planning.started()` | `path_controller_module.py` | Uses Python `keyboard.press('up')` / `.release('up')`; focus/permissions vary | Prefer SOFA-level insertion command interface; don't require global Linux keyboard hooks |
| Hard-coded Windows file paths | `animate_controller_21.py`, `_22.py` | Recording uses `C:\\Users\\...` | Replace with pathlib relative to repository and buffered time-series writing |

## 7. SOFA plugin reasoning (not a 'load everything' recipe)

**Simulation core:** `FreeMotionAnimationLoop` evolves unconstrained mechanical states, then applies a constraint resolution stage. `CollisionPipeline`, `BruteForceBroadPhase` and `BVHNarrowPhase` select potential contact pairs. `LocalMinDistance` sets detection/alarm/contact thresholds. `RuleBasedContactManager` with `FrictionContactConstraint` controls Coulomb friction; `GenericConstraintSolver` handles constraint impulses. `EulerImplicitSolver` advances stiff system dynamics; `SparseLDLSolver`/`BTDLinearSolver` factor structural systems; `LinearSolverConstraintCorrection`/`UncoupledConstraintCorrection` couple constraints to mechanical DOFs. `BeamAdapter` implements rod/guidewire degrees of freedom and interventional insertion. These modules are not interchangeable: an anatomy visualization with OglModels only has **no mechanical collision response**.

**Render-only:** `MeshSTLLoader`, `OglModel`, `RigidMapping`, `LightManager`, `DirectionalLight` and `BackgroundSetting` do not by themselves simulate elastic tissue or contact. A rendered catheter tube does not prove BeamAdapter contact is active.

**Parameter distinctions:** `step` in scene JSON is integration step (seconds), *not necessarily* camera FPS, controller sample period, or reported experimental control frequency. `contactDistance` is an algorithmic contact-detection tolerance, not the vessel wall thickness. `alarmDistance` is a broader proximity threshold; the upstream `simulator_setting.py` sets it to **two times** `contactDistance`. `friction_coefficient` passed to the response manager is a contact friction coefficient, not bulk fluid viscosity. Magnetic moment has SI units A·m²; field T; gradient T/m; torque N·m; force N. **1 gauss = 10⁻⁴ T.**

## 8. Source-of-truth rules for research claims

- **Paper**: Use the original arXiv PDF Tables I–V and Figures 6–10 for reported parameters and validation; their numbers are not automatically the values in a local scene JSON.
- **Upstream source**: Use a pinned Git commit and exact function path; source contains experimental options, commented branches, and hard-coded values not represented in the paper.
- **Linux adaptation**: Use a separate local commit/diff. Our two-arm motion demonstration is *not* equivalent to the paper's reported single-arm GI Case III.
- **Local result**: Cite the screenshot, log, raw position/force data, configuration checksum, SOFA version and commit. Never report a paper-level RMSE based on visually plausible motion.

## 9. Recommended Git workflow — personal research fork

```bash
cd ~/research/magnetic_robotics/MagRobot
git remote -v
git status --short
git checkout -b linux-sofa25-research
mkdir -p docs/linux docs/technical experiments/baselines
cp /home/partha/manage_magrobot_scenes.py docs/linux/manage_magrobot_scenes.py
git add README_LINUX.md docs/linux docs/technical experiments/baselines
git commit -m "Document Linux SOFA baseline and code architecture"
```

First verify which paths are in your current repository and what is untracked. Do not `git add .` with large compiled meshes, recordings, local environments, personal notes or confidential data. A local branch is not automatically a GitHub fork. Create a fork in your account and add it as another remote before pushing. Attribute upstream source and comply with the repository's license; verify the license file and figure permissions before redistribution.

## 10. Experiment protocol for the first publishable benchmark

**E0. Reproducibility:** hash scenes, pin env, save platform and graphics backend.  **E1. Magnetic field unit tests:** test single dipole field and gradient at known points, Maxwell symmetries, and finite-difference gradient agreement.  **E2. Simulator test:** verify capsule acceleration agrees with applied wrench in no-contact conditions.  **E3. Beam mechanics:** vary rod modulus/diameter/mesh density; compare convergence and wall penetration.  **E4. Feedback:** add measurement noise and dropouts while holding geometry fixed.  **E5. Actuator constraints:** impose KUKA joint limits, actual robot collisions, workspace exclusion and field/current limits.  **E6. Real-world anchor:** measure B/gradient in the workspace and quantitatively compare with the simulator.

For suggested mathematical derivations, audit trails, failure modes and KUKA integration, see **`MagRobot_Technical_Monograph.tex`** / PDF accompanying this README. The monograph marks each statement as **[PAPER]**, **[SOURCE]**, **[LOCAL]** or **[PROPOSAL]**.
