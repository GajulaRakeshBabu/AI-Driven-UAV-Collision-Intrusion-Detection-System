# 🚁 AI-Driven UAV Collision & Intrusion Detection System

<img width="1919" height="1077" alt="Screenshot 2025-10-05 231307" src="https://github.com/user-attachments/assets/34c5d214-7305-4a82-b0fc-03231330528f" />

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)](https://streamlit.io/)

## 📋 Description

Welcome to the **AI-Driven UAV Collision & Intrusion Detection System**! This innovative project, developed for a Hackathon, leverages cutting-edge AI technologies to enhance safety in UAV (Unmanned Aerial Vehicle) operations. By integrating YOLOv8 object detection with advanced collision prediction algorithms, this system provides real-time monitoring, intrusion alerts, and comprehensive flight path analysis to prevent accidents and ensure secure airspace management.

Whether you're a drone enthusiast, aviation professional, or developer interested in AI applications, this project offers a robust framework for UAV safety solutions.

## ✨ Key Features

- **🕵️ AI-Powered Detection**: Utilizes YOLOv8 for accurate drone detection in videos and images.
- **📊 Flight Path Simulation**: Generates synthetic UAV flight paths with realistic data (latitude, longitude, altitude, speed).
- **⚠️ Collision Prediction**: Implements algorithms to predict potential collisions and calculate minimum distances.
- **🚨 Intrusion Alerts**: Monitors restricted areas and triggers alerts for unauthorized intrusions, logging to JSON files.
- **📈 2D Visualization**: Interactive plots for flight paths, alerts, and detection results using Matplotlib.
- **🌐 Streamlit Dashboard**: User-friendly web interface for real-time monitoring and data visualization.
- **📝 Comprehensive Logging**: Detailed logs for collision and intrusion events in JSONL format.

## 🛠️ Installation

### Prerequisites
- Python 3.10 or higher
- Git

### Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/GajulaRakeshBabu/AI-Driven-UAV-Collision-Intrusion-Detection-System.git
   cd AI-Driven-UAV-Collision-Intrusion-Detection-System/uav-safety
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare Data**:
   - Place sample videos/images in `data/` (e.g., `sample.mp4` or `sample.jpg` for YOLO testing).

## 🚀 Usage

### Running Individual Scripts

1. **YOLO Object Detection Demo**:
   ```bash
   python scripts/run_yolo_demo.py
   ```
   - Detects objects in sample video/image.
   - Results saved in `runs/predict/`.

2. **Generate Synthetic Flight Paths**:
   ```bash
   python scripts/generate_flights.py
   ```
   - Creates CSV files in `data/` and plots in `runs/`.

3. **Collision Check**:
   ```bash
   python scripts/check_collision.py
   ```
   - Analyzes flight paths for collision risks.

4. **Dataset Generation (Week-2)**:
   ```bash
   python scripts/dataset.py
   ```
   - Generates advanced flight datasets.

5. **Visualization & Intrusion Detection**:
   ```bash
   python scripts/visualize.py
   ```
   - Visualizes paths, checks intrusions, saves alerts.

6. **YOLO Drone Detection**:
   ```bash
   python scripts/yolo_demo.py
   ```
   - Specialized drone detection demo.

### Launch Streamlit Dashboard
```bash
streamlit run streamlit_app.py
```
Access the dashboard at `http://localhost:8501` for interactive monitoring.

## 📸 Screenshots
### Flight Path Visualization
<img width="1919" height="1199" alt="Screenshot 2025-10-05 223543" src="https://github.com/user-attachments/assets/8ed09f92-cada-4af6-ab3c-b88f741769e7" />

### UAV Paths with Alerts
<img width="1919" height="1199" alt="Screenshot 2025-10-05 223708" src="https://github.com/user-attachments/assets/57eb5bbe-078e-4574-b65b-18026e9cd606" />

### Streamlit Dashboard
<img width="1862" height="1199" alt="Screenshot 2025-10-05 224145" src="https://github.com/user-attachments/assets/f39594de-97fd-4ea4-9af3-d62a5abc085e" />
<img width="1854" height="1199" alt="Screenshot 2025-10-05 224205" src="https://github.com/user-attachments/assets/7cb1e25f-9fef-42cb-bbf0-1089fd9a4a35" />

## 📁 Project Structure

```
uav-safety/
├── data/
│   ├── alerts.json          # Intrusion alerts
│   ├── flight1.csv          # Synthetic flight data
│   ├── flight2.csv
│   └── sample.mp4           # Test video
├── scripts/
│   ├── check_collision.py   # Collision prediction
│   ├── dataset.py           # Data generation
│   ├── generate_flights.py  # Flight path creation
│   ├── run_yolo_demo.py     # YOLO demo
│   ├── visualize.py         # Path visualization
│   └── yolo_demo.py         # Drone detection
├── runs/
│   ├── flight_paths.png     # Flight plots
│   ├── paths.png            # Alert plots
│   └── predict/             # YOLO results
├── logs/
│   ├── collision.jsonl      # Collision logs
│   └── intrusion.jsonl      # Intrusion logs
├── requirements.txt         # Dependencies
├── streamlit_app.py         # Dashboard app
└── README.md                # This file
```

## 🧪 Testing

Run tests to ensure everything works:
```bash
python -m pytest tests/
```

## 🤝 Contributing

We welcome contributions! Here's how you can help:
1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/amazing-feature`.
3. Commit changes: `git commit -m 'Add amazing feature'`.
4. Push to branch: `git push origin feature/amazing-feature`.
5. Open a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

We would like to express our sincere gratitude to the following individuals, organizations, and communities for their invaluable contributions to this project:

- **Ultralytics**: For developing and maintaining YOLOv8, the powerful object detection model that serves as the foundation for our AI-driven detection system.
- **The Open-Source Community**: For providing essential libraries and frameworks, including Streamlit for the dashboard, Pandas and NumPy for data manipulation, Matplotlib for visualization, OpenCV for computer vision, and Flask for web integration.
- **Pexels**: For supplying the high-quality images used in our project documentation and promotional materials.
- **Hackathon Organizers and Sponsors**: For creating the platform and resources that enabled the development of innovative solutions for UAV safety and airspace management.

We are also grateful to our mentors, peers, and the broader aviation and AI communities for their inspiration, feedback, and ongoing support in advancing the field of unmanned aerial vehicle safety.

## 📞 Contact

For questions or collaborations:
- **Author**: Gajula Rakesh Babu
- **Email**: grakesh2605@gmail.com
- **GitHub**: [https://github.com/GajulaRakeshBabu](https://github.com/GajulaRakeshBabu)

---

⭐ If you find this project helpful, please give it a star!
