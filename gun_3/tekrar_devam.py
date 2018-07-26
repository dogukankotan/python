# sozluk yazimi
def ornek_fonksiyon(*args):
    print("ahmet", sep="#", end="\n\n")

def yazdirma(*args):
    yazdirilacaklar = args[:-2]
    bitirici = args[-1]
    ayirici = args[-2]
    for kelime in yazdirilacaklar:
        print(kelime, end='', sep='')
        print(ayirici, end='', sep='')
    #print(bitirici)
    print(*yazdirilacaklar, sep=ayirici, end=bitirici)

#yazdirma("ahmet", "mehmet", "ayşe", "fatma", '#22', 'bitirdik')

def kw_yazdirma(**kwargs):
    print(*kwargs.get('yazdiralacaklar'),
          sep=kwargs.get('ayirici'), end=kwargs.get('bitirici'))

# kw_yazdirma(yazdiralacaklar=["ahmet", "mehmet", "ayşe", "fatma"],
     #       ayirici='#22', bitirici='bitirdik')



def args_kwargs_yazdirma(*args,**kwargs):
    print(*args, sep=kwargs.get('ayirici'),
          end=kwargs.get('bitirici'))

sozluk = {
    'ayirici':'#',
    'bitirici':'bitirdim'
}
# **sozluk = ayirici='#', bitirici='bitirdim'
yazdiralacaklar = ["ahmet", "mehmet"]

args_kwargs_yazdirma(*yazdiralacaklar, **sozluk)