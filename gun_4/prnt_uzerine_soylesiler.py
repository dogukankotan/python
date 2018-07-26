print("Hava cok guzel", sep='\t\t')
sansur = {
    'Hava': "H*va"
}
cumle = "Hava cok guzel"
for karakter in cumle:
    if karakter == " ":
        print('\t\t', end="")
        continue
    print(karakter, end="")
print()
# cumle = "\t\t".join(cumle.split(" "))

cumle = cumle.replace(' ', '\t\t')

print(cumle)

