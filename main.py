# Rock, Paper, Scissors -game

# määrittele ulkoiset kirjastot ja paketot
from pathlib import Path
import random


# Määrittele luokat (Class)


# Määrittele funktiot (def (functions))
def voittajanSelvitys(pelaajan_valinta, tietokoneen_valinta):
    kivi_paperi_sakset = {'k': 'kivi', 'p': 'paperi', 's': 'sakset'}
    pelaajan_valinta = kivi_paperi_sakset[pelaajan_valinta]
    tietokoneen_valinta = kivi_paperi_sakset[tietokoneen_valinta]
    print(f'Tietokoneen valinta on {tietokoneen_valinta} ja pelaajan {pelaajan_valinta}.')
    if tietokoneen_valinta == pelaajan_valinta:
        tulos = 'tasapeli'
    elif tietokoneen_valinta == 'kivi':
        if pelaajan_valinta == 'sakset':
            tulos = 'häviö'
        elif pelaajan_valinta == 'paperi':
            tulos = 'voitto'
    elif tietokoneen_valinta == 'paperi':
        if pelaajan_valinta == 'kivi':
            tulos = 'häviö'
        elif pelaajan_valinta == 'sakset':
            tulos = 'voitto'
    elif tietokoneen_valinta == 'sakset':
        if pelaajan_valinta == 'kivi':
            tulos = 'voitto'
        elif pelaajan_valinta == 'paperi':
            tulos = 'häviö'
    return tulos


def pelaa(nimi, tilasto, laskuri):
    peliloop = True
    while peliloop:
        valintaloop = True
        while valintaloop:
            pelaajan_valinta = input(f'{nimi} anna valintasi (k - kivi, p - paperi tai s - sakset): ')
            pelaajan_valinta = pelaajan_valinta.lower()
            if pelaajan_valinta == 'k' or 'p' or 's':
                valintaloop = False
            else:
                pass
        tietokoneen_valinta = tietokoneenValinta()
        tulos = voittajanSelvitys(pelaajan_valinta, tietokoneen_valinta)
        if tulos == 'tasapeli':
            print('Tasapeli - uusintakierros.')
            laskuri += 1
        elif tulos == 'häviö':
            print('Peli päättyi tietokoneen voittoon, parempaa onnea ensi kerralla.')
            laskuri += 1
            peliloop = False
        elif tulos == 'voitto':
            print(f'Onneksi olkoon {nimi}, voitit tietokoneen.')
            lisaaVoitto(nimi, tilasto)
            print(f'Olet voittanut {tilasto[nimi]} kertaa')
            laskuri += 1
            peliloop = False
        else:
            pass
    tilasto['laskuri'] = laskuri
    tallennaTilasto(tilasto)
    return tilasto


def tietokoneenValinta():
    vaihtoehdot = ['k', 'p', 's']
    arvaus = random.choice(vaihtoehdot)
    return arvaus


def tulostaParhaatPelaajatLista(tilasto):
    parhaat_pejaalat = sorted(tilasto.items(), key=lambda kv:kv[1], reverse=True)
    del parhaat_pejaalat[0]
    pelaaja = ''
    voitot = ''
    print('*** *** Parhaat pelaajat *** ***')
    for item in parhaat_pejaalat:
        txt = str(item)
        txt = txt.strip("(")
        txt = txt.strip("'")
        txt = txt.strip(")")
        pelaaja, voitot = txt.split(',')
        pelaaja = pelaaja.strip("'")
        print(f'{pelaaja}       {voitot} voittoa')


def lisaaVoitto(nimi, tilasto):
    if nimi in tilasto:
        tilasto[nimi] += 1
    else:
        tilasto[nimi] = 1


def tallennaTilasto(tilasto):
    with open('tilasto.txt', 'w') as tiedosto:
        for key in tilasto.keys():
            tiedosto.write("%s,%s" % (key, tilasto[key]))
            tiedosto.write('\n')


def lataaTilasto():
    with open("tilasto.txt") as tiedosto:
        for rivi in tiedosto:
            rivi = rivi.rstrip('\n')
            avain, arvo = rivi.split(',')
            arvo = int(arvo)
            tilasto[avain] = arvo


def annaNimi():
    nimiloop = True
    while nimiloop:
        nimi = input('Anna kilpailijan nimi: ')
        if not nimi:
            pass
        else:
            nimiloop = False
    return nimi


# määrittele muuttujat
global nimi, tilasto, laskuri
nimi = ''
tilasto = {}
# tilasto['laskuri'] = 0
menuloop = True
valinta = ''
arvaus = ''
laskuri = 0


# PÄÄOHJELMA
tilasto_tiedosto = Path('tilasto.txt')
if tilasto_tiedosto.exists():
    lataaTilasto()
    laskuri = tilasto['laskuri']
else:
    pass
print('******** Kivi, paperi, sakset -peli ********')
print('')
print('   Pelaa peliä tietokonetta vastaan.')
print('   Peli kerää pelatuista kierroksista tilastoa ja')
print('   tallentaa myös pelaajan voittojen lukumäärän.')
print('   Peli näyttää halutessasi Parhaimmat Pelaajat -listan.')
print('')
while menuloop:
    if not nimi:
        print('Ei määritetty pelaajaa - anna pelaajan nimi ensin.')
    else:
        print(f'Pelaaja: {nimi}       * * *       Pelikierros nro: {laskuri}')
    valinta = input('Anna valintasi (n - anna pelaajan nimi, p = pelaa, l - tulosta Parhaat Pelaajat-lista ja q - lopeta): ')
    valinta = valinta.lower()
    if valinta == 'n':
        nimi = annaNimi()
    elif valinta == 'p':
        tilasto = pelaa(nimi, tilasto, laskuri)
        laskuri = tilasto['laskuri']
    elif valinta == 'l':
        tulostaParhaatPelaajatLista(tilasto)
    elif valinta == 'q':
        menuloop = False
    else:
        pass



