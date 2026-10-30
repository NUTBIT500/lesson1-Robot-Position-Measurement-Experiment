import numpy as np
from experiment import  run_experiment
from validation import theoretical_mae_mm


def test_mae1():
    mae = theoretical_mae_mm(0.002)
    expected = 0.002 * 1000 * np.sqrt(2 / np.pi)
    assert np.isclose(expected, mae, 0, 1e-6)

def test_mae2():
    mae = theoretical_mae_mm(0.004)
    expected = 0.004 * 1000 * np.sqrt(2 / np.pi)
    assert np.isclose(expected, mae, 0, 1e-6)