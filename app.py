import streamlit as st
import pandas as pd
from keras.models import load_model

# upload data
model = load_model('./bppn.h5')

st.title('Klasifikasi prediksi penyakit jantung menggunakan metode backpropagation')
st.write('Masukkan data pasien')

param_names = [
    'Age', 'Sex', 'Cp', 'Trestbps', 'Chol', 'Fbs', 'Restecg',
    'Thalach', 'Exang', 'Oldpeak', 'Slope', 'Ca', 'Thal'
]

Age = [29, 77]
Sex = [0, 1]
Cp = [0, 3]
Trestbps = [94, 200]
Chol = [126, 564]
Fbs = [0, 1]
Restecg = [0, 2]
Thalach = [71, 202]
Exang = [0, 1]
Oldpeak = [0, 6.2]
Slope = [0, 2]
Ca = [0, 4]
Thal = [0, 3]

param_values = []

def normalize(value, min, max):
    return (value - min) / (max - min)

# Membuat input form untuk setiap parameter
# for param_name in param_names:
#     param_val = st.number_input(f"Enter {param_name}:", min_value=eval(param_name)[0], max_value=eval(param_name)[1])
#     param_val = normalize(param_val, eval(param_name)[0], eval(param_name)[1])
#     param_values.append(param_val)
valueAge = st.number_input(f"Enter Age:", min_value=0, max_value=100);
valueAge = normalize(valueAge, Age[0], Age[1])
param_values.append(valueAge)

# Opsi untuk gender
gender_options = {'Male': 1, 'Female': 0}
days_list = ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5', 'Day 6']
# Dropdown untuk memilih gender
# set value male = 1 and female = 0
selected_gender = st.selectbox("Pilih Jenis Kelammin", ['Pria', 'Wanita'])
# selected_gender = st.selectbox(('Pilih Gender:'), ['Male', 'Female'])
# selected_day = st.selectbox(("Start the Challenge 👇"), days_list, key="day")


# valueSex = st.select_slider(f"Select Gender", )


# Membuat DataFrame dari nilai parameter
# input_data = pd.DataFrame([param_values], columns=param_names)

if st.button('Predict'):
    # Melakukan prediksi
    # prediction_result = model.predict(input_data)
    print(selected_gender)
    # Menampilkan hasil prediksi
    st.write("Prediction Results:" + str(selected_gender))
    # st.json({
    #     # 'No Heart Disease (Class 0)': prediction_result[0][0],
    #     'Heart Disease (Class 1)': prediction_result
    #     # Tambahkan kelas lain sesuai kebutuhan
    # })