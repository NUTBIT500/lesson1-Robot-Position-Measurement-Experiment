from scipy.integrate import quad
import numpy as np
import math

def f(z):
    return z * np.exp(-z**2 / 2)

def theoretical_mae_mm(noise_std_m):
    result, error = quad(f, 0, np.inf)
    return ((2.0 * noise_std_m)/math.sqrt(2.0 * math.pi)) * result * 1000
