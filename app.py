import streamlit as st
import numpy as np
import pandas as pd
from scipy.stats import norm
from st_pages import Page, show_pages, add_page_title


st.set_page_config(layout="wide")




# Specify what pages should be shown in the sidebar, and what their titles 
# and icons should be
show_pages(
    [
        Page("app.py", "Hypothesis Testing", ""),
        Page("pages/sample_size.py", "Sample Size Calculator", ""),
    ]
)

def perform_ab_test(control_visitors, control_conversions, treatment_visitors, treatment_conversions, confidence_level):
    
    # Calculate conversion rates
    control_rate = control_conversions / control_visitors
    treatment_rate = treatment_conversions / treatment_visitors
    
    # Calculate pooled standard error 
    pooled_se = np.sqrt(control_rate * (1 - control_rate) / control_visitors + treatment_rate * (1 - treatment_rate) / treatment_visitors)
    
    # Calculate Z-score
    z_score = (treatment_rate - control_rate) / pooled_se
    
    # Calculate p-value using the standard normal distribution 
    p_value = 2 * (1 - norm.cdf(abs(z_score)))
    
    # Compare p-value with significance level 
    significance_level = 1 - confidence_level / 100
    
    if p_value < significance_level:
        if z_score > 0:
            return "Experiment Group is Better"
        else:
            return "Control Group is Better"
    else:
        return "Indeterminate"
    


st.title('Fittlyf - Data Science Intern Assignment')
st.subheader('Hypothesis Testing ✅')
st.markdown('Enter the number of visitors and conversions for the control and treatment groups to determine if the treatment group is better than the control group.')
st.markdown('---')


col_1 = st.columns(2)
with col_1[0]:
    control_visitors = st.number_input('Control Visitors', min_value=0, max_value=100000, value=2)
with col_1[1]:
    control_conversions = st.number_input('Control Conversions', min_value=0, max_value=100000, value=2)

col_2 = st.columns(2)
with col_2[0]:
    treatment_visitors = st.number_input('Treatment Visitors', min_value=0, max_value=100000, value=2)
with col_2[1]:
    treatment_conversions = st.number_input('Treatment Conversions', min_value=0, max_value=100000, value=8)

col_3 = st.columns(3)
with col_3[0]:
    confidence_level = st.selectbox('Conficence Level (%)', options=[90, 95, 99], index=1)


# Perform A/B Test
if st.button('Perform A/B Test'):
    result = perform_ab_test(control_visitors, control_conversions, treatment_visitors, treatment_conversions, confidence_level)
    if result == "Experiment Group is Better":
        st.success(result)
    elif result == "Control Group is Better":
        st.error(result)
    else:
        st.warning(result)  

