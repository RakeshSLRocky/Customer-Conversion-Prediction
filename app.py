import pickle
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
import webbrowser

from PIL import Image

data=pd.read_csv("data_for_streamlit.csv")

pickle_in = open("predictor.pkl","rb")
classifier=pickle.load(pickle_in)
st.set_page_config(page_title='Customer Conversion Prediction', page_icon = 'health-insurance.jpg', layout='wide')
st.title(':white[Customer Conversion Prediction]')
# page_bg_img = """
# <style>
# [data-testid="stAppViewContainer"] {
# background-image: url("https://t4.ftcdn.net/jpg/03/93/13/67/360_F_393136704_Z0J0qqjYvfFwYyQ4mvZIkwxl2Z8BeYs4.jpg");
# background-size: cover;
# }
#
# </style>
# """

# st.markdown(page_bg_img, unsafe_allow_html=True)
def main():
    # Create a page dropdown
    image = Image.open('health-insurance.jpg')
    # st.sidebar.image(image,width=100)
    # st.sidebar.title("Menu")
    # col1, col2 = st.columns(2)
    # with col1:
    # st.title("Customer Conversion Prediction")
    # with col2:
    #    st.image(image,  width=150)
    # page = st.sidebar.selectbox("Select", ['ABOUT',"PREDICTION"])
    page = option_menu(menu_title='',options = ['ABOUT', 'PREDICTION', 'CONTACT'], orientation='horizontal', icons = ['house','graph-up-arrow', 'phone'], styles={"container": {"padding": "0!important", "background-color": "#0E1117","size":"cover"} })
    if page == "ABOUT":
        # st.title('Welcome to Insurance Prediction')
        col1, col2 = st.columns(2)
        with col1:
            st.header('About')
            st.write('This App helps find the customers to reachout to sell term insurance through telephonic marketing campaigns.'
                     'Telephonic campaigns still remain one of the most effective way to reach out to people however they incur a lot of cost.'
                     ' Hence, it is important to identify the customers that are most likely to convert beforehand so that they can be specifically targeted via call.')
            # st.write('#')

            st.write('Built a Machine Learning model that will predict if a client will subscribe to the insurance or not')
            st.write('Using the historical marketing data of the insurance company')


            st.write('Historic data of company is available here')
            url = 'https://drive.google.com/file/d/1BJ_Q8Q-kDRisAQyLltBQggeb0QmdWGZy/view?usp=sharing'

            if st.button('Historic data'):
                webbrowser.open_new_tab(url)

        with col2:
            image = "https://img.freepik.com/premium-photo/young-man-holding-phone-with-insurance-icon_218381-5216.jpg"
            st.image(image)


    if page == "PREDICTION":
        st.header('Enter the details to get the prediction')
        # st.write("Select the Age of the person")
        col1, col2 = st.columns(2)
        with col1 :
            age = st.slider("Select the Age",int(data.age.min()),int(data.age.max()))
            job = st.selectbox("Select the Occupation ",data.job.unique())
            if job == 'blue-collar':
                grouped=data[data['job']=='blue-collar']
                job = 0
            elif job == 'entrepreneur':
                grouped=data[data['job']=='entrepreneur']
                job = 1
            elif job == 'housemaid':
                grouped=data[data['job']=='housemaid']
                job = 2
            elif job == 'services':
                grouped=data[data['job']=='services']
                job = 3
            elif job == 'technician':
                grouped=data[data['job']=='technician']
                job = 4
            # elif job == 'technician':
            #     grouped=data[data['job']=='unknown']
            #     job = 5
            elif job == 'self-employed':
                grouped=data[data['job']=='self-employed']
                job = 5
            elif job == 'admin.':
                grouped=data[data['job']=='admin.']
                job=6
            elif job == 'management':
                grouped=data[data['job']=='management']
                job=7
            elif job == 'unemployed':
                grouped=data[data['job']=='unemployed']
                job=8
            elif job == 'retired':
                grouped=data[data['job']=='retired']
                job=9
            elif job == 'student':
                grouped=data[data['job']=='student']
                job=10
        
            education_qual = st.selectbox("Select the Education qualification ",data.education_qual.unique())
            if education_qual == 'primary':
                grouped=data[data['education_qual']=='primary']
                education_qual = 0
            elif education_qual == 'secondary':
                grouped=data[data['education_qual']=='secondary']
                education_qual=1
            # elif education_qual == 'unknown':
            #     grouped=data[data['education_qual']=='unknown']
            #     education_qual=2
            elif education_qual == 'tertiary':
                grouped=data[data['education_qual']=='tertiary']
                education_qual=2

            call_type = st.selectbox("Select the Call type ",data.call_type.unique())
            if call_type == 'unknown':
                grouped=data[data['call_type']=='unknown']
                call_type = 0
            elif call_type == 'telephone':
                grouped=data[data['call_type']=='telephone']
                call_type=1
            elif call_type == 'cellular':
                grouped=data[data['call_type']=='cellular']
                call_type=2

            day = st.slider("Select the day ",int(data.day.min()),int(data.day.max()))
            # st.write('**from 0 to 11 is jan to dec')
        with col2 :
            dur = st.slider("Select the Call duration ", int(data.dur.min()), int(data.dur.max()))
            mon = st.selectbox("Select the month",data.mon.unique())
            if mon == 'may':
                grouped=data[data['mon']=='may']
                mon = 0
            elif mon == 'jul':
                grouped = data[data['mon'] == 'jul']
                mon = 1
            elif mon == 'jan':
                grouped = data[data['mon'] == 'jan']
                mon =2
            elif mon == 'nov':
                grouped = data[data['mon'] == 'nov']
                mon =3
            elif mon == 'jun':
                grouped = data[data['mon'] == 'jun']
                mon =4
            elif mon == 'aug':
                grouped = data[data['mon'] == 'aug']
                mon =5
            elif mon == 'feb':
                grouped = data[data['mon'] == 'feb']
                mon =6
            elif mon == 'apr':
                grouped = data[data['mon'] == 'apr']
                mon =7
            elif mon == 'oct':
                grouped = data[data['mon'] == 'oct']
                mon =8
            elif mon == 'sep':
                grouped = data[data['mon'] == 'sep']
                mon =9
            elif mon == 'dec':
                grouped = data[data['mon'] == 'dec']
                mon =10
            elif mon == 'mar':
                grouped = data[data['mon'] == 'mar']
                mon =11




    #         marital = st.selectbox("Select the Marital status ",data.marital.unique())
    #         if marital == 'married':
    #             grouped = data[data['marital'] == 'married']
    #             marital = 0
    #         elif marital == 'divorced':
    #             grouped = data[data['marital'] == 'divoreced']
    #             marital = 1
    #         elif marital == 'single':
    #             grouped = data[data['marital'] == 'single']
    #             marital = 2
            marital = st.selectbox("Select the Marital status ",data.marital.unique())
            if marital == 'divorced':
                marital_divorced = 1
            else:
                marital_divorced = 0

            if marital == 'married':
                marital_married = 1
            else:
                marital_married = 0

            if marital == 'single':
                marital_single = 1
            else:
                marital_single = 0


            prev_outcome = st.selectbox("Select the Previous Outcome ",data.prev_outcome.unique())
            if prev_outcome == 'failure':
                prev_outcome_failure=1
            else:
                prev_outcome_failure=0

            if prev_outcome == 'other':
                prev_outcome_other=1
            else:
                prev_outcome_other=0

            if prev_outcome == 'success':
                prev_outcome_success=1
            else:
                prev_outcome_success=0

            if prev_outcome == 'unknown':
                prev_outcome_unknown=1
            else:
                prev_outcome_unknown=0

    #         prev_outcome = st.selectbox("Select the Previous Outcome ",data.prev_outcome.unique())
    #         if prev_outcome == 'unknown ':
    #             grouped = data[data['prev_outcome'] == 'unkown']
    #             prev_outcome = 0
    #         elif prev_outcome == 'failure':
    #             grouped = data[data['prev_outcome'] == 'failure']
    #             prev_outcome = 1
    #         elif prev_outcome == 'other':
    #             grouped = data[data['prev_outcome'] == 'other']
    #             prev_outcome = 2
    #         elif prev_outcome == 'success':
    #             grouped = data[data['prev_outcome'] == 'success']
    #             prev_outcome = 3
            num_calls = st.slider("Select the Number of calls made to customer ", int(data.num_calls.min()),
                                  int(data.num_calls.max()))

        input = pd.DataFrame([[age,job,education_qual, call_type, day, mon, dur,num_calls, marital_divorced,marital_married,marital_single,prev_outcome_failure,prev_outcome_other,prev_outcome_success,prev_outcome_unknown]])


        if st.button("Predict"):
            valu = classifier.predict(input)
            if valu==0:
                st.write('DECLINED')
            else:
                col1, col2 = st.columns(2)
                with col1:
                    st.write('ACCEPTED')
                with col2:
                    # """### gif from url"""
                    st.markdown("![Alt Text](https://media.tenor.com/Hw7f-4l0zgEAAAAC/check-green.gif)")
                    st.snow()

    if page == "CONTACT":
        col1, col2, col3 = st.columns([0.1,0.3,0.8])
        with col2:
            st.write('I am Rakesh S L, a data science enthusiast')
            st.write('Please reach out me @')
            st.write('Phone number : +91-9035584074')
            st.write('Email id : rakeshslrocky@gmail.com')
            st.write("##")
            st.write('Follow me on')
            Facebook = "https://www.facebook.com/rakesh.slrocky/"
            Instagram = "https://www.instagram.com/rocky.slr/"
            Github = "https://github.com/RakeshSLRocky"

            col4, col5, col6 = st.columns([0.15,0.16,0.18])
            with col4:
                if st.button('Github'):
                    webbrowser.open_new_tab(Github)

            with col5:
                if st.button('Facebook'):
                    webbrowser.open_new_tab(Facebook)
            with col6:
                if st.button('Instagram'):
                    webbrowser.open_new_tab(Instagram)







if __name__=='__main__':
    main()
