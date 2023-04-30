import streamlit as st
from PIL import Image, ImageOps, ImageFilter
import numpy as np

def img2sketch(photo, k_size):

    # Convert to Grayscale
    grey_img = photo.convert('L')

    # Invert Grayscale Image
    inv_img = ImageOps.invert(grey_img)

    # Apply Gaussian Blur
    blur_img = inv_img.filter(ImageFilter.GaussianBlur(radius=k_size))

    # Invert Blurred Image
    inv_blur_img = ImageOps.invert(blur_img)

    # Convert Image to NumPy Array
    img_array = np.array(inv_blur_img)

    sketch_array = np.array(grey_img).astype(float)
    invblur_array = np.array(inv_blur_img).astype(float)
    sketch_array /= invblur_array
    sketch_array *= 256
    sketch_array = np.clip(sketch_array, 0, 255).astype(np.uint8)
    sketch_img = Image.fromarray(sketch_array)
    
    return (sketch_img)


def main():
    st.title("Upload Image")

    file_up = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if file_up is not None:
        image = Image.open(file_up)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        img = img2sketch(image,7)
        st.image(img, caption='Sketch Image', use_column_width=True)

if __name__ == '__main__':
    main()
