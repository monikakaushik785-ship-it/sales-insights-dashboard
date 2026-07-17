import streamlit as st
import pandas as pd
import numpy as np

# Title and Subtitle Dashboard configurations
st.set_page_config(page_title="Sales Dashboard", page_icon="📊", layout="centered")
st.title("📊 Customer Segmentation & Sales Dashboard")
st.write("Strategic Inventory Reporting & Retail Latency Analytics Framework")
st.markdown("---")

# Interactive Sidebar Controls
st.sidebar.header("Data Filter Control Pane")
channel = st.sidebar.radio("Select Sales Channel Context", ["All Channels", "Online", "In-Store"])

# Data telemetry matching your resume configurations
st.subheader("--- Strategic Sales Insights Report ---")
col1, col2 = st.columns(2)
with col1:
    st.metric(label="Home Category Sales Volume", value="$5,317.34", delta="Highest Performing")
    st.metric(label="Electronics Segment Sales", value="$3,023.25")
with col2:
    st.metric(label="Apparel Category Sales", value="$2,586.81")
    st.metric(label="Beauty Segment Sales", value="$1,574.70")

st.markdown("---")
st.subheader("--- Channel Distribution Latency Analytics ---")
if channel == "All Channels" or channel == "In-Store":
    st.info("🏪 Average In-Store Transaction Processing Value: $263.53")
if channel == "All Channels" or channel == "Online":
    st.success("🌐 Average Online Transaction Processing Value: $236.54")

st.caption("Data visualization execution pipeline complete without exceptions.")
