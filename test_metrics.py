from metrics import mae_numpy
import numpy as np
import pytest

def test_zero_error():
    actual = np.array([1.0, 2.0, 3.0])
    predicted = np.array([1.0, 2.0, 3.0])

    assert mae_numpy(actual, predicted) == 0.0

def test_nonzero_error():
    actual = np.array([1.0, 2.0, 3.0])
    predicted = np.array([1.2, 2.1, 2.7])
    assert abs(mae_numpy(actual, predicted) - 0.2) < 1e-12



def test_python_lists():
    actual = [1.0, 2.0, 3.0]
    predicted = [1.2, 2.1, 2.7]

    assert mae_numpy(actual, predicted) == pytest.approx(0.2)


def test_different_lengths():
    with pytest.raises(ValueError):
        mae_numpy([1, 2, 3], [1])


def test_empty_inputs():
    with pytest.raises(ValueError):
        mae_numpy([], [])

def test_multidimensional_inputs():
    with pytest.raises(ValueError):
        mae_numpy([[1, 2], [3, 4]],
                  [[1, 2], [3, 4]])


def test_incompatible_shapes():
    with pytest.raises(ValueError):
        mae_numpy([[1], [2]],
                  [[1, 2]])