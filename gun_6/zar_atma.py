# Kullanıcıdan bir zar tahmini alacak
# Doğru ise +1 puan, yanlışsa -1 puan
# Oyundan çıkınca puanını ekrana basacak
from random import randint
def tahmin_sonucu(tahmin):
    gelen_zar = randint(1,6)
    print(f"Kandırmıyorum {gelen_zar}")
    return gelen_zar == tahmin
    #return True if randint(1,6) == tahmin else False

def main():
    puan = 0
    print("Zar oyununa hoşgeldiniz.")
    while True:
        tahmini = int(input("Lütfen değer tahmin edin(çıkmak için 0 tuşlayın)"))
        if tahmini == 0:
            print("Oyundan çıkıyor.")
            break
        if 0 < tahmini < 7:
            sonuc = tahmin_sonucu(tahmini)
            if sonuc:
                print("Doğru tahmin!")
                puan +=1
            else:
                print("Yanlış tahmin")
                puan-=1
        else:
            print("Lütfen 1 ve 6 arasında sayi girin")
            continue

        print(f"Puanınız: {puan}")


main()