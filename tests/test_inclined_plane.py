from mechanics.inclined_plane import (
    calculate_acceleration,
    calculate_final_velocity,
    calculate_time
)

def test_calculate_acceleration():
    result = calculate_acceleration(0.2, 45, 9.80665)

    assert abs(result - 5.547) < 0.001

def test_calculate_final_velocity():
    result = calculate_final_velocity(50, 100, 45, 0.2, 9.80665)

    assert abs(result - 128.009) < 0.001

def test_calculate_time():
    result = calculate_time(50, 45, 0.2, 9.80665)

    assert abs(result - 5.049) < 0.001
