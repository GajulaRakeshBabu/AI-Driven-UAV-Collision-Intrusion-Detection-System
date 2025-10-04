#!/usr/bin/env python3
"""
check_collision.py

This script loads two UAV flight paths from CSV files, estimates constant
velocities from the first two points, calculates the closest approach time
and minimum distance between the UAVs, and prints the results.

Requirements: numpy, pandas
"""

import numpy as np
import pandas as pd


def estimate_velocity(df):
    """
    Estimate constant velocity vector from first two points.

    Args:
        df: DataFrame with columns time, x, y, z

    Returns:
        velocity vector (vx, vy, vz)
    """
    dt = df.loc[1, 'time'] - df.loc[0, 'time']
    dx = df.loc[1, 'x'] - df.loc[0, 'x']
    dy = df.loc[1, 'y'] - df.loc[0, 'y']
    dz = df.loc[1, 'z'] - df.loc[0, 'z']
    vx = dx / dt
    vy = dy / dt
    vz = dz / dt
    return np.array([vx, vy, vz])


def closest_approach(p1, v1, p2, v2):
    """
    Calculate closest approach time and minimum distance between two UAVs
    moving at constant velocities.

    Args:
        p1, p2: initial position vectors (numpy arrays)
        v1, v2: velocity vectors (numpy arrays)

    Returns:
        t_ca: time of closest approach (seconds)
        d_min: minimum distance (meters)
    """
    dp = p1 - p2
    dv = v1 - v2
    dv_norm_sq = np.dot(dv, dv)

    if dv_norm_sq == 0:
        # Velocities are the same, so distance is constant
        t_ca = 0.0
        d_min = np.linalg.norm(dp)
        return t_ca, d_min

    t_ca = -np.dot(dp, dv) / dv_norm_sq

    # Clamp t_ca to >= 0 (future or present)
    t_ca = max(t_ca, 0.0)

    closest_p1 = p1 + v1 * t_ca
    closest_p2 = p2 + v2 * t_ca
    d_min = np.linalg.norm(closest_p1 - closest_p2)

    return t_ca, d_min


def main():
    # Load flight paths
    flight1 = pd.read_csv('data/flight1.csv')
    flight2 = pd.read_csv('data/flight2.csv')

    # Estimate velocities
    v1 = estimate_velocity(flight1)
    v2 = estimate_velocity(flight2)

    # Initial positions
    p1 = flight1.loc[0, ['x', 'y', 'z']].to_numpy()
    p2 = flight2.loc[0, ['x', 'y', 'z']].to_numpy()

    # Calculate closest approach
    t_ca, d_min = closest_approach(p1, v1, p2, v2)

    print(f"Closest approach time: {t_ca:.2f} seconds")
    print(f"Minimum distance at closest approach: {d_min:.2f} meters")


if __name__ == "__main__":
    main()
