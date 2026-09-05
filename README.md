# Machine_learning-SA

# ParkVision AI
# ParkVision AI

## Intelligent Urban Parking Analytics and Space Optimisation

ParkVision AI
Project Overview

ParkVision AI is an intelligent parking analytics system that uses computer vision to detect whether individual parking spaces are empty or occupied from a parking-lot image. It also calculates parking availability, utilisation, congestion level, and provides a recommendation to the user.
<img width="1440" height="900" alt="Screenshot 2026-09-05 at 10 06 02 PM" src="https://github.com/user-attachments/assets/c2bab5c1-9a0d-4d82-bdad-e10ebefd75a7" />
<img width="1440" height="900" alt="Screenshot 2026-09-05 at 10 05 47 PM" src="https://github.com/user-attachments/assets/1b3b994d-b4e8-4e98-b8d4-9c1208944481" />
<img width="1440" height="900" alt="Screenshot 2026-09-05 at 10 05 14 PM" src="https://github.com/user-attachments/assets/4fdf244b-03c3-43a8-b9ca-2b5c190f61e5" />
<img width="1440" height="900" alt="Screenshot 2026-09-05 at 10 04 57 PM" src="https://github.com/user-attachments/assets/649baeb8-1ce0-4919-b6d0-8c2dcc2d7e75" />

Problem Statement

Finding available parking spaces can be inefficient, especially in busy urban areas. ParkVision AI aims to automate parking-space monitoring and provide clear information about parking availability.

Dataset

The project uses a PKLot-based object detection dataset containing parking-lot images with labelled empty and occupied spaces. The dataset includes different environmental conditions such as sunny, cloudy, and rainy weather.

The dataset was converted from COCO annotation format to YOLO format so it could be used for object detection.

Model & Training

A YOLO11n object-detection model was selected because the project requires detecting individual parking spaces rather than simply classifying an entire image.

The model was trained for 15 epochs using 640×640 images and Apple MPS acceleration. Data augmentation and YOLO's built-in training pipeline were used to improve generalisation.

Results

The final model achieved approximately:

Precision: 99.8%
Recall: 98.6%
mAP@50: 98.9%
mAP@50–95: 94.0%

The model detects both space-empty and space-occupied classes.

Parking Analytics

After detection, the application calculates the total number of detected parking spaces, occupied spaces, available spaces, and utilisation percentage.

The system classifies congestion as:

Low: below 40%
Moderate: 40–75%
High: above 75%

It then provides a simple recommendation based on parking availability.

Streamlit Application

The project is deployed as a Streamlit web application. Users can upload a parking-lot image and receive an annotated result where green boxes represent empty spaces and red boxes represent occupied spaces.

The application also includes pages for analytics, model performance, model testing, and an explanation of how the system works.

Testing

The model was tested using unseen parking images to evaluate its ability to detect spaces under different conditions. Testing helped identify the strengths and limitations of the model and application.

Challenges

One of the main challenges was converting the dataset's COCO annotations into YOLO format. Training was also time-consuming on the Mac, requiring several hours to complete. Deployment required additional troubleshooting because the Streamlit Cloud environment used different Python and package configurations from the local development environment.

Limitations & Future Improvements

The current system analyses uploaded images rather than directly processing live CCTV footage. Future improvements could include real-time camera integration, better handling of unusual camera angles and lighting conditions, and further optimisation for faster inference.
<img width="1440" height="900" alt="Screenshot 2026-09-05 at 9 57 27 PM" src="https://github.com/user-attachments/assets/8eb1b112-3fde-4a4f-979f-a482edfc35be" />
<img width="1440" height="900" alt="Screenshot 2026-09-05 at 9 56 49 PM" src="https://github.com/user-attachments/assets/6850cac8-dd59-4bf7-857b-9c84844e8788" />
<img width="1440" height="900" alt="Screenshot 2026-09-05 at 10 02 51 PM" src="https://github.com/user-attachments/assets/11fd6ee5-3628-4f23-ae32-37b64ea7d18a" />

Technologies Used

Python, YOLO11, Ultralytics, OpenCV, Pillow, Streamlit, NumPy, Pandas and Matplotlib.

Deployment

The application is deployed using Streamlit Community Cloud, with the source code and trained model maintained in GitHub.

References
PKLot Dataset and Research Paper
Ultralytics YOLO Documentation
Streamlit Documentation
OpenCV Documentation
TensorFlow Image Classification Resources

LINK TO THE APP : https://idai107-2505445--snigdhareddyguduru-srjuuln2uc3pwyj3qsvdwb.streamlit.app/
