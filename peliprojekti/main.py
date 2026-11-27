import json
from esineet import Esine, Luettava
from huoneet import Huone, Tyhja
from mekanismit import Mekanismi, Este, Kaivinkone
from pelaaja import Pelaaja
import glob

from flask import Flask, request # DEBUG - FLASK ON LOPULLISESSA VERSIOSSA ERIKSEEN?

app = Flask(__name__) # DEBUG - FLASK ON LOPULLISESSA VERSIOSSA ERIKSEEN?

# def paavalikko():
#     while True:
#         try:
#             numerovalinta = input ("\nMinkä komennon haluatte suorittaa?\n1: Uusi peli\n2: Lataa peli\n3: Poistu pelistä\nVastaus: ")
#             break
#         except ValueError:
#             print ("Kirjoittakaa joku edellä olevista numeroista. Pliide.")
#     return numerovalinta

# while True:
#     pelaajan_nimi = input("Mikä on nimenne?\nVastaus: ") # DEBUG - LAITA PÄÄLLE LOPULLISESSA VERSIOSSA
#     if pelaajan_nimi == "":
#         print ("Yritetäänpä uudelleen.")
#     else:
#         break

# while True:
#     try:
#         pelaajan_ika = int(input("Mikä on ikänne?\nVastaus kokonaislukuna: ")) # DEBUG - LAITA PÄÄLLE LOPULLISESSA VERSIOSSA
#         break
#     except ValueError:
#         print ("Kirjoittakaa kokonaisluku.")
# if pelaajan_ika < 0:
#     print ("\nHyvä läppä.")
#     quit
# if pelaajan_ika < 12:
#     print ("\nOlette alaikäinen. Ette voi pelata.")
#     quit

# # pelaajan_nimi = ("Testeri") # DEBUG - LAITA POIS LOPULLISESSA VERSIOSSA
# # pelaajan_ika = 20 # DEBUG - LAITA POIS LOPULLISESSA VERSIOSSA


# -- Huoneet --

huone_2_2 = Huone("Asunto", "auto", "auto", "auto", "auto", "asunnossanne", "Niin paljon huonekaluja, perheen muistoesineitä ja kodinkoneita... Mitään niistä ei voi juoda. Jatkakaa.")
huone_2_3 = Huone("Käytävä", "auto", "auto", huone_2_2, "auto", "asuntorakennuksen käytävässä", "Todella ränsistynyttä! Hmm. Ramin etuovi pohjoisessa on auki..?")
huone_2_4 = Huone("Ramin asunto", "auto", "auto", huone_2_3, "auto", "ramin asunnossa", "Asunto on tyhjä? Hän aina valitti köyhyyttään, mutta tämä tuli yllätyksenä. Hetkinen, lattialla on lappu...")
huone_3_3 = Huone("Eteinen", "auto", "auto", "auto", huone_2_3, "eteisessä", "Näissä etuoven asunnoissa kuulee varmaan jokaisen sisääntulijan. Siis kuuli.", False, True, False, False)
huone_3_4 = Huone("Irenen asunto", "auto", "auto", huone_3_3, "auto", "Irenen asunnossa", "Irene oli yksi ensimmäisistä, jotka lähtivät täältä. Itse ette pitänyt sitä hyökyaaltoa juuri minään. Ettekä vieläkään pidä.")

huone_4_3 = Huone("Katu", "auto", "auto", "auto", huone_3_3, "jalkakäytävällä", "Olittekin unohtanut, kuinka paksua ilma oli... Olisi pitänyt ainakin *harkita* sitä hybridiautoa.")
huone_5_3 = Huone("Presidentin huvila, ulko-ovi", "auto", "auto", "auto", huone_4_3, "presidentin huvilan ulko-ovella", "Nyt vain etsitään keino sisään.")
huone_5_4 = Huone("Presidentin huvila, pergola", "auto", "auto", huone_5_3, "auto", "presidentin huvilan pergolassa", "Mietitte, minne presidentti mahtoi mennä. Naapurinne ainakin pakenivat Pirkanmaan väestönsuojiin.")
huone_6_4 = Huone("Presidentin huvila, heikko seinä", "auto", "auto", "auto", huone_5_4, "presidentin huvilan heikon seinän luona", "Katsos, kaivinkone. Romutetaanpa tuo seinä!", False, False, True)

