import pandas as pd
import numpy as np


def checkNull(df):
    # check null value in all columns
    for i in df.columns:
        null_rate = df[i].isna().sum()/len(df) * 100
        if null_rate > 0:
            print("{} null rate: {}%".format(
                i, round(null_rate, 2)))
    print(null_rate)
    if(null_rate < 0):
        print("no more null")


def cutNull(df):
    # no more null in all columns
    df['country'] = df['country'].fillna(df['country'].mode()[0])
    df['cast'].replace(np.nan, 'No data', inplace=True)
    df['director'].replace(np.nan, 'No data', inplace=True)
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)
    df['date_added'] = pd.to_datetime(df['date_added'])
    df['month_added'] = df['date_added'].dt.month
    df['month_name_added'] = df['date_added'].dt.month_name()
    df['year_added'] = df['date_added'].dt.year
