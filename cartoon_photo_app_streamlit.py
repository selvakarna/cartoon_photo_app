import streamlit as st
from PIL import Image, ImageFilter
import io

# Set up the page
st.set_page_config(page_title="Cartoon Photo Effect", layout="centered")

# App title and description
st.title("🎨 Cartoon Photo Effect Web App")
st.write("Upload a photo and apply a cartoon-style artistic effect to it.")

# Upload image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Load and display the uploaded image
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Original Photo", use_column_width=True)

    # When user clicks "Apply" button
    if st.button("Apply Cartoon Effect"):
        # Placeholder: apply basic artistic enhancement
        cartoon_image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
        cartoon_image = cartoon_image.filter(ImageFilter.DETAIL)

        # Show result
        st.image(cartoon_image, caption="Reworked Photo", use_column_width=True)

        # Prepare for download
        buf = io.BytesIO()
        cartoon_image.save(buf, format="JPEG")
        byte_data = buf.getvalue()

        # Download button
        st.download_button(
            label="📥 Download Reworked Image",
            data=byte_data,
            file_name="cartoonized_photo.jpg",
            mime="image/jpeg"
        )
