# Vehicle Damage Detection and Cost Estimation System

This web-based application allows users to upload a photo of a damaged vehicle, automatically detects any visible damage using a trained YOLO model, and estimates the repair cost based on the detected damage.

## Features

- Upload vehicle damage photos
- Detect visible damage using a YOLOv8 model
- Highlight damaged areas with bounding boxes
- Display highest confidence score
- Show part cost, labor cost, and total repair estimate
- Download analysis results as a PDF

## Project Structure
root
- app.py (flask server backend)
- predict.py (prediction function with trained YOLOv8)
- classfier (YOLOv8)
  -  data.yaml (dataset configuration)
  -  train/ (dataset for training)
  -  valid/ (dataset for validation)
  -  test/ (dataset for test)
  -  train.py (script to train YOLOv8 with train dataset)
  -  test.py (test script, output written into test_results/)
- static
  -  templates
    -  index.html
  -  css
    -  style.css
  -  prediction_out (store annotated output image from YOLOv8)

## Running the app
`python app.py`
Visit http://127.0.0.1:5000 in your browser.

## Instructions
1. Select vehicle angles
![image](https://github.com/user-attachments/assets/9dbca0c7-0c42-4ee6-ac98-dddd4258a019)

2. Upload a clear image of the car part (accepted file extensions: 'png', 'jpg, 'jpeg')
![image](https://github.com/user-attachments/assets/b871f26d-01c1-4d32-962b-b2ac31780cdc)

3. Preview the image selected and click on the button to analyze damage and estimate cost
![image](https://github.com/user-attachments/assets/7b7bb3b0-9ad3-4d50-bfb5-83e793c71366)

4. Scroll down to view the analysis results
![image](https://github.com/user-attachments/assets/16e37e8d-e2ae-48a2-bd5b-2d162c15fdca)

5. Click the download button to download the result as PDF
![image](https://github.com/user-attachments/assets/f9024c76-9398-4d55-aa0d-4fe38b040c30)

6. Upload another image to analyze a new image
![image](https://github.com/user-attachments/assets/7b81bcad-59a6-44e6-8ed1-46f57ee26fce)
![image](https://github.com/user-attachments/assets/57d3f7c4-d1af-4a19-9603-c25a05d94524)
![image](https://github.com/user-attachments/assets/0894fa93-c654-4e28-a974-cbb149828ffb)

