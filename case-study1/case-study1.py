# 1 - Verilen değerlerin veri yapılarını incele.

x = 8
y = 3.2
z = 8j + 18
a = "Hello World"
b= True
c = 23 < 22
l = [1, 2, 3, 4]
d = {"Name": "Jake",
     "Age": 27,
     "Address": "Downtown"}
t = ("Machine Learning", "Data Science")
s = {"Python", "Machine Learn", "Data Science"}

type(s)

# 2 - Verilen string ifadenin tüm harflerini büyük harfe çeviriniz.
#     Virgül ve nokta yerine space koyunuz, kelime kelime ayırınız.

text = "The goal is to turn data into information, into insight."

text = text.upper().replace("."," ").replace(",","").split()

print(text)

############
# 3
############

lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]

# 3.1 - Listenin eleman sayısına bakın.

len(lst)

# 3.2 - Sıfırıncı ve onuncu indeksteki elemanları çağır.

print(lst[0],lst[10])

# 3.3 - Verilen liste üzerinden ["D", "A", "T", "A"] listesi oluştur.
new_lst = lst[0:4]
print(new_lst)

# 3.4 - Sekizinci indeksteki elemanı sil
type(lst)
lst.pop(8)
print(lst)

# 3.5 - Yeni bir eleman ekleyin.
lst.append("R")
print(lst)

# 3.6 - Sekizinci indekse "N" elemanını tekra ekle.
lst.insert(8,"N")
print(lst)


#################
# 4 - Verilen sözlük yapısına aşağıdaki adımları uygula.
#################

dict = {"Christian": ["America", 18],
        "Daisy": ["England", 12],
        "Antonio": ["Spain", 22],
        "Dante": ["Italy", 25]}

# 4.1 - Key değerlerine eriş

dict.keys()

# 4.2 - Value' lara eriş

dict.values()

# 4.3 - Daisy keyine ait 12 değerini 13 olarak güncelle.

dict["Daisy"][1] = 13
dict["Daisy"]

# 4.4 - Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.

dict.update({"Ahmet": ["Tukey", 24]})
print(dict)

# 4.5 - Antonio' yu dictionary' den sil.

dict.pop("Antonio")
dict

###########################
# 5 - Argüman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atayan ve bu listeleri return eden bir fonksiyon yaz.

l = [2, 13, 18, 93, 22]

def func(list):
    tek = []
    cift = []
    for i in list:
        if i % 2 == 0:
            cift.append(i)
        else:
            tek.append(i)
    return tek, cift

odd_list, even_list = func(l)

odd_list
even_list


####################
# 6 - Verilen listede mühendislik ve tıp fakültelerinde dereceye giren öğrencilerin isimleri bulunuyor. Sırasıyla ilk üç öğnreci mühendislik fakültesinin başarı sırasını, son üç öğrenci tıp fakültesinin başarı sırasını gösteriyor. Enumerate kullanarak dereceleri fakülte özelinde yazdır.
####################

ogrenciler = ["Ali", "Veli", "Ayşe", "Talat", "Zeynep", "Ece"]

for index, ogrenci in enumerate(ogrenciler, start=1):
    if index < 4:
        print(f"Mühendislik Fakültesi {index}. Öğrenci: {ogrenci}")
    else:
        print(f"Tıp Fakültesi {index-3}. Öğrenci: {ogrenci}")



############
# 7 - Aşağıdaki listeleri zip kullanarak birleştir
############

ders_kodu = ["CMP1005", "PSY1001", "HUK1005", "SEN2204"]
kredi = [3,4,2,4]
kontenjan = [30, 75, 150, 25]

for ders_kodu, kredi, kontenjan in zip(ders_kodu, kredi, kontenjan):
    print(f"Kredisi {kredi} olan {ders_kodu} kodlu dersin kontenjanı {kontenjan} kişidir.")


########################
# 8 - Aşağıda 2 adet set verilmiştir. 1. küme 2. kümeyi kapsıyorsa ortak elemanları, eğer kapsamıyorsa 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımla.
########################

kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])


def kume (set1, set2):
    if set1.issuperset(set2):
        print(set1.intersection(set2))
    else:
        print(set2.difference(set1))


kume(kume1, kume2)
kume(kume2, kume1)