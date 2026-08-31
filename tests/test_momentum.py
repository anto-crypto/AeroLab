from physics.momentum import (
    calculate_momentum,
    calculate_impulse
)


def test_calculate_momentum():
    result = calculate_momentum(10, 2)

    assert abs(result - 20.000) < 0.001

def test_calculate_impulse():
    result = calculate_impulse(7, 5)

    assert abs(result - 35.000) < 0.001

