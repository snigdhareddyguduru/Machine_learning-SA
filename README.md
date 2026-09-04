# Machine_learning-SA

# ParkVision AI
# ParkVision AI

## Intelligent Urban Parking Analytics and Space Optimisation

ParkVision AI is a computer vision project that detects individual parking spaces from a parking lot image and classifies them as occupied or empty. The system then calculates parking availability, utilisation and congestion and provides a simple recommendation.

The project was developed as part of the Machine Learning and Deep Learning Summative Assessment.

## Problem

Finding available parking in busy areas can take time and can contribute to unnecessary movement and congestion. ParkVision AI uses computer vision to analyse a parking lot image and provide information about which parking spaces are occupied and which are available.

## How It Works

The system follows this process:

**Parking Image → YOLO11n → Parking Space Detection → Occupied/Empty Classification → Parking Analytics → Recommendation**

Green boxes represent empty spaces and red boxes represent occupied spaces.

## Dataset

The project uses a PKLot-based parking-space dataset.

| Split | Images | Annotations |
|---|---:|---:|
| Training | 8,691 | 497,856 |
| Validation | 2,483 | 143,316 |
| Testing | 1,242 | 70,684 |
| Total | 12,416 | 711,856 |

The two classes used are:

- `space-empty`
- `space-occupied`

The original annotations were in COCO format and were converted to YOLO format using a Python script.

## Model

YOLO11n was selected because the project requires object detection at the individual parking-space level.

The final model was trained for 15 epochs using Apple M1 MPS acceleration.

| Parameter | Value |
|---|---|
| Model | YOLO11n |
| Classes | 2 |
| Epochs | 15 |
| Image Size | 640 × 640 |
| Batch Size | 4 |
| Device | Apple M1 MPS |
| Pretrained | Yes |
| Augmentation | Yes |

## Results

The final model achieved the following validation results:

| Metric | Result |
|---|---:|
| Precision | 99.8% |
| Recall | 98.6% |
| mAP@50 | 98.9% |
| mAP@50-95 | 94.0% |

The project also generated a confusion matrix and other evaluation plots.

## Parking Analytics

The application calculates:

- Total parking spaces
- Occupied spaces
- Available spaces
- Parking utilisation
- Congestion level

Congestion is classified as:

| Utilisation | Level |
|---|---|
| Below 40% | Low |
| 40–75% | Moderate |
| Above 75% | High |

A recommendation is then generated based on the parking situation.

## Streamlit Application

The application is built using Streamlit and includes separate sections for:

- Dashboard
- Analyze Parking
- Parking Analytics
- How It Works
- Model Performance
- About

Users can upload a parking lot image and view the model's detections and parking statistics.

## Screenshots

### Dashboard

![Dashboard](screenshot/dashboard.png)

### Parking Analysis

![Parking Analysis](screenshot/analysis.png)

### Detection Output

![Detection Output](screenshot/detection.png)

### Model Performance

![Model Performance](screenshot/performance.png)

## Project Structure

```text
PARKVISION_AI/
├── app/
│   └── app.py
├── dataset/
├── models/
│   └── best.pt
├── notebooks/
├── runs/
├── scripts/
│   └── convert_coco_to_yolo.py
├── parkvision.yaml
├── requirements.txt
└── README.md

Testing

The model was tested during development using validation and unseen parking-lot images. Testing focused on detection accuracy, occupied/empty classification, parking counts, utilisation and congestion recommendations.

The application was also tested locally using Streamlit.

Challenges

One of the main challenges was training time. An initial CPU test took around 8.6 hours for one epoch, so Apple M1 MPS acceleration was tested and used for the final training.

Another challenge was converting the COCO annotations into YOLO format. A custom Python script was created to handle this conversion.

Limitations

The current system works with uploaded images rather than live CCTV footage. Performance may also vary with different camera angles, lighting conditions and parking layouts.

Future Improvements

Future versions could include:

Live CCTV monitoring
Historical parking data
Parking availability prediction
Multiple-camera support
Peak-hour analysis
Automatic parking alerts
Technologies

Python, YOLO11n, Ultralytics, PyTorch, Streamlit, Pillow, NumPy, GitHub and the PKLot dataset.
himwhtayyjeatwvqskwt6v.streamlit.app/Analyze_Parking<img width="1440" height="900" alt="Screenshot 2026-09-04 at 2 24 02 PM" src="https://github.com/user-attachments/assets/bdc28ada-7147-4182-ac63-ebd1355865e3" />
<img width="1440" height="900" alt="Screenshot 2026-09-04 at 2 26 31 PM" src="https://github.com/user-attachments/assets/e12de1a0-5080-4247-84f9-4c3892124b61" />
<img width="1440" height="900" alt="Screenshot 2026-09-04 at 2 26 04 PM" src="https://github.com/user-attachments/assets/04ac3bef-a5b9-4ff1-8d96-8a30f90cc700" />


Link

Live Streamlit App:https://machinelearning-sa-himwhtayyjeatwvqskwt6v.streamlit.app/Analyze_Parking

References
PKLot: A Robust Dataset for Parking Lot Classification
Ultralytics YOLO Documentation
Streamlit Documentation
OpenCV Documentation
TensorFlow Image Classification Documentation
