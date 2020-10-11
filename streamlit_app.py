import streamlit as st
import joblib
import numpy as np
import pandas as pd
import sklearn

df = pd.read_csv('merged.csv')
st.title('Laptop Prices Predictor')

model = joblib.load('model1.pkl')

st.markdown( "## All the fields are mandatory.")
st.subheader('Laptop Details:')

company = st.selectbox("Company", options=df["Company"].unique())

def company_laptop(company):
    if company == "HP":
        return 6
    elif company == "Asus":
        return 3
    elif company == "Acer":
        return 0
    elif company == "Dell":
        return 5
    elif company == "Lenovo":
        return 7
    elif company == "MSI":
        return 8
    elif company == "Apple":
        return 2
    elif company == "Microsoft":
        return 10
    elif company == "MarQ":
        return 9
    elif company == "Avita":
        return 4
    elif company == "Alienware":
        return 1
    elif company == "Nexstgo":
        return 11

company_of_laptop = company_laptop(company)


processor_name = st.selectbox("Name of the Processor",options=df["Processor Name"].unique())


def pro_name(processor_name):
    if processor_name == "Intel":
        return 1
    elif processor_name == "AMD":
        return 0
    elif processor_name == "Microsoft":
        return 2

name_of_the_processor = pro_name(processor_name)


processor_type = st.selectbox("Type of the Processor(CPU)",options=df["Processor Type"].unique())


def pro_type(processor_type):
    if processor_type  == "i5":
        return 8
    elif processor_type == "Ryzen 5":
        return 4
    elif processor_type  == "i7":
        return 9
    elif processor_type  == "i3":
        return 7
    elif processor_type  == "Ryzen 7":
        return 5
    elif processor_type  == "Ryzen 3":
        return 3
    elif processor_type  == "SQ1":
        return 6
    elif processor_type  == "APU":
        return 0
    elif processor_type  == "Pentium":
        return 2
    elif processor_type  == "m3":
        return 11
    elif processor_type  == "i9":
        return 10
    elif processor_type  == "Athlon":
        return 1

type_of_the_processor = pro_type(processor_type)

generation = st.number_input('Generation', step=1, min_value=2)

ram_in_gb = st.number_input('RAM in GB', step=4, min_value=4)

ddr_version = st.number_input('DDR Version', step=1, min_value=3)

operating_system_type = st.selectbox("Operating System",options=df["Operating System Type"].unique())


def os_type(operating_system_type):
    if operating_system_type  == "Windows":
        return 3
    elif operating_system_type == "Mac":
        return 2
    elif operating_system_type  == "DOS":
        return 0
    elif operating_system_type  == "Linux":
        return 1

type_of_os = os_type(operating_system_type)

diskdrive_type = st.selectbox("Disk Drive",options=df["Disk Drive"].unique())


def disk_type(diskdrive_type):
    if diskdrive_type  == "SSD":
        return 2
    elif diskdrive_type == "HDD":
        return 1
    elif diskdrive_type  == "Both":
        return 0

type_of_diskdrive = disk_type(diskdrive_type)

size_in_inches = st.number_input('Size of the laptop in Inches', step=0.1, min_value=10.0)

graphic_card = st.radio("Graphic Card (0-No,1-Yes)", options=[0, 1])
touchscreen  = st.radio("Touchscreen (0-No,1-Yes)", options=[0, 1])

features=[company_of_laptop,name_of_the_processor,type_of_the_processor,generation,ram_in_gb,ddr_version,type_of_os,type_of_diskdrive, size_in_inches,graphic_card,touchscreen]
final_features = np.array(features).reshape(1, -1)

if st.button('Predict'):
    prediction = model.predict(final_features)
    st.balloons()
    #st.success(f'Your predicted price of the laptop is {round(prediction[0],3)}')
    st.success(f'Your predicted price of the laptop is {prediction[0]}')

