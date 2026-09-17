import numpy as np

from src.jacobians import axis_rate, pose_wrench_jacobians
from src.magnetics import (
    dipole_field,
    dipole_force,
    magnetic_energy,
    magnetic_torque,
    normalize,
    numerical_gradient,
)


def test_field_is_even_under_position_reversal():
    r = np.array([0.08, -0.02, 0.11])
    m = np.array([1.2, 0.3, -0.1])
    np.testing.assert_allclose(dipole_field(r, m), dipole_field(-r, m), rtol=1e-12)


def test_force_is_negative_energy_gradient():
    r = np.array([0.07, -0.03, 0.12])
    m_source = np.array([1.4, 0.2, -0.3])
    m_receiver = np.array([-0.1, 0.06, 0.025])
    numerical = -numerical_gradient(
        lambda point: magnetic_energy(point, m_source, m_receiver), r, step=2e-7
    )
    np.testing.assert_allclose(dipole_force(r, m_source, m_receiver), numerical, rtol=2e-8)


def test_torque_vanishes_when_receiver_aligns_with_field():
    r = np.array([0.0, 0.0, 0.1])
    source = np.array([0.0, 0.0, 1.0])
    field = dipole_field(r, source)
    receiver = 0.05 * normalize(field)
    np.testing.assert_allclose(magnetic_torque(r, source, receiver), np.zeros(3), atol=1e-16)


def test_axis_rate_is_tangent_to_unit_sphere():
    axis = normalize(np.array([0.2, 0.4, 0.8]))
    rate = axis_rate(axis, np.array([0.5, -0.2, 0.3]))
    assert abs(axis @ rate) < 1e-14


def test_translation_blocks_are_equal_and_opposite():
    J_source, J_receiver = pose_wrench_jacobians(
        p_source=np.array([0.02, 0.01, -0.03]),
        e_source=normalize(np.array([0.2, 0.1, 1.0])),
        p_receiver=np.array([0.08, -0.01, 0.11]),
        e_receiver=normalize(np.array([-0.2, 0.8, 0.4])),
        source_moment=1.7,
        receiver_moment=0.04,
    )
    np.testing.assert_allclose(J_source[:, :3], -J_receiver[:, :3], rtol=1e-8, atol=1e-10)
