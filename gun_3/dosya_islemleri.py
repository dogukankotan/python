# r -> read
# w -> write
# a -> append
# x -> create

dosya = open('dosya.txt', 'a')
dosya.write("Bunu da ekle")
# icerik = dosya.readlines()
#
try:
    dosya = open('dosya.txt', 'w')
    icerik = dosya.readlines()
    temizlenmis_icerik = []
    # for satir in icerik:
    #     temizlenmis_icerik.append(satir.strip())
    print(temizlenmis_icerik)
    icerik = [satir.strip() for satir in icerik]
    dosya.close()
except Exception:
    print("Dosya yoktur.")