import streamlit as st


st.set_page_config(
    page_title="ParkVision AI",
    page_icon="🚗",
    layout="wide"
)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    """
    <div style="
        padding: 35px;
        border-radius: 22px;
        background: linear-gradient(135deg, #071A2B, #0B4F71);
        color: white;
        margin-bottom: 30px;
    ">
        <h1 style="font-size: 42px; margin-bottom: 8px;">
            🚗 ParkVision AI
        </h1>
        <p style="font-size: 19px; margin: 0;">
            Intelligent Urban Parking Analytics & Space Optimisation Platform
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SYSTEM STATUS
# ============================================================

st.success("🟢 AI System Ready")

st.write(
    "ParkVision AI uses computer vision and object detection "
    "to identify individual parking spaces and determine "
    "whether they are empty or occupied."
)


# ============================================================
# MODEL PERFORMANCE
# ============================================================

st.markdown("---")

st.subheader("🏆 Model Performance")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Precision", "99.8%")

with col2:
    st.metric("Recall", "98.6%")

with col3:
    st.metric("mAP@50", "98.9%")

with col4:
    st.metric("mAP@50–95", "94.0%")


# ============================================================
# FEATURES
# ============================================================

st.markdown("---")

st.subheader("✨ What ParkVision AI Can Do")

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown("### 🅿️ Slot Detection")

    st.write(
        "Detect individual parking spaces from a parking-lot image "
        "and classify them as empty or occupied."
    )


with col2:

    st.markdown("### 📊 Parking Analytics")

    st.write(
        "Calculate total spaces, occupied spaces, available spaces "
        "and overall parking utilisation."
    )


with col3:

    st.markdown("### 🚦 Smart Recommendations")

    st.write(
        "Convert parking utilisation into low, moderate or high "
        "congestion levels and provide actionable recommendations."
    )


# ============================================================
# WORKFLOW
# ============================================================

st.markdown("---")

st.subheader("🔄 How It Works")

steps = [
    "📷 Upload a parking-lot image",
    "🔍 Detect individual parking spaces",
    "🟢🔴 Classify spaces as empty or occupied",
    "📊 Calculate parking availability",
    "🚦 Determine congestion level",
    "💡 Generate a recommendation"
]

for step in steps:
    st.write(step)


# ============================================================
# CALL TO ACTION
# ============================================================

st.markdown("---")

st.info(
    "👈 Use the navigation menu to explore ParkVision AI. "
    "Start with **Analyze Parking** to test the trained model "
    "on an image."
)