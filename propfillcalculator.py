import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd
import streamlit as st

# Streamlit app Title
st.title('Hydraulic Fracturing - Proppant Fill Calculator')

# Side Bar Title
st.sidebar.title('Input')

# Taking Inputs from user by number inputs
Proppant_Specific_Gravity = st.sidebar.number_input("Proppant Specific Gravity (SG)", min_value = 1, max_value = 4.65,value =3.5)
lbs_of_Proppant_in_Tubular = st.sidebar.number_input("lbs of Proppant in Tubular (lbs)", min_value = 1, max_value = 1000000,value =50000)
Tubing_Depth_Top_of_Perf = st.sidebar.number_input("Top of Perf Tubing Depth (feet)", min_value = 100, max_value = 30000,value =15000)
Tubing_ID = st.sidebar.number_input("Tubing ID (inch)", min_value = 2.99, max_value = 7,value =3.74)
Casing_Depth_HUD = st.sidebar.number_input("End of Cas-ing/Tubing Depth (feet)", min_value = 100, max_value = 30000,value =15000)
Casing_ID = st.sidebar.number_input("Casing/Tubing ID (inch)", min_value = 2.99, max_value = 10,value =3.74)

# Logic & Calculation
A = (lbs_of_Proppant_in_Tubular / (Proppant_Specific_Gravity / 2.65) * 14.3)
B = (0.0408 * (Casing_ID ** 2)) * (Casing_Depth_HUD - Tubing_Depth_Top_of_Perf)
C = (Tubing_Depth_Top_of_Perf - ((lbs_of_Proppant_in_Tubular / ((Proppant_Specific_Gravity / 2.65) * 14.3) - ((0.0408 * Casing_ID ** 2) * (Casing_Depth_HUD - Tubing_Depth_Top_of_Perf)))) * (24.51 / Tubing_ID ** 2))
D = (Casing_Depth_HUD - (lbs_of_Proppant_in_Tubular / ((Proppant_Specific_Gravity / 2.65) * 14.3)) * (24.51 / Tubing_ID ** 2))
     
if A > B:
    top_of_proppant = C
    st.write(f'Top of Proppant = {top_of_proppant} feet')
else:
    top_of_proppant = D
    st.write(f'Top of Proppant = {top_of_proppant} feet')

# Visualize the wellbore schematic
if st.button("Visualize Wellbore"):
     plt.figure(figsize = (6,8))
     fig,ax = plt.subplots()
     ax.set_xlim([-1, 1])
     ax.set_ylim([Casing_Depth_HUD+ 1, 0])
     ax.axhline(y=0, color='black', linewidth=1)
     ax.axhline(y=Casing_Depth_HUD, color='black', linewidth=1)
     ax.axhline(y=Tubing_Depth_Top_of_Perf, color='red', linewidth=1)
     ax.axhline(y=top_of_proppant, color='green', linewidth=3)
     ax.text(-0.1, -0.5, "Wellbore", ha='center', va='bottom')
     ax.text(-0.2, Tubing_Depth_Top_of_Perf, "Top of Perf", ha='right', va='bottom', color='red')
     
     st.pyplot(fig)
     
     ax.text(-0.2, top_of_proppant, "Top of Proppant", ha='right', va='bottom', color='green')
     ax.axis('off')
