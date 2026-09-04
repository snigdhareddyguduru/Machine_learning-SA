import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="ParkVision AI - Analytics",
    page_icon="📊",
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
            📊 Parking Analytics
        </h1>
        <p style="font-size: 17px; margin: 0;">
            Understand parking utilisation and availability
            at a glance.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# DEMONSTRATION ANALYTICS
# ============================================================

st.subheader("📈 Parking Utilisation Overview")

st.write(
    "The dashboard below demonstrates how ParkVision AI "
    "can convert slot-level detections into useful parking analytics."
)


# Example analytics data
data = pd.DataFrame(
    {
        "Parking Area": [
            "Area A",
            "Area B",
            "Area C",
            "Area D",
            "Area E"
        ],
        "Total Slots": [
            120,
            100,
            150,
            80,
            110
        ],
        "Occupied": [
            42,
            71,
            128,
            24,
            89
        ]
    }
)

data["Available"] = (
    data["Total Slots"] - data["Occupied"]
)

data["Utilisation"] = (
    data["Occupied"] /
    data["Total Slots"] *
    100
)


# ============================================================
# TOP METRICS
# ============================================================

total_slots = int(data["Total Slots"].sum())
total_occupied = int(data["Occupied"].sum())
total_available = int(data["Available"].sum())

overall_utilisation = (
    total_occupied / total_slots * 100
)


col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Parking Slots",
        total_slots
    )

with col2:
    st.metric(
        "Occupied Slots",
        total_occupied
    )

with col3:
    st.metric(
        "Available Slots",
        total_available
    )

with col4:
    st.metric(
        "Overall Utilisation",
        f"{overall_utilisation:.1f}%"
    )


# ============================================================
# CHARTS
# ============================================================

st.markdown("---")

left, right = st.columns(2)

with left:

    st.subheader("🅿️ Occupied vs Available")

    chart_data = data[
        ["Parking Area", "Occupied", "Available"]
    ].set_index("Parking Area")

    st.bar_chart(chart_data)


with right:

    st.subheader("📊 Utilisation by Area")

    utilisation_data = data[
        ["Parking Area", "Utilisation"]
    ].set_index("Parking Area")

    st.bar_chart(utilisation_data)


# ============================================================
# CONGESTION
# ============================================================

st.markdown("---")

st.subheader("🚦 Congestion Classification")

for _, row in data.iterrows():

    utilisation = row["Utilisation"]

    if utilisation < 40:
        status = "🟢 Low"

    elif utilisation <= 75:
        status = "🟡 Moderate"

    else:
        status = "🔴 High"

    st.write(
        f"**{row['Parking Area']}** — "
        f"{utilisation:.1f}% utilisation — {status}"
    )


# ============================================================
# DATA TABLE
# ============================================================

st.markdown("---")

st.subheader("📋 Parking Area Details")

display_data = data.copy()

display_data["Utilisation"] = (
    display_data["Utilisation"]
    .round(1)
    .astype(str)
    + "%"
)

st.dataframe(
    display_data,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# INSIGHT
# ============================================================

st.markdown("---")

if overall_utilisation > 75:

    st.error(
        "🔴 Overall parking utilisation is high. "
        "Drivers should consider alternative parking areas."
    )

elif overall_utilisation >= 40:

    st.warning(
        "🟡 Overall parking utilisation is moderate. "
        "Parking availability should be checked before arrival."
    )

else:

    st.success(
        "🟢 Overall parking utilisation is low. "
        "A large number of spaces are currently available."
    )