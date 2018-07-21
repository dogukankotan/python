def ortalama_hesapla(gecici_vize, gecici_final):
    if type(gecici_vize) == int and type(gecici_final) == int:
        if 0 < gecici_vize < 100 and 0 < gecici_final < 100:
            sonuc = (gecici_vize * 40 + gecici_final * 60) / 100
            if 0 < sonuc <= 40:
                print("Notunuz dc")
            elif 40 < sonuc <= 60:
                print("Notunuz cb")
            elif 60 < sonuc <= 80:
                print("Notunuz bb")
            elif 80 < sonuc <= 100:
                print("Notunuz aa")
            else:
                print("Tanımsız")
    else:
        print("Lütfen sayi giriniz")

ogr_1_vize = int(input("ilk ogrencinin vizesini giriniz"))
ogr_1_final = int(input("ilk ogrencinin finalini girin"))
ortalama_hesapla(ogr_1_vize, ogr_1_final)