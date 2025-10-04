import streamlit as st
import pandas as pd
import time
import json
import os


# Set page config for better UI
st.set_page_config(
    page_title="UAV Safety Dashboard",
    page_icon="🚁",
    layout="wide"
)

# Title
st.title("🚁 UAV Safety Dashboard")


# Function to read JSONL files
def read_jsonl(file_path):
    """
    Reads a JSONL file and returns a pandas DataFrame.
    Each line in the file is a JSON object.
    """
    data = []
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            for line in f:
                data.append(json.loads(line.strip()))
    return pd.DataFrame(data)


# Auto-refresh placeholder
placeholder = st.empty()

# Main loop for auto-refresh every 5 seconds
while True:
    with placeholder.container():
        # Read log files
        collision_df = read_jsonl('logs/collision.jsonl')
        intrusion_df = read_jsonl('logs/intrusion.jsonl')

        # Check if logs are available
        if collision_df.empty and intrusion_df.empty:
            st.warning(
                "No log data available. Please ensure "
                "logs/collision.jsonl and logs/intrusion.jsonl exist."
            )
            break

        # Collision Status Section
        st.header("🔍 Collision Status")
        if not collision_df.empty:
            # Get the latest collision entry
            latest_collision = collision_df.iloc[-1]
            time_closest = latest_collision.get('time', 'N/A')
            min_distance = latest_collision.get('min_distance', 'N/A')
            risk = latest_collision.get('risk', 'UNKNOWN')

            # Determine card color
            if risk == "ALERT":
                st.error(
                    f"🚨 ALERT: Closest Approach at {time_closest}, "
                    f"Min Distance: {min_distance} meters"
                )
            elif risk == "OK":
                st.success(
                    f"✅ OK: Closest Approach at {time_closest}, "
                    f"Min Distance: {min_distance} meters"
                )
            else:
                st.info(
                    f"ℹ️ Status: Closest Approach at {time_closest}, "
                    f"Min Distance: {min_distance} meters, Risk: {risk}"
                )
        else:
            st.info("No collision data available.")

        # Intrusion Status Section
        st.header("⚠️ Intrusion Status")
        if not intrusion_df.empty:
            # Get last 5 intrusion detections
            last_5_intrusions = intrusion_df.tail(5)
            for idx, row in last_5_intrusions.iterrows():
                status = row.get('status', 'UNKNOWN')
                time_stamp = row.get('time_s', 'N/A')  # Use 'time_s' instead of 'time'
                if status == "INTRUSION":
                    st.error(f"🚨 Intrusion Detected at {time_stamp}")
                elif status == "CLEAR":
                    st.success(f"✅ Clear at {time_stamp}")
                else:
                    st.info(f"ℹ️ Status: {status} at {time_stamp}")
        else:
            st.info("No intrusion data available.")

        # Charts Section
        st.header("📊 Charts")

        # Line Chart: Distance over time from collision predictor
        if (not collision_df.empty and 'time' in collision_df.columns
                and 'distance' in collision_df.columns):
            st.subheader("Distance Over Time (Collision Predictor)")
            # Assuming 'time' is datetime or numeric, 'distance' is numeric
            chart_df = collision_df[['time', 'distance']].copy()
            # Convert 'time' to datetime, handle errors by coercing to NaT
            chart_df['time'] = pd.to_datetime(
                chart_df['time'], errors='coerce'
            )
            # Drop rows with NaT in 'time' or NaN in 'distance'
            chart_df = chart_df.dropna(subset=['time', 'distance'])
            if not chart_df.empty:
                st.line_chart(chart_df.set_index('time'))
            else:
                st.info("Insufficient data for distance chart.")
        else:
            st.info(
                "Collision data missing 'time' or 'distance' columns for chart."
            )

        # Bar Chart: Intrusion detections over last N frames (assuming N=10)
        if not intrusion_df.empty and 'time_s' in intrusion_df.columns:
            st.subheader("Intrusion Detections Over Last 10 Frames")
            # Convert 'time_s' to datetime, handle errors by coercing to NaT
            intrusion_df['time_s'] = pd.to_datetime(intrusion_df['time_s'], errors='coerce')
            # Drop rows with NaT in 'time_s'
            intrusion_df = intrusion_df.dropna(subset=['time_s'])
            # Group by time_s and count intrusions
            last_10 = intrusion_df.tail(10)
            if not last_10.empty:
                intrusion_counts = last_10.groupby('time_s')['status'].apply(
                    lambda x: (x == 'INTRUSION').sum()
                ).reset_index(name='Intrusions')
                st.bar_chart(intrusion_counts.set_index('time_s'))
            else:
                st.info("Insufficient data for intrusion chart.")
        else:
            st.info("Intrusion data missing 'time_s' column for chart.")

    # Wait 5 seconds before refreshing
    time.sleep(5)
    st.rerun()
