from gun_4.dosya_acc import dosya_ac

def dosya_oku(dosya):
    return dosya.read()

def dosya_yaz(*args):
    yeni_dosya = open(args[1], 'w')
    yeni_dosya.write(args[0])

# dosya.txt dosyasını başka dosyaya kopyalayın

dosya = dosya_ac('dosya.txt')
icerik = dosya_oku(dosya)
dosya_yaz(icerik, 'yeni_dosya3.txt')