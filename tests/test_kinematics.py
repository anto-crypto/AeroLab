from physics.kinematics import (
    calculate_final_position,
    calculate_final_velocity
)


def test_calculate_final_position():
    result = calculate_final_position(10, 100, 3, 5)

    assert abs(result - 547.500) < 0.001

def test_calculate_final_velocity():
    result = calculate_final_velocity(100, 3, 5)

    assert abs(result - 115.000) < 0.001

