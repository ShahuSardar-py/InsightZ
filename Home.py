import streamlit as st
st.set_page_config(
    page_title="InsightZ | NPTEL Report Generator",
    page_icon="📈",
)

st.title("InsightZ ")
st.header(":blue[_Automated NPTEL Report Generator_]")
st.divider()

st.sidebar.success("Select app")

st.header('How to use this app:')

st.markdown(
    """
    :green[Upload Your Files]\n
    Select app & head to the sidebar and upload your NPTEL files in .xlsx or .xls format.

    :green[View the Main Data]\n
    After the files are successfully uploaded, expand the "Main Data" section to see your cleaned and combined data.

    :green[Generate Your Report]\n
    Click the :blue["Generate Report"] button to automatically create visual report.

"""
)

footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: white;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: #00010d;
color: white;
text-align: center;
}
</style>
<div class="footer">
<p>Developed By Shahu Sardar For Dept. OF Data Science GHRCEM</p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)
