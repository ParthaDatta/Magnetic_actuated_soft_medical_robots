"""Generate the repository's Jupyter notebooks using only the standard library."""

from __future__ import annotations

import json
from pathlib import Path
from textwrap import dedent


ROOT = Path(__file__).resolve().parents[1]
NOTEBOOKS = ROOT / "notebooks"


def source(text: str) -> list[str]:
    return dedent(text).lstrip("\n").splitlines(keepends=True)


def markdown(text: str) -> dict:
    return {"cell_type": "markdown", "metadata": {}, "source": source(text)}


def code(text: str) -> dict:
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": source(text),
    }


def notebook(cells: list[dict]) -> dict:
    return {
        "cells": cells,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3.11"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


NOTEBOOK_1 = notebook([
    markdown(r"""
    # 01 — Dipole field, force, torque, and source-formula check

    **Question.** Does the closed-form force in the supplied appendix agree with the gradient of magnetic potential energy?

    We use a convention that removes ambiguity:

    - `r = p_receiver - p_source` points from the EPM to the IPM;
    - `m_source` is the EPM moment and `m_receiver` is the IPM moment;
    - returned force and torque act on the IPM.

    The independent identities are

    $$
    \mathbf B=\frac{\mu_0}{4\pi r^3}(3\hat{\mathbf r}\hat{\mathbf r}^T-I)\mathbf m_E,
    \quad U=-\mathbf m_I^T\mathbf B,
    $$

    $$
    \mathbf F=-\nabla_{\mathbf r}U,
    \qquad \boldsymbol\tau=\mathbf m_I\times\mathbf B.
    $$
    """),
    code("""
    from pathlib import Path
    import sys
    import numpy as np
    import matplotlib.pyplot as plt

    ROOT = Path.cwd().resolve()
    if ROOT.name == "notebooks":
        ROOT = ROOT.parent
    sys.path.insert(0, str(ROOT))

    from src.magnetics import (
        MU0, dipole_field, dipole_force, magnetic_energy,
        magnetic_torque, normalize, numerical_gradient,
    )
    np.set_printoptions(precision=8, suppress=False)
    """),
    markdown(r"""
    ## A generic nonsymmetric test pose

    Axis-aligned examples can accidentally make an incorrect cross term vanish. We therefore use nonparallel magnet moments and an oblique relative position.
    """),
    code("""
    r = np.array([0.071, -0.026, 0.113])            # m, EPM -> IPM
    m_E = 2.40 * normalize(np.array([0.34, 0.18, 0.92]))  # A m^2
    m_I = 0.055 * normalize(np.array([-0.25, 0.83, 0.49]))

    B = dipole_field(r, m_E)
    F_closed = dipole_force(r, m_E, m_I)
    F_energy = -numerical_gradient(
        lambda x: magnetic_energy(x, m_E, m_I), r, step=2e-7
    )
    T = magnetic_torque(r, m_E, m_I)

    print("B [T]       =", B)
    print("F closed [N]=", F_closed)
    print("F=-grad U [N]=", F_energy)
    print("Torque [Nm] =", T)
    print("relative force error =", np.linalg.norm(F_closed-F_energy)/np.linalg.norm(F_energy))
    assert np.allclose(F_closed, F_energy, rtol=2e-8)
    """),
    markdown(r"""
    ## Matrix form and the apparent printed cross-term error

    Let $\mathbf m_E=m_E\hat{\mathbf e}_E$, $\mathbf m_I=m_I\hat{\mathbf e}_I$,
    $Z=I-5\hat{\mathbf r}\hat{\mathbf r}^T$, and
    $\lambda=\mu_0m_Em_I/(4\pi r^3)$. The energy-consistent matrix expression is

    $$
    \mathbf F=\frac{3\lambda}{r}
    [\hat e_I\hat e_E^T+\hat e_E\hat e_I^T+(\hat e_I^TZ\hat e_E)I]\hat r.
    $$

    The printed appendix appears to repeat $\hat e_I$ in the scalar term. We compute both versions.
    """),
    code("""
    distance = np.linalg.norm(r)
    r_hat = r / distance
    e_E, e_I = normalize(m_E), normalize(m_I)
    lambda_ = MU0 * np.linalg.norm(m_E) * np.linalg.norm(m_I) / (4*np.pi*distance**3)
    Z = np.eye(3) - 5*np.outer(r_hat, r_hat)

    common = np.outer(e_I, e_E) + np.outer(e_E, e_I)
    F_cross = 3*lambda_/distance * (
        common + (e_I @ Z @ e_E)*np.eye(3)
    ) @ r_hat
    F_printed = 3*lambda_/distance * (
        common + (e_I @ Z @ e_I)*np.eye(3)
    ) @ r_hat

    for label, force in [("energy gradient", F_energy),
                         ("standard cross term", F_cross),
                         ("printed repeated-IPM term", F_printed)]:
        print(f"{label:27s}", force)
    print("standard relative error:", np.linalg.norm(F_cross-F_energy)/np.linalg.norm(F_energy))
    print("printed relative error :", np.linalg.norm(F_printed-F_energy)/np.linalg.norm(F_energy))
    assert np.allclose(F_cross, F_energy, rtol=2e-8)
    assert not np.allclose(F_printed, F_energy, rtol=1e-3)
    """),
    markdown(r"""
    ## Surgical-depth scaling

    For fixed moments and orientation, field and torque scale as $r^{-3}$ while force scales as $r^{-4}$. The plot normalizes both to their values at 50 mm. It visualizes why abdominal-wall thickness and target depth dominate permanent-magnet design.
    """),
    code("""
    distances_mm = np.linspace(50, 250, 401)
    torque_ratio = (50 / distances_mm)**3
    force_ratio = (50 / distances_mm)**4

    fig, ax = plt.subplots(figsize=(7.5, 4.5))
    ax.semilogy(distances_mm, torque_ratio, label=r"field / torque $r^{-3}$", lw=2.5)
    ax.semilogy(distances_mm, force_ratio, label=r"force $r^{-4}$", lw=2.5)
    ax.axvspan(100, 180, color="tab:orange", alpha=.12, label="example human-scale depth band")
    ax.set(xlabel="EPM–IPM separation [mm]", ylabel="ratio relative to 50 mm",
           title="Distance penalty for dipole actuation")
    ax.grid(True, which="both", alpha=.3)
    ax.legend()
    plt.show()
    """),
    markdown(r"""
    ## Interpretation

    - The energy gradient is the independent reference, not another rearrangement of the same force equation.
    - The standard cross term matches that reference at a generic pose.
    - The expression with two IPM axes generally does not.
    - A model that is adequate at 50 mm can become physically weak at 150–200 mm even before robot reach, collisions, or tissue are considered.
    """),
])


NOTEBOOK_2 = notebook([
    markdown(r"""
    # 02 — Wrench-rate Jacobian and sign-convention validation

    The supplied appendix ends with

    $$\dot{\mathbf w}_m=J_q\dot{\mathbf q}+J_\chi\dot{\boldsymbol\chi}.$$

    This notebook constructs the EPM/source and IPM/receiver twist-to-wrench Jacobians by central differences and verifies the local prediction. This is the reference against which an analytic derivation should be tested.
    """),
    code("""
    from pathlib import Path
    import sys
    import numpy as np

    ROOT = Path.cwd().resolve()
    if ROOT.name == "notebooks":
        ROOT = ROOT.parent
    sys.path.insert(0, str(ROOT))

    from src.jacobians import (
        axis_rate, damped_pseudoinverse, pose_wrench_jacobians,
        rotate_axis_first_order,
    )
    from src.magnetics import magnetic_wrench, normalize
    np.set_printoptions(precision=6, suppress=True)
    """),
    markdown(r"""
    ## Pose, moments, and numerical Jacobians

    Twists are ordered $[v_x,v_y,v_z,\omega_x,\omega_y,\omega_z]^T$. Rotations are right-handed spatial perturbations. The returned Jacobians satisfy

    $$\dot w\approx J_E v_E+J_I v_I.$$
    """),
    code("""
    p_E = np.array([0.015, 0.025, -0.040])
    e_E = normalize(np.array([0.25, -0.15, 0.96]))
    p_I = np.array([0.085, -0.005, 0.105])
    e_I = normalize(np.array([-0.30, 0.82, 0.48]))
    m_E, m_I = 2.5, 0.050

    J_E, J_I = pose_wrench_jacobians(p_E, e_E, p_I, e_I, m_E, m_I)
    print("source/EPM Jacobian shape:", J_E.shape)
    print("receiver/IPM Jacobian shape:", J_I.shape)
    print("translation cancellation norm:", np.linalg.norm(J_E[:, :3] + J_I[:, :3]))
    assert np.allclose(J_E[:, :3], -J_I[:, :3], rtol=1e-8, atol=1e-10)
    """),
    markdown(r"""
    Translation of both magnets by the same velocity cannot change the relative geometry, so the two translation blocks must cancel. This is a powerful sign check.
    """),
    code("""
    v_E = np.array([0.003, -0.002, 0.001, 0.06, -0.04, 0.03])
    v_I = np.array([-0.001, 0.0015, 0.0005, -0.02, 0.01, 0.04])
    dt = 1e-4

    w0 = magnetic_wrench(p_I-p_E, m_E*e_E, m_I*e_I)
    predicted = J_E @ v_E + J_I @ v_I

    p_E_next = p_E + dt*v_E[:3]
    p_I_next = p_I + dt*v_I[:3]
    e_E_next = rotate_axis_first_order(e_E, dt*v_E[3:])
    e_I_next = rotate_axis_first_order(e_I, dt*v_I[3:])
    w1 = magnetic_wrench(p_I_next-p_E_next, m_E*e_E_next, m_I*e_I_next)
    measured = (w1-w0)/dt

    print("predicted wrench rate:", predicted)
    print("finite-step rate       :", measured)
    print("relative error         :", np.linalg.norm(predicted-measured)/np.linalg.norm(measured))
    assert np.allclose(predicted, measured, rtol=4e-3, atol=1e-8)
    """),
    markdown(r"""
    ## The unit-axis derivative

    For a spatial angular velocity,

    $$\dot{\hat e}=\omega\times\hat e=[\hat e]_\times^T\omega.$$

    Its derivative must lie in the tangent plane of the unit sphere, so $\hat e^T\dot{\hat e}=0$.
    """),
    code("""
    omega = np.array([0.4, -0.2, 0.1])
    e_dot = axis_rate(e_E, omega)
    print("e_dot:", e_dot)
    print("e.T e_dot (must be zero):", e_E @ e_dot)
    assert abs(e_E @ e_dot) < 1e-14
    """),
    markdown(r"""
    ## Damped differential inverse

    Assume the EPM end-effector twist is directly commanded. Given a desired wrench rate $y$ after compensating IPM motion, a damped solution is

    $$v_E=J_E^T(J_EJ_E^T+\rho^2I)^{-1}y.$$

    The numerical value of $\rho$ is meaningful only after force/torque and translation/rotation scaling. This example uses explicit row scaling solely for demonstration.
    """),
    code("""
    # Convert torque rows to an equivalent force using a 50 mm characteristic length.
    length_scale = 0.05
    W = np.diag([1, 1, 1, 1/length_scale, 1/length_scale, 1/length_scale])
    J_scaled = W @ J_E
    desired_wrench_rate = np.array([0.003, -0.002, 0.001, 3e-5, -2e-5, 1e-5])
    y_scaled = W @ desired_wrench_rate

    for rho in [1e-9, 1e-4, 1e-2]:
        v_command = damped_pseudoinverse(J_scaled, rho) @ y_scaled
        residual = J_E @ v_command - desired_wrench_rate
        print(f"rho={rho:8.1e} |v|={np.linalg.norm(v_command):.5g} "
              f"scaled residual={np.linalg.norm(W@residual):.5g}")
    """),
    markdown(r"""
    ## Implementation checklist

    1. Verify the relative-position derivative before grouping terms.
    2. Specify spatial versus body angular velocity.
    3. Check the analytic Jacobian at many nonsymmetric poses.
    4. Scale mixed force/torque and translation/rotation units.
    5. Monitor rank, saturation, and residual task slack online.
    6. Include internal motion, localization delay, and contact disturbances in the closed-loop test.
    """),
])


NOTEBOOK_3 = notebook([
    markdown(r"""
    # 03 — Surgical-depth scaling and architecture selection

    This notebook turns the dipole scaling laws into a first hardware-screening calculation. It does **not** replace a finite-magnet model or measurements.

    We compare the on-axis force and maximum torque of example EPM/IPM moments over clinically relevant separations, then build a transparent architecture scorecard.
    """),
    code("""
    from pathlib import Path
    import sys
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    ROOT = Path.cwd().resolve()
    if ROOT.name == "notebooks":
        ROOT = ROOT.parent
    sys.path.insert(0, str(ROOT))

    from src.magnetics import dipole_field, dipole_force
    """),
    markdown(r"""
    ## Example moments and depth sweep

    The source and receiver moments below are placeholders. Replace them with identified values and repeat with measured field/force maps. For axial attraction both moments and the separation axis are aligned. For maximum torque the IPM is perpendicular to the local field.
    """),
    code("""
    m_E_mag = 25.0      # A m^2, illustrative large external permanent magnet
    m_I_mag = 0.050     # A m^2, illustrative embedded magnet
    depths_mm = np.linspace(50, 250, 401)

    forces, torques = [], []
    for depth_mm in depths_mm:
        r = np.array([0.0, 0.0, depth_mm/1000])
        m_E = np.array([0.0, 0.0, m_E_mag])
        m_I_axial = np.array([0.0, 0.0, m_I_mag])
        m_I_perp = np.array([m_I_mag, 0.0, 0.0])
        forces.append(abs(dipole_force(r, m_E, m_I_axial)[2]))
        torques.append(m_I_mag*np.linalg.norm(dipole_field(r, m_E)))

    fig, axes = plt.subplots(1, 2, figsize=(11, 4.2))
    axes[0].semilogy(depths_mm, forces, lw=2.5)
    axes[0].set(xlabel="separation [mm]", ylabel="axial attraction [N]", title="Illustrative force")
    axes[1].semilogy(depths_mm, torques, lw=2.5, color="tab:orange")
    axes[1].set(xlabel="separation [mm]", ylabel="maximum torque [N m]", title="Illustrative torque")
    for ax in axes:
        ax.grid(True, which="both", alpha=.3)
    plt.tight_layout()
    plt.show()
    """),
    code("""
    query_depths = np.array([75, 100, 125, 150, 180, 200])
    table = pd.DataFrame({"depth_mm": query_depths})
    table["force_N"] = np.interp(query_depths, depths_mm, forces)
    table["max_torque_Nm"] = np.interp(query_depths, depths_mm, torques)
    table
    """),
    markdown(r"""
    ## Architecture scorecard

    Scores are deliberately explicit and editable: 1 is poor, 5 is strong. The example weights reflect a human-scale minimally invasive system that values deep reach, clinical access, fast control, and thermal safety. They are **not universal rankings**.
    """),
    code("""
    scores = pd.DataFrame({
        "deep_reach":       [4, 4, 3, 3, 5, 3],
        "fast_modulation":  [2, 2, 3, 5, 4, 1],
        "patient_access":   [3, 2, 3, 2, 5, 4],
        "low_heat":         [5, 5, 5, 2, 2, 5],
        "field_flexibility": [2, 4, 4, 5, 4, 1],
        "simple_calibration":[3, 2, 2, 3, 2, 3],
    }, index=[
        "single robot EPM", "dual robot EPM", "rotating-PM array",
        "fixed coil array", "under-table/mobile coils", "magnetic anchor"
    ])
    weights = pd.Series({
        "deep_reach": .24, "fast_modulation": .16, "patient_access": .22,
        "low_heat": .12, "field_flexibility": .18, "simple_calibration": .08
    })
    scores["weighted_total"] = scores[weights.index].mul(weights).sum(axis=1)
    scores.sort_values("weighted_total", ascending=False)
    """),
    code("""
    ordered = scores.sort_values("weighted_total")
    fig, ax = plt.subplots(figsize=(7.5, 4.5))
    ax.barh(ordered.index, ordered["weighted_total"], color="tab:blue")
    ax.set(xlim=(0, 5), xlabel="weighted score [1–5]",
           title="Example decision score — replace with project evidence")
    ax.grid(axis="x", alpha=.3)
    plt.tight_layout()
    plt.show()
    """),
    markdown(r"""
    ## How to use this responsibly

    1. Replace moment estimates with identified magnet parameters.
    2. Replace the dipole sweep with the calibrated or finite-magnet model inside its valid domain.
    3. Define force/torque requirements from the task, flow, tether, gravity, and tissue contact.
    4. Score architectures with measured workspace, heat, collision, imaging, and access data.
    5. Perform sensitivity analysis over uncertain anatomy and preferences.
    6. Keep “no feasible architecture yet” as a valid outcome.
    """),
])


def main() -> None:
    NOTEBOOKS.mkdir(parents=True, exist_ok=True)
    payloads = {
        "01_dipole_field_force_torque.ipynb": NOTEBOOK_1,
        "02_wrench_jacobian_validation.ipynb": NOTEBOOK_2,
        "03_surgical_depth_and_architecture.ipynb": NOTEBOOK_3,
    }
    for filename, payload in payloads.items():
        destination = NOTEBOOKS / filename
        destination.write_text(json.dumps(payload, indent=1), encoding="utf-8")
        print(destination.relative_to(ROOT))


if __name__ == "__main__":
    main()
