import logging
from multiprocessing import freeze_support

import torch
from ultralytics import YOLO
import ultralytics
import gc

gc.collect()
torch.cuda.empty_cache()
ultralytics.checks()
"""
logging 설정
"""
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.StreamHandler().setFormatter(formatter)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler('./detect.log'))


# Load the model.
def yolo_train():
    freeze_support()
    model = YOLO('yolov8n.pt')
    # Training.
    model.train(
        data='C:\\dog-skin-disease\\data\\custom.yaml',
        epochs=100,
        optimizer='Adam',
        lr0=1E-3,
        name='yolov8n_custom',
        imgsz=(600, 337.5),
        device=0
    )

    results = model.val()  # evaluate model performance on the validation set
    logger.info(results)


def yolo_predict():
    # Load our custom goat model
    model = YOLO("runs/detect/yolov8n_custom20/weights/best.pt")

    # Use the model to detect object - goat
    model.predict(source="2.jpg", save=True, show=True, conf=0.05)


def yolo_validation():
    model = YOLO("runs/detect/yolov8n_custom20/weights/best.pt")
    val = model.val()
    result = model('2.jpg')
    logger.info(val)
    logger.info(val.box)


if __name__ == '__main__':
    yolo_train()
