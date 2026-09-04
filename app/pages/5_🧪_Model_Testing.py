import streamlit as st
from ultralytics import YOLO
from PIL import Image
from pathlib import Path
import numpy as np


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="ParkVision AI - Model Testing",
    page_icon="🧪",
    layout="wide"
)


# ============================================================
# PROJECT + MODEL
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]
MODEL_PATH = PROJECT_ROOT / "models" / "best.pt"


@st.cache_resource
def load_model():
    return YOLO(str(MODEL_PATH))


model = load_model()


# ============================================================
# HEADER
# ============================================================

st.title("🧪 Model Testing")

st.write(
    "Test ParkVision AI on new parking-lot images and observe "
    "how the trained model performs."
)

st.divider()


# ============================================================
# INTRODUCTION
# ============================================================

st.header("🔬 Test on an Unseen Image")

st.write(
    "Upload a parking-lot image that was not used during training "
    "and evaluate the model's slot-level predictions."
)

st.info(
    "Testing the model on unseen images helps assess how well "
    "it generalises beyond the images used during training."
)


# ============================================================
# DETECTION CONFIDENCE
# ============================================================

confidence = st.slider(
    "Detection Confidence",
    min_value=0.10,
    max_value=0.90,
    value=0.25,
    step=0.05
)

st.caption(
    "Higher values make the model more selective, while lower "
    "values allow more possible detections."
)


# ============================================================
# IMAGE UPLOAD
# ============================================================

uploaded_file = st.file_uploader(
    "Upload an unseen parking-lot image",
    type=["jpg", "jpeg", "png"]
)


if uploaded_file is None:

    st.info(
        "Upload an image above to begin model testing."
    )


else:

    image = Image.open(uploaded_file).convert("RGB")

    st.subheader("🖼️ Test Image")

    st.image(
        image,
        use_container_width=True
    )

    st.divider()


    # ========================================================
    # RUN TEST
    # ========================================================

    if st.button(
        "🧪 Test Model",
        type="primary",
        use_container_width=True
    ):

        with st.spinner(
            "Running the trained YOLO model..."
        ):

            results = model.predict(
                source=np.array(image),
                conf=confidence,
                verbose=False
            )

            result = results[0]


        # ====================================================
        # COUNT DETECTIONS
        # ====================================================

        empty = 0
        occupied = 0

        if result.boxes is not None and len(result.boxes) > 0:

            classes = result.boxes.cls.cpu().numpy()

            for class_id in classes:

                if int(class_id) == 0:
                    empty += 1

                elif int(class_id) == 1:
                    occupied += 1


        total = empty + occupied
        available = empty


        if total > 0:
            utilisation = (occupied / total) * 100
        else:
            utilisation = 0


        # ====================================================
        # DISPLAY RESULT
        # ====================================================

        st.success(
            "Model testing completed."
        )

        st.header("🤖 Model Prediction")

        annotated = result.plot()

        st.image(
            annotated,
            channels="BGR",
            use_container_width=True
        )

        st.caption(
            "🟢 Empty parking space   |   🔴 Occupied parking space"
        )


        # ====================================================
        # TEST RESULTS
        # ====================================================

        st.divider()

        st.header("📊 Test Results")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "Total Slots",
                total
            )

        with col2:
            st.metric(
                "Occupied",
                occupied
            )

        with col3:
            st.metric(
                "Available",
                available
            )

        with col4:
            st.metric(
                "Utilisation",
                f"{utilisation:.1f}%"
            )


        # ====================================================
        # CONGESTION
        # ====================================================

        st.divider()

        st.header("🚦 Congestion Interpretation")

        if utilisation < 40:

            st.success(
                "🟢 LOW CONGESTION"
            )

            st.write(
                "The parking area has a relatively large number "
                "of available spaces."
            )

        elif utilisation <= 75:

            st.warning(
                "🟡 MODERATE CONGESTION"
            )

            st.write(
                "The parking area is moderately occupied and "
                "available spaces may be limited."
            )

        else:

            st.error(
                "🔴 HIGH CONGESTION"
            )

            st.write(
                "The parking area is highly occupied and "
                "alternative parking may be useful."
            )


        # ====================================================
        # TESTING NOTES
        # ====================================================

        st.divider()

        st.header("📝 Testing Interpretation")

        if total == 0:

            st.warning(
                "No parking spaces were detected in this image. "
                "Try another parking-lot image or adjust the "
                "confidence threshold."
            )

        else:

            st.write(
                f"The model identified {total} parking spaces "
                f"in the uploaded image. "
                f"{occupied} were classified as occupied and "
                f"{available} were classified as empty."
            )

            st.write(
                "This test demonstrates how the trained object "
                "detection model can convert visual parking-space "
                "detections into availability information."
            )