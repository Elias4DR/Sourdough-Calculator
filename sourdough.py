import streamlit as st
import pandas as pd

# Set page title and layout
st.set_page_config(page_title="Sourdough Bread Calculator", layout="centered")
st.title("🥖 Sourdough Bread Calculator")

st.markdown("Adjust your ingredients below to calculate your sourdough dough:")

# Use columns for compact input layout
col1, col2 = st.columns(2)

with col1:
    flour = st.number_input("🌾 Flour (g)", min_value=100.0, max_value=2000.0, value=500.0, step=10.0)
    hydration = st.number_input("💧 Hydration %", min_value=50.0, max_value=85.0, value=70.0, step=0.5)

with col2:
    starter_pct = st.number_input("🍞 Starter %", min_value=10.0, max_value=30.0, value=20.0, step=0.5)
    salt_pct = st.number_input("🧂 Salt %", min_value=1.0, max_value=3.0, value=2.0, step=0.1)

def sourdough_recipe(flour, hydration=70, starter_pct=20, salt_pct=2):
    water = flour * (hydration / 100)
    starter = flour * (starter_pct / 100)
    salt = flour * (salt_pct / 100)
    total = flour + water + starter + salt
    return {
        "Flour (g)": round(flour, 1),
        "Water (g)": round(water, 1),
        "Starter (g)": round(starter, 1),
        "Salt (g)": round(salt, 1),
        "Total Dough (g)": round(total, 1)
    }

# Calculate recipe
recipe = sourdough_recipe(flour, hydration, starter_pct, salt_pct)

# Display nicely as a table
st.markdown("### 🍽 Ingredients")
st.table(pd.DataFrame([recipe]))

