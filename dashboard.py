import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Basic Elements
st.title("Dashboard Penjualan")
st.subheader("Laporan Penjualan Tahunan")
st.text("Dea Febianty Utama-240534001 Slamet Riyadi-240534002 Refdi Rahmandha-240534005")

# Data Dummy
data = pd.DataFrame({
    "Bulan": ["Januari", "Februari", "Maret", "April", "Mei", "Juni"],
    "Penjualan": [100, 150, 200, 250, 300, 350],
    "Keuntungan": [50, 70, 90, 110, 130, 150]
})

# Sidebar Widgets
st.sidebar.header("Pengaturan")
grafik = st.sidebar.selectbox("Pilih Grafik", ["Bar Chart", "Line Chart", "Pie Chart"])
filter_penjualan = st.sidebar.slider("Filter Penjualan Minimum", 0, 400, 100)
tampilkan_data = st.sidebar.checkbox("Tampilkan Data")

# Filter Data
filtered_data = data[data["Penjualan"] >= filter_penjualan]

# Basic Layout: Tampilkan Data
if tampilkan_data:
    st.write("### Data Penjualan")
    st.dataframe(filtered_data)

# Layout Columns for Charts
col1, col2 = st.columns(2)

# Grafik 1: Bar Chart
with col1:
    st.write("### Bar Chart Penjualan")
    fig, ax = plt.subplots()
    ax.bar(filtered_data["Bulan"], filtered_data["Penjualan"], color="blue")
    ax.set_title("Penjualan per Bulan")
    st.pyplot(fig)

# Grafik 2: Line Chart
with col2:
    st.write("### Line Chart Penjualan")
    fig, ax = plt.subplots()
    ax.plot(filtered_data["Bulan"], filtered_data["Penjualan"], marker='o', label="Penjualan", color="green")
    ax.plot(filtered_data["Bulan"], filtered_data["Keuntungan"], marker='o', label="Keuntungan", color="orange")
    ax.legend()
    st.pyplot(fig)

# Grafik 3: Pie Chart
st.write("### Komposisi Penjualan (Pie Chart)")
fig, ax = plt.subplots()
ax.pie(filtered_data["Penjualan"], labels=filtered_data["Bulan"], autopct="%1.1f%%", colors=sns.color_palette("pastel"))
st.pyplot(fig)
