dizi = [
    [None, "bir", "iki", "uc", "dort",
          "bes", "alti", "yedi", "sekiz", "dokuz"]
,[None, "on", "yirmi", "otuz", "kırk", "elli",
         "atmış", "yetmiş", "seksen", "doksan"],
[None, "yüz", "ikiyüz", "üçyüz", "dörtyüz", "beşyüz",
         "altıyüz", "yediyüz", "sekizyüz", "dokuzyüz"],
[None, "bin", "ikibin", "ucbin", "dortbin",
          "besbin", "altibin", "yedibin", "sekizbin", "dokuzbin"]
]

sayi = "3853"
sayi = sayi[::-1]

okunus = []
for i,s in enumerate(sayi):
    print(i, s)
    okunus.append(dizi[i][int(s)])
print(" ".join(reversed(okunus)))
print(okunus)