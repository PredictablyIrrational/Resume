import streamlit as st
import matplotlib as plt
import pandas as pd
from streamlit_lottie import st_lottie
import requests
import base64
from pathlib import Path
from PIL import Image


# FUNCTIONS

def image_rounder(photo_path):
    with open(profile_photo, 'rb') as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    html = f"""
        <div style="text-align:center;">
            <img src="data:image/jpg;base64, {encoded_string}"
                style="border-radius: 45px; width: 200px;"/>
        </div>
            """
    return st.markdown(html, unsafe_allow_html=True)


# ______PATH_SETTINGS_______
current_dir = Path(__file__).parent
css_file = current_dir / "styles" / 'main.css'
resume_file = current_dir / 'assets' / 'Jathan Torres Resume October 2024.pdf'
profile_photo = current_dir / 'assets' / 'Photo of Jathan Torres.jpg'
print(current_dir)

#________GENERAL_VARIABLES______
page_title = 'Jathan Torres'
page_icon = ':wave:'
name = 'Jathan Torres'
email_address = 'jathantorres@gmail.com'
description = '''
B.A. in Economics from the University of Chicago  
Associate Media Accounting Analyst
'''
links = {
    "LinkedIn": "https://www.linkedin.com/in/jathan-torres-5a27571a1/"
}

st.set_page_config(page_title=page_title, page_icon=page_icon, layout='wide', initial_sidebar_state="collapsed")


# HEADER SECTION
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, 'rb') as pdf_file:
    pdf_bytes = pdf_file.read()

# profile_image = image_rounder(profile_photo)

# profile_photo = image_rounder(profile_photo)
# # profile_image = Image.open(profile_photo)
# profile_image = Image.frombytes(profile_photo)
with st.container():
    col1, col2 = st.columns(2, gap='small')
    with col1:
        image_rounder(profile_photo)
    with col2:
        st.title(page_title)
        st.write(description)
        st.download_button(
            label='📄 Download CSV',
            data=pdf_bytes,
            file_name=resume_file.name,
            mime='application/octet-stream'
        )
        st.write('✉️', email_address)
        st.link_button(label='LinkedIn Profile', url='https://www.linkedin.com/in/jathan-torres-5a27571a1/')


with st.container():
    st.header('Experience and Qualifications')
    st.markdown('''
        - ✅  B.A. in Economics from a top university, The University of Chicago
        - ✅  5+ years work experience
        - ✅  Strong understanding of economic micro and macro economic processes
        such as global economic forces on inflation and interest rates
        - ✅  Extensive experience communicating between external and internal departments  in order to ensure efficient 
        project completion
        - ✅ Hands on experience within SQL, Python, and Excel
        - ✅ Experience using APIs and JSON data
        - ✅ Understanding of Data Analysis practices, including data insertion and visualization
    ''')
with st.container():
    st.header('Hard Skills')
    st.markdown('''
        - Programming: Python (Pandas, Numpy, Matplotlib), SQL, JSON, APIs, GitHub
        - Ad Centers: Meta Ads Manager, Google Analytics
        - AI: Understanding of how to use and proof AI tools such as ChatGPT 
        - Microsoft Suite: Excel, Powerpoint, Word
        - Google Suite: Sheets, Docs, Slides
    ''')

with st.container():
    st.header('Work Experience')
    st.divider()
    with st.container():
        st.write('🖥️', 'Associate Media Accounting Analyst | MERGE (Marketing Agency)')
        st.write('06/2023 - Present')
        st.markdown('''
            - Facilitated the reception, entry, and transfer of media accounts payable invoices from vendors into Strata and Advantage.
            - Communicated frequently with various internal departments to manage incoming invoices and go over monthly spending by those departments
            - Requested payment information from vendor representatives and ensured a secure exchange of sensitive information
            - Managed the request and acquisition of invoices that were not correctly sent by vendors at first
            - Created Weekly Reports with information necessary to make payments to various vendors we worked with
    
        ''')
    with st.container():
        st.write('🖥️', 'Marketing and Administrative Assistant')
        st.write('03/2020 - 03/2021')
        st.markdown('''
                - Facilitated all aspects of marketing and communications including website design and management, layout and 
                design, social media management and communications, customer and faculty communications, and brainstorming for 
                improved customer acquisitions.
                - Developed outreach programs to encourage student enrollment post-pandemic.
                - Managed a team of ten volunteers working on customer communications, event planning, financial administration, 
                website design, as well as other individual tasks as required
        ''')
    with st.container():
        st.write('🖥️', 'Marketing Intern')
        st.write('06/2020 - 08/2020')
        st.markdown('''
        - Secured new users for firm’s character-focused movie, TV shows books, and video game discovery platform through 
        the creation of written materials to be published on the company website.
        - In collaboration with CEO, developed marketing strategies such as how to best use written character 
        materials on company social media accounts to encourage more interaction and exposure.
        - Researched markets and other similar competitors to inform development of new marketing strategies.
        ''')


