def yazdir_soz():
    print('Merhaba Dünya')
    print('Merhaba Mars')

def iki_defa_yazir():
    yazdir_soz()
    yazdir_soz()

# iki_defa_yazir()

def dondur_soz():
    return "Merhaba Dünya"


def iki_yazdir(soz):
    print(soz)
    print(soz)
    iki_yazdir(soz)

# soz = dondur_soz()
# iki_yazdir(soz)


def hata_dondur():
    raise ValueError("Value Error verdi")

#int('a')
#hata_dondur()

def main(arg1=10):
    try:
        x = dondur_soz()
        # hata_dondur()
    except:
        print('Diğer Hata')
    else:
        print("Hata yok")
        print(x)
    finally:
        print('Sürekli Çalıştı')
    print(arg1)


def yeni(arg1=10):
    liste = list(range(1,20,3))
    print(liste)
    liste.sort(reverse=True)
    print(liste)
    print(arg1)
    
yeni()