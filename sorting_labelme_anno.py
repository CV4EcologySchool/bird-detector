import os
import shutil
import json

# # Removing the images that don't have a corresponding JSON file - it didn't delete them all before
# # You can adjust the script to handle uppercase extensions as well by converting the file extension to lowercase before checking
# main_folder_path = '/home/sicily/bird-detector/bird-detect3/yolo_data'

# for folder_name in os.listdir(main_folder_path):
#     folder_path = os.path.join(main_folder_path, folder_name)
#     if os.path.isdir(folder_path):
#         for file_name in os.listdir(folder_path):
#             file_base_name, file_extension = os.path.splitext(file_name)
#             if file_extension.lower() in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp']:
#                 json_file_path = os.path.join(folder_path, file_base_name + '.json')
#                 if not os.path.exists(json_file_path):
#                     image_path = os.path.join(folder_path, file_name)
#                     os.remove(image_path)
#                     print(f"Deleted: {image_path}")

# rename the jsons and the images
main_folder_path = '/home/sicily/bird-detector/bird-detect3/yolo_data'
new_base_folder_path  = '/home/sicily/bird-detector/bird-detect3/yolo_copy_try'

for folder_name in os.listdir(main_folder_path):
    folder_path = os.path.join(main_folder_path, folder_name)
    new_folder_path = os.path.join (new_base_folder_path, folder_name)

    os.mkdir (new_folder_path)

    if os.path.isdir(folder_path):
        image_index = 1
        json_index = 1
        
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            file_base_name, file_extension = os.path.splitext(file_name)

            new_image_name = ''

            # Check if the file is an image or JSON
            if file_extension.lower() == '.jpg' or file_extension.lower() == '.jpeg':
                new_image_name = f"{folder_name}{image_index}{file_extension}"
                new_image_path = os.path.join(new_folder_path, new_image_name)
                
                shutil.copyfile(file_path, new_image_path)
                print(f"Renamed image: {file_path} -> {new_image_path}")

                # takes the first part of the string
                json_path = file_path.split('.')[0]+ '.json'

            # elif file_extension.lower() == '.json':

                new_file_name = f"{folder_name}{image_index}.json"
                new_json_path = os.path.join(new_folder_path, new_file_name)
                print (new_json_path)
                # load the json in and define the new file path
                # Load COCO annotations from a JSON file, will open and close the file separately
                with open(json_path) as json_file:
                    new_json = json.load(json_file)
                # rename the image path in the json to the new file name as well so they match
                new_json["imagePath"] = new_image_name
                del new_json['imageData']

                # dump and save the new json
                with open(new_json_path, 'w') as new_json_file:
                    json.dump (new_json, new_json_file)
                # os.rename(file_path, new_file_path)
                print(f"Renamed JSON: {json_path} -> {new_json_path}")

                image_index += 1

# # # # Copying all the jsons and images from each subfolder into a whole new folder with all jsons and jpgs
# # main_folder_path = '/home/sicily/bird-detector/bird-detect3/yolo_data'
# # output_folder_path = '/home/sicily/bird-detector/bird-detect3/melted_data'

# # for folder_name in os.listdir(main_folder_path):
# #     folder_path = os.path.join(main_folder_path, folder_name)
# #     if os.path.isdir(folder_path):
# #         for file_name in os.listdir(folder_path):
# #             file_base_name, file_extension = os.path.splitext(file_name)
# #             if file_extension.lower() in ['.jpg', '.jpeg', '.png', '.gif', '.json']:
# #                 source_path = os.path.join(folder_path, file_name)
# #                 destination_path = os.path.join(output_folder_path, file_name)
# #                 if not os.path.exists(destination_path):
# #                     shutil.copy2(source_path, destination_path)
# #                     print(f"Copied: {source_path} -> {destination_path}")
# #                 else:
# #                     print(f"File already exists: {destination_path}")
