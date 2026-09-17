# 3. Magnetic actuation architectures

No architecture is “best” without a target depth, required wrench, field bandwidth, imaging modality, sterile workflow, and emergency strategy.

## 3.1 Comparative design table

| Architecture | Control input | Local authority | Surgical strengths | Principal limitations | Representative sources |
|---|---|---|---|---|---|
| Robotically actuated single EPM | 6- or 7-DOF arm pose | Coupled field/gradient; practical 5-DOF device manipulation | High field without Joule heating; large reachable workspace; intuitive capsule/catheter platform | Moving mass near patient; coupled wrench; singularities; collision and speed limits | Mahoney & Abbott 2016; Pittiglio *et al.* 2019 |
| Two robotically actuated EPMs | Two arm poses | Enlarged field/gradient set; collaborative shaping | More independent wrench shaping; reduced need to approach closely | Magnet–magnet forces; dual-arm collision planning; local minima; safety interlocks | Pittiglio *et al.* 2023; Brockdorff *et al.* 2025 |
| Rotating permanent-magnet array | Rotor angles/speeds | Field and gradient produced mechanically | Low electrical heating; compact around small workspace | Bearings/motors; mechanical bandwidth; complex calibration; acoustic/vibration concerns | Ryan & Diller 2017 |
| Multi-coil electromagnetic system | Coil currents | Linear current-to-field map before saturation | Fast modulation; no moving magnet; optimization-friendly | Joule heating, current limits, bulky cores/coils, finite bore/workspace | OctoMag; BigMag; Navion-family systems |
| Mobile/under-table coils | Coil currents and sometimes platform pose | Human-scale field/gradient at depth | Less obstruction near operating table; compatible access for clinicians | Power/thermal management; weaker gradients at depth; room integration | Pancaldi *et al.* preprint; human-scale systems |
| Magnetic anchoring and guidance | External hand-held or robotic magnet plus internal anchor | Attraction/retention and limited steering | Removes shafts/trocars for camera or retractor; useful in laparoscopy | Abdominal-wall thickness; pressure injury; loss/retrieval; limited dexterity | MAGS clinical literature |
| MRI gradient/main field | Scanner field, gradients, RF sequences | Scanner-constrained force/torque | Deep anatomical imaging and actuation in one environment | Low available actuation gradient, scanner scheduling, MR safety, sequence constraints | MRI microrobotics literature |
| Local magnetic coupling | Magnet/electromagnet near port or tool | Strong short-range force/torque | Efficient in confined laparoscopic workspace | Requires internal access; local heating/size; cable or port burden | Magnetic retraction and coupled-tool literature |

## 3.2 Single robotically actuated permanent magnet

The external robot moves and rotates one EPM. Its pose determines both $\mathbf B$ and $\nabla\mathbf B$ at the IPM. This architecture is mechanically simple and avoids coil heating, but the field and gradient cannot be assigned independently.

The usual control chain is

$$
\dot{\mathbf q}
\rightarrow
\mathbf v_E
\rightarrow
\dot{\mathbf w}_m
\rightarrow
\dot{\boldsymbol\chi}.
$$

The external arm may have seven joints, but the magnetic task can still lose rank. Redundancy should therefore be used for collision avoidance, joint-limit avoidance, field-model quality, or keeping the heavy EPM away from the patient—not just for an arbitrary posture objective.

## 3.3 Two external permanent magnets

Two EPMs superpose their fields:

$$
\mathbf B=\mathbf B_1+\mathbf B_2,
\qquad
\nabla\mathbf B=\nabla\mathbf B_1+\nabla\mathbf B_2.
$$

Superposition increases local controllability but creates global planning problems. Each EPM exerts a large wrench on the other; robot arms can collide; and a locally good field solution can require an unsafe transition between actuator poses. A complete planner must therefore optimize both the internal magnetic command and the external robot trajectories.

Brockdorff *et al.* demonstrate why actuator-space planning matters: restricting the EPM paths and explicitly suppressing unwanted actuation avoids field/gradient spikes during transitions. The lesson generalizes to surgery: a safe final magnetic configuration is insufficient if the path to it causes transient tissue force.

## 3.4 Electromagnetic arrays

For $n$ coils operated in a linear range,

$$
\mathbf u_m=
\begin{bmatrix}\mathbf B\\\operatorname{vec}_5(\nabla\mathbf B)\end{bmatrix}
=A(\mathbf p)\mathbf i,
$$

where $A(\mathbf p)\in\mathbb R^{8\times n}$ is the actuation matrix and $\mathbf i$ contains coil currents. At a fixed point, the minimum-norm current is

$$
\mathbf i=A^\dagger\mathbf u_d,
$$

but a surgical controller normally solves a constrained problem:

$$
\min_{\mathbf i}\;
\|W(A\mathbf i-\mathbf u_d)\|_2^2+\rho\|\mathbf i\|_2^2
\quad\text{s.t.}\quad
|i_k|\le i_{k,\max},\;T_k\le T_{k,\max}.
$$

Coil geometry determines whether all desired field/gradient combinations are achievable and how rapidly current and temperature limits are reached. The minimum-number-of-electromagnets literature should be read together with actual workspace maps; algebraic rank at one point does not guarantee usable actuation throughout an anatomical volume.

## 3.5 Rotating permanent magnets

Rotating-dipole systems modulate field and gradient using motor angles instead of current. They can produce strong actuation without coil heating, but the input-to-field map is nonlinear and periodic. Useful controller states include rotor phases and speeds, while constraints include angular acceleration, motor torque, vibration, and forbidden phase combinations.

Ryan and Diller's full-dexterity system is a key example: eight rotating permanent magnets generate three-dimensional fields and gradients for microscale manipulation. Its significance is architectural—mechanical phase becomes a high-bandwidth magnetic control variable.

## 3.6 Magnetic anchoring in laparoscopy

Magnetic anchoring and guidance systems couple an internal camera, retractor, or tool to an external magnet across the abdominal wall. The magnetic interaction replaces a rigid shaft crossing the incision.

For these systems, “control accuracy” is only part of performance. At minimum, report:

- abdominal-wall thickness and tissue composition;
- attraction force versus separation and lateral offset;
- internal contact footprint and estimated pressure;
- slip under respiration, insufflation, and instrument interaction;
- deployment and retrieval method;
- failure response if coupling is lost;
- interference with metallic laparoscopic tools.

The same $r^{-4}$ force scaling that enables strong close-range anchoring can create high tissue compression. Force limits must be derived from tissue contact, not only magnet ratings.

## 3.7 Architecture-selection worksheet

Before selecting hardware, fill these values:

| Requirement | Value to determine |
|---|---|
| deepest target and expected body-wall range | mm |
| required force/torque envelope | N, N·m |
| required controlled DOF | field, force, pose, shape |
| dynamic bandwidth | Hz |
| surgical access cone around patient | degrees / volume |
| imaging modality and line-of-sight constraints | modality |
| allowable surface/device/tissue temperature | °C |
| allowable ferromagnetic equipment | inventory |
| localization latency and uncertainty | ms, mm, degrees |
| emergency removal or passive-safe state | procedure |

Choose the architecture only after comparing these requirements with full-workspace field, gradient, thermal, and collision maps.
