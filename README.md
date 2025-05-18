# Cat Detection System (Trained with 329 cats)

This project is a real-time cat detection system using a computer camera. It is developed using the YOLOv5 object detection model.

## Features

- Real-time cat detection
- High-resolution camera support (1280x720)
- Simple and user-friendly interface

## Requirements

- Python 3.7+
- PyTorch
- OpenCV (cv2)
- YOLOv5

## Installation

1. Install required Python packages:
```bash
pip install torch torchvision
pip install opencv-python
```

2. Clone YOLOv5 and install dependencies:
```bash
git clone https://github.com/ultralytics/yolov5
cd yolov5
pip install -r requirements.txt
```

## Usage

1. Run the program:
```bash
python detect_camera.py
```

2. While the program is running:
   - Camera feed will open automatically
   - Detected cats will be displayed on screen
   - Press 'q' to quit

## Notes

- The program uses the computer's built-in camera by default
- To use an external camera, change `cv2.VideoCapture(0)` to `cv2.VideoCapture(1)`
- The model file (`yolov5s.pt`) should be in the project root directory

## License

This project is licensed under the MIT License. 