huone_5_2 = Huone("Presidentin huvila, puutarha", huone_5_3, "auto", "auto", "auto", "presidentin huvilan puutarhassa", "Ei ole kukkia. On vain levää... Jos mikään enää tuoksuisi, ette tiedä, tuoksuisiko tämä miljöö miltään.")
huone_6_2 = Huone("Presidentin huvila, takapiha", "auto", "auto", "auto", huone_5_2, "presidentin huvilan takapihalla", "Tuolla ylhäällä on ikkuna. Jotenkin pitäisi kiivetä sinne.", True)

huone_u_1 = Huone("Tunnelin alku", Tyhja(), "auto", "auto", "auto", "tunnelin alussa", "Ette pääse enää takaisin. On pimeää. Seuratkaa ilmavirtaa.")
huone_u_0 = Huone("ei mitään?", "auto", huone_5_2, huone_u_1, "auto", "maakuopan ympärillä", "Tuolla on jotain... Hypätkää alas. Ilma ottaa kopin.")
huone_u_2 = Huone("Tunneli", "auto", "auto", "auto", huone_u_1, "jossain päin tunnelia")
huone_u_3 = Huone("Tunneli", "auto", "auto", "auto", huone_u_2, "jossain päin tunnelia")
maali = Huone("Presidentin huvila, KEITTIÖ", huone_6_4, "auto", huone_6_2, "auto", "presidentin huvilan keittiössä", "TÄÄLLÄ ON VETTÄ.")
huone_u_4 = Huone("Tunneli", maali, "auto", "auto", huone_u_3, "jossain päin tunnelia")


for huone in Huone.lista_huoneista:
    huone.korjaa_huoneet()

# -- Esineet --

rami_lappu_1 = Luettava("Ramin lappu", 0.1, ("Tilapäinen")) # Teksti korvataan uuden maailman luomisen tai pelin lataamisen yhteydessä.
rami_lappu_2 = Luettava("Ramin lappu 2", 0.1, ("Tilapäinen")) # Teksti korvataan uuden maailman luomisen tai pelin lataamisen yhteydessä.
irene_kirja = Luettava("Sensaatiolehti", 0.6, "Selaatte lehteä: 'VESI TAPPAA MEIDÄT KAIKKI! * \nalan huipputieteilijät ovat ennustaneet, että vuoteen 2600 mennessä ihmiskunta saa kärsiä historian rankimman hyökyaallon. Katukaa syntejänne ja tilatkaa SENSAATIOLEHTI PLUS, ja me ehkä selviämme!!!       \n* Astrologian'")
lore_dump = Luettava("Ramin lappu 0", 0.2, "Lapussa lukee: 'Niin se sitten meni. Hyökyaalto saapui, ja nousi nousemistaan. Jos satelliitit toimisivat enää, näkymä olisi aaaika kiinnostava. Itse olen ainakin samaa mieltä niiden astrologien kanssa, että nyt, kun *vettä* on hirveän *paljon* ja *ilmaa* niin *vähän*, voitaisiin vaihtaa niiden nimet. Nyt me hengitämme vettä ja juomme ilmaa. Onneksi kävin sillä kesäleirillä. Opinpa sukeltamaan!'")
tikkaat = Esine("Tikkaat", 10, "Uimataidottomat pääsevät näillä korkeuksiin.")
malja = Luettava("Graalin malja", 1, "\n¨'-.    VOITITTE         ,-^-.__,,_,.-'-.___\n     `^-._+' .   `+_,--'\n      PELIN_,.--''\nOlette saaneet vettä janoonne. Juodessanne graalista mietitte, onko avaruutta enää edes olemassa.\nVoitte jatkaa pelaamista, jos jotain jäi hampaan väliin.", True)

