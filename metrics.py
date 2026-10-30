import numpy as np

def mae_numpy(actual, predicted):
    actual = np.asarray(actual)
    predicted = np.asarray(predicted)
    if(np.size(actual) == 0 or np.size(predicted) == 0):
        raise ValueError
    if(np.ndim(actual) != 1 or np.ndim(predicted) != 1):
            raise ValueError
    if(np.shape(actual) == np.shape(predicted)):
        errors = np.abs(actual - predicted)
        return np.average(errors)
    else:
        raise ValueError
    

    