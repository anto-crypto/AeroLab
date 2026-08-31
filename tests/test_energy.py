from physics.energy import (
    calculate_kinetic_energy,
    calculate_gravitational_potential_energy,
    calculate_mechanical_energy
)


def test_calculate_kinetic_energy():
    result = calculate_kinetic_energy(10, 2)

    assert abs(result - 20.000) < 0.001

def test_calculate_gravitational_potential_energy():
    result = calculate_gravitational_potential_energy(10, 9.80665, 20)

    assert abs(result - 1961.330) < 0.001

def test_calculate_mechanical_energy():
    result = calculate_mechanical_energy(10, 2, 9.80665, 20)

    assert abs(result - 1981.330) < 0.001

