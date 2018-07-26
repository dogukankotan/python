birler = [None, "bir", "iki", "uc", "dort",
          "bes", "alti", "yedi", "sekiz", "dokuz"]
onlar = [None, "on", "yirmi", "otuz", "kırk", "elli",
         "atmış", "yetmiş", "seksen", "doksan"]

sayi = "2238"
sayi = sayi[::-1]

okunus = []
okunus.append(birler[int(sayi[0])])

if len(sayi) >= 2:
    okunus.append(onlar[int(sayi[1])])
if len(sayi) >= 3:
    if sayi[2] == "1":
        okunus.append("yuz")
    else:
        okunus.append(birler[int(sayi[2])] + "yuz")
if len(sayi) >= 4:
    okunus.append(birler[int(sayi[3])] + "bin")
print(okunus)
print(" ".join(okunus[::-1]))