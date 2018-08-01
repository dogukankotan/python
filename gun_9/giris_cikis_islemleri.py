class Kullanici:
    def __init__(self, k_adi, parola, eposta,
                 isim, soyisim):
        self.k_adi = k_adi
        self.parola = parola
        self.eposta = eposta
        self.isim = isim
        self.soyisim = soyisim
        if not self.varlik_kontrolu(self.k_adi):
            with open("veritabani.txt", "a+") as dosya:
                dosya.write("|".join(self.__dict__.values()) + "\n")

    @staticmethod
    def varlik_kontrolu(k_adi):
        kullanicilar = {}
        with open("veritabani.txt", 'r') as dosya:
            str_kullanicilar = dosya.read()
            for klnclr in str_kullanicilar:
                kullanicilar[klnclr] = Kullanici(*klnclr)
        if k_adi in kullanicilar.keys():
            return True
        return False


class EyesBook:
    kullanicilar = []

    def __init__(self):
        with open('veritabani.txt', 'r') as dosya:
            str_kullanicilar = dosya.read()
            self.kullanicilar = [Kullanici(*x) for x in str_kullanicilar]

    def menu(self):


    def kayit(self):
        if Kullanici.varlik_kontrolu("10"):
            pass
        pass

    def giris(self):
        pass


if __name__ == '__main__':
    # mailde @ sarti arasin
    # daha once kaydoldu mu?
    # online kullanicilari listele
    # kullanici online ise giriş yapamasın
    ornek = Kullanici("Excalibur_13", "123", "s@s.com", "Sezer", "Haznedaroglu")
