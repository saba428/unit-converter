

import streamlit as st
from pint import UnitRegistry

# Title
st.title("🔄 Unit Converter")
st.write("Convert units easily between different categories like Length, Mass, and Temperature.")

# Create Unit Registry
ureg = UnitRegistry()

# Category-wise units
units = {
    "Length": ["meter", "kilometer", "mile", "inch", "foot", "centimeter"],
    "Mass": ["gram", "kilogram", "pound", "ounce"],
    "Temperature": ["celsius", "fahrenheit", "kelvin"]
}

# Sidebar for selection
category = st.selectbox("Select Category", list(units.keys()))
from_unit = st.selectbox("From Unit", units[category])
to_unit = st.selectbox("To Unit", units[category])
value = st.number_input("Enter Value", value=1.0)

# Conversion function
def convert(val, from_u, to_u):
    try:
        q = ureg.Quantity(val, from_u)
        res = q.to(to_u)
        return round(res.magnitude, 4)
    except Exception as e:
        return f"Error: {e}"

# Output
result = convert(value, from_unit, to_unit)
st.markdown("""f### Result **{value} {from_unit} {to_unt}""")