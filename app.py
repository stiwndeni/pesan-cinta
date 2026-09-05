import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

st.set_page_config(page_title="Pesan Cinta", page_icon="💖")
st.title("Kartu Ucapan Spesial 💖")

# Input interaktif untuk pengunjung web
pesan = st.text_input("Tulis pesanmu di sini:", "I Love You ❤️")

# Kalkulasi Grafik Hati
t = np.linspace(0, 2 * np.pi, 1000)
x = 16 * np.sin(t) ** 3
y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

# Menggambar Grafik
fig, ax = plt.subplots(figsize=(6, 6))
ax.plot(x, y, color="#e63946", linewidth=3)
ax.fill(x, y, color="#ffccd5")
ax.text(
    0,
    0,
    pesan,
    fontsize=18,
    fontweight="bold",
    color="#d62828",
    ha="center",
    va="center",
)
ax.axis("equal")
ax.axis("off")

# Menampilkan di web
st.pyplot(fig)