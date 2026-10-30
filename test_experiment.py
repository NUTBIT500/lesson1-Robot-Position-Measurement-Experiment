import numpy as np
from experiment import  run_experiment
import pytest

# def main():
#     measurements_100_1, mae_mm_100_1 = run_experiment(42)
#     measurements_100_2, mae_mm_100_2 = run_experiment(42)
#     measurements_200_1, mae_mm_200_1 = run_experiment(43)
#     print(np.array_equal(measurements_100_1,measurements_100_2))
#     print(mae_mm_100_1, mae_mm_100_2, mae_mm_200_1)

        
# if __name__ == "__main__":
#      main()

def test_same_seed():
    measurements1, mae1 = run_experiment(42)
    measurements2, mae2 = run_experiment(42)

    assert np.array_equal(measurements1, measurements2)
    assert mae1 == mae2

def test_different_seed():
    measurements1, _ = run_experiment(42)
    measurements2, _ = run_experiment(32)

    assert not np.array_equal(measurements1, measurements2)
    