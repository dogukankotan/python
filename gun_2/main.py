ornek = "Bu gun hava cok guzel"
ozel_sayim = 13
# print(ornek.capitalize())
# print(ornek.upper())
# print("Bu gun Hava durumu:" + str(ozel_sayim))
# print("Bu gun hava durumu: {}".format(ornek))
# print("Bu gun hava durumu: ", ozel_sayim, ornek)
# print(ozel_sayim == None)

meyveler = ["elma", "armut", "ananas"]
# print(meyveler.append("kiraz"))
# print(meyveler)
meyveler.insert(1, "avokado")
ozel_sayilar = [10,2,5,21,16]
ozel_sayilar.sort()

varsayilan_not = { "vize": 0, "final": 0}
ogrenciler = {
    'Sezer Bozkir': {'vize': 80, "final": 90},
    'Fatmanur Bilke': {'vize': 60, "final": 100}
}
# print(ogrenciler.get('Enes Şahin'))

if ogrenciler.get('Enes Şahin') == None:
    ogrenciler.update({'Enes Şahin': varsayilan_not,
                       'Mustafa Ersoy': varsayilan_not})

# "Yaşar Celep"
# print(ogrenciler.get("Yaşar Celep", varsayilan_not))
# print(ogrenciler)
# print(ogrenciler.items())

for ogrenci, notu in ogrenciler.items():
    ogrenciler[ogrenci]['vize'] = 0

for key in ogrenciler:

# print(ogrenciler)

vize_final_notları = {}
for i in range(5):
    ogrenci_ismi = input('Öğrenci İsmi:')
    vize_notu = int(input('Vize Notu'))
    final_notu = int(input('Final Notu'))
    vize_final_notları.update({
        ogrenci_ismi:{'vize':vize_notu,
                      'final':final_notu}
    })

print(vize_final_notları)