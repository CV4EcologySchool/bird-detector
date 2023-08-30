import os
import shutil

# # removing the images that don't have a json file

# main_folder_path = '/home/sicily/bird-detector/bird-detect-copy'

# for folder_name in os.listdir(main_folder_path):
#     folder_path = os.path.join(main_folder_path, folder_name)
#     if os.path.isdir(folder_path):
#         for file_name in os.listdir(folder_path):
#             file_base_name, file_extension = os.path.splitext(file_name)
#             if file_extension.lower() in ['.jpg']:  # Add more image formats if needed
#                 json_file_path = os.path.join(folder_path, file_base_name + '.json')
#                 if not os.path.exists(json_file_path):
#                     image_path = os.path.join(folder_path, file_name)
#                     os.remove(image_path)
#                     print(f"Deleted: {image_path}")

# # rename the jsons and jpgs based on the folder name
# main_folder_path = '/home/sicily/bird-detector/bird-detect-copy/yolo_data'

# for folder_name in os.listdir(main_folder_path):
#     folder_path = os.path.join(main_folder_path, folder_name)
#     if os.path.isdir(folder_path):
#         index = 1
#         for file_name in os.listdir(folder_path):
#             file_path = os.path.join(folder_path, file_name)
#             file_base_name, file_extension = os.path.splitext(file_name)
#             new_file_name = f"{folder_name}{index}{file_extension}"
#             new_file_path = os.path.join(folder_path, new_file_name)
            
#             os.rename(file_path, new_file_path)
#             print(f"Renamed: {file_path} -> {new_file_path}")
            
#             index += 1

# Copying all the jsons and images from each subfolder into a whole new folder with all jsons and jpgs
main_folder_path = '/home/sicily/bird-detector/bird-detect-copy/yolo_data'
output_folder_path = '/home/sicily/bird-detector/bird-detect-copy/melted_data'


for folder_name in os.listdir(main_folder_path):
    folder_path = os.path.join(main_folder_path, folder_name)
    if os.path.isdir(folder_path):
        for file_name in os.listdir(folder_path):
            file_base_name, file_extension = os.path.splitext(file_name)
            if file_extension.lower() in ['.jpg', '.jpeg', '.png', '.gif', '.json']:
                source_path = os.path.join(folder_path, file_name)
                destination_path = os.path.join(output_folder_path, file_name)
                if not os.path.exists(destination_path):
                    shutil.copy2(source_path, destination_path)
                    print(f"Copied: {source_path} -> {destination_path}")
                else:
                    print(f"File already exists: {destination_path}")

# now we have run LabelMe to JSON
import os
import shutil

source_dir = '/home/username/labelme_json_dir/YOLODataset'
destination_dir = '/home/username/combined_dataset'

# Create destination directories if they don't exist
train_destination = os.path.join(destination_dir, 'train')
val_destination = os.path.join(destination_dir, 'val')
os.makedirs(train_destination, exist_ok=True)
os.makedirs(val_destination, exist_ok=True)

# Move training data from the default Labelme2YOLO to the format YOLO requires
train_image_dir = os.path.join(source_dir, 'images', 'train')
train_label_dir = os.path.join(source_dir, 'labels', 'train')
for file_name in os.listdir(train_image_dir):
    image_path = os.path.join(train_image_dir, file_name)
    label_path = os.path.join(train_label_dir, file_name.replace('.jpg', '.json'))

    if os.path.exists(label_path):
        shutil.copy2(image_path, os.path.join(train_destination, file_name))
        shutil.copy2(label_path, os.path.join(train_destination, file_name.replace('.jpg', '.json')))
        print(f"Moved training data: {file_name}")

# Move validation data
val_image_dir = os.path.join(source_dir, 'images', 'val')
val_label_dir = os.path.join(source_dir, 'labels', 'val')
for file_name in os.listdir(val_image_dir):
    image_path = os.path.join(val_image_dir, file_name)
    label_path = os.path.join(val_label_dir, file_name.replace('.jpg', '.json'))

    if os.path.exists(label_path):
        shutil.copy2(image_path, os.path.join(val_destination, file_name))
        shutil.copy2(label_path, os.path.join(val_destination, file_name.replace('.jpg', '.json')))
        print(f"Moved validation data: {file_name}")