#
#
# profile_photo = ('Photo of Jathan Torres.jpg')
# # uchicago_logo = ('/Users/jathantorres/Downloads/uchicago_logo.webp')
# def load_lottie(url):
#     r = requests.get(url)
#     if r.status_code != 200:
#         return None
#     return r.json()
#
#
# lottie_animation = load_lottie('https://lottie.host/9881288e-8f85-467e-aaff-4e964e6031a1/PIM85NWPNw.json')
#
#
# text =  ('''
#         ## :violet[Digital Resume]
#         # :blue-background[Jathan Torres]
#         [LinkedIn Profile](https://www.linkedin.com/in/jathan-torres-5a27571a1/)
#         I graduated from the :red-background[University of Chicago] in the summer of 2023 with a B.A. in :green[Economics] and I'm extremely
#         grateful for my experience. Now for the past year and a half I have been working at a marketing agency (MERGE)
#         as an Associate Media Accounting Analyst.
#         While I am grateful for my experience with MERGE I am looking to take the next
#         step in my career as I am always eager to learn through challenging myself.
#
#          ## :blue[Professional Ambition]
#         I am seeking a role where I can utilize my high-level problem solving and communication skills, that
#         I harnessed in my time at university. But not only that I want to continue to utilize and enhance
#         my technical skills that I am and have been developing throughout my career.
#
#         I aim to utilize my skills in economic strategic thinking combined with
#         my invaluable technical skills in order to be a productive addition to any team.
#
#         ## :blue[Key Academic Experience]
#         At the University of Chicago I learned from the rigourous coursework the crucial skills
#         that I have continued to hone throughout the start of my professional career.
#         I have become an excellent communicator and team-player as I understand the importance of cooperation.
#         Without cooperation, the scale at which any one individual can have an impact is greatly reduced.
#
#         ### :blue[Relevant Coursework]
#         - **Operational Management**
#         - **Managing in Organizations**
#         - **Financial Accounting**
#         - **Marketing Management**
#         - **Fundamentals of Psychology**
#
#         ### :blue[Takeaways]
#         With my academic and personal experience I have learned the importance of understanding the perspective of
#         your target audience. By being able to understand how different biases affect your decisions then you
#         are best suited to understand what is needed in any given moment to make the best decisions.
#
#         ### :blue[Technical Skills]
#         I aim to be able to have technical expertise that allows for a greatly improved to help business
#         make great strategic decisions.
#         - **SQL**
#             - I even have experience using Python to seamlessly automate the process
#                 of inserting and querying data within SQL.
#         - **Python**
#             - This site was built all within Python using various modules such as
#                 Pandas, Streamlit, Matplotlib, etc.
#         - **Excel**
#             - Experience with Formulas and Pivot Tables.
#             - Experience using openpyxl python module to automate the process of working
#             within Excel
#         - **Data Visualization Tools (such as Streamlit which powers this site)**
#         - **Meta Ads Manager**
#         - **GitHub**
#         - **Power BI**
#
# ''')
#
#

#
# col1, col2 = st.columns([2,1])
# # with st.container():
# #     with col1:
# #         st.subheader("My name is Jathan Torres is my Interactive Career Journery")
# #         # st.write("[Listen Now>]()")
#
# # st.markdown("*Streamlit* is **really** ***cool***.")
# # st.markdown('''
# #     :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
# #     :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.''')
# # st.markdown("Here's a bouquet &mdash;\
# #             :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")
# #
# # multi = '''If you end a line with two spaces,
# # a soft return is used for the next line.
# #
# # Two (or more) newline characters in a row will result in a hard return.
# # '''
# # st.markdown(multi)
# with st.container():
#     with col1:
#         st.markdown(text)
# with col2:
#     # st.image(uchicago_logo, use_column_width=True)
#     st.markdown('<br><br><br><br>', unsafe_allow_html=True)
#     image_rounder(profile_photo)
#     st.markdown('<br><br><br><br>', unsafe_allow_html=True)
#     st.divider()
#     st.markdown('<br><br><br>', unsafe_allow_html=True)
#     st_lottie(lottie_animation, width=350, key='coding')
# #
# # st.markdown("# This is a Heading 1")
# # st.markdown("## This is a Heading 2")
# # st.markdown("### This is a Heading 3")
#
# # st.image('/Users/jathantorres/Movies/AUDIO SURVIVOR APPLICATION VIDEO/Photo of Jathan Torres.jpg', width=350)
