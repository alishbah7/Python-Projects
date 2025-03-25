import streamlit as st

st.set_page_config(page_title="Unit Converter 🔃", layout="wide")

from header import Header
Header()


#--==== CSS ====--#
st.markdown("""
    <style>
        .title{
            color: white;
            text-shadow: 0px 1px 20px rgb(233, 193, 134);
            font-size: 45px;
            font-weight: 900;    
            letter-spacing: 2px;
            margin-bottom: 20px;
        }
        .typeSel{
            color: white;
            margin-bottom: -5px;
        }
        .convTitle{
            margin-top: 20px;
            font-size: 30px;
            color: white !important;
            text-shadow: 0px 1px 10px rgb(233, 193, 134);
        }
        span{
          color: rgb(233, 193, 134);
        } 
        div.stButton > button {
            background-color: rgb(216, 168, 94) !important; 
            color: white !important;  
            border-radius: 8px !important; 
            border: 2px solid white !important;
            padding: 10px 20px !important;
            font-size: 16px !important;
            font-weight: 900 !important;
            box-shadow: 0px 1px 10px rgb(233, 193, 134) !important;
            transition: background-color 0.3s ease-in-out !important;
        }
        div.stButton > button:hover {
            background-color: rgb(233, 193, 134) !important; 
        }
        label {
            color: white !important;
            font-size: 16px !important;
            font-weight: bold !important;
        }
        div[data-testid="stNumberInput"] button {
            background-color: transparent !important;
            border: 2px solid white !important;
            color: white !important;
            transition: background-color 0.3s ease-in-out !important;
        }
        .convValue{
            color: white;
            font-size: 25px;
            text-shadow: 0px 1px 10px rgb(233, 193, 134);
        }
        @media screen and (max-width: 640px){
            .title{
                font-size: 30px;
                letter-spacing: 0;
                text-align: center
            }
            .typeSel{
                text-align: center
            }    
            .convTitle{
                text-align: center
            }
            .convValue{
                font-size: 15px
            }
        }
    </style>
    """,
    unsafe_allow_html=True)
st.markdown("<div class='title'>Unit Converter</div>", unsafe_allow_html=True)


#--==== SESSION STATE ====--#
if "active_tab" not in st.session_state:
    st.session_state.active_tab = "Length"


#--==== FUNCTION TO SET ACTIVE TAB ====--#
def set_active_tab(tab_name):
    st.session_state.active_tab = tab_name


#--==== TABS FOR TYPES ====--#
tabs = ["Length", "Weight", "Temperature", "Speed"]


#--==== SUB TITLE ====--#
st.markdown("<p class='typeSel'>Select What You Want To Convert!</p>", unsafe_allow_html=True)


#--==== RENDERING BUTTONS ====--#
cols = st.columns(len(tabs), gap="small")  # Use 'small' gap for reduced spacing
for i, tab in enumerate(tabs):
    with cols[i]:
        if st.button(tab, use_container_width=True):  # Use container width for better button fit
            set_active_tab(tab)


#--==== CONVERT {TYPE} TITLE ====--#
st.markdown(f"<div class='convTitle'>Convert <span>{st.session_state.active_tab}</span></div>", unsafe_allow_html=True)


#--==== INPUT FOR VALUE ====--#
value = st.number_input("Enter Value", min_value=1.0, step=1.0,)


#--==== FUNCTION FOR LENGTH ====--#
def convert_length(value, from_unit, to_unit):
    units = {
        "meters": 1,
        "kilometers": 0.001,
        "miles": 0.000621371,
        "yards": 1.09361,
        "feet": 3.28084,
        "inches": 39.3701
    }
    return value * (units[to_unit] / units[from_unit])


#--==== FUNCTION FOR WEIGHT ====--#
def convert_weight(value, from_unit, to_unit):
    units = {
        "grams": 1,
        "kilograms": 0.001,
        "pounds": 0.00220462,
        "ounces": 0.035274
    }
    return value * (units[to_unit] / units[from_unit])


#--==== FUNCTION FOR TEMPERATURE ====--#
def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "Celsius":
        return (value * 9/5) + 32 if to_unit == "Fahrenheit" else value + 273.15
    elif from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else ((value - 32) * 5/9) + 273.15
    elif from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else ((value - 273.15) * 9/5) + 32


#--==== FUNCTION FOR SPEED ====--#
def convert_speed(value, from_unit, to_unit):
    units = {
        "m/s": 1,
        "km/h": 3.6,
        "mph": 2.23694,
        "knots": 1.94384
    }
    return value * (units[to_unit] / units[from_unit])


#--==== CONVERSIONS OPTIONS IF TAB IS LENGTH ====--#
if st.session_state.active_tab == "Length":
    from_unit = st.selectbox("From", ["meters", "kilometers", "miles", "yards", "feet", "inches"])
    to_unit = st.selectbox("To", ["meters", "kilometers", "miles", "yards", "feet", "inches"])
    result = convert_length(value, from_unit, to_unit)
    st.write(f"<div class='convValue'>Converted Value: <span>{result} {to_unit}</span></div>", unsafe_allow_html=True)


#--==== CONVERSIONS OPTIONS IF TAB IS WEIGHT ====--#
elif st.session_state.active_tab == "Weight":
    from_unit = st.selectbox("From", ["grams", "kilograms", "pounds", "ounces"])
    to_unit = st.selectbox("To", ["grams", "kilograms", "pounds", "ounces"])
    result = convert_weight(value, from_unit, to_unit)
    st.write(f"<div class='convValue'>Converted Value: <span>{result} {to_unit}</span></div>", unsafe_allow_html=True)


#--==== CONVERSIONS OPTIONS IF TAB IS TEMPERATURE ====--#
elif st.session_state.active_tab == "Temperature":
    from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])
    result = convert_temperature(value, from_unit, to_unit)
    st.write(f"<div class='convValue'>Converted Value: <span>{result} {to_unit}</span></div>", unsafe_allow_html=True)


#--==== CONVERSIONS OPTIONS IF TAB IS SPEED ====--#
elif st.session_state.active_tab == "Speed":
    from_unit = st.selectbox("From", ["m/s", "km/h", "mph", "knots"])
    to_unit = st.selectbox("To", ["m/s", "km/h", "mph", "knots"])
    result = convert_speed(value, from_unit, to_unit)
    st.write(f"<div class='convValue'>Converted Value: <span>{result} {to_unit}</span></div>", unsafe_allow_html=True)