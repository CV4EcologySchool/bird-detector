import os
import random
import shutil

annotations_folder = "/home/sicily/bird-detector/bird-detect3/annotations"
images_folder = "/home/sicily/bird-detector/bird-detect3/images"
train_folder = "/home/sicily/bird-detector/bird-detect3/train"
validation_folder = "/home/sicily/bird-detector/bird-detect3/validation"


for filename in os.listdir(images_folder):
    if os.path.splitext(filename)[1] == '.jpg' and not os.path.isfile(os.path.join(images_folder, filename)):
        print(f"Problem file: {os.path.join(images_folder, filename)}")
        
        new_name = os.path.splitext(filename)[0] + "_renamed.jpg"
        new_path = os.path.join(images_folder, new_name)
        
        print(f"Renaming to: {new_path}")
        os.rename(os.path.join(images_folder, filename), new_path)

# List the files in the annotations folder
annotation_files = os.listdir(annotations_folder)

# Set a seed for reproducibility
random.seed(42)

# Shuffle the annotation list
random.shuffle(annotation_files)

# Calculate the split index based on 80/20 ratio
split_index = int(0.8 * len(annotation_files))

# Get the lists of files for train and validation
train_annotations = annotation_files[:split_index]
validation_annotations = annotation_files[split_index:]

# Move annotations and corresponding images to train and validation folders
for annotation_file in train_annotations:
    image_file = annotation_file.replace(".json", ".jpg")
    annotation_path = os.path.join(annotations_folder, annotation_file)
    image_path = os.path.join(images_folder, image_file)

    shutil.copy(annotation_path, os.path.join(train_folder, annotation_file))
    shutil.copy(image_path, os.path.join(train_folder, image_file))

for annotation_file in validation_annotations:
    image_file = annotation_file.replace(".json", ".jpg")
    annotation_path = os.path.join(annotations_folder, annotation_file)
    image_path = os.path.join(images_folder, image_file)

    shutil.copy(annotation_path, os.path.join(validation_folder, annotation_file))
    shutil.copy(image_path, os.path.join(validation_folder, image_file))
