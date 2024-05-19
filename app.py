import streamlit as st
from streamlit_login_auth_ui.widgets import __login__
import numpy as np
import urllib.request
from PIL import Image
import warnings
warnings.filterwarnings("ignore")


__login__obj = __login__(auth_token = "pk_test_2EKXYR8HSBM7TRJNXSG54G5GNFX8",
                    company_name = "Synthcheck",
                    width = 200, height = 250,
                    logout_button_name = 'Logout', hide_menu_bool = False,
                    hide_footer_bool = False,
                    lottie_url = 'https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json')

LOGGED_IN= __login__obj.build_login_ui()
username= __login__obj.get_username()

if LOGGED_IN == True:

    st.markdown("Your Streamlit Application Begins here!")
   #st.markdown(st.session_state)
    st.write('Welcome ',username)
    
    model = None


    @st.cache_resource
    def load_model():
        global model
        pass
       
    def classify_image(file_path):
        image = Image.open(file_path) # reading the image
        image = image.resize((32, 32)) 
        img = np.asarray(image) # converting it to numpy array
        img = np.expand_dims(img/255, 0)
        res = 'Try'
        
        return res
        
    st.write("Upload an image to check whether it is a fake or real image.")

    file_uploaded = st.file_uploader("Choose the Image File", type=["jpg", "png", "jpeg"])
    if file_uploaded is not None:
        res = classify_image(file_uploaded)
        c1, buff, c2 = st.columns([2, 0.5, 2])
        c1.image(file_uploaded, use_column_width=True)
        c2.subheader("Classification Result")
        c2.write("The image is classified as **{}**.".format(res.title()))
      
    st.button('Check', use_container_width=True) 
