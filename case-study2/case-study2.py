# 1- List Comprehension yapısı kullanarak car_crasher verisindeki numeric değişkenlerin isimlerini büyük harfe çevirin ve başına NUM ekleyin.
import pandas as pd
import seaborn as sns
from numba.core.cgutils import is_null

df = sns.load_dataset("car_crashes")
df.columns



cols_up = [col.upper() for col in df.columns]

["NUM_" + col.upper() for col in df.columns if df[col].dtype != "O"]

# 2- "no" barındırmayan isimlerin sonuna "FLAG" yaz

[col.upper() + "_FLAG" if "no" not in col else col.upper() for col in df.columns]

# 3- Verilen değişken isimlerinden farklı olan değişkenlerin isimlerini seçip yeni bir DataFrame oluştur.

og_list = ["abbrev", "no_previous"]

new_cols = [col for col in df.columns if col not in og_list]
new_df = df[new_cols]
new_df.head()

# 4.1

import seaborn as sns
df = sns.load_dataset("titanic")

# 4.2

df["sex"].value_counts()

# 4.3

df.nunique()

# 4.4

df["pclass"].nunique()

# 4.5

df[["pclass","parch"]].nunique()

# 4.6

df["embarked"].dtype

df["embarked"] = df["embarked"].astype("category")
df["embarked"].dtype

# 4.7

df[df["embarked"]=="C"].head(10)

# 4.8

df[df["embarked"]!="S"].head(10)

# 4.9

df[(df["age"] < 30) & (df["sex"] == "female")].head(10)

# 4.10

df[(df["fare"] > 500) | (df["age"] > 70)].head(10)

# 4.11

df.isnull().sum()

# 4.12

df.drop(columns=["embarked"])

# 4.13

df["deck"].isnull()

df["deck"].mode()

type(df["deck"].mode())

df["deck"].mode()[0]

df["deck"].fillna((df["deck"].mode()[0]), inplace=True)

df.head(25)


# 4.14

type(df["age"].median())

df["age"].fillna((df["age"].median()), inplace=True)

# 4.15

df.groupby(["pclass","sex"]).agg({"survived":["count","mean", "sum"]})

# 4.16

df["age_flag"] = df["age"].apply(lambda x: 1 if x < 30 else 0)

df.head(25)

# 4.17

df = sns.load_dataset("tips")

# 4.18

df.head(25)

df.groupby(["time"]).agg({"total_bill": ["sum","min", "max", "mean"]})

# 4.19

df.groupby(["day", "time"]).agg({"total_bill": ["sum","min", "max", "mean"]})


# 4.20

df[(df["time"] == "Lunch") & (df["sex"] == "Female")].groupby("day").agg({"total_bill": ["sum","min", "max", "mean"],
                                                                  "tip":["sum", "min", "max", "mean"]})
# 4.21

df.loc[(df["size"] < 3) & (df["total_bill"] > 10), "total_bill"].mean()

# 4.22

df["total_bill_tip_sum"] = (df["total_bill"] + df["tip"])

df.head(25)

# 4.23

new_df = df.sort_values("total_bill_tip_sum", ascending=False)[:30]

new_df.head()