# -- Mekanismit (eivät muutu tallennustiedoston mukaan, joten lisätään täällä) --

kasa = Este("Kasa huonekaluja", huone_3_3, "Siirsitte huonekalut pois etuoven tieltä. Kova urakka. Eivätpä estäneet tulvaa. Eivätkä janovuosia.", True, "auto", False, "auto", "auto")
huone_3_3.lisaa_mekanismi(kasa)
ikkuna = Este("Ikkuna", huone_6_2, "Pääsitte ikkunan luokse ja avasitte sen.", False, False, "auto", "auto", "auto", tikkaat)
huone_6_2.lisaa_mekanismi(ikkuna)
global kaivinkone
kaivinkone = Kaivinkone("Kaivinkone", huone_6_4)
huone_6_4.lisaa_mekanismi(kaivinkone)

pelaaja = Pelaaja("Tilapäinen", huone_2_2, 20)

# -- UUSI PELI --

@app.route("/peli_uusi/<pelaajan_nimi>/<pelaajan_ika>") # DEBUG - FLASK ON LOPULLISESSA VERSIOSSA ERIKSEEN?
def peli_uusi(pelaajan_nimi, pelaajan_ika):
    # Uusi peli alkaa. Alustetaan se asettamalla kaikki paikoilleen. Tekisi mieli ladata tämäkin vain .json-tiedostosta, mutta ei jaksa.

    huone_2_4.lisaa_esine(rami_lappu_1)
    huone_3_4.lisaa_esine(rami_lappu_2)
    huone_3_4.lisaa_esine(irene_kirja)
    huone_u_1.lisaa_esine(lore_dump)
    huone_6_4.lisaa_esine(tikkaat)
    maali.lisaa_esine(malja)
    global pelaaja # Jotta pelaajan vuoro -funktio voisi lukea ja mutatoida pelaajaa
    pelaaja.nimi = pelaajan_nimi
    pelaaja.ika = pelaajan_ika

    # Päivitetään vielä Ramin laput sisältämään pelaajan nimi.

    rami_lappu_1.teksti = (f"Lapussa lukee: '{pelaaja.nimi}, minun lähdettyäni olet ainoa sielu koko kylässä.\nEn ole dorka; tiedän, että huomasit, kuinka varastin pressan huvilasta juomavettä kaikki nämä vuodet. Aion jättää tämän tiedon sinulle, hyvä ystäväni. Eksäni talossa on lisää tietoa. Ainoa nainen koko rakennuksessa.'")
    rami_lappu_2.teksti = (f"Lapussa lukee: '{pelaaja.nimi}, pressan huvilaan on kolme reittiä. Ikkuna, seinästä läpi tai piilotettu, maanalainen tunneli. Aukinainen ikkuna on rakennuksen eteläisessä seinässä, heikko muuraus pohjoisessa ja tunneli on kadun lähellä piilossa.'")

    return pelin_data(pelaaja, "Olette asunnossanne. Nukuitte niin huonosti...", "1. Liiku\n2. Katso ympärille\n3. Käytä esine tavaraluettelossa\n4. Nouki esine ympäristöstä\n5. Vuorovaikuta mekanismin kanssa\n0. Tallenna peli")

# -- PELIN LATAAMINEN --

@app.route("/tallennukset")
def listaa_tallennukset():
    tallennukset = glob.glob("*.json")
    return tallennukset

