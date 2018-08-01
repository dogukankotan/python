ortak_deger = 10
def skor_yazdir(k_adi, puan):
    print(f"{k_adi} puan deger: {puan}")

def menu():
    print("Oyuna hosgeldiniz.")

if __name__ == '__main__':

    menu()
    k_adi = "John Doe"
    skor = "20"

    skor_yazdir(k_adi, skor)