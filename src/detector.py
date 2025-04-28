from ultralytics import YOLO
import torch

class Detector:
    def __init__(self, model_path='models/yolov8n.pt', conf_threshold=0.5):
        self.model = YOLO(model_path)
        # Choose device (GPU if available)
        device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model.to(device)
        self.conf_threshold = conf_threshold

    def detect(self, frame):
        results = self.model(frame)[0]
        detections = []
        for data in results.boxes.data.tolist():
            x1, y1, x2, y2, conf, class_id = data
            if conf < self.conf_threshold:
                continue
            detections.append([x1, y1, x2, y2, conf, class_id])
        return detections
