from probability.roulette import simulate_spins, build_wheel, calculate_winnings
import pytest


@pytest.fixture
def wheel():
    return build_wheel()


def test_calculate_winnings_red(wheel):
    results = simulate_spins(wheel, 2)
    assert -2 <= calculate_winnings(results, 1, 2, color="red") <= 2


def test_calculate_winnings_black(wheel):
    results = simulate_spins(wheel, 2)
    assert -2 <= calculate_winnings(results, 1, 2, color="black") <= 2


def test_calculate_winnings_green(wheel):
    results = simulate_spins(wheel, 2)
    assert -2 <= calculate_winnings(results, 1, 2, color="green") <= 34


def test_calculate_winnings_num(wheel):
    results = simulate_spins(wheel, 2)
    assert -2 <= calculate_winnings(results, 1, 2, number=1) <= 70
