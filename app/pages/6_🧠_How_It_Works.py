import streamlit as st


st.set_page_config(
    page_title="ParkVision AI - How It Works",
    page_icon="🧠",
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
            🧠 How ParkVision AI Works
        </h1>
        <p style="font-size: 17px; margin: 0;">
            From a parking-lot image to intelligent availability
            insights.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# OVERVIEW
# ============================================================

st.subheader("🚗 System Overview")

st.write(
    "ParkVision AI is an intelligent urban parking analytics "
    "system designed to identify individual parking spaces and "
    "classify them as either empty or occupied."
)

st.write(
    "The system uses a YOLO object-detection model trained on "
    "parking-space annotations from the PKLot dataset. The "
    "detected spaces are then converted into availability and "
    "parking-utilisation information."
)


# ============================================================
# WORKFLOW
# ============================================================

st.markdown("---")

st.subheader("⚙️ The ParkVision Pipeline")

steps = [
    (
        "01",
        "📷 Image Input",
        "A parking-lot image is uploaded to the Streamlit application."
    ),
    (
        "02",
        "🔍 Object Detection",
        "The trained YOLO model searches the image for individual parking spaces."
    ),
    (
        "03",
        "🟢🔴 Classification",
        "Each detected parking space is classified as empty or occupied."
    ),
    (
        "04",
        "📊 Availability Calculation",
        "The system counts total, occupied and available parking spaces."
    ),
    (
        "05",
        "🚦 Congestion Analysis",
        "Parking utilisation is converted into low, moderate or high congestion."
    ),
    (
        "06",
        "💡 Recommendation",
        "The system provides a simple recommendation based on parking availability."
    )
]


for number, title, description in steps:

    col1, col2 = st.columns([1, 8])

    with col1:
        st.markdown(
            f"""
            <div style="
                background: #0B4F71;
                color: white;
                border-radius: 50%;
                width: 48px;
                height: 48px;
                display: flex;
                align-items: center;
                justify-content: center;
                font-weight: bold;
                font-size: 14px;
            ">
                {number}
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(f"### {title}")
        st.write(description)


# ============================================================
# MODEL
# ============================================================

st.markdown("---")

st.subheader("🤖 The AI Model")

col1, col2 = st.columns(2)

with col1:

    st.markdown("### YOLO11n")

    st.write(
        "ParkVision uses YOLO11n, a lightweight object-detection "
        "model from the Ultralytics YOLO family."
    )

    st.write(
        "Unlike simply counting vehicles, the model detects the "
        "parking-space regions themselves. This allows the system "
        "to determine the status of individual spaces."
    )


with col2:

    st.markdown("### 🎯 Two Detection Classes")

    st.write(
        "The model identifies two parking-space classes:"
    )

    st.success("🟢 Space Empty")

    st.error("🔴 Space Occupied")


# ============================================================
# DATA
# ============================================================

st.markdown("---")

st.subheader("🗂️ Training Data")

st.write(
    "The project uses a PKLot-based object-detection dataset "
    "containing parking-lot images captured under different "
    "conditions."
)

data_col1, data_col2, data_col3 = st.columns(3)

with data_col1:
    st.metric(
        "Total Images",
        "12,416"
    )

with data_col2:
    st.metric(
        "Parking-Space Annotations",
        "711,856"
    )

with data_col3:
    st.metric(
        "Classes",
        "2"
    )


# ============================================================
# LOGIC
# ============================================================

st.markdown("---")

st.subheader("🚦 Congestion Logic")

st.write(
    "After detecting the parking spaces, ParkVision calculates "
    "utilisation using the proportion of occupied spaces."
)

logic_data = {
    "Utilisation": [
        "< 40%",
        "40% – 75%",
        "> 75%"
    ],
    "Congestion": [
        "🟢 Low",
        "🟡 Moderate",
        "🔴 High"
    ],
    "System Response": [
        "Parking is relatively available.",
        "Parking is moderately occupied.",
        "Parking is highly occupied."
    ]
}

st.table(logic_data)


# ============================================================
# WHY OBJECT DETECTION?
# ============================================================

st.markdown("---")

st.subheader("💡 Why Object Detection?")

st.write(
    "Parking occupancy is a spatial problem: the system needs "
    "to know where each parking space is located and determine "
    "its individual status."
)

st.write(
    "Object detection is therefore suitable because it provides "
    "both the location of each parking space and its predicted "
    "class."
)


# ============================================================
# END-TO-END
# ============================================================

st.markdown("---")

st.subheader("🔄 End-to-End Example")

st.code(
    """
Parking Image
      ↓
YOLO11n Detection
      ↓
Parking Space Bounding Boxes
      ↓
Empty / Occupied Classification
      ↓
Count Available Spaces
      ↓
Calculate Utilisation
      ↓
Determine Congestion
      ↓
Generate Recommendation
    """,
    language="text"
)

st.success(
    "🚀 ParkVision AI transforms a single parking-lot image "
    "into actionable parking information."
)