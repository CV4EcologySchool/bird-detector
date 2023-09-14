import os
import ultralytics
from ultralytics import YOLO
import yaml
from PIL import Image

# Create an Ultralytics YOLOv8 model
model = ultralytics.YOLO('/home/sicily/bird-detector/yolov8s.pt')

# Folder containing images
image_folder = '/home/sicily/bird-detector/bird-detect3/bc_hanging_parrot_test'

# Output folder for saving prediction results
output_folder = 'output_results'


# Load experiment config
cfg = ultralytics.cfg.get_cfg(cfg='default.yaml')

# Create YOLO model and load the trained weights
model = YOLO(cfg.model)
model.load("/home/sicily/bird-detector/yolov8s.pt")  # Replace with the path to your trained weights file

# Specify the folder containing unseen images
image_folder = '/home/sicily/bird-detector/bird-detect3/bc_hanging_parrot_test'

# List all image files in the folder
image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]

# Specify the output folder for saving prediction results
output_folder = 'prediction_results'

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Process each unseen image
for image_file in image_files:
    image_path = os.path.join(image_folder, image_file)

    # Open the unseen image using PIL
    image = Image.open(image_path)

    # Perform object detection on the image
    results_pred = model.predict(source=image, imgsz=320)

    # Save bounding box information for each image individually
    with open(os.path.join(output_folder, f'{os.path.splitext(image_file)[0]}.txt'), 'w') as output_file:
        for det in results_pred.xyxy[0]:
            label = int(det[5])  # Class label
            confidence = det[4]  # Confidence score
            x1, y1, x2, y2 = det[:4]  # Bounding box coordinates
            # Save bounding box information to the output file
            output_file.write(f"{label} {confidence} {x1} {y1} {x2} {y2}\n")

    print(f"Saved prediction results for {image_file}")