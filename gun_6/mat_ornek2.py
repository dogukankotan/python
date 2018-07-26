# Kullanıcıdan bir zar tahmini alacak
# Doğru ise +1 puan, yanlışsa -1 puan
# Oyundan çıkınca puanını ekrana basacak
from math import sqrt
import random

def uzaklik(*args):
    sonuc = sqrt(
        (args[2]-args[0])**2
        +
        (args[3] - args[1])**2
    )
    return sonuc

def main():
    x1, y1, x2, y2 = random.randint(1,20), \
                     random.randint(1,20), \
                     random.randint(1,20), \
                     random.randint(1,20)

    sonuc = uzaklik(x1, y1, x2, y2)
    print(f"({x1}, {y1}) ile ({x2}, {y2}) "
          f"arasındaki uzaklık:{sonuc}")

main()