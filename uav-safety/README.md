# AI-Driven UAV Collision & Intrusion Detection System

This is a solo project for a Hackathon, focusing on AI-driven safety for UAVs (Unmanned Aerial Vehicles).

## Week-1 Goals
- Set up Python environment
- Create basic project folder structure
- Run YOLOv8 object detection on a sample image/video
- Generate synthetic UAV flight paths (CSV + plots)
- Implement a simple collision prediction algorithm

## Week-2 Goals
- Prepare fake UAV flight dataset (latitude, longitude, altitude, speed)
- Visualize UAV paths in 2D (matplotlib)
- Use YOLOv8 for detecting drones in images/video
- Simulate UAV intrusion detection (alert if enters restricted area, save to JSON)
- Visualization of UAV paths with alerts shown

## Folder Structure
```
uav-safety/
├── data/
│   ├── sample.mp4  # Dummy video for YOLO testing (provide your own)
│   ├── flight1.csv # Generated UAV flight path 1
│   ├── flight2.csv # Generated UAV flight path 2
├── scripts/
│   ├── run_yolo_demo.py
│   ├── generate_flights.py
│   ├── check_collision.py
├── runs/
│   ├── predict/     # YOLO results
│   ├── flight_paths.png # Flight path plot
├── requirements.txt
├── README.md
```

## Setup
1. Ensure Python 3.10+ is installed.
2. Install dependencies: `pip install -r requirements.txt`
3. Place a sample video or image in `data/sample.mp4` or `data/sample.jpg` for YOLO testing.

## Running Scripts

1. **Install dependencies**: `pip install -r requirements.txt`

2. **Run YOLO demo**:
   - Place a sample video in `data/sample.mp4` or image in `data/sample.jpg`.
   - Run: `python scripts/run_yolo_demo.py`
   - Results saved in `runs/predict/`.

3. **Generate flight paths**:
   - Run: `python scripts/generate_flights.py`
   - CSVs saved in `data/`, plot in `runs/flight_paths.png`.

4. **Check collision**:
   - Run: `python scripts/check_collision.py`
   - Prints closest approach time and minimum distance.

## Week-2 Scripts

5. **Generate Week-2 dataset**:
   - Run: `python scripts/dataset.py`
   - CSVs saved in `data/flight1.csv` and `data/flight2.csv`.

6. **Visualize paths and check intrusion**:
   - Run: `python scripts/visualize.py`
   - Checks for intrusions, saves alerts to `data/alerts.json`, plot to `runs/paths.png`.

7. **YOLO drone detection demo**:
   - Run: `python scripts/yolo_demo.py`
   - Results in `runs/predict/`.
