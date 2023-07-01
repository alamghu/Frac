import streamlit as st
import matplotlib as plt

# Streamlit app Title
st.title('Hydraulic Fracturing - Proppant Fill Calculator')

# Side Bar Title
st.sidebar.title('Input')

# Taking Inputs from user by number inputs
Proppant_Specific_Gravity = st.sidebar.number_input("Proppant Specific Gravity (SG)")
lbs_of_Proppant_in_Tubular = st.sidebar.number_input("lbs of Proppant in Tubular (lbs)")
Tubing_Depth_Top_of_Perf = st.sidebar.number_input("Top of Perf Tubing Depth (feet)")
Tubing_ID = st.sidebar.number_input("Tubing ID (inch)")
Casing_Depth_HUD = st.sidebar.number_input("End of Cas-ing/Tubing Depth (feet)")
Casing_ID = st.sidebar.number_input("Casing/Tubing ID (inch)")

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
if st.button("Visualize Well"):
     fig, ax = plt.subplots(figsize=(6, 8))
     ax.set_xlim([-1, 1])
     ax.set_ylim([0, casing_depth_hud + 1])
     ax.axhline(y=0, color='black', linewidth=1)
     ax.axhline(y=casing_depth_hud, color='black', linewidth=1)
     ax.axhline(y=tubing_depth_top_of_perf, color='red', linewidth=1)
     ax.axhline(y=top_of_proppant, color='green', linewidth=1)
     ax.text(-0.1, -0.5, "Wellbore", ha='center', va='bottom')
     ax.text(-0.2, tubing_depth_top_of_perf, "Top of Perf", ha='right', va='bottom', color='red')
     ax.text(-0.2, top_of_proppant, "Top of Proppant", ha='right', va='bottom', color='green')
     ax.axis('off')
