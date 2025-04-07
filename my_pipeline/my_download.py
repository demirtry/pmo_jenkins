import pandas as pd


def download_data():

    df = pd.read_csv('https://raw.githubusercontent.com/demirtry/PMO_datasets/refs/heads/main/student_performance_dataset.csv')
    df.to_csv("student_performance_dataset.csv", index=False)

    return df


def preprocessing(path2df):
    df = pd.read_csv(path2df)

    columns_to_drop = [x for x in df.columns if df[x].isna().mean() > 0.15]
    columns_to_drop.append('Final_Exam_Score')
    columns_to_drop.append('Student_ID')
    df.drop(columns=columns_to_drop, inplace=True)

    df['Pass_Fail'] = df['Pass_Fail'].apply(lambda x: 1 if x == 'Pass' else 0)

    cat_columns = ['Gender', 'Parental_Education_Level', 'Internet_Access_at_Home', 'Extracurricular_Activities']
    df_encoded = pd.get_dummies(df, columns=cat_columns, drop_first=True)

    df_encoded.to_csv('student_performance_clear.csv')
    return True


download_data()
preprocessing("student_performance_dataset.csv")