import numpy as np
from experiment import  run_experiment
from validation import theoretical_mae_mm

def test_same_seed():
    measurements1, mae1 = run_experiment(42)
    measurements2, mae2 = run_experiment(42)

    assert np.array_equal(measurements1, measurements2)
    assert mae1 == mae2

def test_different_seed():
    measurements1, _ = run_experiment(42)
    measurements2, _ = run_experiment(32)

    assert not np.array_equal(measurements1, measurements2)

def test_mae():
    _, mae1 = run_experiment(42)
    mae2 = theoretical_mae_mm(0.002)
    assert np.isclose(mae1, mae2, 0.05, 0)

def test_mae2():
    mae = theoretical_mae_mm(0.002)
    expected = 0.002 * 1000 * np.sqrt(2 / np.pi)
    assert np.isclose(expected, mae, 0, 1e-6)
    