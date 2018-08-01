class Motorsiklet(object):
    def __init__(self, lastik):
        self._lastik = lastik
        self.__motor = 'Btwin'

    def gosterge(self):
        print(self._lastik)

    def get_lastik(self):
        return self._lastik

    def set_lastik(self, lastik):
        self._lastik = lastik

sezer_hocanin_chopperi = Motorsiklet(2)
sezer_hocanin_chopperi.set_lastik(10)
dogukan_hocanin_motoru = Motorsiklet(3)
print(sezer_hocanin_chopperi.get_lastik())
print(dogukan_hocanin_motoru.get_lastik())
print(sezer_hocanin_chopperi._lastik)
print(sezer_hocanin_chopperi.__motor)