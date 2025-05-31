import os
import csv
from ultralytics import YOLO
import cv2

# Folder containing input images
PHOTO_DIR = os.path.join('.', 'test','images')  # Change to your folder path
OUTPUT_IMG_DIR = os.path.join('.', 'photos_out')
os.makedirs(OUTPUT_IMG_DIR, exist_ok=True)

# CSV output file path
CSV_OUTPUT = os.path.join('.', 'detection_results.csv')

# Load your YOLO model
model_path = os.path.join('.', 'runs', 'detect', 'train9', 'weights', 'best.pt')
model = YOLO(model_path)

threshold = 0.5

# Get list of image files (change extensions as needed)
image_files = [f for f in os.listdir(PHOTO_DIR) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp'))]
image_files.sort()

# Prepare CSV header and open file
with open(CSV_OUTPUT, mode='w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    # Write header
    csv_writer.writerow(['image_filename', 'class_name', 'score', 'x1', 'y1', 'x2', 'y2'])

    for img_name in image_files:
        img_path = os.path.join(PHOTO_DIR, img_name)
        img = cv2.imread(img_path)
        if img is None:
            print(f"Warning: Could not read image {img_path}, skipping.")
            continue

        results = model(img)[0]

        # Draw detections on image and write to CSV
        for box in results.boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = box
            if score > threshold:
                class_name = results.names[int(class_id)].upper()
                # Write detection row
                csv_writer.writerow([img_name, class_name, score, int(x1), int(y1), int(x2), int(y2)])

                # Draw box and label on image
                cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                cv2.putText(img, f'{class_name} {score:.2f}', (int(x1), int(y1) - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2, cv2.LINE_AA)

        # Save the annotated image to output folder
        output_img_path = os.path.join(OUTPUT_IMG_DIR, img_name)
        cv2.imwrite(output_img_path, img)

print(f"Detection completed on {len(image_files)} images. Results saved in {CSV_OUTPUT}")
