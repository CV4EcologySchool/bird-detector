import os
import json
import glob
import shutil

# # Path to the directory containing the LabelMe JSON annotation files and images
labelme_dir = "/home/sicily/bird-detector/bird-detect-copy2/melted_data"

# # Path to the directory where you want to save the YOLO annotations
yolo_dir = "/home/sicily/bird-detector/yolo/annotations"

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
    image_height = data["imageHeight"]
    
    yolo_annotation = []
    
    for shape in data["shapes"]:
        label = preprocess_label(shape["label"])
        if label in class_mapping:
            class_id = class_mapping[label]
        else:
            # If label is not in class_mapping, skip this annotation
            continue
        
        x_points = [point[0] for point in shape["points"]]
        y_points = [point[1] for point in shape["points"]]
        
        x_min = min(x_points) / image_width
        x_max = max(x_points) / image_width
        y_min = min(y_points) / image_height
        y_max = max(y_points) / image_height
        
        width = x_max - x_min
        height = y_max - y_min
        
        x_center = x_min + width / 2
        y_center = y_min + height / 2
        
        yolo_annotation.append(f"{class_id} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}")
    
    yolo_annotation_text = "\n".join(yolo_annotation)
    
    yolo_annotation_path = os.path.join(yolo_dir, os.path.splitext(image_name)[0] + ".txt")
    
    with open(yolo_annotation_path, "w") as f:
        f.write(yolo_annotation_text)

print("Conversion complete.")

# # Create a new folder for YOLO images
# # Define the path to the directory where you want to save the YOLO images
yolo_images_dir = "/home/sicily/bird-detector/yolo/images"  # Define this variable

# # Find all image files in the labelme_dir
image_files = glob.glob(os.path.join(labelme_dir, "*.jpg"))  # Update the extension if needed

# Copy image files to the new YOLO images folder
for image_file in image_files:
    image_name = os.path.basename(image_file)
    dest_image_path = os.path.join(yolo_images_dir, image_name)
    shutil.copy(image_file, dest_image_path)

# Count the number of files in the annotations and images directories
num_annotations = len(os.listdir(yolo_dir))
num_images = len(os.listdir(yolo_images_dir))

print(f"Number of annotations: {num_annotations}")
print(f"Number of images: {num_images}")
