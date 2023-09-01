import os
import ultralytics
import matplotlib.pyplot as plt

# Create an Ultralytics YOLOv8 model
model = ultralytics.YOLO('yolov8n-seg.pt')

# Folder containing images
image_folder = 'path/to/your/image/folder'

# Output folder for saving prediction results
output_folder = 'output_results'

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# List all image files in the folder
image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]

# Lists to store metrics
mAP_values = []

# Loop through images and perform object detection
for image_file in image_files:
    image_path = os.path.join(image_folder, image_file)

    # Perform object detection on the image
    results = model.predict(source=image_path, imgsz=320)

    # Save prediction results to the output folder
    output_path = os.path.join(output_folder, f'{os.path.splitext(image_file)[0]}.txt')
    results.save(output_path)

    # Append mAP value to the list
    mAP = results.metrics[0]['AP']['all']
    mAP_values.append(mAP)

    print(f"Saved prediction results for {image_file} to {output_path}")

# Plotting
plt.figure(figsize=(10, 6))
plt.bar(image_files, mAP_values, color='blue')
plt.xlabel('Image')
plt.ylabel('mAP')
plt.title('mAP Scores for Object Detection')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()