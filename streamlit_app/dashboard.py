import streamlit as st
import os
import json
import glob
import pandas as pd

LOG_DIR = os.path.join(os.path.dirname(__file__), "lineage_logs")
DATA_DIR = os.path.join(os.path.dirname(__file__), "../data")

def load_lineage_events():
    files = sorted(glob.glob(os.path.join(LOG_DIR, "*.json")))
    events = []
    for file in files:
        with open(file, "r") as f:
            event = json.load(f)
            events.append(event)
    return events

def display_file_preview(title, file_path):
    if os.path.exists(file_path):
        st.markdown(f"### {title}")
        df = pd.read_csv(file_path) if file_path.endswith(".csv") else pd.read_parquet(file_path)
        st.dataframe(df.head())
        st.success(f"{file_path} loaded successfully.")
    else:
        st.warning(f"{file_path} not found.")

def main():
    st.title(" HealthETL Lineage & Data Dashboard")

    # Lineage Section
    st.header("Lineage Events")
    events = load_lineage_events()
    st.write(f"Total lineage events: `{len(events)}`")

    for i, event in enumerate(events[-10:][::-1], 1):
        st.markdown(f"#### Event #{i} — Job: `{event['job']['name']}`")
        st.code(json.dumps(event, indent=2), language="json")

    # Data Preview Section
    st.header(" ETL Data Samples")
    display_file_preview("1. Raw Extracted Data", os.path.join(DATA_DIR, "raw_data.csv"))
    display_file_preview("2. Transformed Data", os.path.join(DATA_DIR, "transformed_data.csv"))
    display_file_preview("3. Final Parquet Data", os.path.join(DATA_DIR, "final_data.parquet"))

if __name__ == "__main__":
    main()
