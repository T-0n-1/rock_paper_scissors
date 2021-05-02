# Rock, Paper, Scissors -game

# määrittele ulkoiset kirjastot ja paketot
from pathlib import Path
import random
import os
from time import sleep


# Määrittele luokat (Class)


# Määrittele funktiot (def (functions))
def voittajanSelvitys(pelaajan_valinta, tietokoneen_valinta):
    kivi_paperi_sakset = {'k': 'kivi', 'p': 'paperi', 's': 'sakset'}
    pelaajan_valinta = kivi_paperi_sakset[pelaajan_valinta]
    tietokoneen_valinta = kivi_paperi_sakset[tietokoneen_valinta]
    print(f'{pelaajan_valinta:>19} ', end = '');sleep(0.4)
    print('.', end = '');sleep(0.6)
    print('.', end = '');sleep(0.6)
    print('. ', end = '');sleep(0.6)
    print(f'{tietokoneen_valinta}')
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
    cls()
    peliloop = True
    while peliloop:
        valintaloop = True
        while valintaloop:
            syöte = "[K]     kivi  "; print(f'{syöte:>30}')
            syöte = "[P]     paperi"; print(f'{syöte:>30}')
            syöte = "[S]     sakset"; print(f'{syöte:>30}')
            syöte = f"{nimi} anna valintasi"; print(f'{syöte:>19}', end = '')
            print('     Tietokoneen valinta')
            syöte = ">>> "; pelaajan_valinta = input(f'{syöte:>18}')
            pelaajan_valinta = pelaajan_valinta.lower()
            if pelaajan_valinta == 'k':
                valintaloop = False
            elif pelaajan_valinta == 'p':
                valintaloop = False
            elif pelaajan_valinta == 's':
                valintaloop = False
            else:
                pass
        tietokoneen_valinta = tietokoneenValinta()
        tulos = voittajanSelvitys(pelaajan_valinta, tietokoneen_valinta)
        if tulos == 'tasapeli':
            syöte = 'Tasapeli - uusintakierros'; print(f'{syöte:^43}')
            laskuri += 1
        elif tulos == 'häviö':
            syöte = '\nPeli päättyi tietokoneen voittoon,'; print(f'{syöte:^43}')
            syöte = '\nparempaa onnea ensi kerralla.'; print(f'{syöte:^43}')
            laskuri += 1
            sleep(7)
            peliloop = False
        elif tulos == 'voitto':
            syöte = f'\nOnneksi olkoon {nimi}, voitit tietokoneen.'; print(f'{syöte:^43}')
            lisaaVoitto(nimi, tilasto)
            syöte = f'Olet voittanut {tilasto[nimi]} kertaa'; print(f'{syöte:^43}')
            laskuri += 1
            sleep(7)
            peliloop = False
        else:
            pass
    tilasto['laskuri'] = laskuri
    tallennaTilasto(tilasto)
    cls()
    return tilasto


def tietokoneenValinta():
    vaihtoehdot = ['k', 'p', 's']
    arvaus = random.choice(vaihtoehdot)
    return arvaus


def tulostaParhaatPelaajatLista(tilasto):
    parhaat_pejaalat = sorted(tilasto.items(), key=lambda kv:kv[1], reverse=True)
    if tilasto == {}:
        pass
    else:
        del parhaat_pejaalat[0]
    pelaaja = ''
    voitot = ''
    player = 'pelaaja'
    wins = 'voittoja'
    cls()
    print('\n\n************ Parhaat pelaajat ************')
    print(f'  pelattuja kierroksia            {laskuri:>6}  \n')
    print(f'  {player:<19}{wins:>19}  ')
    for item in parhaat_pejaalat:
        txt = str(item)
        pelaaja, voitot = txt.split(',')
        pelaaja = pelaaja.lstrip("('")
        pelaaja = pelaaja.rstrip("'")
        voitot = voitot.rstrip(')')
        print(f'  {pelaaja:<19}{voitot:>19}  ')
    print('******************************************')


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
    cls()
    return nimi


# määrittele muuttujat
global nimi, tilasto, laskuri, cls
nimi = ''
tilasto = {}
# tilasto['laskuri'] = 0
menuloop = True
valinta = ''
arvaus = ''
laskuri = 0
cls = lambda: os.system('clear')


# PÄÄOHJELMA
tilasto_tiedosto = Path('tilasto.txt')
if tilasto_tiedosto.exists():
    lataaTilasto()
    laskuri = tilasto['laskuri']
else:
    pass
cls()
print('**************** Kivi, paperi, sakset -peli ****************')
print('*                                                          *')
print('*   Pelaa peliä tietokonetta vastaan.                      *')
print('*   Peli kerää pelatuista kierroksista tilastoa ja         *')
print('*   tallentaa myös pelaajan voittojen lukumäärän.          *')
print('*   Peli näyttää halutessasi Parhaimmat Pelaajat -listan.  *')
print('*                                                          *')
print('************************************************************')
while menuloop:
    if not nimi:
        print('\nEi määritetty pelaajaa - aloita antamalla pelaajana nimi.\n')
    else:
        print(f'\n* * *       Pelikierros nro: {laskuri}\n* * *       Pelaaja:   {nimi}')
    syöte = """ 
            Valikko
            [N]   Anna/Vaihda pelaajan nimi
            [P]   Pelaa Kivi, Paperi, Sakset -peliä
            [L]   Tulosta Parhaat Pelaajat
            [Q]   Lopeta peli
            
            Valintasi: """
    valinta = input(syöte)
    valinta = valinta.lower()
    print('\n\n')
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