@app.route("/peli_lataa/<tallennus>")
def peli_lataa(tallennus):
    with open (f"{tallennus}", "r") as tallennus:
        data_luettu = json.load(tallennus)

    # Tyhjennetään olemassa oleva data siltä varalta, että toinen peli ladataan kesken pelin
    pelaaja.esineet = []
    pelaaja.tilavuus = 0
    pelaaja.nykyinen_valikko = "pelaajavalikko"

    pelaaja.nimi = data_luettu["pelaajan nimi"]
    pelaaja.ika = data_luettu["pelaajan ikä"]

    pelaajan_esineet = data_luettu["pelaajan esineet"]
    pelaajan_sijainti = data_luettu["pelaajan sijainti"]

    for huone in Huone.lista_huoneista:
        huone.esineet = [] # Tyhjennetään olemassa oleva data
        huone.pohjoinen_estetty, huone.ita_estetty, huone.etela_estetty, huone.lansi_estetty = data_luettu[str(huone.id) + "esteet"]
        if huone.id == pelaajan_sijainti:
            pelaaja.sijainti = huone
        for esine_id in data_luettu[str(huone.id) + "esineet"]: # Käydään läpi kaikki esineet kaikissa huoneissa
            for esine in Esine.lista_esineista:
                if esine.id == esine_id:
                    huone.lisaa_esine(esine)

    for esine_id in pelaajan_esineet:
        for esine in Esine.lista_esineista:
            if esine.id == esine_id:
                pelaaja.lisaa_esine(esine)

    # Päivitetään vielä Ramin laput sisältämään pelaajan nimi.

    rami_lappu_1.teksti = (f"Lapussa lukee: '{pelaaja.nimi}, minun lähdettyäni olet ainoa sielu koko kylässä.\nEn ole dorka; tiedän, että huomasit, kuinka varastin pressan huvilasta juomavettä kaikki nämä vuodet. Aion jättää tämän tiedon sinulle, hyvä ystäväni. Eksäni talossa on lisää tietoa. Ainoa nainen koko rakennuksessa.'")
    rami_lappu_2.teksti = (f"Lapussa lukee: '{pelaaja.nimi}, pressan huvilaan on kolme reittiä. Ikkuna, seinästä läpi tai piilotettu, maanalainen tunneli. Aukinainen ikkuna on rakennuksen eteläisessä seinässä, heikko muuraus pohjoisessa ja tunneli on kadun lähellä piilossa.'")

    return pelin_data(pelaaja, "Tervetuloa takaisin", "1. Liiku\n2. Katso ympärille\n3. Käytä esine tavaraluettelossa\n4. Nouki esine ympäristöstä\n5. Vuorovaikuta mekanismin kanssa\n0. Tallenna peli")

# -- PELAAJAN OHJAAMINEN -- 

