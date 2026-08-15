from mechanics.circular_motion import (
    calculate_angular_velocity,
    calculate_angular_velocity_v,
    calculate_centripetal_acceleration,
    calculate_centripetal_acceleration_v,
    calculate_frequency,
    calculate_frequency_v,
    calculate_period,
    calculate_period_v
)

def test_calculate_angular_velocity():
    result = calculate_angular_velocity(45, 10)

    assert abs(result - 0.079) < 0.001

def test_calculate_angular_velocity_v():
    result = calculate_angular_velocity_v(100, 20)

    assert abs(result - 5.000) < 0.001

def test_calculate_centripetal_acceleration():
    result = calculate_centripetal_acceleration(45, 10, 20)

    assert abs(result - 0.123) < 0.001

def test_calculate_centripetal_acceleration_v():
    result = calculate_centripetal_acceleration_v(100, 20)

    assert abs(result - 500.000) < 0.001

def test_calculate_frequency():
    result = calculate_frequency(45, 10)

    assert abs(result - 0.013) < 0.001

def test_calculate_frequency_v():
    result = calculate_frequency_v(100, 20)

    assert abs(result - 0.796) < 0.001

def test_calculate_period():
    result = calculate_period(45, 10)

    assert abs(result - 80.000) < 0.001

def test_calculate_period_v():
    result = calculate_period_v(100, 20)

    assert abs(result - 1.257) < 0.001
