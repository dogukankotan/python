
# for ve while döngüsü
sayilar = []
for say in range(1,10):
    if say % 2 == 0:
        sayilar.append(say*say)

sayilar2 = [say*say for say in range(1,10) if say % 2 == 0]
print(sayilar2)