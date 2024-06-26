from streamlit_login_auth_ui.widgets import __login__

import warnings
warnings.filterwarnings("ignore")


__login__obj = __login__(auth_token = "pk_test_2EKXYR8HSBM7TRJNXSG54G5GNFX8", 
                    company_name = "Shims",
                    width = 200, height = 250, 
                    logout_button_name = 'Logout', hide_menu_bool = False, 
                    hide_footer_bool = False, 
                    lottie_url = 'https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json')

LOGGED_IN = __login__obj.build_login_ui()

if LOGGED_IN == True:

    st.markown("Your Streamlit Application Begins here!")
