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

# Input ekspresi matematika
expression = st.text_input(
    "Masukkan perhitungan panjang (contoh: 1000km + 200hm - 50dam * 2 / 5cm):",
    placeholder="Gunakan operator: +, -, *, /"
)

# Pilih unit hasil
result_unit = st.selectbox("Pilih unit hasil:", units)

# Proses perhitungan
if st.button("Hitung"):
    try:
        # Parsing ekspresi matematika
        import re
        tokens = re.findall(r"(\d+\.?\d*)([a-zA-Z]+)|([+\-*/])", expression)
        
        # Konversi semua nilai ke meter
        values_in_meters = []
        operators = []

        for token in tokens:
            if token[0]:  # Angka dengan unit
                value = float(token[0])
                unit = next((u for u in conversion_factors if u.startswith(token[1])), None)
                if unit:
                    values_in_meters.append(to_meters(value, unit))
                else:
                    st.error(f"Unit tidak dikenal: {token[1]}")
                    break
            elif token[2]:  # Operator matematika
                operators.append(token[2])

        # Lakukan perhitungan dalam meter
        result_in_meters = values_in_meters[0]
        for i, operator in enumerate(operators):
            if operator == "+":
                result_in_meters += values_in_meters[i + 1]
            elif operator == "-":
                result_in_meters -= values_in_meters[i + 1]
            elif operator == "*":
                result_in_meters *= values_in_meters[i + 1]
            elif operator == "/":
                if values_in_meters[i + 1] != 0:
                    result_in_meters /= values_in_meters[i + 1]
                else:
                    st.error("Tidak dapat membagi dengan nol.")
                    result_in_meters = None
                    break

        # Konversi hasil ke unit tujuan
        if result_in_meters is not None:
            result = from_meters(result_in_meters, result_unit)
            st.success(f"Hasil: {result} {result_unit}")
    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")
