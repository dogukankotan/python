# lambda map filter reduce

behzat_c = [5, 10, 2, 18, 21, 55]

def carpma(say, say2):
    return say * say2

a = lambda say1,say2: say1*say2
b = lambda deger: str(deger)

# def sayi_dondur():
#     for say in range(1,10):
#         return say
#         # return say
# print(sayi_dondur())
# print(sayi_dondur())
# print(sayi_dondur())
# siradaki = sayi_dondur()
# print(siradaki.__next__())
#print(siradaki.__next__())
# print(siradaki.__next__())

# print(b("ornek"))
#print(a(10,15))

# bir_dizi_var = [5,10,2,18,21,55]
# string_deger = []
# for deger in bir_dizi_var:
#     string_deger.append(str(deger))

yeni_deger = map(b, behzat_c)
# print(list(yeni_deger))
# print(list(yeni_deger))

# print(bir_dizi_var, string_deger, sep="\n")
# print(yeni_deger)

sonuc = filter(lambda say: say %2 == 0, behzat_c)
# print(list(sonuc))

from functools import reduce

print(behzat_c)
toplam = 0
for deg in behzat_c:
    toplam += deg

print(toplam)
resp = reduce(lambda x,y: x*y, behzat_c)
print(resp)