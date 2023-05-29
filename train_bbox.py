from multiprocessing import freeze_support

import torch
from ultralytics import YOLO
import ultralytics
ultralytics.checks()
print(torch.cuda.is_available())
# Load the model.

def yolo_train():
    freeze_support()
    model = YOLO('yolov8n.pt')
    # Training.
    results = model.train(
        data='C:\\dog-skin-disease\\data\\custom.yaml',
        epochs=20,
        batch=10,
        name='yolov8n_custom',
        imgsz=(1920, 1080),
        device=0)

def yolo_predict():
    from ultralytics import YOLO

    # Load our custom goat model
    model = YOLO("runs/detect/yolov8n_custom3/weights/last.pt")

    # Use the model to detect object - goat
    model.predict(source="1.jpg", save=True, show=True)


if __name__ == '__main__':
    yolo_train()