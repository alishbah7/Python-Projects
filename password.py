import streamlit as st
st.set_page_config(layout="wide", page_title="Password Strength Meter")
import re
from header import Header
Header()

def password_strength(password):
    score = 0
    feedback = []
    
    #--==== THIS WILL CHECK THE LENGTH OF THE PASSWORD ====--#
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Increase the length to at least 8 characters.")
    
    #--==== THIS WILL CHECK FOR UPPERCASE LETTER ====--#
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Include at least one uppercase letter.")
    
    #--==== THIS WILL CHECK FOR LOWERCASE LETTER ====--#
    if re.search(r"[a-z]", password): 
        score += 1
    else:
        feedback.append("Include at least one lowercase letter.")
    
    #--==== THIS WILL CHECK FOR INTERGERS ====--#
    if re.search(r"\d", password): # the regular expression "\d" is used to match integers from 0 to 9
        score += 1
    else:
        feedback.append("Include at least one integer.")
    
    #--==== THIS WILL CHECK FOR SPECIAL CHARACHTERS ====--#
    if re.search(r"[@$!%*?&]", password):
        score += 1
    else:
        feedback.append("Include at least one special character (@$!%*?&).")
    
    #--==== THIS WILL DETERMINE STRENGTH BASED ON SCORE ====--#
    if score <= 2: # if score is less than or equals 2 then the strength "weak" will be shown
        strength = "Weak"
        color = "#ff4d4d"
    elif score <= 4: # if score is less than or equals 4 then the strength "moderate" will be shown
        strength = "Moderate"
        color = "#ffcc00"
    else: # otherwise strength "strong" will be shown
        strength = "Strong"
        color = "#33cc33"
    
    return strength, color, feedback

def password_strength_meter():

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
            .label{
                color: white;
                margin-bottom: -20px !important
            }
            div[data-testid="stTextInput"] > div {
                margin-top: -20px !important;
                border: 2px solid  rgb(233, 193, 134) !important
            }
            .suggest{
                color: white    
            }
            .suggestHeading{
                color: rgb(233, 193, 134);
                font-size: 25px;
                margin-bottom: 5px;
                text-shadow: 0px 1px 20px rgb(233, 193, 134);
            }
            @media screen and (max-width: 640px){
                .title{
                    font-size: 30px;
                    letter-spacing: 0;
                    text-align: center
                }
            }
        </style>
    """
    ,unsafe_allow_html=True)

    st.markdown("<div class='title'>🔐 Password Strength Meter</div>", unsafe_allow_html=True)
    
    st.markdown("<div class='label'>Enter your password:</div>", unsafe_allow_html=True)
    password = st.text_input("", type="password")
    
    if password:
        strength, color, feedback = password_strength(password)
        
        st.markdown(f"<h3 style='color:white';>Strength: <span style='color:{color}'>{strength}</span></h3>", unsafe_allow_html=True)
        
        if feedback:
            st.write("<div class='suggestHeading'>Suggestions to improve your password:</div>", unsafe_allow_html=True)
            for suggestions in feedback:
                st.write(f"<div class='suggest'>- {suggestions}</div>", unsafe_allow_html=True)


password_strength_meter() 
