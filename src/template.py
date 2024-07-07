import streamlit as st
import pandas as pd

# I have provided most of what you need for to use streamlit here and in README.md
# You can also check the streamlit docs at https://docs.streamlit.io/get-started
# Also, you can check a simple example from class:
# Page: https://simpson-dashboard-class.streamlit.app/
# GitHub Repo: https://github.com/RodrigoGrijalba/python-dashboard-class

st.set_page_config(page_title = "<<Your page title here>>", layout = "wide")

tab1, tab2, tab3, tab4 = st.tabs(["Original Paper", "Proposed Extention", "Extenson Results", "Referencres"])

with tab1:
    st.markdown("""
    ### Design description
    ##### Research Question
    Does compulsory schooling laws, which mandate the minimum age at which students can drop out of school, have a causal effect on the amount of schooling individuals receive and their earnings in adulthood?
    
    ##### Main Hypothesis
    Compulsory school attendance laws increase educational attainment and, consequently, lead to higher earnings in the labor market
    
    ### Data
    ##### Description of Data: 
    Longitudinal data for demographics, U.S. Population Censuses of 1960, 1970, and 1980 for education and labor outcomes.
    
    ##### Unit of Observation: 
    Individuals
    
    ##### Experiment or Quasi-experiment: 
    Quasi-experimental
    
    ##### Instrument: 
    Quarter of birth of the individual
    
    ##### Controls: 
    Race, SMSA, Married, Age-Squared

    ### Original results
    Higher levels of educational attainment resulting from increased compulsory schooling laws correspond to higher earnings in adulthood: the monetary return to an additional year of schooling for those who are compelled to attend school by compulsory schooling laws is about 7.5 percent.
    """
    )
    ##### OLS and TSLS estimates of the return to education for men born 1920-1929
    st.image("images/Table4.png")
                
    
with tab2:

    st.markdown("""
    ### Proposed extension: 

    ### Justification
    <<Your description here, in Markdown>>
    """
    )
    # st.image("<<path to image from project's root, if needed>>") # uncomment this line if you would like to add an image
    # table = pd.read_csv("<<path/to/table.csv>>") # load a table from csv to show it on the page
    # st.table(table) # show table


with tab3:

    st.markdown("""
    ### Extension results

    <<Your description here, in Markdown>>
    """
    )
    # st.image("<<path to image from project's root, if needed>>") # uncomment this line if you would like to add an image

with tab4:

    st.markdown("""
    <<Your description here, in Markdown>>
    """
    )
    # st.image("<<path to image from project's root, if needed>>") # uncomment this line if you would like to add an image

