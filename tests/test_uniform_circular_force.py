from mechanics.uniform_circular_force import (
    calculate_angular_velocity_v,
    calculate_centripetal_acceleration_v,
    calculate_frequency_v,
    calculate_period_v,
    calculate_centripetal_force
)


def test_calculate_angular_velocity_v():
    result = calculate_angular_velocity_v(100, 20)

    assert abs(result - 5.000) < 0.001

def test_calculate_centripetal_acceleration_v():
    result = calculate_centripetal_acceleration_v(100, 20)

    assert abs(result - 500.000) < 0.001

def test_calculate_frequency_v():
    result = calculate_frequency_v(100, 20)

    assert abs(result - 0.796) < 0.001

def test_calculate_period_v():
    result = calculate_period_v(100, 20)

    assert abs(result - 1.257) < 0.001

def test_calculate_centripetal_force():
    result = calculate_centripetal_force(10, 100, 20)

    assert abs(result - 50) < 0.001

