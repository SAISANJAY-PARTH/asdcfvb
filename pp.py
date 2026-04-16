import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Heart Curve", page_icon="❤️", layout="centered")

st.title("❤️ love you butkuuu")
st.write("heheheheheheee aata kal puppi dunga")

# Sidebar controls
st.sidebar.header("Customization")
color = st.sidebar.color_picker("Heart Color", "#ff004f")
line_width = st.sidebar.slider("Outline Width", 1, 8, 3)
fill_alpha = st.sidebar.slider("Fill Intensity", 0.0, 1.0, 0.25)

# Higher resolution grid for smoother curve
x = np.linspace(-2, 2, 1200)
y = np.linspace(-2, 2, 1200)
X, Y = np.meshgrid(x, y)

# Classic smooth heart implicit function (more stable visually)
Z = (X**2 + Y**2 - 1)**3 - X**2 * Y**3

fig, ax = plt.subplots(figsize=(6, 6))

# Fill heart region (improves aesthetics)
ax.contourf(X, Y, Z, levels=[-10, 0], colors=[color], alpha=fill_alpha)

# Crisp boundary
ax.contour(X, Y, Z, levels=[0], colors=color, linewidths=line_width, antialiased=True)

ax.set_aspect("equal")
ax.axis("off")

st.pyplot(fig)

st.success("❤️")