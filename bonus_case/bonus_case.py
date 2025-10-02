# Görev 1

# 1
import pandas as pd
pd.set_option("display.max_rows", None)
df = pd.read_csv("persona.csv")
df.head()
df.shape
df.info()

# 2
df["SOURCE"].nunique()
df["SOURCE"].value_counts()

# 3

df["PRICE"].nunique()

# 4
df["PRICE"].value_counts()

# 5

df["COUNTRY"].value_counts()
df.groupby("COUNTRY")["PRICE"].count()
df.pivot_table(values="PRICE",index="COUNTRY",aggfunc="count")

# 6
df.groupby("COUNTRY").agg({"PRICE":"sum"})

# 7

df["SOURCE"].value_counts()

# 8

df.groupby("COUNTRY")["PRICE"].mean()

# 9

df.groupby("SOURCE").agg({"PRICE":"mean"})

# 10

df.groupby(["SOURCE","COUNTRY"]).agg({"PRICE":"mean"})
df.pivot_table(values ="PRICE",index="SOURCE",columns="COUNTRY",aggfunc="mean" )


# Görev 2

df.groupby(["COUNTRY","SOURCE","SEX","AGE"]).agg({"PRICE":"mean"})

# Görev 3

agg_df = df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE":"mean"}).sort_values("PRICE",ascending=False)
agg_df.head(20)

# Görev 4
agg_df = agg_df.reset_index()
agg_df.head()

# Görev 5

bins = [0, 18, 23, 30, 45, agg_df["AGE"].max()]

age_labels = ["0_18", "19_23", "24_30", "31_45", "46_" + str(agg_df["AGE"].max())]

agg_df["age_cat"] = pd.cut(agg_df["AGE"], bins, labels=age_labels)
agg_df.head()

# Görev 6

agg_df["customers_level_based"] = agg_df[["COUNTRY", "SOURCE", "SEX", "age_cat"]].agg(lambda x: "_".join(x).upper(), axis=1)
agg_df.head()

agg_df = agg_df[["customers_level_based", "PRICE"]]
agg_df.head()

agg_df = agg_df.groupby("customers_level_based").agg({"PRICE":"mean"})
agg_df = agg_df.reset_index()
agg_df["customers_level_based"].value_counts()
agg_df.head()


# Görev 7

agg_df["SEGMENT"] = pd.qcut(agg_df["PRICE"], q=4, labels= ["D","C","B","A"])
agg_df.head()

agg_df.groupby("SEGMENT")["PRICE"].mean()


# Görev 8

#
n_user = "TUR_ANDROID_FEMALE_31_45"
agg_df[agg_df["customers_level_based"] == n_user]

#
n_user = "FRA_IOS_FEMALE_31_45"
agg_df[agg_df["customers_level_based"] == n_user]

agg_df.tail()