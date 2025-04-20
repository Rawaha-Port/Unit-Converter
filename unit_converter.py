import streamlit as st

# --- Conversion Functions ---
def convert_length(value, from_unit, to_unit):
    units = {
        "Metre": 1.0,
        "Kilometre": 1000.0,
        "Centimetre": 0.01,
        "Millimetre": 0.001,
        "Inch": 0.0254,
        "Foot": 0.3048,
        "Yard": 0.9144,
        "Mile": 1609.34
    }
    result = value * units[from_unit] / units[to_unit]
    multiplier = round(units[from_unit] / units[to_unit], 5)
    return result, f"multiply the length value by {multiplier}"

def convert_weight(value, from_unit, to_unit):
    units = {
        "Gram": 1.0,
        "Kilogram": 1000.0,
        "Milligram": 0.001,
        "Pound": 453.592,
        "Ounce": 28.3495
    }
    result = value * units[from_unit] / units[to_unit]
    multiplier = round(units[from_unit] / units[to_unit], 5)
    return result, f"multiply the weight value by {multiplier}"

def convert_temperature(value, from_unit, to_unit):
    formula = ""
    if from_unit == to_unit:
        return value, "same unit, no conversion"
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return (value * 9/5) + 32, "multiply by 9/5 and add 32"
        elif to_unit == "Kelvin":
            return value + 273.15, "add 273.15"
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5/9, "subtract 32 and multiply by 5/9"
        elif to_unit == "Kelvin":
            return ((value - 32) * 5/9) + 273.15, "subtract 32, multiply by 5/9, then add 273.15"
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15, "subtract 273.15"
        elif to_unit == "Fahrenheit":
            return ((value - 273.15) * 9/5) + 32, "subtract 273.15, multiply by 9/5, then add 32"

# --- Page Setup ---
st.set_page_config("Unit Converter", layout="centered")
st.markdown("<h2 style='text-align:center;'>🔄 Google-style Unit Converter</h2>", unsafe_allow_html=True)
st.divider()

# --- Tabs ---
tabs = st.tabs(["📏 Length", "⚖️ Weight", "🌡 Temperature"])

# --- Length Tab ---
with tabs[0]:
    units = ["Metre", "Kilometre", "Centimetre", "Millimetre", "Inch", "Foot", "Yard", "Mile"]
    col1, col2 = st.columns(2)
    with col1:
        value = st.number_input("", value=1.0, label_visibility="collapsed")
        from_unit = st.selectbox("", units, index=0, label_visibility="collapsed")
    with col2:
        to_unit = st.selectbox("", units, index=2, label_visibility="collapsed")
        result, formula = convert_length(value, from_unit, to_unit)
        st.markdown(f"<div style='font-size: 32px; font-weight: bold; text-align:center;'>{round(result, 5)}</div>", unsafe_allow_html=True)
    st.markdown(f"<div style='background-color: #fff3cd; border-left: 6px solid #ffeeba; padding: 10px; border-radius: 5px;'><b>Formula</b>: {formula}</div>", unsafe_allow_html=True)

# --- Weight Tab ---
with tabs[1]:
    units = ["Gram", "Kilogram", "Milligram", "Pound", "Ounce"]
    col1, col2 = st.columns(2)
    with col1:
        value = st.number_input(" ", value=1.0, label_visibility="collapsed")
        from_unit = st.selectbox(" ", units, index=1, label_visibility="collapsed")
    with col2:
        to_unit = st.selectbox("  ", units, index=0, label_visibility="collapsed")
        result, formula = convert_weight(value, from_unit, to_unit)
        st.markdown(f"<div style='font-size: 32px; font-weight: bold; text-align:center;'>{round(result, 5)}</div>", unsafe_allow_html=True)
    st.markdown(f"<div style='background-color: #fff3cd; border-left: 6px solid #ffeeba; padding: 10px; border-radius: 5px;'><b>Formula</b>: {formula}</div>", unsafe_allow_html=True)

# --- Temperature Tab ---
with tabs[2]:
    units = ["Celsius", "Fahrenheit", "Kelvin"]
    col1, col2 = st.columns(2)
    with col1:
        value = st.number_input("  ", value=0.0, label_visibility="collapsed")
        from_unit = st.selectbox("   ", units, index=0, label_visibility="collapsed")
    with col2:
        to_unit = st.selectbox("    ", units, index=1, label_visibility="collapsed")
        result, formula = convert_temperature(value, from_unit, to_unit)
        st.markdown(f"<div style='font-size: 32px; font-weight: bold; text-align:center;'>{round(result, 2)}</div>", unsafe_allow_html=True)
    st.markdown(f"<div style='background-color: #fff3cd; border-left: 6px solid #ffeeba; padding: 10px; border-radius: 5px;'><b>Formula</b>: {formula}</div>", unsafe_allow_html=True)
