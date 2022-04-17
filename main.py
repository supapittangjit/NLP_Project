import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display
from library.nullAnalyze import cutNull, checkNull

df = pd.read_csv('netflix_titles.csv')
# display(df.head())

cutNull(df)
checkNull(df)
# print(df['country'][300])
# df['first_country'] = df['country'].apply(lambda x: x+2)
# df['first_country'][300]
