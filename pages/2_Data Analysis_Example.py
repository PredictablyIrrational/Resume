import streamlit as st
import markdown
import matplotlib as plt
import pandas as pd
from streamlit_lottie import st_lottie
import requests
import base64


st.set_page_config(page_title='Jathan Torres Resume', page_icon=":pencil:", layout='wide', initial_sidebar_state="collapsed")

gym_csv_path = ('/Users/jathantorres/PycharmProjects/Data_Visualization/gym_membership_data/gym_membership.csv')


def load_data_frame(csv):
    df = pd.read_csv(csv)
    return df


