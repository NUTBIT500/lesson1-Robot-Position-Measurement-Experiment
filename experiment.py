import numpy as np
import matplotlib.pyplot as plt
import json
from pathlib import Path
from metrics import mae_numpy
import logging

SEED = 42
N = 1000
DESIRED_POSITION = 0.500
NOISE_STD = 0.002


def run_experiment(seed=SEED):
    logging.info("Seed=%d, samples=%d", seed, N)
    rng = np.random.default_rng(seed)

    samples = rng.normal(loc = 0.0, scale = NOISE_STD, size= N)

    measured_position = DESIRED_POSITION + samples
    desired_position = np.full_like(measured_position, DESIRED_POSITION)
    MAE = mae_numpy(measured_position, desired_position) * 1000
    return measured_position, MAE


def main():

    output_dir = Path("output")
    output_dir.mkdir(parents=True,exist_ok=True)
    logging.basicConfig(
        filename=output_dir / "experiment.log",
        filemode="a",
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        encoding="utf-8"
    )
    logging.info("Experiment started")
    
    measurements, mae_mm = run_experiment()
    logging.info("MAE=%.6f mm", mae_mm)

    result = {
        "SEED": SEED,
        "n_samples": N,
        "desired_position_m": DESIRED_POSITION,
        "noise_std_m": NOISE_STD,
        "mae_mm": float(mae_mm)
    }
    
    with open(output_dir / "results.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, allow_nan=False)

    print(mae_mm)
    print(measurements - DESIRED_POSITION)
    fig, ax = plt.subplots()
    ax.hist(x = (measurements - DESIRED_POSITION) * 1000, bins=30)
    ax.set_xlabel("Position error (mm)")
    ax.set_ylabel("Frequency")
    ax.set_title("Robot Position Measurement Errors")

    fig.savefig(output_dir / "position_errors.png", dpi=150)
    plt.show()
    plt.close(fig)


if __name__ == "__main__":
    main()