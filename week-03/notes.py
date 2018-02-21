import pandas as pd
import numpy as np
import matplotlib
%matplotlib inline
# ^^^ last two lines are wrong???

new_list = []
df = pd.DataFrame()
print(df)

df['name'] = ['Bilbo', 'Frodo', 'Samwise']

df

df.assign(height = [0.5, 0.4, 0.6])

import os
os.chdir('week-03')

df = pd.read_csv('data/skyhook_2017-07.csv', sep=',')

df.head()

df.shape[1]

df.columns
df['cat_name'].unique()
df['cat_name']
df.cat_name
# problem with dot method is if name is the same as a command
df['count']
df.count

one_fifty_eight = df[df['hour'] == 158]

one_fifty_eight.shape

df[(df['hour'] == 158) & (df['count'] > 50)].shape

bastille = df[df['date'] == '2017-07-14']
bastille.head()

bastille['count'].mean()

# greater than average cells
lovers_of_bastille = bastille[bastille['count'] > bastille['count'].mean()]

lovers_of_bastille['count'].describe()

df.groupby('date')['count'].describe()

df['count'].max()
df['count'].min()
df['count'].mean()
df['count'].std()
df['count'].count()

df[df['count'] == df['count'].max()]

df['hour'].unique()
jul_sec = df[df['date'] == '2017-07-02']

jul_sec.groupby('hour')['count'].sum().plot()

df['date_new'] = pd.to_datetime(df['date'], format = '%Y-%m-%d')

df[df['date_new'] == '2017-07-03']['weekday']

df['weekday'] = df['date_new'].apply(lambda x: x.weekday() + 1)

df['weekday'].replace(7, 0, inplace = True)

for i in range(0, 168, 24):
    j = range()
    df.drop(df[df['weekday'] == (i/24) &
    (
    (df['hour']) < i | df['hour'] > i + 24
    )
    ])

# THIS SHIT IS ALL ON GITHUB AND NOT FINISHED IN THIS DOC
