import streamlit as st
import qrcode
from io import BytesIO

st.set_page_config(page_title="QR Code Generator", page_icon="@")

st.title(" QR Code Generator")
st.write("Enter a URL or text below to generate a QR code instantly.")

# --- User Inputs ---
# 1. Input the URL
url = st.text_input("Enter the URL or Text:", placeholder="https://www.google.com")

# 2. Pick Colors (Optional feature for better UX)
col1, col2 = st.columns(2)
with col1:
    fill_color = st.color_picker("Pick the QR Color", "#000000")
with col2:
    back_color = st.color_picker("Pick the Background", "#FFFFFF")

# --- Generation Logic ---
if st.button("Generate QR Code"):
    if url:
        # Create the QR Code object
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)

        # Create the image with user-selected colors
        img = qr.make_image(fill_color=fill_color, back_color=back_color)

        # --- The Important Part: Memory Buffer ---
        # Instead of saving to a file like "img.png", we save to a memory buffer
        # This prevents creating junk files on your server/computer
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        
        # Display the image
        st.image(buffer, caption="Your QR Code")

        # Create a download button
        st.download_button(
            label="Download QR Code",
            data=buffer.getvalue(),
            file_name="my_qr_code.png",
            mime="image/png"
        )
    else:

        st.warning("Please enter some text or a URL first.")
