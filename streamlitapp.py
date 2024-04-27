import streamlit as st
from PIL import Image
import mouse 

# title 
st.title("FINAL YEAR PROJECT")
def run_virtual_mouse():
    global gc1
    gc1 = mouse.GestureController()
    gc1.start()

def close_program():
    if 'gc1' in globals():
        gc1.gc_mode = 0  # Stop gesture recognition
    st.stop()

#st.set_page_config(page_title="Gesture Recognition System", page_icon="LOGONEW.PNG")

# Load background image
bg_image = Image.open("aaaa (5).png")  # Replace "background_image.jpg" with the path to your image

# Display background image
st.image(bg_image, use_column_width=True)

# Create buttons
col1, col2 = st.columns(2)
with col1:
    start_button = st.button("START", key="start_button", help="Start gesture recognition", on_click=run_virtual_mouse)

with col2:
    close_button = st.button("CLOSE", key="close_button", help="Close the program", on_click=close_program)

# You can add more Streamlit components as needed

# This line is not necessary as Streamlit automatically runs the app
# st.run_app()
