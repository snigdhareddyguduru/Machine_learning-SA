import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="ParkVision AI - Model Performance",
    page_icon="📈",
    layout="wide"
)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    """
    <div style="
        padding: 28px;
        border-radius: 20px;
        background: linear-gradient(135deg, #071A2B, #0B4F71);
        color: white;
        margin-bottom: 25px;
    ">
        <h1 style="margin-bottom: 5px;">
            📈 Model Performance
        </h1>
        <p style="font-size: 17px; margin: 0;">
            Evaluation results from the trained ParkVision AI
            YOLO object-detection model.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# MODEL INFORMATION
# ============================================================

st.subheader("🤖 Model Configuration")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Model", "YOLO11n")

with col2:
    st.metric("Training Epochs", "15")

with col3:
    st.metric("Image Size", "640 × 640")

with col4:
    st.metric("Device", "Apple MPS")


# ============================================================
# MAIN RESULTS
# ============================================================

st.markdown("---")

st.subheader("🏆 Validation Results")

st.write(
    "The model was trained for 15 epochs using the PKLot parking-space "
    "dataset. Performance was evaluated on the validation dataset."
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Precision",
        "99.8%"
    )

with col2:
    st.metric(
        "Recall",
        "98.6%"
    )

with col3:
    st.metric(
        "mAP@50",
        "98.9%"
    )

with col4:
    st.metric(
        "mAP@50–95",
        "94.0%"
    )


# ============================================================
# CLASS PERFORMANCE
# ============================================================

st.markdown("---")

st.subheader("🎯 Performance by Parking-Space Class")

class_data = pd.DataFrame(
    {
        "Class": [
            "Space Empty",
            "Space Occupied"
        ],
        "Precision": [
            99.7,
            99.8
        ],
        "Recall": [
            97.9,
            99.3
        ],
        "mAP@50": [
            98.4,
            99.4
        ],
        "mAP@50–95": [
            94.1,
            93.9
        ]
    }
)

st.dataframe(
    class_data,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# VISUAL COMPARISON
# ============================================================

st.markdown("---")

st.subheader("📊 Class Performance Comparison")

chart_data = class_data.set_index("Class")[
    [
        "Precision",
        "Recall",
        "mAP@50",
        "mAP@50–95"
    ]
]

st.bar_chart(chart_data)


# ============================================================
# CONFUSION MATRIX
# ============================================================

st.markdown("---")

st.subheader("🧩 Confusion Matrix")

st.write(
    "The confusion matrix helps evaluate how effectively the model "
    "distinguishes between empty and occupied parking spaces."
)

st.info(
    "The final confusion-matrix visual from the YOLO training run "
    "will be added here from the generated evaluation results."
)


# ============================================================
# TRAINING OBSERVATION
# ============================================================

st.markdown("---")

st.subheader("🔎 Key Observations")

observations = [
    "The model achieved very high precision, indicating that most detected parking spaces were classified correctly.",
    "Recall was also high, meaning the model successfully detected the majority of parking spaces.",
    "The mAP@50 score of 98.9% indicates strong object-detection performance.",
    "The mAP@50–95 score of 94.0% shows that the model maintained strong localisation performance under stricter IoU thresholds.",
    "The occupied-space class achieved a recall of 99.3%, showing particularly strong detection of occupied parking spaces."
]

for observation in observations:
    st.write(f"• {observation}")


# ============================================================
# TRAINING TIME
# ============================================================

st.markdown("---")

st.subheader("⏱️ Training Information")

st.write(
    "Final training took approximately 8.5 hours on an Apple M1 "
    "using the MPS backend. The model was trained for 15 epochs."
)

st.success(
    "✅ ParkVision AI achieved strong validation performance "
    "and is ready for deployment testing."
)