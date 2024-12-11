import streamlit as st

# Judul aplikasi
st.title("Kalkulator Perhitungan dan Konversi Panjang")

# Pilihan unit
units = ["Kilometer (km)", "Hektometer (hm)", "Dekameter (dam)", "Meter (m)", "Desimeter (dm)", "Centimeter (cm)", "Milimeter (mm)"]

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

# Fungsi konversi ke meter
def to_meters(value, unit):
    return value * conversion_factors[unit]

# Fungsi konversi dari meter
def from_meters(value_in_meters, unit):
    return value_in_meters / conversion_factors[unit]

# Input nilai pertama
value1 = st.number_input("Masukkan angka pertama:", min_value=0.0, step=0.1)
unit1 = st.selectbox("Pilih unit pertama:", units)

# Pilih operasi matematika
operation = st.selectbox("Pilih operasi:", ["Tambah", "Kurang", "Kali", "Bagi"])

# Input nilai kedua
value2 = st.number_input("Masukkan angka kedua:", min_value=0.0, step=0.1)
unit2 = st.selectbox("Pilih unit kedua:", units)

# Pilih unit hasil
result_unit = st.selectbox("Pilih unit hasil:", units)

# Proses perhitungan
if st.button("Hitung"):
    # Konversi nilai ke meter
    value1_in_meters = to_meters(value1, unit1)
    value2_in_meters = to_meters(value2, unit2)

    # Lakukan operasi matematika
    if operation == "Tambah":
        result_in_meters = value1_in_meters + value2_in_meters
    elif operation == "Kurang":
        result_in_meters = value1_in_meters - value2_in_meters
    elif operation == "Kali":
        result_in_meters = value1_in_meters * value2_in_meters
    elif operation == "Bagi":
        if value2_in_meters != 0:
            result_in_meters = value1_in_meters / value2_in_meters
        else:
            st.error("Tidak dapat membagi dengan nol.")
            result_in_meters = None

    # Konversi hasil ke unit tujuan
    if result_in_meters is not None:
        result = from_meters(result_in_meters, result_unit)
        st.success(f"Hasil: {result} {result_unit}")
