import streamlit as st
from streamlit_login_auth_ui.widgets import __login__
import numpy as np
import urllib.request
import tensorflow as tf
# from tensorflow.keras.models import load_model
from PIL import Image
import requests
import os
import warnings
warnings.filterwarnings("ignore")


__login__obj = __login__(auth_token = "pk_prod_T7HPXECPJ74CNHGT9T30W621JGWQ",
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

# GitHub URL of your model file (replace with your actual URL)
    github_model_url = "https://raw.githubusercontent.com/ShreyashSomvanshi/test_synthcheck/main/firstModel.h5"
    
    
    # Download the model file
    @st.cache_resource
    def load_model(github_model_url):
            
        response = requests.get(github_model_url)
        with open("firstModel.h5", "wb") as f:
            f.write(response.content)
        
        # Load the model using TensorFlow
        
        model = tf.keras.models.load_model("firstModel.h5")
        return model
    
    model = load_model(github_model_url)
    
    def classify_image(file_path):
        # model = load_model('firstModel.h5')
        image = Image.open(file_path) # reading the image
        image = image.resize((32, 32)) # resizing the image to fit the trained model   
        img = np.asarray(image) # converting it to numpy array
        img = np.expand_dims(img/255, 0)
        predictions = model.predict(img) # predicting the label
        if predictions > 0.5:
            res = 'REAL'
        else:
            res = 'SYNTHETIC'
        return res
    
        
        
    st.write("Upload an image to check whether it is a fake or real image.")
    
    file_uploaded = st.file_uploader("Choose the Image File", type=["jpg", "jpeg"])
    
    #Notice: By accessing our website, users acknowledge and accept full responsibility for their activities conducted within the platform. We prioritize your privacy and do not retain or distribute any images you upload
    
    if st.button('Check', use_container_width=True):
        if file_uploaded is not None:
            st.toast("Please note that results may not always be accurate. We prioritize your privacy and do not store or distribute any images you upload.",icon="⚠️")
            res = classify_image(file_uploaded)
            c1, buff, c2 = st.columns([2, 0.5, 2])
            c1.image(file_uploaded, use_column_width=True)
            c2.subheader("Classification Result")
            c2.write("The image is classified as **{}**.".format(res.title()))
        else:
            st.error('Please upload an image to verify.', icon="❌")





  
    
    # model = None


    # # @st.cache_resource
    # def load_model():
    #     global model
    #     pass
       
    # def classify_image(file_path):
    #     image = Image.open(file_path) # reading the image
    #     image = image.resize((32, 32)) 
    #     img = np.asarray(image) # converting it to numpy array
    #     img = np.expand_dims(img/255, 0)
    #     res = 'Try'
        
    #     return res
        
    # st.write("Upload an image to check whether it is a fake or real image.")

    # file_uploaded = st.file_uploader("Choose the Image File", type=["jpg", "png", "jpeg"])
    # if file_uploaded is not None:
    #     res = classify_image(file_uploaded)
    #     c1, buff, c2 = st.columns([2, 0.5, 2])
    #     c1.image(file_uploaded, use_column_width=True)
    #     c2.subheader("Classification Result")
    #     c2.write("The image is classified as **{}**.".format(res.title()))
      
    # st.button('Check') 
