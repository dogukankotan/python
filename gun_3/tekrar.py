def us_alma(deger_1=1, deger_2=1):
    sonuc = deger_1 ** deger_2
    print("Sonuç: {}".format(sonuc))
    return sonuc
try:
    deger1= int(input("Lütfen ilk degeri giriniz."))
    deger2 = int(input("Lütfen ikinci değeri giriniz."))
    sonucu = us_alma(deger1, deger2)
except ValueError as e:
    print(e)
    print("Hata: Lütfen sayi degeri giriniz.")
except Exception as e:
    print(e)
    print("Bir hata oluştu :(")
else:
    print(sonucu)
# if type(deger1) == int and type(deger2) == int:
#     sonucu = us_alma(deger1, deger2)
#     print(sonucu)
# else:
#     print("Lutfen sayi degeri giriniz.")

def topla_cikarma(say1, say2, topla=True):
    return say1 + say2 if topla else say1 -say2
    # if topla:
    #     return say1 + say2
    # return say1 - say2

deger1= int(input("Lütfen ilk degeri giriniz."))
deger2 = int(input("Lütfen ikinci değeri giriniz."))

topla_cikarma(say2=deger1, say1=deger2)