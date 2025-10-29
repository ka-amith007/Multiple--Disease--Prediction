import streamlit as st

st.title("🏥 Multiple Disease Prediction - Test")
st.write("Testing basic Streamlit functionality...")

# Test basic imports
try:
    import pandas as pd
    st.success("✅ Pandas imported successfully")
except Exception as e:
    st.error(f"❌ Pandas error: {e}")

try:
    import numpy as np
    st.success("✅ Numpy imported successfully")
except Exception as e:
    st.error(f"❌ Numpy error: {e}")

try:
    import plotly.express as px
    import plotly.graph_objects as go
    st.success("✅ Plotly imported successfully")
    
    # Create a simple test chart
    df = pd.DataFrame({'x': [1, 2, 3, 4], 'y': [10, 11, 12, 13]})
    fig = px.line(df, x='x', y='y', title='Test Chart')
    st.plotly_chart(fig)
    
except Exception as e:
    st.error(f"❌ Plotly error: {e}")

try:
    from streamlit_option_menu import option_menu
    st.success("✅ Streamlit-option-menu imported successfully")
except Exception as e:
    st.error(f"❌ Streamlit-option-menu error: {e}")

st.write("If all imports show ✅, the basic setup works!")