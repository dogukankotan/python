def yazdir(kelime):
    print(kelime)
    return kelime

#degisken = yazdir('Meyve')
#print(degisken)

def args_yazdir(birinci, ikinci, *args):
    print(args)
    print(birinci)
    print(ikinci)

# args_yazdir(1,2,3,4,5,6)

def kwargs_yazdir(bir=1,**kwargs):
    print(kwargs)
    print(bir)

# kwargs_yazdir(iki=2, hasan=2)


def args_kwargs_yazdir(ilki, ikinci, *args, bir, hasan,
                       **kwargs):
    print(ilki)
    print(ikinci)
    print(args)
    print(bir)
    print(hasan)
    print(kwargs)

# args_kwargs_yazdir(6,7,8,9,8, hasan=2, bir=1, test=10)

def dongu():
    for i in range(1,10):
        yield str(i)

generator = dongu()
print(generator.__next__())
print(generator.__next__())
print(generator.__next__())
print(generator.__next__())
print('For')
for x in generator:
    print(x)