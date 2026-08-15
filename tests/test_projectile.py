from mechanics.projectile import (
    calculate_flight_time,
    calculate_max_height,
    calculate_range
)

def test_calculate_flight_time():
    result = calculate_flight_time(100, 45, 9.80665)

    assert abs(result - 14.421) < 0.001

def test_calculate_max_height():
    result = calculate_max_height(100, 45, 9.80665)

    assert abs(result - 254.929) < 0.001

def test_calculate_range():
    result = calculate_range(100, 45, 9.80665)

    assert abs(result - 1019.716) < 0.001