@app.route("/pelaajan_vuoro/<numerovalinta>") # DEBUG - FLASK ON LOPULLISESSA VERSIOSSA ERIKSEEN?
def pelaajan_vuoro(numerovalinta): # Jokainen pelaajan valinta kulkee tämän funktion kautta.
    tarinateksti = pelaaja.sijainti.kuvaus
    tieto2 = ""
    numerovalinta = int(numerovalinta)

    if pelaaja.nykyinen_valikko == "pelaajavalikko":
        tieto2 = "1. Liiku\n2. Katso ympärille\n3. Käytä esine tavaraluettelossa\n4. Nouki esine ympäristöstä\n5. Vuorovaikuta mekanismin kanssa\n0. Tallenna peli"
        if numerovalinta == 1: # Liiku
            pelaaja.nykyinen_valikko = "liikkuminen"
            tarinateksti = "Mihin suuntaan haluatte liikkua?"
            tieto2 =  "1: pohjoinen\n2: itä\n3: etelä\n4: länsi"

        elif numerovalinta == 2: # Katso ympärille
            tarinateksti = pelaaja.katso_ymparille()

        elif numerovalinta == 3: # Käytä esine tavaraluettelossa
            pelaaja.nykyinen_valikko = "valitse esine"
            tarinateksti = pelaaja.luettele_esineet()
            tieto2 = "Valitkaa esinettä vastaava numero."

        elif numerovalinta == 4: # Nouki esine ympäristöstä
            pelaaja.nykyinen_valikko = "nouki esine"
            tarinateksti = pelaaja.sijainti.luettele_esineet()
            tieto2 = "Valitkaa esinettä vastaava numero."

        elif numerovalinta == 5: # Vuorovaikuta mekanismin kanssa
            pelaaja.nykyinen_valikko = "vuorovaikuta mekanismin kanssa"
            tarinateksti = pelaaja.sijainti.luettele_mekanismit()
            tieto2 = "Valitkaa mekanismia vastaava numero."

        elif numerovalinta == 0:
            tallenna_peli(pelaaja)

        else:
            print("Invalidi valinta")

    # -- LIIKKUMISVALIKKO (1) --

    elif pelaaja.nykyinen_valikko == "liikkuminen":
        if numerovalinta == 1: # Pohjoinen
            pelaaja.liiku("P")
        elif numerovalinta == 2: # Itä
            pelaaja.liiku("I")
        elif numerovalinta == 3: # Etelä
            pelaaja.liiku("E")
        elif numerovalinta == 4: # Länsi
            pelaaja.liiku("L")
        elif numerovalinta == 0:
            tallenna_peli(pelaaja)
        else:
            print("Invalidi valinta")
        tarinateksti = pelaaja.sijainti.kuvaus
        tieto2 = "1. Liiku\n2. Katso ympärille\n3. Käytä esine tavaraluettelossa\n4. Nouki esine ympäristöstä\n5. Vuorovaikuta mekanismin kanssa\n0. Tallenna peli"

        pelaaja.nykyinen_valikko = "pelaajavalikko"

    # -- KAIVINKONEEN VALIKKO --

    elif pelaaja.nykyinen_valikko == "kaivinkone":
        tarinateksti = kaivinkone.toiminto(pelaaja, numerovalinta)
        tieto2 = "1: Kahva vasemmalla\n2: Kahva edessänne\n3: Kahva etuoikealla\n4: Kahva keskioikealla\n5: Kahva oikealla\n6: Poljin vasemmalla\n7: Poljin keskellä\n8: Poljin oikealla\n9: Avaimet\n10: Nappi vieressänne\n0: POIS TÄÄLTÄ"

    # -- TAVARALUETTELOVALIKKO (3) --

    elif pelaaja.nykyinen_valikko == "valitse esine":
        try:
            if numerovalinta == 0:
                tallenna_peli(pelaaja)
            else:
                global esinevalinta
                esinevalinta = numerovalinta
                pelaaja.nykyinen_valikko = "käytä/pudota esine"
        except ValueError:
                print ("Kirjoittakaa esineen numero ylhäällä olevan listan perusteella.")
                pelaaja.nykyinen_valikko = "pelaajavalikko"
        except IndexError:
                print ("Numero ei ole listalla.")
                pelaaja.nykyinen_valikko = "pelaajavalikko"
        tarinateksti = "Haluatteko käyttää vai pudottaa esineen?"
        tieto2 = "1: Käytä\n2: Pudota"

    # -- TAVARALUETTELON KÄYTÄ TAI PUDOTA -VALIKKO (3) --

    elif pelaaja.nykyinen_valikko == "käytä/pudota esine":
        if numerovalinta == 1:
            tarinateksti = pelaaja.kayta_esine(esinevalinta)
        elif numerovalinta == 2:
            tarinateksti = pelaaja.pudota_esine(esinevalinta)
        elif numerovalinta == 0:
            tallenna_peli(pelaaja)
        else:
            print("Invalidi valinta")
        tarinateksti = pelaaja.sijainti.kuvaus
        tieto2 = "1. Liiku\n2. Katso ympärille\n3. Käytä esine tavaraluettelossa\n4. Nouki esine ympäristöstä\n5. Vuorovaikuta mekanismin kanssa\n0. Tallenna peli"
        pelaaja.nykyinen_valikko = "pelaajavalikko"

    # -- ESINEEN NOUKKIMISVALIKKO (4) --

    elif pelaaja.nykyinen_valikko == "nouki esine":
        try:
            if numerovalinta == 0:
                tallenna_peli(pelaaja)
            else:
                numerovalinta -= 1
                if numerovalinta < len(pelaaja.sijainti.esineet):
                    hyvaksynta, tarinateksti = pelaaja.lisaa_esine(pelaaja.sijainti.esineet[numerovalinta])
                    if hyvaksynta == True: # Eli jos lisaa_esine -metodi hyväksyy tämän.
                        pelaaja.sijainti.esineet.pop(numerovalinta)
        except ValueError:
            print ("Kirjoittakaa esineen numero ylhäällä olevan listan perusteella.")
        except IndexError:
            print ("Numero ei ole listalla.")
        tarinateksti = pelaaja.sijainti.kuvaus
        tieto2 = "1. Liiku\n2. Katso ympärille\n3. Käytä esine tavaraluettelossa\n4. Nouki esine ympäristöstä\n5. Vuorovaikuta mekanismin kanssa\n0. Tallenna peli"
        pelaaja.nykyinen_valikko = "pelaajavalikko"

    # -- MEKANISMIVALIKKO (5) --
    
    elif pelaaja.nykyinen_valikko == "vuorovaikuta mekanismin kanssa":
        pelaaja.nykyinen_valikko = "pelaajavalikko" # Tämä on alussa, jotta kaivinkone voisi ylikirjoittaa nykyisen valikon.
        try:
            if numerovalinta == 0:
                tallenna_peli(pelaaja)
            else:
                numerovalinta -= 1
                if numerovalinta < len(pelaaja.sijainti.mekanismit):
                    tarinateksti = pelaaja.sijainti.mekanismit[numerovalinta].kayta_mekanismi(pelaaja)
        except ValueError:
            print ("Kirjoittakaa mekanismin numero yllä olevan listan perusteella.")
        except IndexError:
            print ("Numero ei ole listalla.")
        tarinateksti = pelaaja.sijainti.kuvaus
        tieto2 = "1. Liiku\n2. Katso ympärille\n3. Käytä esine tavaraluettelossa\n4. Nouki esine ympäristöstä\n5. Vuorovaikuta mekanismin kanssa\n0. Tallenna peli"

    return pelin_data(pelaaja, tarinateksti, tieto2)
