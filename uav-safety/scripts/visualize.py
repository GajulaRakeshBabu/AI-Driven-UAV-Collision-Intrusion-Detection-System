#!/usr/bin/env python3
"""
visualize.py

This script loads UAV flight datasets, checks for intrusion into a restricted area,
visualizes the paths in 2D (latitude vs longitude), marks alerts, and saves alerts to JSON.

Beginner-friendly: Uses shapely for geometry, matplotlib for plotting.

Requirements: pandas, matplotlib, shapely, json
"""

import pandas as pd
import matplotlib.pyplot as plt
from shapely.geometry import Point, Polygon
import json
import os

def check_intrusion(x, y, restricted_area):
    """
    Check if a point is inside the restricted area.

    Args:
        x, y: Coordinates
        restricted_area: Shapely Polygon

    Returns:
        True if inside, else False
    """
    point = Point(x, y)
    return restricted_area.contains(point)

def main():
    # Define restricted area: Rectangle in x,y coordinates
    # Polygon: (x, y) points, e.g., a square from 20-30 x, 10-20 y
    restricted_coords = [
        (20, 10),
        (30, 10),
        (30, 20),
        (20, 20)
    ]
    restricted_area = Polygon(restricted_coords)

    # Load datasets
    flight1 = pd.read_csv('data/flight1.csv')
    flight2 = pd.read_csv('data/flight2.csv')

    # Check intrusions and collect alerts
    alerts = []
    alert_times1 = []
    alert_xs1 = []
    alert_ys1 = []
    alert_times2 = []
    alert_xs2 = []
    alert_ys2 = []

    for _, row in flight1.iterrows():
        if check_intrusion(row['x'], row['y'], restricted_area):
            alerts.append({
                'uav_id': 1,
                'time': row['time'],
                'x': row['x'],
                'y': row['y'],
                'z': row['z']
            })
            alert_times1.append(row['time'])
            alert_xs1.append(row['x'])
            alert_ys1.append(row['y'])

    for _, row in flight2.iterrows():
        if check_intrusion(row['x'], row['y'], restricted_area):
            alerts.append({
                'uav_id': 2,
                'time': row['time'],
                'x': row['x'],
                'y': row['y'],
                'z': row['z']
            })
            alert_times2.append(row['time'])
            alert_xs2.append(row['x'])
            alert_ys2.append(row['y'])

    # Save alerts to JSON
    os.makedirs('data', exist_ok=True)
    with open('data/alerts.json', 'w') as f:
        json.dump(alerts, f, indent=4)
    print(f"Alerts saved to data/alerts.json ({len(alerts)} alerts)")

    # Visualize
    plt.figure(figsize=(10, 8))
    plt.plot(flight1['x'], flight1['y'], label='UAV 1 Path', color='blue')
    plt.scatter(alert_xs1, alert_ys1, color='red', label='UAV 1 Alerts', s=50, marker='x')
    plt.plot(flight2['x'], flight2['y'], label='UAV 2 Path', color='green')
    plt.scatter(alert_xs2, alert_ys2, color='orange', label='UAV 2 Alerts', s=50, marker='x')

    # Plot restricted area
    x, y = restricted_area.exterior.xy
    plt.fill(x, y, alpha=0.3, color='red', label='Restricted Area')

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('UAV Flight Paths with Intrusion Alerts')
    plt.legend()
    plt.grid(True)

    # Save plot
    os.makedirs('runs', exist_ok=True)
    plt.savefig('runs/paths.png')
    print("Visualization saved to runs/paths.png")
    plt.show()

if __name__ == "__main__":
    main()
