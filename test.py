import pandas as pd
import random

lst = ['robot'] * 10 + ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

one_hot = pd.DataFrame()

for category in data['whoAmI'].unique():
    one_hot[f"is_{category}"] = (data['whoAmI'] == category).astype(int)

print(one_hot.head())
