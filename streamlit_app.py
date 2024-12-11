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

# Input ekspresi matematika
expression = st.text_input("Masukkan ekspresi matematika panjang (contoh: 1000km + 1000cm * 200hm):")
to_unit = st.selectbox("Konversi hasil ke unit:", units)

# Fungsi untuk mengevaluasi ekspresi
import re

def evaluate_expression(expression, to_unit):
    # Ekstrak nilai dan unit dari ekspresi
    tokens = re.findall(r"(\d+\.?\d*)\s*([a-zA-Z]+)", expression)
    if not tokens:
        return "Ekspresi tidak valid"

    # Konversi semua nilai ke meter
    values_in_meters = []
    for value, unit in tokens:
        unit_full = next((u for u in conversion_factors if unit in u), None)
        if unit_full:
            values_in_meters.append(float(value) * conversion_factors[unit_full])
        else:
            return f"Unit tidak dikenal: {unit}"

    # Ganti nilai+unit dalam ekspresi dengan nilai dalam meter
    for (value, unit), value_in_meters in zip(tokens, values_in_meters):
        expression = expression.replace(f"{value}{unit}", str(value_in_meters))

    # Evaluasi ekspresi matematika dalam meter
    try:
        result_in_meters = eval(expression)
    except Exception as e:
        return f"Error dalam evaluasi: {e}"

    # Konversi hasil ke unit yang diminta
    result_in_target_unit = result_in_meters / conversion_factors[to_unit]
    return result_in_target_unit

# Proses perhitungan
if st.button("Hitung"):
    if expression and to_unit:
        result = evaluate_expression(expression, to_unit)
        if isinstance(result, str):
            st.error(result)
        else:
            st.success(f"Hasil: {result} {to_unit}")
    else:
        st.error("Silakan masukkan ekspresi dan pilih unit tujuan.")
