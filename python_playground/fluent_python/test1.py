import numpy as np
import pandas as pd
from pandas import DataFrame, Series


srs = Series({"ky": 100, "kiruen": 10000})
# print(srs)

df = DataFrame({"name": ["g", "z", "l", "z"], "Chinese": [100, 20, None, 78], "Math": [55, 66, 77, 100]})


# print(df)
# df["Chinese"]["g"].nu
def calc_score(df):
    df["score"] = df["Chinese"] + df["Math"]
    return df

df["Chinese"].fillna(df["Chinese"].mean(), inplace=True)
df = df.apply(calc_score, axis=1)  # 小心拷贝的特性啊！
print(df)
print(df.describe())