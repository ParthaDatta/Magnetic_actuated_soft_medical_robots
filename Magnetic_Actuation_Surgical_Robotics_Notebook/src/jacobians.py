"""Finite-difference and kinematic helpers for magnetic wrench Jacobians."""

from __future__ import annotations

import numpy as np

from .magnetics import magnetic_wrench, normalize, skew


def axis_rate(axis: np.ndarray, angular_velocity: np.ndarray) -> np.ndarray:
    """Unit-axis derivative: e_dot = omega × e = [e]_x.T omega."""
    axis = normalize(axis)
    return skew(axis).T @ np.asarray(angular_velocity, dtype=float).reshape(3)


def central_jacobian(function, point: np.ndarray, step: float = 1e-6) -> np.ndarray:
    point = np.asarray(point, dtype=float)
    base = np.asarray(function(point), dtype=float)
    jacobian = np.empty((base.size, point.size), dtype=float)
    for index in range(point.size):
        delta = np.zeros_like(point)
        delta[index] = step
        jacobian[:, index] = (function(point + delta) - function(point - delta)) / (2.0 * step)
    return jacobian


def rotate_axis_first_order(axis: np.ndarray, rotation_vector: np.ndarray) -> np.ndarray:
    """First-order axis update, normalized for finite-difference evaluation."""
    axis = normalize(axis)
    rotation_vector = np.asarray(rotation_vector, dtype=float).reshape(3)
    return normalize(axis + np.cross(rotation_vector, axis))


def pose_wrench_jacobians(
    p_source: np.ndarray,
    e_source: np.ndarray,
    p_receiver: np.ndarray,
    e_receiver: np.ndarray,
    source_moment: float,
    receiver_moment: float,
    step_position: float = 1e-6,
    step_angle: float = 1e-6,
) -> tuple[np.ndarray, np.ndarray]:
    """Return numerical 6x6 source and receiver twist-to-wrench Jacobians.

    Each twist is ordered [linear velocity; angular velocity]. Rotations are
    spatial, right-handed infinitesimal rotations. This function is intended
    for checking an analytic derivation, not for a real-time controller.
    """
    p_source = np.asarray(p_source, dtype=float).reshape(3)
    p_receiver = np.asarray(p_receiver, dtype=float).reshape(3)
    e_source = normalize(e_source)
    e_receiver = normalize(e_receiver)

    def evaluate(ps, es, pr, er):
        return magnetic_wrench(
            pr - ps,
            source_moment * normalize(es),
            receiver_moment * normalize(er),
        )

    source_jacobian = np.empty((6, 6))
    receiver_jacobian = np.empty((6, 6))
    for index in range(3):
        dp = np.zeros(3)
        dp[index] = step_position
        source_jacobian[:, index] = (
            evaluate(p_source + dp, e_source, p_receiver, e_receiver)
            - evaluate(p_source - dp, e_source, p_receiver, e_receiver)
        ) / (2.0 * step_position)
        receiver_jacobian[:, index] = (
            evaluate(p_source, e_source, p_receiver + dp, e_receiver)
            - evaluate(p_source, e_source, p_receiver - dp, e_receiver)
        ) / (2.0 * step_position)

        dtheta = np.zeros(3)
        dtheta[index] = step_angle
        es_plus = rotate_axis_first_order(e_source, dtheta)
        es_minus = rotate_axis_first_order(e_source, -dtheta)
        er_plus = rotate_axis_first_order(e_receiver, dtheta)
        er_minus = rotate_axis_first_order(e_receiver, -dtheta)
        source_jacobian[:, 3 + index] = (
            evaluate(p_source, es_plus, p_receiver, e_receiver)
            - evaluate(p_source, es_minus, p_receiver, e_receiver)
        ) / (2.0 * step_angle)
        receiver_jacobian[:, 3 + index] = (
            evaluate(p_source, e_source, p_receiver, er_plus)
            - evaluate(p_source, e_source, p_receiver, er_minus)
        ) / (2.0 * step_angle)
    return source_jacobian, receiver_jacobian


def damped_pseudoinverse(matrix: np.ndarray, damping: float) -> np.ndarray:
    """Right damped inverse A# = A.T (A A.T + rho^2 I)^-1."""
    matrix = np.asarray(matrix, dtype=float)
    rows = matrix.shape[0]
    return matrix.T @ np.linalg.solve(
        matrix @ matrix.T + damping**2 * np.eye(rows), np.eye(rows)
    )
