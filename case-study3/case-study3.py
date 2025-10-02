################################
# Gezinomi Kural Tabanlı Sınıflandırma
################################

# Görev 1

# 1
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = pd.read_excel("miuul_gezinomi.xlsx")
df.head()


# 2
df["SaleCityName"].nunique()
df["SaleCityName"].value_counts()

# 3

df["ConceptName"].nunique()

# 4

df["ConceptName"].value_counts()

# 5

df.groupby("SaleCityName")["Price"].sum()

# 6

df.groupby("ConceptName")["Price"].sum()

# 7

df.groupby("SaleCityName")["Price"].mean()

# 8

df.groupby("ConceptName")["Price"].mean()

# 9

df.groupby(["SaleCityName", "ConceptName"])["Price"].mean()



# Görev 2

bins = [-1, 7, 30, 90, df["SaleCheckInDayDiff"].max()]
labels = ["Last Minuters", "Potential Planners", "Planners", "Early Bookers"]

df["EB_Score"] = pd.cut(df["SaleCheckInDayDiff"], bins=bins, labels=labels)
df.head(50)


# Görev 3: Şehir,Concept, [EB_Score,Sezon,CInday] kırılımında ücret ortalamalarına ve frekanslarına bakınız

df.groupby(["SaleCityName", "ConceptName", "EB_Score"]).agg({"Price": ["mean", "count"]})
df.groupby(["SaleCityName", "ConceptName", "Seasons"]).agg({"Price": ["mean", "count"]})
df.groupby(["SaleCityName", "ConceptName", "CInDay"]).agg({"Price": ["mean", "count"]})


# Görev 4: City-Concept-Season kırılımın çıktısını PRICE'a göre sıralayınız.
# Önceki sorudaki çıktıyı daha iyi görebilmek için sort_values metodunu azalan olacak şekilde PRICE'a uygulayınız.
# Çıktıyı agg_df olarak kaydediniz.

agg_df = df.groupby(["SaleCityName", "ConceptName", "Seasons"]).agg({"Price": "mean"}).sort_values("Price", ascending=False)
agg_df.head(20)

# Görev 5: Indekste yer alan isimleri değişken ismine çeviriniz.
# Üçüncü sorunun çıktısında yer alan PRICE dışındaki tüm değişkenler index isimleridir.
# Bu isimleri değişken isimlerine çeviriniz.
# İpucu: reset_index()

agg_df.reset_index(inplace=True)
agg_df.head(20)

# Görev 6: Yeni level based satışları tanımlayınız ve veri setine değişken olarak ekleyiniz.
# sales_level_based adında bir değişken tanımlayınız ve veri setine bu değişkeni ekleyiniz.

agg_df["sales_level_based"] = agg_df[["SaleCityName", "ConceptName", "Seasons"]].agg(lambda x: '_'.join(x).upper(), axis=1)

agg_df.head(20)


# Görev 7: Personaları segmentlere ayırınız.
# PRICE'a göre segmentlere ayırınız,
# segmentleri "SEGMENT" isimlendirmesi ile agg_df'e ekleyiniz
# segmentleri betimleyiniz

agg_df["SEGMENT"] = pd.qcut(agg_df["Price"], q=4, labels= ["D", "C", "B", "A"])
agg_df.head(20)

agg_df.groupby("SEGMENT").agg({"Price": ["mean","max","sum"]})

# Görev 8: Oluşan son df'i price değişkenine göre sıralayınız.
# # "ANTALYA_HERŞEY DAHIL_HIGH" hangi segmenttedir ve ne kadar ücret beklenmektedir?

agg_df.sort_values("Price")

n_user = "ANTALYA_HERŞEY DAHIL_HIGH"

agg_df[agg_df["sales_level_based"] == n_user][["sales_level_based","Price", "SEGMENT"]]