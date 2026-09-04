import streamlit as st
from ultralytics import YOLO
from PIL import Image
from pathlib import Path
import numpy as np
import io


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="ParkVision AI - Analyze",
    page_icon="🔍",
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

st.title("🔍 Analyze Parking")

st.write(
    "Upload a parking-lot image and let ParkVision AI "
    "analyse every detected parking space."
)

st.divider()


# ============================================================
# SIDEBAR - DETECTION SETTINGS
# ============================================================

st.sidebar.header("⚙️ Detection Settings")

confidence = st.sidebar.slider(
    "Detection Confidence",
    min_value=0.10,
    max_value=0.90,
    value=0.25,
    step=0.05
)

st.sidebar.write(
    f"Current threshold: **{confidence:.2f}**"
)

st.sidebar.caption(
    "Higher values make the model more selective. "
    "Lower values allow more possible detections."
)


# ============================================================
# IMAGE UPLOAD
# ============================================================

st.header("📷 Upload Parking Image")

st.write(
    "Choose a JPG, JPEG or PNG image of a parking lot."
)

uploaded_file = st.file_uploader(
    "Upload image",
    type=["jpg", "jpeg", "png"]
)


# ============================================================
# NO IMAGE
# ============================================================

if uploaded_file is None:

    st.info(
        "Upload a parking-lot image above to begin your analysis."
    )


# ============================================================
# IMAGE UPLOADED
# ============================================================

else:

    image = Image.open(uploaded_file).convert("RGB")

    st.subheader("🖼️ Image Preview")

    st.image(
        image,
        use_container_width=True
    )

    st.divider()

    # ========================================================
    # ANALYZE BUTTON
    # ========================================================

    if st.button(
        "🚀 Run ParkVision AI",
        type="primary",
        use_container_width=True
    ):

        with st.spinner(
            "AI is analysing the parking spaces..."
        ):

            results = model.predict(
                source=np.array(image),
                conf=confidence,
                verbose=False
            )

            result = results[0]

        # ====================================================
        # COUNT PARKING SPACES
        # ====================================================

        occupied = 0
        empty = 0

        if result.boxes is not None and len(result.boxes) > 0:

            classes = result.boxes.cls.cpu().numpy()

            for class_id in classes:

                if int(class_id) == 0:
                    empty += 1

                elif int(class_id) == 1:
                    occupied += 1

        total = occupied + empty
        available = empty

        # ====================================================
        # UTILISATION
        # ====================================================

        if total > 0:
            utilisation = (occupied / total) * 100
        else:
            utilisation = 0

        # ====================================================
        # CONGESTION + RECOMMENDATION
        # ====================================================

        if utilisation < 40:

            congestion = "LOW"

            recommendation = (
                "Plenty of parking spaces are available. "
                "Proceed to the parking area."
            )

        elif utilisation <= 75:

            congestion = "MODERATE"

            recommendation = (
                "Parking is moderately busy. "
                "Available spaces may be limited."
            )

        else:

            congestion = "HIGH"

            recommendation = (
                "Parking is highly occupied. "
                "Consider trying another parking area."
            )

        # ====================================================
        # DETECTION RESULT
        # ====================================================

        st.success(
            "Analysis completed successfully!"
        )

        st.header("🤖 AI Parking Detection")

        annotated = result.plot()

        st.image(
            annotated,
            channels="BGR",
            use_container_width=True
        )

        st.caption(
            "🟢 Empty parking space   |   🔴 Occupied parking space"
        )

        st.divider()

        # ====================================================
        # PARKING AVAILABILITY
        # ====================================================

        st.header("🅿️ Parking Availability")

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

        st.divider()

        # ====================================================
        # CONGESTION ANALYSIS
        # ====================================================

        st.header("🚦 Congestion Analysis")

        if congestion == "HIGH":

            st.error(
                "🔴 HIGH CONGESTION"
            )

        elif congestion == "MODERATE":

            st.warning(
                "🟡 MODERATE CONGESTION"
            )

        else:

            st.success(
                "🟢 LOW CONGESTION"
            )

        st.write(
            recommendation
        )

        st.divider()

        # ====================================================
        # PARKING BREAKDOWN
        # ====================================================

        st.header("📊 Parking Breakdown")

        chart_data = {
            "Occupied": occupied,
            "Available": available
        }

        st.bar_chart(chart_data)

        st.divider()

        # ====================================================
        # EXPORT
        # ====================================================

        st.header("⬇️ Export Analysis")

        image_buffer = io.BytesIO()

        Image.fromarray(
            annotated[:, :, ::-1]
        ).save(
            image_buffer,
            format="PNG"
        )

        st.download_button(
            label="📥 Download Annotated Image",
            data=image_buffer.getvalue(),
            file_name="parkvision_analysis.png",
            mime="image/png",
            use_container_width=True
        )