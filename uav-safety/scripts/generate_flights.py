#!/usr/bin/env python3
"""
generate_flights.py

This script generates synthetic flight paths for two UAVs with different
starting points and velocities. Saves as CSV files in data/ and plots
the paths, saving the plot in runs/flight_paths.png

Requirements: numpy, pandas, matplotlib
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os


def generate_flight(start_pos, velocity, duration=10, dt=0.1):
    """
    Generate flight path points.

    Args:
        start_pos: (x0, y0, z0) starting position
        velocity: (vx, vy, vz) velocity in m/s
        duration: total time in seconds
        dt: time step

    Returns:
        DataFrame with columns: time, x, y, z
    """
    times = np.arange(0, duration + dt, dt)
    x = start_pos[0] + velocity[0] * times
    y = start_pos[1] + velocity[1] * times
    z = start_pos[2] + velocity[2] * times
    df = pd.DataFrame({'time': times, 'x': x, 'y': y, 'z': z})
    return df

def main():
    # UAV 1: starts at (0, 0, 100), velocity (10, 5, 0) m/s
    start1 = (0, 0, 100)
    vel1 = (10, 5, 0)
    flight1 = generate_flight(start1, vel1)

    # UAV 2: starts at (100, 100, 100), velocity (-5, 10, 0) m/s
    start2 = (100, 100, 100)
    vel2 = (-5, 10, 0)
    flight2 = generate_flight(start2, vel2)

    # Save to CSV
    flight1.to_csv('data/flight1.csv', index=False)
    flight2.to_csv('data/flight2.csv', index=False)
    print("Flight paths saved as data/flight1.csv and data/flight2.csv")

    # Plot flight paths (2D: x vs y)
    plt.figure(figsize=(8, 6))
    plt.plot(flight1['x'], flight1['y'], label='UAV 1', color='blue')
    plt.plot(flight2['x'], flight2['y'], label='UAV 2', color='red')
    plt.xlabel('X position (m)')
    plt.ylabel('Y position (m)')
    plt.title('UAV Flight Paths')
    plt.legend()
    plt.grid(True)

    # Ensure runs directory exists
    os.makedirs('runs', exist_ok=True)
    plt.savefig('runs/flight_paths.png')
    print("Plot saved as runs/flight_paths.png")

    plt.show()  # Optional, to display if running interactively

if __name__ == "__main__":
    main()
