from multiprocessing import freeze_support

import torch
from ultralytics import YOLO
import ultralytics
import gc
gc.collect()
torch.cuda.empty_cache()
ultralytics.checks()
print(torch.cuda.is_available())
# Load the model.

def yolo_train():
    freeze_support()
    model = YOLO('yolov8n.pt')
    # Training.
    results = model.train(
        data='C:\\dog-skin-disease\\data\\custom.yaml',
        epochs=300,
        optimizer='Adam',
        lr0=1E-3,
        name='yolov8n_custom',
        imgsz=(600, 337.5),
        device=0)
    results = model.val()  # evaluate model performance on the validation set
    print(results)
    # model = YOLO('yolov8n.yaml')  # build a new model from YAML
    # model = YOLO('yolov8n.pt')  # load a pretrained model (recommended for training)
    # model = YOLO('yolov8n.yaml').load('yolov8n.pt')  # build from YAML and transfer weights
    #
    # # Train the model
    # model.train(data='coco128.yaml', epochs=100, imgsz=640, device=0)

def yolo_predict():
    from ultralytics import YOLO

    # Load our custom goat model
    model = YOLO("runs/detect/yolov8n_custom20/weights/last.pt")

    # Use the model to detect object - goat
    model.predict(source="1.jpg", save=True, show=True)


if __name__ == '__main__':
    yolo_predict()