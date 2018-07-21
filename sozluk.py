sozluk = {'one':'bir', 'two':[2,10,3,1]}

#print(sozluk.get('two'))

#print(dir(sozluk))

sozluk['one'] = 1

# print(sozluk)

sozluk.update({'two':2})
sozluk.update({'three':3})
sozluk.update({1:'one'})
# print(sozluk)

sozluk['four'] = 4
#print(sozluk)

del sozluk['one']

#print(sozluk)

#print(sozluk.pop('two'))

#print(sozluk)
print(sozluk)
print(sozluk.keys())
print(sozluk.values())
print(sozluk.items())