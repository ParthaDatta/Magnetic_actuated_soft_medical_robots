"""Canonical point-dipole equations with explicit geometric conventions.

Convention
----------
``r = p_receiver - p_source`` points from the source magnet to the receiver.
The returned force and torque act on the receiver. Magnetic moments use SI
units A m^2; position uses metres; field, force, and torque are T, N, and N m.
"""

from __future__ import annotations

import numpy as np

MU0 = 4.0e-7 * np.pi


def _vec3(value: np.ndarray, name: str) -> np.ndarray:
    vector = np.asarray(value, dtype=float).reshape(3)
    if not np.all(np.isfinite(vector)):
        raise ValueError(f"{name} must contain finite values")
    return vector


def normalize(value: np.ndarray, *, atol: float = 1e-15) -> np.ndarray:
    vector = _vec3(value, "value")
    norm = np.linalg.norm(vector)
    if norm <= atol:
        raise ValueError("cannot normalize a zero vector")
    return vector / norm


def skew(value: np.ndarray) -> np.ndarray:
    """Return [v]_x such that [v]_x a = v × a."""
    x, y, z = _vec3(value, "value")
    return np.array([[0.0, -z, y], [z, 0.0, -x], [-y, x, 0.0]])


def dipole_field(r: np.ndarray, m_source: np.ndarray) -> np.ndarray:
    """Field at a receiver displaced by ``r`` from a point dipole source."""
    r = _vec3(r, "r")
    m_source = _vec3(m_source, "m_source")
    distance = np.linalg.norm(r)
    if distance <= 0.0:
        raise ValueError("point-dipole field is singular at r = 0")
    r_hat = r / distance
    D = 3.0 * np.outer(r_hat, r_hat) - np.eye(3)
    return MU0 / (4.0 * np.pi * distance**3) * D @ m_source


def magnetic_energy(r: np.ndarray, m_source: np.ndarray, m_receiver: np.ndarray) -> float:
    """Potential energy U = -m_receiver · B_source."""
    m_receiver = _vec3(m_receiver, "m_receiver")
    return float(-m_receiver @ dipole_field(r, m_source))


def dipole_force(r: np.ndarray, m_source: np.ndarray, m_receiver: np.ndarray) -> np.ndarray:
    """Force on the receiver: F = ∇_r(m_receiver · B_source)."""
    r = _vec3(r, "r")
    m_source = _vec3(m_source, "m_source")
    m_receiver = _vec3(m_receiver, "m_receiver")
    distance = np.linalg.norm(r)
    if distance <= 0.0:
        raise ValueError("point-dipole force is singular at r = 0")
    r_hat = r / distance
    a = float(m_source @ r_hat)
    b = float(m_receiver @ r_hat)
    c = float(m_source @ m_receiver)
    bracket = a * m_receiver + b * m_source + c * r_hat - 5.0 * a * b * r_hat
    return 3.0 * MU0 / (4.0 * np.pi * distance**4) * bracket


def magnetic_torque(r: np.ndarray, m_source: np.ndarray, m_receiver: np.ndarray) -> np.ndarray:
    """Torque on the receiver: T = m_receiver × B_source."""
    m_receiver = _vec3(m_receiver, "m_receiver")
    return np.cross(m_receiver, dipole_field(r, m_source))


def magnetic_wrench(r: np.ndarray, m_source: np.ndarray, m_receiver: np.ndarray) -> np.ndarray:
    """Stack the receiver force and torque as [F_x,F_y,F_z,T_x,T_y,T_z]."""
    return np.concatenate(
        (dipole_force(r, m_source, m_receiver), magnetic_torque(r, m_source, m_receiver))
    )


def numerical_gradient(function, point: np.ndarray, step: float = 1e-6) -> np.ndarray:
    """Central-difference gradient used only for derivation checks."""
    point = np.asarray(point, dtype=float)
    gradient = np.empty_like(point)
    for index in range(point.size):
        delta = np.zeros_like(point)
        delta[index] = step
        gradient[index] = (function(point + delta) - function(point - delta)) / (2.0 * step)
    return gradient
