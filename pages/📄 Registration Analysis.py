import streamlit as st
import pandas as pd
import plotly.express as px
from modules.preprocessor import preprocess_Reg_Data
import time
#page config
st.set_page_config(page_title="InsightZ - NPTEL Report Generator",
                   page_icon="📈",
                   layout="wide")

st.markdown(
    """
    <style>
    .kpi-box {
        background-color: #141424;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
        border: solid 1px white;
    }
    .kpi-box h1 {
        font-size: 2.8em;
        margin: 0;
    }
    .kpi-box h2 {
        font-size: 2em;
        color: #e6e6e6;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("InsightZ - :orange[Registration Analysis]")
st.caption("Registration analysis for NPTEL registrations. Load data in sidebar.")
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
    st.toast("Data Has Been Uploaded Successfully")

if uploaded_files:
    # Loading Preprocessed data 
    columns_to_drop = ['College Roll Number', 'Unproctored programming exam score out of 25', 'Emailid']
    combined_df, cleaned_df, faculty_df, student_df, stats = preprocess_Reg_Data(uploaded_files, columns_to_drop)
    dept_wise_count = stats['dept_wise_count']
    male_count = stats['male_count']
    female_count = stats['female_count']
    faculty_male = stats['faculty_male']
    faculty_female = stats['faculty_female']
    student_male = stats['student_male']
    student_female = stats['student_female']
    courses = stats['courses']
    ST_SC = stats['ST_SC']


    with st.spinner("Hang on Tight! Generating report in"):
        time.sleep(5)
    total_registered = cleaned_df.shape[0]
    # Display results

    col1 = st.columns(1)[0]
    st.markdown(f"""
            <div class="kpi-box">
                <h2>Total Enrolled</h2>
                <h1>{total_registered}</h1>
            </div>
            """, unsafe_allow_html=True)

    a, b = st.columns(2)
    c, d, e, f = st.columns(4)

    a.metric("Male Count", male_count, border=True)
    b.metric("Female Count", female_count, border=True)

    c.metric("Male Student", student_male, border=True)
    d.metric("Female Student", student_female, border=True)
    e.metric("Male Faculty", faculty_male, border=True)
    f.metric("Female Faculty", faculty_female, border=True)
    st.subheader(f'''
    :red[SC/ST]:
                {ST_SC} 
                ''')
    st.caption("Note: The difference between total registered and (male + female) represents 'other' gender entries.")
    
    st.divider()
    st.header(":blue[Department wise Count]")

    col1, col2 = st.columns(2)
    with col1:
        st.table(data=dept_wise_count)
    with col2:
        st.caption("You Can Expand the Chart")
        dep_count_histogram = px.bar(cleaned_df, x="Department", color="Department")
        st.plotly_chart(dep_count_histogram, use_container_width=True)

    st.divider()
    st.header("Courses Offered")
    with st.expander("Expand Course List"):
        st.table(courses)

    with st.expander('About', expanded=True):
        st.caption('''InsightZ- NPTEL report generator. 
                    V 1.2.6
                    A robust data analyser and report generator for NPTEL data
                    ♥
                        
        ''')

else:
    st.write("Please upload the files in the sidebar")
