import numpy as np
import matplotlib.pyplot as plt
import mplcyberpunk

plt.style.use("cyberpunk")


class PoissonProcess:
    def __init__(self, intensity, T):
        self.intensity = intensity
        self.T = T

    def generate_trajectory(self):
        t = 0
        trajectory = [0]
        while t < self.T:
            t += np.random.exponential(1 / self.intensity)
            if t < self.T:
                trajectory.append(t)
        return trajectory


def plot_trajectories(processes, labels):
    fig, axs = plt.subplots(len(processes), 1, figsize=(10, 6 * len(processes)))
    for i, process in enumerate(processes):
        for trajectory in process:
            axs[i].step([0] + trajectory, range(len(trajectory) + 1), where='post')
        axs[i].set_title(labels[i])
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    lambdas = [0.1, 0.25]
    T = 100
    trajectories = []
    labels = []
    for lam in lambdas:
        process = PoissonProcess(lam, T)
        trajectories.append([process.generate_trajectory() for _ in range(2)])
        labels.append(f"Poisson process with λ={lam}")
    plot_trajectories(trajectories, labels)