# --------------------------

# # -- Tallentaminen --

def pelin_data(pelaaja, tarinateksti, tieto2):
    tallennus_data = {
        "pelaajan nimi": pelaaja.nimi,
        "pelaajan ikä": pelaaja.ika,
        "pelaajan esineet": pelaaja.serialisoi_esineet(),
        "pelaajan tavaraluettelotila": pelaaja.tilavuus,
        "pelaajan sijainti": pelaaja.sijainti.id,
        "pelaajan valikko": pelaaja.nykyinen_valikko,
        "tarinateksti": tarinateksti,
        "tieto2": tieto2
    }

    for huone in Huone.lista_huoneista:
            tallennus_data[str(huone.id) + "esineet"] = huone.serialisoi_esineet()
            tallennus_data[str(huone.id) + "esteet"] = huone.serialisoi_esteet()

    return tallennus_data

def tallenna_peli(pelaaja):
    with open (f"{pelaaja.nimi}.json", "w") as tallennus:
        json.dump(pelin_data(pelaaja, "Tervetuloa takaisin", "1: Liiku\n2: Katso ympärille\n3: Käytä esine tavaraluettelossa\n4: Nouki esine ympäristöstä\n5: Vuorovaikuta mekanismin kanssa\n0: Tallenna peli"), tallennus)

if __name__ == '__main__': # DEBUG - FLASK ON LOPULLISESSA VERSIOSSA ERIKSEEN?
    app.run(host='127.0.0.1', port=3000, use_reloader=True) # DEBUG - FLASK ON LOPULLISESSA VERSIOSSA ERIKSEEN?
