import streamlit as st
import pandas as pd
import plotly.express as px
from modules.preprocessor import preprocess_data, preprocess_Reg_Data

st.set_page_config(page_title="InsightZ - NPTEL Report Generator",
                   page_icon="📈",
                   layout="wide")


st.title("Registration analysis playground")
st.subheader("version 1")

def value_counter(df: pd.DataFrame, column: str, value: str) -> int:
    return df[column].value_counts().get(value, 0)

def count_department_entries(df: pd.DataFrame, column: str = "Department") -> pd.Series:
    return df[column].value_counts()



uploaded_files = st.sidebar.file_uploader(
    "Upload the result files", 
    accept_multiple_files=True, 
    type=["xlsx", "xls"]
)

if uploaded_files:
    st.sidebar.success("File Upload Successful!")
    columns_to_drop = ['College Roll Number', 'Unproctored programming exam score out of 25', 'Emailid']

    # Preprocessed data loaded
    combined_df, cleaned_df, faculty_df, student_df = preprocess_Reg_Data(uploaded_files,columns_to_drop)

    dept_wise_count=count_department_entries(cleaned_df)
    st.write(dept_wise_count)

    male_count = value_counter(cleaned_df, 'Gender', 'male')
    female_count = value_counter(cleaned_df, 'Gender', 'female')
    st.write(male_count)
    st.write(female_count)

    faculty_male=cleaned_df[(cleaned_df['Gender'] == 'male') & (cleaned_df['Role'] == 'faculty')].shape[0]
    faculty_female= cleaned_df[(cleaned_df['Gender']== 'female') & (cleaned_df['Role']=='faculty')].shape[0]
    
    
    student_male= cleaned_df[(cleaned_df['Gender']== 'male') & (cleaned_df['Role']=='student')].shape[0]
    student_female= cleaned_df[(cleaned_df['Gender']== 'female') & (cleaned_df['Role']=='student')].shape[0]
    

    st.write(faculty_male)
    st.write(faculty_female)
    st.write(student_male)
    st.write(student_female)
