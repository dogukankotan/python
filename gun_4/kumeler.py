demet = ('a', 'b', 'c', 'a')
dizi = ['a', 'b', 'c', 'a']
kume = {'a', 'b', 'c', 'a'}

print(demet)
print(dizi)
print(kume)

print(set(dizi))

#yeni_kume = {{'a'}, 'a'}
#print(yeni_kume)

sehir = 'ankara'
sehir2 = 'istanbul'
sehir_kume = set(sehir)
# print(sehir_kume[0])
sehir2_kume = set(sehir2)

birlesik_kume = sehir_kume.union(sehir2_kume)
print(birlesik_kume)
dizi_birlesik_kume = list(birlesik_kume)
print(dizi_birlesik_kume)

print("-".join(sehir))
print("-".join(birlesik_kume))
print("\t".join(dizi_birlesik_kume))