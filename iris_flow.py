from prefect import task, flow
import pandas as pd


@task
def extract_data(file_path):
    return pd.read_csv(file_path)


@task
def transform_data(df):
    return df[df['variety'] == 'Setosa']


@task
def load_data(df, file_path):
    return df.to_csv(file_path)


@flow
def iris_flow():
    df = extract_data('iris.csv')

    transformed_df = transform_data(df)

    load_data(transformed_df, 'transformed_iris.csv')