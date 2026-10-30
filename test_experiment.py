import numpy as np
from experiment import  run_experiment

def test_same_seed():
    measurements1, mae1 = run_experiment(42)
    measurements2, mae2 = run_experiment(42)

    assert np.array_equal(measurements1, measurements2)
    assert mae1 == mae2

def test_different_seed():
    measurements1, _ = run_experiment(42)
    measurements2, _ = run_experiment(32)

    assert not np.array_equal(measurements1, measurements2)
    