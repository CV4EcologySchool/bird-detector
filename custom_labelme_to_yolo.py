import os
import json
import glob
import shutil

# Path to the directory containing the LabelMe JSON annotation files and images
labelme_dir = "/home/sicily/bird-detector/bird-detect3/melted_data"

# Path to the directory where you want to save the YOLO annotations
yolo_dir = "/home/sicily/bird-detector/bird-detect3/annotations"

# Create a new folder for YOLO images / Define the path to the directory where you want to save the YOLO images
yolo_images_dir = "/home/sicily/bird-detector/bird-detect3/images"

# Iterate through each JSON file in the LabelMe directory
json_files = glob.glob(os.path.join(labelme_dir, "*.json"))

# Extract all unique class labels from JSON files
all_class_labels = set()
for json_file in json_files:
    with open(json_file, "r") as f:
        data = json.load(f)
        
        for shape in data["shapes"]:
            label = shape["label"]
            all_class_labels.add(label)

# Mapping all unique labels to class ID 0 (bird)
class_mapping = {label: 0 for label in all_class_labels}

# Function to preprocess label names
def preprocess_label(label):
    return label.lower().replace(" ", "_")  # Convert to lowercase and replace spaces with underscores

# Convert annotations to YOLO format
for json_file in json_files:
    with open(json_file, "r") as f:
        data = json.load(f)
    
    image_name = os.path.basename(data["imagePath"])
    image_width = data["imageWidth"]
    image_height = data["imageHeight
