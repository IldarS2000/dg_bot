import os

API_TOKEN = os.environ["DG_BOT_TOKEN"]
LOG_FILE_PATH = os.path.join("logs", "log.log")
TAG_MODEL_PATH = os.path.join("training", "models", "resnet50_coco_best_v2.1.0.h5")
DESC_MODEL_PATH = os.path.join("training", "models", "model_9.h5")
TOKENIZER_PATH = os.path.join("training", "train_data", "tokenizer.p")
