import os
import ultralytics
from ultralytics import YOLO
import yaml
from PIL import Image

# Create an Ultralytics YOLOv8 model
model = ultralytics.YOLO('/home/sicily/bird-detector/runs/detect/train7/weights/best.pt')

# Specify the folder containing unseen images
image_folder = '/home/sicily/bird-detector/bird-detect3/bc_hanging_parrot_test'

# List all image files in the folder
image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]

# Specify the output folder for saving prediction results
output_folder = 'prediction_results'

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Process images in batches
batch_size = 8  # Adjust this based on your available memory
for i in range(0, len(image_files), batch_size):
    batch_files = image_files[i:i + batch_size]
    batch_images = [Image.open(os.path.join(image_folder, f)) for f in batch_files]

    # Perform object detection on the batch of images
    results_batch = model(batch_images)

    # Save bounding box information for each image in YOLO format
    for j, image_file in enumerate(batch_files):
        results_batch[j].save_txt(os.path.join(output_folder, f'{os.path.splitext(image_file)[0]}.txt'))

    print(f"Saved prediction results for batch {i + 1}-{i + len(batch_files)}")
