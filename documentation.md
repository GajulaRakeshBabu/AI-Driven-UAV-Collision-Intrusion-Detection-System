# 🚁 AI-Driven UAV Collision & Intrusion Detection System - Documentation

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Architecture](#architecture)
4. [Installation](#installation)
5. [Usage](#usage)
6. [API Reference](#api-reference)
7. [Configuration](#configuration)
8. [Testing](#testing)
9. [Troubleshooting](#troubleshooting)
10. [Contributing](#contributing)
11. [License](#license)
12. [Acknowledgments](#acknowledgments)
13. [Contact](#contact)
14. [FAQ](#faq)

## Overview
The AI-Driven UAV Collision & Intrusion Detection System is an innovative solution developed for enhancing UAV safety through AI-powered detection and monitoring. It integrates YOLOv8 for object detection with collision prediction algorithms to provide real-time alerts and flight path analysis.

### Purpose
- Prevent UAV collisions in shared airspace
- Detect intrusions in restricted areas
- Provide real-time monitoring through a web dashboard
- Generate synthetic flight data for testing and simulation

### Technologies Used
- **AI/ML**: YOLOv8 for object detection
- **Backend**: Python with libraries like OpenCV, Pandas, NumPy
- **Frontend**: Streamlit for the dashboard
- **Visualization**: Matplotlib for plots
- **Data Handling**: JSONL for logging, CSV for flight data

## Features
- AI-powered drone detection in videos and images
- Synthetic flight path generation with realistic parameters
- Collision prediction with minimum distance calculations
- Intrusion detection with alert logging
- 2D flight path visualization
- Real-time Streamlit dashboard
- Comprehensive logging in JSONL format

## Architecture
The system consists of several modules:
- **Detection Module**: Uses YOLOv8 for identifying UAVs in media
- **Simulation Module**: Generates synthetic flight paths
- **Analysis Module**: Predicts collisions and detects intrusions
- **Visualization Module**: Creates plots and charts
- **Dashboard Module**: Streamlit app for real-time monitoring

### Data Flow
1. Flight data generation or input
2. Collision analysis and intrusion checking
3. Logging of events
4. Visualization and dashboard display

## Installation

### Prerequisites
- Python 3.10 or higher
- Git
- pip

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/GajulaRakeshBabu/AI-Driven-UAV-Collision-Intrusion-Detection-System.git
   cd AI-Driven-UAV-Collision-Intrusion-Detection-System/uav-safety
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Download YOLOv8 model (if not included):
   - The yolov8n.pt file should be in the root directory

### Dependencies
Key libraries:
- ultralytics (YOLOv8)
- streamlit
- pandas
- numpy
- matplotlib
- opencv-python
- flask (if used)

## Usage

### Running Individual Components

#### YOLO Object Detection Demo
```bash
python scripts/run_yolo_demo.py
```
- Processes sample.mp4 or sample.jpg
- Outputs results to runs/predict/

#### Generate Flight Paths
```bash
python scripts/generate_flights.py
```
- Creates flight1.csv, flight2.csv in data/
- Generates plots in runs/

#### Collision Analysis
```bash
python scripts/check_collision.py
```
- Analyzes flight paths for collision risks
- Logs results to logs/collision.jsonl

#### Intrusion Detection
```bash
python scripts/visualize.py
```
- Checks for intrusions and visualizes paths
- Saves alerts to data/alerts.json

#### Dataset Generation
```bash
python scripts/dataset.py
```
- Generates advanced flight datasets

### Launching the Dashboard
```bash
streamlit run streamlit_app.py
```
- Access at http://localhost:8501
- Auto-refreshes every 5 seconds

### Example Workflow
1. Generate flight data
2. Run collision check
3. Run visualization for intrusions
4. Launch dashboard for monitoring

## API Reference
The system primarily consists of scripts rather than a formal API. However, key functions include:

### From scripts/check_collision.py
- `calculate_min_distance()`: Computes minimum distance between flight paths
- `predict_collision()`: Predicts collision risk

### From scripts/visualize.py
- `plot_flight_paths()`: Creates 2D plots of flight paths
- `check_intrusion()`: Detects intrusions in restricted areas

### Streamlit App Functions
- `read_jsonl()`: Reads log files into DataFrames
- Auto-refresh loop for real-time updates

## Configuration
- **Log Files**: Located in logs/ (collision.jsonl, intrusion.jsonl)
- **Data Files**: In data/ (flight CSVs, alerts.json)
- **Model**: yolov8n.pt in root
- **Output**: runs/ for predictions and plots

Modify paths in scripts if needed. Dashboard reads from logs/ directory.

## Testing
Run tests with:
```bash
python -m pytest tests/
```
(Note: Test directory may need to be created if not present)

### Manual Testing
- Verify YOLO detection on sample media
- Check flight path generation and plots
- Test collision prediction with sample data
- Ensure dashboard loads and refreshes correctly

## Troubleshooting

### Common Issues
1. **Import Errors**: Ensure all dependencies are installed
2. **Model Not Found**: Verify yolov8n.pt is in the correct location
3. **No Log Data**: Run analysis scripts before launching dashboard
4. **Streamlit Not Starting**: Check port 8501 availability

### Performance Tips
- Use GPU for YOLO inference if available
- Reduce video resolution for faster processing
- Clear logs periodically to manage file size

### Error Messages
- "No log data available": Run data generation and analysis scripts first
- "Module not found": Install missing packages with pip

## Contributing
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/new-feature`
3. Make changes and test thoroughly
4. Commit: `git commit -m 'Add new feature'`
5. Push: `git push origin feature/new-feature`
6. Open a Pull Request

### Guidelines
- Follow PEP 8 style guide
- Add docstrings to functions
- Update documentation for new features
- Test changes before submitting

## License
This project is licensed under the MIT License. See LICENSE file for details.

## Acknowledgments
- Ultralytics for YOLOv8
- Open-source community for libraries
- Hackathon organizers
- Pexels for images

## Contact
- Author: Gajula Rakesh Babu
- Email: grakesh2605@gmail.com
- GitHub: https://github.com/GajulaRakeshBabu

## FAQ
**Q: Can this run on CPU?**
A: Yes, but GPU is recommended for better performance.

**Q: How to add custom flight data?**
A: Place CSV files in data/ with columns: latitude, longitude, altitude, speed, time.

**Q: Is real-time detection supported?**
A: The dashboard updates every 5 seconds; for true real-time, modify the refresh interval.

**Q: Can I deploy this on the cloud?**
A: Yes, use platforms like Streamlit Cloud or Heroku for the dashboard.
