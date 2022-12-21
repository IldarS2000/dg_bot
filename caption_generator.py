from imageai.Detection import ObjectDetection
from config import CAP_MODEL_PATH

detector = None


class ObjectDetector:
    def __init__(self):
        self.detector = ObjectDetection()
        self.detector.setModelTypeAsRetinaNet()
        self.detector.setModelPath(CAP_MODEL_PATH)
        self.detector.loadModel()

    def detect_objects(self, image_path):
        image_copy, detections = self.detector.detectObjectsFromImage(input_image=image_path, output_type="array")
        object_names = [detection["name"] for detection in detections]
        return set(object_names)


DETECTOR = ObjectDetector()
