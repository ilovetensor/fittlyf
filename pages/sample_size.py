import streamlit as st
import numpy as np
import pandas as pd
from scipy.stats import norm


st.set_page_config(layout="wide")

def calculate_sample_size(alpha, beta, baseline_conversion, mde):
    # Standard normal critical values at alpha/2 and 1 - beta
    z_alpha_2 = norm.ppf(1 - alpha / 2)
    z_beta = np.abs(norm.ppf(1 - beta))
    
    # Calculate sample size
    sample_size = ((z_alpha_2 + z_beta)**2 * baseline_conversion * (1 - baseline_conversion) )/ (mde**2)
    
    return int(round(sample_size)) *  2

st.title('Fittlyf - Data Science Intern Assignment')
st.subheader('Sample Size Calculator 📏')
st.markdown('Enter the baseline conversion rate and the minimum detectable effect to calculate the sample size needed for an A/B test.')
st.markdown('---')

col_1 = st.columns(2)
with col_1[0]:
    baseline_conversion = st.number_input('Baseline Conversion Rate', min_value=0.0, max_value=1.0, value=0.2, step=0.01)
with col_1[1]:
    mde = st.number_input('Minimum Detectable Effect', min_value=0.0, max_value=1.0, value=0.05, step=0.01)

col_2 = st.columns(2)
with col_2[0]:
    alpha = st.selectbox('Significance Level', options=[0.01, 0.05, 0.10], index=1)
with col_2[1]:
    beta = st.selectbox('Power', options=[0.9, 0.8, 0.7, 0.6], index=1)

# Calculate sample size
if st.button('Calculate Sample Size'):
    sample_size = calculate_sample_size(alpha, beta, baseline_conversion, mde)
    # st.metric(label="Sample Size :", value=sample_size)
    st.markdown('Sample Size :')
    col_3 = st.columns([4,2,4])
    with col_3[1]:
        st.markdown(f"# :rainbow[{sample_size}] :balloon:")
    st.markdown('---')
    st.markdown('**Note:** The sample size calculated is the total for both groups (control and treatment).')