import pandas as pd

#RESULT DATA CLEANING 

#concats the input file
def combiner(uploaded_files, engine='openpyxl'):
    combined_df = pd.DataFrame()
    for file in uploaded_files:
        df = pd.read_excel(file, engine=engine)
        combined_df = pd.concat([combined_df, df], ignore_index=True)
    return combined_df


def drop_columns(df, columns_to_drop):
    return df.drop(columns=columns_to_drop, errors='ignore')


def filter_rows(df, column, value):
    return df[df[column] == value]

# Segregate  'faculty' and 'student'.
def segregate_data(df, role_col='Role'):
    faculty_df = df[df[role_col] == 'faculty']
    student_df = df[df[role_col] == 'student']
    return faculty_df, student_df


def gender(df, gender_col='Gender'):
    male_df = df[df[gender_col] == 'male']
    female_df = df[df[gender_col] == 'female']
    return male_df, female_df

  





















# Main preprocessing function.
def preprocess_data(uploaded_files, columns_to_drop, attendance_col='Present/Absent', role_col='Role'):
    combined_df = combiner(uploaded_files)
    cleaned_df = drop_columns(combined_df, columns_to_drop)
    main_df = filter_rows(cleaned_df, attendance_col, 'Present')
    absent_df = filter_rows(cleaned_df, attendance_col, 'Absent')
    faculty_df, student_df = segregate_data(main_df, role_col)
    
    return combined_df, cleaned_df, main_df, absent_df, faculty_df, student_df

def preprocess_Reg_Data(uploaded_files, columns_to_drop,role_col='Role'):
    combined_df = combiner(uploaded_files)
    cleaned_df = drop_columns(combined_df, columns_to_drop)
    faculty_df, student_df = segregate_data(cleaned_df, role_col)
    
    return combined_df, cleaned_df, faculty_df, student_df
