#!/usr/bin/env python3
"""
dataset.py

This script generates a fake UAV flight dataset with latitude, longitude,
altitude, and speed. Saves as CSV files in data/ for two UAVs.

Beginner-friendly: Uses simple loops and numpy for data generation.

Requirements: numpy, pandas
"""

import numpy as np
import pandas as pd

def generate_uav_dataset(start_lat, start_lon, start_alt, velocity_lat, velocity_lon, velocity_alt, speed, duration=60, dt=1):
    """
    Generate UAV flight data.

    Args:
        start_lat, start_lon, start_alt: Starting position
        velocity_lat, velocity_lon, velocity_alt: Velocity components (degrees/s for lat/lon approx)
        speed: Constant speed (m/s)
        duration: Total time (s)
        dt: Time step (s)

    Returns:
        DataFrame with time, latitude, longitude, altitude, speed
    """
    times = np.arange(0, duration + dt, dt)
    latitudes = start_lat + velocity_lat * times
    longitudes = start_lon + velocity_lon * times
    altitudes = start_alt + velocity_alt * times
    speeds = np.full_like(times, speed)  # Constant speed

    df = pd.DataFrame({
        'time': times,
        'latitude': latitudes,
        'longitude': longitudes,
        'altitude': altitudes,
        'speed': speeds
    })
    return df

def main():
    # UAV 1: Starts at lat 37.7749, lon -122.4194, alt 100m, velocity (0.00001 deg/s lat, 0.00002 deg/s lon, 0 alt), speed 20 m/s
    # Note: Velocity in deg/s is approximate for demo
    start1 = (37.7749, -122.4194, 100)
    vel1 = (0.00001, 0.00002, 0)  # Slow movement for demo
    speed1 = 20.0
    flight1 = generate_uav_dataset(*start1, *vel1, speed1)

    # UAV 2: Starts at lat 37.7750, lon -122.4190, alt 120m, velocity (-0.000015, 0.00001, 0), speed 15 m/s
    start2 = (37.7750, -122.4190, 120)
    vel2 = (-0.000015, 0.00001, 0)
    speed2 = 15.0
    flight2 = generate_uav_dataset(*start2, *vel2, speed2)

    # Save to CSV
    flight1.to_csv('data/flight1.csv', index=False)
    flight2.to_csv('data/flight2.csv', index=False)
    print("Datasets saved: data/flight1.csv and data/flight2.csv")

if __name__ == "__main__":
    main()
