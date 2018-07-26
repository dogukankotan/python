meyveler = {'yaz_meyveleri':
                {'sevdiklerimiz': {'avokado', 'guantanamo elması', 'Çarkıfelek'},
                 'sevmediklerimiz': ['elma', 'armut', 'kiraz']
                 },
            'kis_meyveleri': {
                'ozlediklerimiz': "portakal cilek mandalina",
                "efsaneler": 0
            }
            }
# print(meyveler['yaz_meyvelerii'])
if meyveler.get("bahar_meyveleri"):
    print(meyveler.get("bahar_meyveleri"))
elif meyveler.get("sonbahar_meyveleri"):
    print(meyveler.get('sonbahar_meyveleri'))
else:
    meyveler.update({'bahar_meyveleri': {}})
    meyveler.update({'sonbahar_meyveleri': {}})

print(meyveler)