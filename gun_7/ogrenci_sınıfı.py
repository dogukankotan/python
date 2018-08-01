class Ogrenci(object):

    def __init__(self, isim, soyisim, numara, anne_adi, baba_adi):
        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara
        self.anne_adi = anne_adi
        self.baba_adi = baba_adi

    def ogrenci_goruntule(self):
        print("N:{} İ:{} S:{}".format(
            self.numara, self.isim, self.soyisim))

    def anne_adi_degistir(self, cici_anne_adi):
        self.anne_adi = cici_anne_adi

sezer = Ogrenci('Sezer', 'Bozkır', 120101003, 'Gönül', 'Can')
sezer.isim = 'Doğukan'
sezer.ogrenci_goruntule()
