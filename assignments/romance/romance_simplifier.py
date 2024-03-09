import pandas as pd

df = pd.read_csv('profiles.csv', low_memory=False)
df.dropna(axis=0, how='all', inplace=True)

print(df.shape)

df.to_csv('romance_small.csv', index=False)
