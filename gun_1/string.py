test_degiskeni = "\r\n bu bir test değişkenidir     "

x = "5"
y = 1
z = int(x)/y

dogru = True
yanlis = False

liste = [x, y, x, "elma", dogru, z]
liste.append("armut")
liste.insert(0,"yeni")

# cikarilan = liste.pop(2)
# print(liste)

liste2 = [5,4,3,2,1]

liste.append(liste2)
#print(liste)
# print(liste[liste.index(liste2)])

liste.extend(liste2)
#print(liste)

liste3 = sorted(liste2)

# print(liste2)
# print(liste3)


liste4 = [2,6,1,9,10,1,2]

liste4.sort(reverse=True)
# print(liste4)
liste4.reverse()
# print(liste4)

# print(liste4.count(1)
#print(len(liste4))
print(min(liste4))

