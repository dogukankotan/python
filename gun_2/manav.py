"""
Manav Uygulaması

1-) Ürün Ekle
2-) Ürün Sil
3-) Stok Görüntüle
"""

def menu():
    secenek=input("""
    1-) Ürün Ekle
    2-) Ürün Sil
    3-) Stok Görüntüle 
    """)
    return secenek

def main():
    try:
        secenek = int(menu())
        # try:
        #     secenek / 0
        # except ZeroDivisionError:
        #     print('Sıfıra bölünme hatası')
    except ValueError:
        print('Harf Girdiniz. Lütfen sayı girin.')
        main()
    else:
        if secenek == 1:
            menu1()
        elif secenek == 2:
            pass
        elif secenek == 3:
            pass

def menu1():
    print("Menü 1")


main()

