# r -> okuma
# r+ -> okuma ve yazma
# w -> yazma (dosya yoksa yaratmaz, varsa baştan yazar)
# w+ -> okuma ve yazma (dosya yoksa yaratır)
# a -> son satıra yazma
# a+ -> son satıra yazma ve okuma (dosya yoksa yaratır)
with open("ornek.txt", "r+") as f:
    komple = f.read()
    print(komple)
    print(f.tell())
    f.seek(0)
    ilk_5 = f.read(5)
    print(ilk_5)
    print(f.tell())
    f.seek(0)
    f.write("Ornek")
    # f.write("Yazdir")