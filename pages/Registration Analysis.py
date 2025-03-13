import streamlit as st
import pandas as pd
import plotly.express as px
from modules.preprocessor import preprocess_Reg_Data

#page config
st.set_page_config(page_title="InsightZ - NPTEL Report Generator",
                   page_icon="📈",
                   layout="wide")


st.title("Registration analysis")
st.caption("Registration analysis for NPTEL registrations. Load data in sidebar. ")
st.divider()
#uploader in side bar
uploaded_files = st.sidebar.file_uploader(
    "Upload the CSV files", 
    accept_multiple_files=True, 
    type=["xlsx", "xls"]
)

#counts entries
def value_counter(df: pd.DataFrame, column: str, value: str) -> int:
    return df[column].value_counts().get(value, 0)

#department wise entries
def count_department_entries(df: pd.DataFrame, column: str = "Department") -> pd.Series:
    return df[column].value_counts()


    

if uploaded_files:
    st.toast("Data Has Been Uploaded Sucessfully")


    # Loading Preprocessed data 
    columns_to_drop = ['College Roll Number', 'Unproctored programming exam score out of 25', 'Emailid']
    combined_df, cleaned_df, faculty_df, student_df,stats = preprocess_Reg_Data(uploaded_files,columns_to_drop)
    dept_wise_count = stats['dept_wise_count']
    male_count = stats['male_count']
    female_count = stats['female_count']
    faculty_male = stats['faculty_male']
    faculty_female = stats['faculty_female']
    student_male = stats['student_male']
    student_female = stats['student_female']
    courses = stats['courses']
    ST_SC = stats['ST_SC']


    total_registered = cleaned_df.shape[0]
    registred=int(total_registered)
    # Display results

    col1 = st.columns(1)
    col1.metric("Total Registered",value=registred)
    a, b = st.columns(2)
    c, d = st.columns(2)



    st.write(total_registered)
    st.write(ST_SC)
    st.write(faculty_male)
    st.write(faculty_female)
    st.write(student_male)
    st.write(student_female)
    st.write(dept_wise_count)
    st.write(male_count)
    st.write(female_count)
    st.write(courses)

else:
    st.write("Please upload the files in the sidebar")
