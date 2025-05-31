import os
import cv2
from ultralytics import YOLO

def detect_objects_in_image(image_path, model_path, threshold=0.1):
    UPLOAD_IMG_DIR = os.path.join('.', 'static','uploads',image_path)
    OUTPUT_IMG_DIR = os.path.join('.', 'static','prediction_out')
    img = cv2.imread(UPLOAD_IMG_DIR)
    if img is None:
        raise ValueError(f"Could not read image: {image_path}")

    # Load model
    model = YOLO(model_path)

    # Run detection
    results = model(img)[0]
    detections = []
    if len(results) == 0:
        return image_path, None, 0; 
    for box in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = box
        if score >= threshold:
            class_name = results.names[int(class_id)].upper()
            #class_name = 'DAMAGE'
            detections.append((class_name, score, int(x1), int(y1), int(x2), int(y2)))

            # Draw on image
            cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
            cv2.putText(img, f'{class_name} {score:.2f}', (int(x1), int(y1) - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
            output_img_path = os.path.join(OUTPUT_IMG_DIR, image_path)
            cv2.imwrite(output_img_path, img)
        scores = [det[1] for det in detections]

        if scores:
            highest_score = max(scores)
        else:
            highest_score = 0  # or None

    return image_path, detections, f"{highest_score * 100:.2f}%"


#image_path = './damaged.jpg'

#output_img, results = detect_objects_in_image(image_path=image_path, model_path= os.path.abspath(os.path.join('classifier','runs', 'detect', 'train9', 'weights', 'best.pt')))

# print("Detections:")
#for det in results:
#     print(det)
#print(output_img)