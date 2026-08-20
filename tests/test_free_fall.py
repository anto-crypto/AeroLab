from mechanics.free_fall import (
    calculate_fall_time,
    calculate_final_velocity
)


def test_calculate_fall_time():
    result = calculate_fall_time(100, 50, 9.80665)

    assert abs(result - 10.685) < 0.001

def test_calculate_final_velocity():
    result = calculate_final_velocity(100, 50, 9.80665)

    assert abs(result + 4.789) < 0.001

