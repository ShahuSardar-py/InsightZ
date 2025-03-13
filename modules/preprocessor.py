import pandas as pd

#concats the input file
def combiner(uploaded_files, engine='openpyxl'):
    combined_df = pd.DataFrame()
    for file in uploaded_files:
        df = pd.read_excel(file, engine=engine)
        combined_df = pd.concat([combined_df, df], ignore_index=True)
    return combined_df

def filter_present(df):
    return df[df['Present/Absent'] == 'Present']

# Count department-wise entries
def count_department_entries(df):
    return df['Department'].value_counts()

# Count values based on column and condition
def value_counter(df, column, value):
    return df[column].value_counts().get(value, 0)

def drop_columns(df, columns_to_drop):
    return df.drop(columns=columns_to_drop, errors='ignore')

def filter_rows(df, column, value):
    return df[df[column] == value]

# Segregate  'faculty' and 'student'.
def segregate_data(df, role_col='Role'):
    faculty_df = df[df[role_col] == 'faculty']
    student_df = df[df[role_col] == 'student']
    return faculty_df, student_df

# gender segregation
def gender(df, gender_col='Gender'):
    male_df = df[df[gender_col] == 'male']
    female_df = df[df[gender_col] == 'female']
    return male_df, female_df


def compute_statistics(df):
    dept_wise_count = count_department_entries(df)

    # Gender count
    male_count = value_counter(df, 'Gender', 'male')
    female_count = value_counter(df, 'Gender', 'female')

    # Faculty gender count
    faculty_male = df[(df['Gender'] == 'male') & (df['Role'] == 'faculty')].shape[0]
    faculty_female = df[(df['Gender'] == 'female') & (df['Role'] == 'faculty')].shape[0]

    # Student gender count
    student_male = df[(df['Gender'] == 'male') & (df['Role'] == 'student')].shape[0]
    student_female = df[(df['Gender'] == 'female') & (df['Role'] == 'student')].shape[0]

    # Unique courses
    courses = df['Course Name'].unique()

    # Count SC/ST students
    ST_SC = df[df['SC/ST status'].astype(str).str.upper() == 'TRUE'].shape[0]

    return {
        'dept_wise_count': dept_wise_count,
        'male_count': male_count,
        'female_count': female_count,
        'faculty_male': faculty_male,
        'faculty_female': faculty_female,
        'student_male': student_male,
        'student_female': student_female,
        'courses': courses,
        'ST_SC': ST_SC
    }

    









# RESULT ANALYSIS PREPROCESSOR
#do not touch for any changes
def preprocess_result_data(uploaded_files, columns_to_drop, attendance_col='Present/Absent', role_col='Role'):
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
    stats = compute_statistics(cleaned_df)

    return combined_df, cleaned_df, faculty_df, student_df,stats
