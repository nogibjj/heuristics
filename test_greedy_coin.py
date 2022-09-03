# write a test for greedy_coin
from greedy_coin import greedy_coin


def test_greedy_coin():
    assert greedy_coin(0.25) == {0.25: 1, 0.10: 0, 0.05: 0, 0.01: 0}
    assert greedy_coin(1.51) == {0.25: 6, 0.10: 0, 0.05: 0, 0.01: 1}
