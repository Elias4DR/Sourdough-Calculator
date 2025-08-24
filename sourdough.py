import streamlit as st

def sourdough_recipe(flour, hydration=70, starter_pct=20, salt_pct=2):
    water = flour * (hydration / 100)
    starter = flour * (starter_pct / 100)
    salt = flour * (salt_pct / 100)
    total = flour + water + starter + salt
    return water, starter, salt, total

st.title("🥖 Sourdough Calculator")

flour = st.number_input("Flour (g)", min_value=100, max_value=2000, value=500, step=10)
hydration = st.number_input("Hydration %", 50.0, 85.0, 70.0, step=0.5)
starter_pct = st.number_input("Starter %", 10.0, 30.0, 20.0, step=0.5)
salt_pct = st.number_input("Salt %", 1.0, 3.0, 2.0, step=0.1)

water, starter, salt, total = sourdough_recipe(flour, hydration, starter_pct, salt_pct)

st.write(f"**Water:** {water:.1f} g")
st.write(f"**Starter:** {starter:.1f} g")
st.write(f"**Salt:** {salt:.1f} g")
st.write(f"**Total Dough:** {total:.1f} g")

