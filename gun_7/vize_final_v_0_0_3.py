class Ogrenci:
    def __init__(self, isim, soyisim, numara, vize, final):
        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara
        self.vize = vize
        self.final = final

    def __str__(self):
       return f"""Ogrenci ismi: {self.isim}
              Ogrenci numarasi: {self.numara}
              Ogrenci ortalamasi: {self.ortalamasi()}"""

    def ortalamasi(self):
        return self.vize * 0.4 + self.final * 0.6

class Sinif:
    ogrenciler = []

    def ogrenci_ekle(self):
        try:
            isim = input("Ogrencinin ismi")
            soyisim = input("Ogrencinin soyismi")
            numarasi = input("Numarasi")
            vize = int(input("Ogrenci vizesi"))
            final = int(input("Ogrenci finali"))
            self.ogrenciler.append(Ogrenci(isim, soyisim,
                              numarasi,
                              final=final,
                              vize=vize))
            return True
        except Exception as e:
            print(e)
            return False

    def ogrencileri_goruntule(self):
        for ogrenci in self.ogrenciler:
            print(ogrenci)

    def ogrenci_sil(self):
        ogrenci_no = input("Öğrenci Numarası")
        self.ogrenciler = list(filter(lambda x: x.numara
                                                != ogrenci_no,
                                      self.ogrenciler))

    def sinif_ortalamasi(self):
        from functools import reduce
        ortalama = reduce(lambda x,y: x.ortalamasi()+y.ortalamasi(),
               self.ogrenciler) / len(self.ogrenciler)
        return ortalama

    def dosyaya_kaydet(self):
        with open("ogrenciler.txt", "w+") as f :
            for ogrenci in self.ogrenciler:
                # f.write(ogrenci.numara)
                # f.write(",")
                # f.write(ogrenci.isim)
                # f.write(",")
                # f.write(ogrenci.soyisim)
                # f.write(",")
                # f.write(str(ogrenci.vize))
                # f.write(",")
                # f.write(str(ogrenci.final))
                print(ogrenci, file=f)






    def dosyadan_oku(self):
        pass


if __name__ == '__main__':
    python_1b = Sinif()
    while True:
        secim = input("""
                       1) Ogrenci Ekle(e)
                       2) Ogrenci Sil(s)
                       3) Ogrencileri Goruntule(g)
                       4) Ortalamaları Goruntule (d)
                       5) Dosyaya kaydet (k)
                       6) Dosyadan oku (o)
                       7) Çıkış(c)\n""").lower()
        if secim == 'e':
            python_1b.ogrenci_ekle()
        elif secim == 'g':
            python_1b.ogrencileri_goruntule()
        elif secim == 's':
            python_1b.ogrenci_sil()
        elif secim == 'c':
            break
        elif secim == 'd':
            python_1b.sinif_ortalamasi()
        elif secim == 'k':
            python_1b.dosyaya_kaydet()
        elif secim == 'o':
            python_1b.dosyaya_kaydet()
        else:
            print("Bilinmeyen bir komut girdiniz.")

