import numpy as np
import pandas as pd

# creating a dataframe
df = pd.DataFrame({'Name': ['Raj', 'Akhil', 'Sonum', 'Tilak', 'Divya', 'Megha'],
                   'Age': [20, 22, 21, 19, 17, 23],
                   'Rank': [1, np.nan, 8, 9, 4, np.nan]})
print(df)
sorted_df = df.sort_values(by=['Age'], ascending=False)
print(sorted_df)