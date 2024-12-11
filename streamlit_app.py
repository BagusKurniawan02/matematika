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

# Input jumlah perhitungan
total_calculations = st.number_input("Berapa kali perhitungan ingin dilakukan?", min_value=1, step=1, value=1)

values = []
units = []
operations = []

# Input untuk masing-masing perhitungan
for i in range(total_calculations):
    st.subheader(f"Perhitungan ke-{i+1}")
    value = st.number_input(f"Masukkan angka untuk perhitungan ke-{i+1}", min_value=0.0, step=0.1, key=f"value_{i}")
    unit = st.selectbox(f"Pilih unit untuk angka ke-{i+1}", units, key=f"unit_{i}")
    values.append((value, unit))

    if i < total_calculations - 1:
        operation = st.selectbox(f"Pilih operasi setelah angka ke-{i+1}", ["Tambah", "Kurang", "Kali", "Bagi"], key=f"operation_{i}")
        operations.append(operation)

# Pilih unit hasil
result_unit = st.selectbox("Pilih unit hasil:", units)

# Proses perhitungan
if st.button("Hitung"):
    # Konversi nilai ke meter
    converted_values = [to_meters(value, unit) for value, unit in values]

    # Lakukan perhitungan
    result_in_meters = converted_values[0]
    for i, operation in enumerate(operations):
        if operation == "Tambah":
            result_in_meters += converted_values[i + 1]
        elif operation == "Kurang":
            result_in_meters -= converted_values[i + 1]
        elif operation == "Kali":
            result_in_meters *= converted_values[i + 1]
        elif operation == "Bagi":
            if converted_values[i + 1] != 0:
                result_in_meters /= converted_values[i + 1]
            else:
                st.error("Tidak dapat membagi dengan nol.")
                result_in_meters = None
                break

    # Konversi hasil ke unit tujuan
    if result_in_meters is not None:
        result = from_meters(result_in_meters, result_unit)
        st.success(f"Hasil: {result} {result_unit}")
