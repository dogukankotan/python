ogrenciler = {
    '120101003': {'vize': 80, "final": 90},
    '120101004': {'vize': 60, "final": 100}
}
try:
    dosya = open('ogrenciler.txt', 'a+')
except Exception:
    dosya = open('ogrenciler.txt', 'x')

for ogr_no, notlar in ogrenciler.items():
    dosya.write("{} numarali ogrecinin vizesi: {} finali: {}\n".
        format(ogr_no,
        notlar.get('vize'), notlar.get('final')))

# r -> okuma
# r+ -> okuma ve yazma
# w -> yazma (dosya yoksa yaratmaz, varsa baştan yazar)
# w+ -> okuma ve yazma (dosya yoksa yaratır)
# a -> son satıra yazma
# a+ -> son satıra yazma ve okuma (dosya yoksa yaratır)

# ogrenci kayit islemi
# ogrenci silme
# ogrencileri goruntuleme
# ogrencileri temizleme
metin = ""
metin.sp