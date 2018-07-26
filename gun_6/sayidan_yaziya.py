def yazdir(say):
    birler = ["", "bir", "iki", "uc", "dort", "bes"]
    onlar = ["", "on", "yirmi", "otuz", "kırk", "elli"]
    yuzler = "yuz"
    basamak = len(say)
    if basamak == 1:
        if say == 0:
            print("sıfır")
        else:
            print(birler[say])
    elif basamak == 2:
        print(onlar[int(say[1])] + " " + birler[int(say[0])])
    elif basamak == 3:
        if say[0] != "1":
            print(birler[int(say[0])]+ " " + yuzler + " " + onlar[int(say[1])] + " " + birler[int(say[2])])
        else:
            print(yuzler + " " + onlar[int(say[1])] + " " + birler[int(say[2])])

sayi = input("Sayiyi giriniz?")
yazdir(sayi)
