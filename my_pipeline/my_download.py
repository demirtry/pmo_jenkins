import pandas as pd


def download_data():

    df = pd.read_csv('https://raw.githubusercontent.com/demirtry/PMO_datasets/refs/heads/main/student_performance_dataset.csv')
    df.to_csv("student_performance_dataset.csv", index=False)

    return df


def preprocessing(path2df):
    df = pd.read_csv(path2df)

    columns_to_drop = [x for x in df.columns if df[x].isna().mean() > 0.15]
    columns_to_drop.append('Final_Exam_Score')
    df.drop(columns=columns_to_drop, inplace=True)

    for num_col in df.columns:
        df[num_col] = df[num_col].fillna(df[num_col].median())

    df.to_csv('student_performance_clear.csv')
    return True


download_data()
preprocessing("student_performance_dataset.csv")