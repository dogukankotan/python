class Kullanici:
    def __init__(self, k_adi, parola, eposta,
                 isim, soyisim, veritabani="ogrenciler.txt"):
        self.k_adi = k_adi
        self.parola = parola
        self.eposta = eposta
        self.isim = isim
        self.soyisim = soyisim
        self.veritabani = veritabani
        if not self.varlik_kontrolu(self.k_adi):
            with open(veritabani, "a+") as f:
                f.write("{}|{}|{}|{}|{}\n".format(self.k_adi,
                                                  self.parola,
                                                  self.eposta,
                                                  self.isim,
                                                  self.soyisim))

    @staticmethod
    def varlik_kontrolu(k_adi, veritabani="ogrenciler.txt"):
        kullanicilar = []
        with open(veritabani, 'r') as f:
            str_kul = f.readlines()
            kullanicilar.extend([x.split("|")[0] for x in str_kul])
        resp = list(filter(lambda x: x == k_adi, kullanicilar))
        return bool(len(resp))

    def goruntule(self):
        print(f"Kullanici Adı:\t{self.k_adi}\n"
              f"Eposta:\t{self.eposta}\n"
              f"İsim:\t{self.isim}\n"
              f"Soyisim:\t{self.soyisim}\n\n")


class EyesBook:
    kullanicilar = []

    def __init__(self):
        pass

    def kayit(self, k_adi, parola, isim, soyisim, eposta):
        self.kullanicilar.append(Kullanici(k_adi=k_adi, parola=parola, isim=isim, soyisim=soyisim, eposta=eposta))

    def giris(self,k_adi, parola):
        if not Kullanici.varlik_kontrolu(k_adi):
            pass
        else:
            pass

    def tumunu_goruntule(self):
        pass


if __name__ == '__main__':
    # mailde @ sarti arasin
    # daha once kaydoldu mu?
    # online kullanicilari listele
    # kullanici online ise giriş yapamasın
    # ornek = Kullanici("Excalibur_13", "123", "s@s.com", "Sezer", "Haznedaroglu")
    # resp = Kullanici.varlik_kontrolu("Excalibur_133")
    # ornek.goruntule()
    # print(resp)

    eyesbook = EyesBook()
    print("EyesBook'a hos geldiniz")
    while True:

        secenek = input("Kayit icin 1'e basiniz\n"
                        "Giris icin 2'ye basiniz\n")

        if secenek == "1":
            k_adi = input("kullanici adini girin: ")
            parola = input("parolayi giriniz: ")
            eposta = input("epostanızı giriniz: ")
            isim = input("isminizi giriniz: ")
            soyisim = input("soyisminizi giriniz: ")
            eyesbook.kayit(k_adi, parola, isim, soyisim, eposta)

        elif secenek == "2":
            k_adi = input("kullanici adini girin: ")
            parola = input("parolayi giriniz: ")
            eyesbook.giris(k_adi, parola)

        else:
            break
