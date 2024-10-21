import streamlit as st
import matplotlib as plt
import pandas as pd
from streamlit_lottie import st_lottie
import requests
import base64


st.set_page_config(page_title='Jathan Torres Resume', page_icon=":pencil:", layout='wide', initial_sidebar_state="collapsed")

profile_photo = ('/Users/jathantorres/Movies/AUDIO SURVIVOR APPLICATION VIDEO/Photo of Jathan Torres.jpg')
uchicago_logo = ('/Users/jathantorres/Downloads/uchicago_logo.webp')
def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_animation = load_lottie('https://lottie.host/9881288e-8f85-467e-aaff-4e964e6031a1/PIM85NWPNw.json')


text =  ('''
        ## :violet[Digital Resume]
        # :blue-background[Jathan Torres]
        I graduated from the :red-background[University of Chicago] in the summer of 2023 with a B.A. in :green[Economics] and I'm extremely
        grateful for my experience. Now for the past year and a half I have been working at a marketing agency (MERGE)
        as an Associate Media Accounting Analyst.
        While I am grateful for my experience with MERGE I am looking to take the next
        step in my career as I am always eager to learn through challenging myself.
        
         ## :blue[Professional Ambition]
        I am seeking a role where I can utilize my high-level problem solving and communication skills, that 
        I harnessed in my time at university. But not only that I want to continue to utilize and enhance
        my technical skills that I am and have been developing throughout my career.
        
        I aim to utilize my skills in economic strategic thinking combined with
        my invaluable technical skills in order to be a productive addition to any team.
        
        ## :blue[Key Academic Experience]
        At the University of Chicago I learned from the rigourous coursework the crucial skills
        that I have continued to hone throughout the start of my professional career.  
        I have become an excellent communicator and team-player as I understand the importance of cooperation.  
        Without cooperation, the scale at which any one individual can have an impact is greatly reduced.
        
        ### :blue[Relevant Coursework]
        - **Operational Management**
        - **Managing in Organizations**
        - **Financial Accounting**
        - **Marketing Management**
        - **Fundamentals of Psychology**
        
        ### :blue[Takeaways]
        With my academic and personal experience I have learned the importance of understanding the perspective of  
        your target audience. By being able to understand how different biases affect your decisions then you  
        are best suited to understand what is needed in any given moment to make the best decisions.

        ### :blue[Technical Skills]
        I aim to be able to have technical expertise that allows for a greatly improved to help business
        make great strategic decisions.
        - **SQL**
            - I even have experience using Python to seamlessly automate the process  
                of inserting and querying data within SQL.
        - **Python**
            - This site was built all within Python using various modules such as  
                Pandas, Streamlit, Matplotlib, etc.
        - **Excel**
            - Experience with Formulas and Pivot Tables. 
            - Experience using openpyxl python module to automate the process of working  
            within Excel
        - **Data Visualization Tools (such as Streamlit which powers this site)**
        - **Meta Ads Manager**
        - **Power BI**
        
''')


def image_rounder(photo_path):
    with open(profile_photo, 'rb') as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    html = f"""
        <div style="text-align:center;">
            <img src="data:image/jpg;base64, {encoded_string}" 
                style="border-radius: 45px; width: 450px;"/>
        </div>
            """
    return st.markdown(html, unsafe_allow_html=True)

col1, col2 = st.columns([2,1])
# with st.container():
#     with col1:
#         st.subheader("My name is Jathan Torres is my Interactive Career Journery")
#         # st.write("[Listen Now>]()")

# st.markdown("*Streamlit* is **really** ***cool***.")
# st.markdown('''
#     :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
#     :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.''')
# st.markdown("Here's a bouquet &mdash;\
#             :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")
#
# multi = '''If you end a line with two spaces,
# a soft return is used for the next line.
#
# Two (or more) newline characters in a row will result in a hard return.
# '''
# st.markdown(multi)
with st.container():
    with col1:
        st.markdown(text)
with col2:
    # st.image(uchicago_logo, use_column_width=True)
    st.markdown('<br><br><br><br>', unsafe_allow_html=True)
    image_rounder(profile_photo)
    st.markdown('<br><br><br><br>', unsafe_allow_html=True)
    st.divider()
    st.markdown('<br><br><br>', unsafe_allow_html=True)
    st_lottie(lottie_animation, width=350, key='coding')
#
# st.markdown("# This is a Heading 1")
# st.markdown("## This is a Heading 2")
# st.markdown("### This is a Heading 3")

# st.image('/Users/jathantorres/Movies/AUDIO SURVIVOR APPLICATION VIDEO/Photo of Jathan Torres.jpg', width=350)
