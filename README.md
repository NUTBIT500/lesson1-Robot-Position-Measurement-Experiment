
# Robot Position Measurement Experiment

## 1. Overview

This project simulates one-dimensional robot position
measurements with Gaussian noise.

The goal is to evaluate position errors and demonstrate
reproducible experiments using Python and NumPy.

## 2. Research Question

How does Gaussian measurement noise affect the mean
absolute position error?

## 3. Mathematical Model

Measured position:

p_i = p_desired + epsilon_i

where epsilon_i follows N(0, sigma^2).

Evaluation metric:

MAE = mean(abs(measured - desired))

The resulting MAE is reported in millimeters.

## 4. Experimental Configuration

| Parameter | Value |
|---|---|
| Desired position | 0.500 m |
| Noise standard deviation | 0.002 m |
| Number of samples | 1000 |
| Random seed | 42 |

## 5. Environment

- Operating system: Windows
- Python version: 3.14.7
- Dependencies: See requirements.txt

## 6. Installation

Open PowerShell in the project directory.

Create the virtual environment:

    py -m venv .venv

Install dependencies:

    .\.venv\Scripts\python.exe -m pip install -r requirements.txt

## 7. Running the Experiment

Execute:

    .\.venv\Scripts\python.exe experiment.py

Generated files:

- output/results.json
- output/experiment.log
- output/position_errors.png

## 8. Running the Tests

Execute:

    .\.venv\Scripts\python.exe -m pytest -q

The tests verify the MAE function and random-seed
reproducibility.

## 9. Results

Seed 42:

- MAE: 1.563891842282548 mm
- Figure: output/position_errors.png

## 10. Reproducibility

Use the recorded seed, dependency versions,
experiment parameters, and source-code commit.

The same seed and compatible software environment
should reproduce the same numerical results.

## 11. Limitations

This experiment simulates measurement noise only.

It does not model real robot dynamics, controller
tracking errors, sensor bias, or hardware calibration.
