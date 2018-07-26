ogrenciler = {
    '120101003': {'vize': 80, "final": 90},
    '120101004': {'vize': 60, "final": 100}
}

# with open("ogrencilerim", 'a+') as f:
#     for ogr_no, notlar in ogrenciler.items():
#         f.write("{} {} {}\n".format(ogr_no,
#                                     notlar.get('vize'),
#                                     notlar.get('final')))
veri_tabani = {}
with open('ogrencilerim', 'r') as f:
    okunan_ogrenciler = f.readlines()
    print(okunan_ogrenciler)
    for satir in okunan_ogrenciler:
        ogrenci = satir.strip().split(' ')
        veri_tabani.update({ogrenci[0]: dict(vize=ogrenci[1], final=ogrenci[2])})
print(veri_tabani)
