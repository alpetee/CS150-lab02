import pandas as pd
from pandas import DataFrame

s = pd.Series([42, 21, 3.5, 4])
# print(s)

df = DataFrame({'age' : [23, 21, 18],
                'name': ['Aidan', 'Allie', 'Simon'],
                'cardio': [60, 1000, 200]})

# select by column
# print(df['age'])
# select by label-- just
# print(df.loc[:, 'age'])

# select by row-- this access the second row only. inclusive, exclusive.
#print(df[2:3])
# 1 column of 2nd row (index starts at 0)
#print(df.iloc[2, 1])

# boolean indexing-- prints rows that
# print(df[df['age'] > 19])

# modifying an existing dataframe
df.loc[1:, 'age'] = 16 # changes all but first

# adding a column
df.loc[:, 'friend'] = 'Jesus'

print(df)
