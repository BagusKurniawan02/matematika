import streamlit as st

# Judul aplikasi
st.title("Kalkulator Perhitungan dan Konversi Panjang")

# Pilihan unit
units = ["Kilometer (km)", "Hektometer (hm)", "Dekameter (dam)", "Meter (m)", "Desimeter (dm)", "Centimeter (cm)", "Milimeter (mm)"]

# Input nilai dan unit awal
value = st.number_input("Masukkan nilai panjang:", min_value=0.0, step=0.1)
from_unit = st.selectbox("Dari unit:", units)
to_unit = st.selectbox("Ke unit:", units)

# Faktor konversi (dalam meter)
conversion_factors = {
    "Kilometer (km)": 1000,
    "Hektometer (hm)": 100,
    "Dekameter (dam)": 10,
    "Meter (m)": 1,
    "Desimeter (dm)": 0.1,
    "Centimeter (cm)": 0.01,
    "Milimeter (mm)": 0.001,
}

# Pilih operasi matematika
operation = st.selectbox("Pilih operasi:", ["Konversi", "Penjumlahan", "Pengurangan", "Perkalian", "Pembagian"])

# Input nilai kedua jika bukan konversi
if operation != "Konversi":
    value2 = st.number_input("Masukkan nilai kedua:", min_value=0.0, step=0.1)

# Proses perhitungan
if st.button("Hitung"):
    if operation == "Konversi":
        if from_unit and to_unit:
            # Konversi ke meter
            value_in_meters = value * conversion_factors[from_unit]
            # Konversi dari meter ke unit tujuan
            converted_value = value_in_meters / conversion_factors[to_unit]
            st.success(f"{value} {from_unit} = {converted_value} {to_unit}")
        else:
            st.error("Silakan pilih unit awal dan unit tujuan.")
    elif operation == "Penjumlahan":
        result = value + value2
        st.success(f"Hasil Penjumlahan: {result}")
    elif operation == "Pengurangan":
        result = value - value2
        st.success(f"Hasil Pengurangan: {result}")
    elif operation == "Perkalian":
        result = value * value2
        st.success(f"Hasil Perkalian: {result}")
    elif operation == "Pembagian":
        if value2 != 0:
            result = value / value2
            st.success(f"Hasil Pembagian: {result}")
        else:
            st.error("Tidak dapat membagi dengan nol.")
