import streamlit as st
import cv2
import base64
from PIL import Image
import numpy as np

def img2sketch(img, k_size):

    # Convert to Grey Image
    grey_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Invert Image
    invert_img=cv2.bitwise_not(grey_img)

    # Blur image
    blur_img=cv2.GaussianBlur(invert_img, (k_size,k_size),0)

    # Invert Blurred Image
    invblur_img=cv2.bitwise_not(blur_img)

    # Sketch Image
    sketch_img=cv2.divide(grey_img,invblur_img, scale=256.0)

    # Save Sketch 
    return sketch_img

def process_image(image):
    image = np.array(image.convert('RGB'))
    image = cv2.cvtColor(image, 1)
    image= img2sketch(image, 7)
    return image

def main():
    st.title("Upload Image")

    file_up = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if file_up is not None:
        image = Image.open(file_up)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        img = process_image(image)
        st.image(img, caption='Sketch Image', use_column_width=True)

if __name__ == '__main__':
    main()
