import os
import random
import shutil
from pathlib import Path


annotations_folder = "/home/sicily/bird-detector/bird-detect3/annotations"
annotations = os.listdir(annotations_folder)
print("Number of files in the annotation folder:") 
print(len(annotations))


images_folder = "/home/sicily/bird-detector/bird-detect3/images"
images = os.listdir(images_folder)
print("Number of files in the images folder:")
print(len(images))

folder = '/home/sicily/bird-detector/bird-detect3/images'

for filepath in Path(folder).glob('*.JPG'):
    new_name = filepath.with_suffix('.jpg')
    filepath.rename(new_name)

print('Conversion complete!')

train_folder = "/home/sicily/bird-detector/bird-detect3/train"
validation_folder = "/home/sicily/bird-detector/bird-detect3/validation"

# I think there may also be some mismatched images and annotations, if they weren't already deleted before

annotations_folder = "/home/sicily/bird-detector/bird-detect3/annotations"
annotations = os.listdir(annotations_folder)

images_folder = "/home/sicily/bird-detector/bird-detect3/images" 
images = os.listdir(images_folder)

annotation_bases = [os.path.splitext(a)[0] for a in annotations]
image_bases = [os.path.splitext(i)[0] for i in images]

common_bases = set(annotation_bases) & set(image_bases)

removed_annotations = 0
removed_images = 0

for a in annotations:
  if os.path.splitext(a)[0] not in common_bases:
    os.remove(os.path.join(annotations_folder, a))
    removed_annotations += 1
    
for i in images:
  if os.path.splitext(i)[0] not in common_bases:
    os.remove(os.path.join(images_folder, i))
    removed_images += 1

print("Removed annotations:", removed_annotations)
print("Removed images:", removed_images)

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
    image_file = annotation_file.replace(".txt", ".jpg")
    annotation_path = os.path.join(annotations_folder, annotation_file)
    image_path = os.path.join(images_folder, image_file)

    shutil.copy(annotation_path, os.path.join(train_folder, annotation_file))
    shutil.copy(image_path, os.path.join(train_folder, image_file))

for annotation_file in validation_annotations:
    image_file = annotation_file.replace(".txt", ".jpg")
    annotation_path = os.path.join(annotations_folder, annotation_file)
    image_path = os.path.join(images_folder, image_file)

    shutil.copy(annotation_path, os.path.join(validation_folder, annotation_file))
    shutil.copy(image_path, os.path.join(validation_folder, image_file))
