#!/usr/bin/env python3
"""
yolo_demo.py

This script uses YOLOv8 pretrained model to detect objects in a sample image/video,
focusing on potential drone detection (e.g., airplanes, birds, or small objects).
Results saved in runs/predict/

Beginner-friendly: Loads model, runs inference, saves results.

Requirements: ultralytics, opencv-python
"""

import os
from ultralytics import YOLO

def main():
    # Load pretrained YOLOv8 model
    model = YOLO('yolov8n.pt')

    # Input file
    video_path = 'data/sample.mp4'
    image_path = 'data/sample.jpg'

    if os.path.exists(video_path):
        source = video_path
    elif os.path.exists(image_path):
        source = image_path
    else:
        print("No sample file found in data/. Add sample.mp4 or sample.jpg")
        return

    # Run inference, save results
    results = model.predict(source=source, save=True, project='runs', name='predict')

    # Print detections (for demo, assume some are drones)
    print("YOLO detections completed. Check runs/predict/")
    for result in results:
        print("Detected objects:", result.boxes.cls)  # Class indices
        # Note: Class 4 is airplane in COCO, could be drone-like

if __name__ == "__main__":
    main()
