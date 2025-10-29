import streamlit as st
import pandas as pd
import numpy as np

st.title("Multiple Disease Prediction System")
st.write("Testing basic functionality...")

# Test if we can import basic libraries
try:
    import joblib
    st.success("✅ joblib imported successfully")
except ImportError as e:
    st.error(f"❌ joblib import failed: {e}")

try:
    from sklearn.ensemble import RandomForestClassifier
    st.success("✅ scikit-learn imported successfully")
except ImportError as e:
    st.error(f"❌ scikit-learn import failed: {e}")

st.info("If you see green checkmarks above, the basic setup is working!")