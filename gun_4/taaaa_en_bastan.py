# print fonksiyonu ve ozellikleri
yuz_olcumu = "200"
tevellut = "1990"
# print("Burasi Cok guzel sende gelsene")
# print("Bizim koyun yuz olcumu " + yuz_olcumu + " tevellutu " + tevellut)
# print("Bizim koyun yuz olcumu {} tevellutu {}".format(yuz_olcumu, tevellut))
# print("Bizim koyun yuz olcumu {yo} tevellutu {tv}".format(yo=yuz_olcumu,
#                                                           tv=tevellut))
# # print("Bizim koyun yuz olcumu ".join(yuz_olcumu))
# print(""" ornek \n
#             ornek \t""")
# print("ornek degisken", end="")
# print(" burada tırnak \" ")
# ilk_parca = "Bizim koyun yuz olcumu "
# print(ilk_parca[0])
# for gelecek_sey in ilk_parca:
#     print(gelecek_sey)


# cumle = "\t\t".join(cumle.split(" "))
# cumle = cumle.replace(' ', '\t\t')

# degisken turleri ve kullanımları
ilk = "ornek"
iki = 10
uc = 10.0
ornek = True
kocaman_sayi = 23842348237487462874682736427384623
# input fonksiyonu ve tip dönüşümleri

# ad = input("Adınız")
# liste nedir? nerelerde kullanılır?
bu_bir_listedir = ["bir", "kac", "tane", "bilinen", "degisken"]
farkli_liste = ["baska", "liste"]
# bu_bir_listedir.append(farkli_liste)
print(bu_bir_listedir)
# bu_bir_listedir.extend(farkli_liste)
# print(bu_bir_listedir)
# bu_bir_listedir.append({"bu": "sozluktur" })
# for degisken in bu_bir_listedir:
#     if type(degisken) == dict:
#         print(degisken.get("bu"))
#         continue
#     print(degisken)
# print(bu_bir_listedir[3][0:5])
print("Listenin ilk hali: {}".format(bu_bir_listedir))
siralanmis_liste = sorted(bu_bir_listedir, reverse=True)
print("Listenin sorted fonksiyonundan sonraki hali: {}\nSiralanmis hali:{}".
      format(bu_bir_listedir, siralanmis_liste))
bu_bir_listedir.sort()
print("Sort fonksiyonu çalıştıktan sonraki hali:")
print(bu_bir_listedir)

liste1 = ['a', 'b', 'f']
liste2 = ['c', 'd']
yeni_liste = []
yeni_liste.extend(liste2)
yeni_liste.extend([*liste1])
print(liste1)
print(liste2)
print(yeni_liste)

# print(list('a', 'b', 'f'))

# sözlükler
ozlenen_kis_meyveleri = ["portakal", 'cilek', 'mandalina']
meyveler = {'yaz_meyveleri':
                {'sevdiklerimiz': {'avokado', 'guantanamo elması', 'Çarkıfelek'},
                 'sevmediklerimiz': ['elma', 'armut', 'kiraz']
                 },
            'kis_meyveleri': {
                'ozlediklerimiz': "portakal cilek mandalina",
                "efsaneler": 0
            }
            }
l_meyveler = [
    [
        ['avokado', 'guantanamo elması', 'Çarkıfelek'],
        ['elma', 'armut', 'kiraz']],
    [[],
     []]]
# koşullu ifadeler
degisken = ['a', 'b', 'c']
degisken2 = degisken
if degisken == degisken2:
    print("1")
    print(id(degisken), id(degisken2))
if degisken is degisken2:
    print("2")
print("İkinci ornek:\n\n")
degisken = ['a', 'b', 'c']
degisken2 = degisken[:]
if degisken == degisken2:
    print(id(degisken), id(degisken2))
    print("1")
if degisken is degisken2:
    print("2")
    print(id(degisken), id(degisken2))


# fonksiyonlar

# hata kontrol yapısı
# args ve kwargs
# birkaç tane varsayılan fonksiyonlar (len, type, range, )
# dosya işlemleri
