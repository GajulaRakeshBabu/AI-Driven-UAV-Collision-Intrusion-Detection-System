#!/usr/bin/env python3
"""
run_yolo_demo.py

This script loads a pretrained YOLOv8 model and runs object detection
on a sample video or image located in the data/ folder.
Results are saved in runs/predict/

Requirements: ultralytics, opencv-python
"""

import os
from ultralytics import YOLO


def main():
    # Load pretrained YOLOv8 model (nano version for speed)
    model = YOLO('yolov8n.pt')  # Downloads if not present

    # Define input file paths
    video_path = 'data/sample.mp4'
    image_path = 'data/sample.jpg'

    # Check which file exists
    if os.path.exists(video_path):
        source = video_path
        print("Running YOLO on video:", source)
    elif os.path.exists(image_path):
        source = image_path
        print("Running YOLO on image:", source)
    else:
        print("Error: Neither data/sample.mp4 nor data/sample.jpg found.")
        print("Please add a sample file.")
        return

    # Run inference and save results
    # save=True saves annotated images/videos
    # project='runs' saves in runs/ folder
    # name='predict' creates runs/predict/ subfolder
    _ = model.predict(source=source, save=True, project='runs', name='predict')

    print("YOLO inference completed. Results saved in runs/predict/")

    # Attempt to open the output video automatically (Windows only)
    try:
        # Check if nested 'predict' folder exists, else use 'runs/predict'
        nested_dir = os.path.join('runs', 'predict', 'predict')
        if os.path.exists(nested_dir):
            output_dir = nested_dir
        else:
            output_dir = os.path.join('runs', 'predict')

        # Find the first .avi file in the output directory
        for file in os.listdir(output_dir):
            if file.endswith('.avi'):
                output_video_path = os.path.join(output_dir, file)
                print(f"Opening output video: {output_video_path}")
                os.startfile(output_video_path)  # Windows only
                break
    except Exception as e:
        print(f"Could not open output video automatically: {e}")


if __name__ == "__main__":
    main()
