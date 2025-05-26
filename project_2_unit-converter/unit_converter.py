import streamlit as st 

def unit_converter(value, unit_from, unit_to):
    conversions = {
        "meter_kilometer" : 0.001,
        "kilometer_meter" : 1000,
        "gram_kilogram" : 0.001,
        "kilogram_gram" : 1000,  
        "hour_mintue" : 60,
        "mintue_hour" : 0.01667,
        "hour_second" : 3600,
        "second_hour" : 0.0000277,

 }
    
    key = f"{unit_from}_{unit_to}"

    if key in conversions :
        conversion = conversions[key]
        return value * conversion
    
    else:
        return "conversion not found"
    
st.title("Unit Converter")    
st.write("To convert value from one unit to another unit")

value = st.number_input("Enter the input value: " , )
unit_from = st.selectbox("Convert from:" ,["meter", "kilometer", "gram", "kilogram", "hour", "mintue", "second"])
unit_to = st.selectbox("Convert to:" ,["meter", "kilometer", "gram", "kilogram","hour","mintue", "second"])

if st.button("Convert"):
    result = unit_converter(value, unit_from, unit_to)
    st.write(f"Converted value : {result}")
 
