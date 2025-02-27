import streamlit as st

# Conversion functions
def convert_length(value, from_unit, to_unit):
    length_units = {
        "Meters": 1, "Kilometers": 1000, "Miles": 1609.34,
        "Feet": 0.3048, "Inches": 0.0254
    }
    return value * (length_units[to_unit] / length_units[from_unit])

def convert_weight(value, from_unit, to_unit):
    weight_units = {
        "Kilograms": 1, "Grams": 0.001, "Pounds": 0.453592,
        "Ounces": 0.0283495
    }
    return value * (weight_units[to_unit] / weight_units[from_unit])

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius":
        return value if to_unit == "Celsius" else (value * 9/5 + 32 if to_unit == "Fahrenheit" else value + 273.15)
    if from_unit == "Fahrenheit":
        return value if to_unit == "Fahrenheit" else ((value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15)
    if from_unit == "Kelvin":
        return value if to_unit == "Kelvin" else (value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32)

# Streamlit UI
st.title("🌟 Unit Converter Web App")
st.sidebar.header("Choose Conversion Type")
conversion_type = st.sidebar.selectbox("Select a category", ["Length", "Weight", "Temperature"])

# Set unit options
units = {
    "Length": ["Meters", "Kilometers", "Miles", "Feet", "Inches"],
    "Weight": ["Kilograms", "Grams", "Pounds", "Ounces"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"]
}

from_unit = st.selectbox("Convert from:", units[conversion_type])
to_unit = st.selectbox("Convert to:", units[conversion_type])
value = st.number_input("Enter value:", min_value=0.0, format="%.2f")

if st.button("Convert"):
    if conversion_type == "Length":
        result = convert_length(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = convert_weight(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = convert_temperature(value, from_unit, to_unit)
    
    st.success(f"✅ Result: {result:.2f} {to_unit}")

st.markdown("---")
st.markdown("💡 **Created using Streamlit ❤️**")
