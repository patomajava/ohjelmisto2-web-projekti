class Mekanismi():
    def __init__(self, nimi):
        self.nimi = nimi
        # Ei ID:tä, koska mekanismin sijainti ei muutu. Se lisätään sijaintiinsa main.py:n sisällä.

    def kayta_mekanismi(self, pelaaja):
        tarinateksti = (f"Käytitte mekanismin {self.nimi}.")
        return tarinateksti

    def kayta_esineella(self, pelaaja, esine):
        if esine in pelaaja.esineet:
            tarinateksti = (f"Käytitte mekanismin {self.nimi}.")
            return tarinateksti
        else:
            return ("Teiltä puuttuu jokin esine.")

class Este(Mekanismi):
    def __init__(self, nimi, vaikutusalue, toimintokuvaus = ("Käytitte mekanismin."), kertakayttoinen = False, esta_pohjoinen = False, esta_ita = False, esta_etela = False, esta_lansi = False, vaadittu_esine = "auto"):
        super().__init__(nimi)
        self.vaikutusalue = vaikutusalue # MINKÄ huoneen yhteydet muutetaan. Itse mekanismin sijainti on erikseen.
        self.toimintokuvaus = toimintokuvaus
        self.kertakayttoinen = kertakayttoinen
        self.esta_pohjoinen = esta_pohjoinen
        self.esta_ita = esta_ita
        self.esta_etela = esta_etela
        self.esta_lansi = esta_lansi
        self.vaadittu_esine = vaadittu_esine
        self.mekanismi_vaihe = True # Jos False, vaikutus on päinvastainen. Pohjoisen sulkeminen olisi nyt pohjoisen avaaminen.
        self.mekanismi_kaytettava = True # Muuttuu riippuen esim. kertakäyttöisyydestä.

    def kayta_mekanismi(self, pelaaja): # Jos haluaa huoneeseen estetyn suunnan pelin alusta asti, se pitää tehdä huonetta luodessa.
        if self.mekanismi_kaytettava == False:
            tarinateksti = (f"Mekanismia {self.nimi} ei voi käyttää!")
        elif self.vaadittu_esine != "auto" and self.vaadittu_esine not in pelaaja.esineet:
                tarinateksti = (f"Mekanismi {self.nimi} vaatii esineen, jota teillä ei ole.")
        else:
            tarinateksti = (self.toimintokuvaus)
            if self.mekanismi_vaihe == True:
                if self.esta_pohjoinen == True or self.esta_pohjoinen == False: # Esim. jos kirjoittaa "auto", mikään ei muutu käytettäessä mekanismia.
                    self.vaikutusalue.pohjoinen_estetty = self.esta_pohjoinen
                    tarinateksti += (f"\nPohjoinen estetty: {self.vaikutusalue.pohjoinen_estetty}!")
                if self.esta_ita == True or self.esta_ita == False:
                    self.vaikutusalue.ita_estetty = self.esta_ita
                    tarinateksti += (f"\nItä estetty: {self.vaikutusalue.ita_estetty}!")
                if self.esta_etela == True or self.esta_etela == False:
                    self.vaikutusalue.etela_estetty = self.esta_etela
                    tarinateksti += (f"\nEtelä estetty: {self.vaikutusalue.etela_estetty}!")
                if self.esta_lansi == True or self.esta_lansi == False:
                    self.vaikutusalue.lansi_estetty = self.esta_lansi
                    tarinateksti += (f"\nLänsi estetty: {self.vaikutusalue.lansi_estetty}!")
                if self.kertakayttoinen == True:
                    self.mekanismi_kaytettava = False
                    tarinateksti += (f"\nMekanismi {self.nimi} ei ole enää käytettävissä.")
                self.mekanismi_vaihe = False
            
            else:
                tarinateksti += (f"Mekanismi {self.nimi} käytettiin taas.")
                self.vaikutusalue.pohjoinen_estetty = not self.esta_pohjoinen
                tarinateksti += (f"Pohjoinen estetty: {self.vaikutusalue.pohjoinen_estetty}!")
                self.vaikutusalue.ita_estetty = not self.esta_ita
                tarinateksti += (f"Itä estetty: {self.vaikutusalue.ita_estetty}!")
                self.vaikutusalue.etela_estetty = not self.esta_etela
                tarinateksti += (f"Etelä estetty: {self.vaikutusalue.etela_estetty}!")
                self.vaikutusalue.lansi_estetty = not self.esta_lansi
                tarinateksti += (f"Länsi estetty: {self.vaikutusalue.lansi_estetty}!")
                self.mekanismi_vaihe = True
        return tarinateksti

class Kaivinkone(Este):
    def __init__(self, nimi, vaikutusalue, toimintokuvaus="\nOlette kaivinkoneessa.", kertakayttoinen=True, esta_pohjoinen="auto", esta_ita="auto", esta_etela=False, esta_lansi="auto", vaadittu_esine="auto"):
        super().__init__(nimi, vaikutusalue, toimintokuvaus, kertakayttoinen, esta_pohjoinen, esta_ita, esta_etela, esta_lansi, vaadittu_esine)

    def kayta_mekanismi(self, pelaaja):
        tarinateksti = (self.toimintokuvaus)
        if self.vaikutusalue.etela_estetty == False:
            tarinateksti = ("Seinä on jo murrettu.")
            pelaaja.nykyinen_valikko = "pelaajavalikko"
            return tarinateksti
        else:
            pelaaja.nykyinen_valikko = "kaivinkone"
            self.virta = False
            self.suunta = "pohjoiseen"
            self.etaisyys = 3
            self.seina_hp = 2
            self.kasijarru = False
            self.kytkin = False
            tarinateksti = ("Edessänne on viisi kahvaa, kolme poljinta ja kaksi nappia. Missään ei ole ohjeita. Avain on jo koneessa, mutta kone ei ole käynnissä.\nMitä haluatte tehdä?\n1: Kahva vasemmalla\n2: Kahva edessänne\n3: Kahva etuoikealla\n4: Kahva keskioikealla\n5: Kahva oikealla\n6: Poljin vasemmalla\n7: Poljin keskellä\n8: Poljin oikealla\n9: Avaimet\n10: Nappi vieressänne\n0: POIS TÄÄLTÄ")
            return tarinateksti
    def toiminto(self, pelaaja, numerovalinta):
        if numerovalinta == 1:
            if self.virta == False:
                tarinateksti = ("Mitään ei tapahdu.")
                return tarinateksti
            else:
                tarinateksti = ("Koura liikkuu ulommas.")
                if self.suunta == "etelään" and self.etaisyys == 2:
                    if self.seina_hp == 2:
                        tarinateksti += ("\nKoura törmää seinään ja jättää jälkeensä tuhoa, sirpaleita ja murtumia. Seinä on kuitenkin yhä tolpillaan. Tee se uudelleen.")
                        self.seina_hp = 1
                        return tarinateksti
                    elif self.seina_hp == 1:
                        tarinateksti += ("\nTällä kertaa koura leikkaa suoraan seinän läpi. Tunnette hytissä tärähdyksiä vielä useita sekunteja osuman jälkeen. Seinä on murskattu.")
                        self.seina_hp = 0
                        self.vaikutusalue.etela_estetty = False
                        pelaaja.nykyinen_valikko = "pelaajavalikko"
                        return tarinateksti
                elif self.suunta == "etelään" and self.etaisyys < 2:
                    tarinateksti = ("Kouralla ei ole tilaa kerätä voimaa. Se tömähtää seinään heikosti. Seinälle ei käy kuinkaan.")
                    return tarinateksti
            return tarinateksti
        elif numerovalinta == 2:
            if self.virta == False:
                tarinateksti = ("Mitään ei tapahdu.")
                return tarinateksti
            else:
                if self.suunta == "pohjoiseen":
                    self.suunta = "itään"
                elif self.suunta == "itään":
                    self.suunta = "etelään"
                elif self.suunta == "etelään":
                    self.suunta = "länteen"
                elif self.suunta == "länteen":
                    self.suunta = "pohjoiseen"
                tarinateksti = (f"Kaivinkone pyörii myötäpäivään. Se osoittaa nyt {self.suunta}.")
                return tarinateksti
        elif numerovalinta == 3:
            if self.virta == False:
                tarinateksti = ("Mitään ei tapahdu.")
                return tarinateksti
            else:
                tarinateksti = ("Koura liikkuu vaakasuorassa, mutta todella vähän. Huoltoryhmä on mokannut.")
                return tarinateksti
        elif numerovalinta == 4:
            if self.kasijarru == False:
                tarinateksti = ("Kahva jäi asentoonsa. Kaivinkone nytkähti hieman. Jokin on nyt päällä.")
                self.kasijarru = True
                return tarinateksti
            else:
                tarinateksti = ("Palautatte kahvan alkuperäiseen asentoonsa.")
                self.kasijarru = False
                return tarinateksti
        elif numerovalinta == 5:
            if self.virta == False:
                tarinateksti = ("Mitään ei tapahdu.")
                return tarinateksti
            else:
                tarinateksti = ("Hytti keinahtaa lievästi.")
                return tarinateksti
        elif numerovalinta == 6:
            if self.kasijarru == True or self.kytkin == False or self.virta == False:
                tarinateksti = ("Mitään ei tapahdu.")
                return tarinateksti
            else:
                if self.suunta == "etelään":
                    tarinateksti = ("Kaivuri liikkuu taaksepäin.")
                    self.etaisyys += 1
                    return tarinateksti
                elif self.suunta == "pohjoiseen":
                    if self.etaisyys == 0:
                        tarinateksti = ("Kaivuri ajaa suoraan seinästä läpi! Ette näe kaaosta, mutta kuulette sen ja tunnette tärinän luuytimissänne. Tämä oli tässä.")
                        self.seina_hp = 0
                        self.vaikutusalue.etela_estetty = False
                        pelaaja.nykyinen_valikko = "pelaajavalikko"
                    tarinateksti = ("Kaivuri liikkuu taaksepäin.")
                    self.etaisyys -= 1
                    return tarinateksti
                elif self.suunta == "itään" or self.suunta == "länteen":
                    tarinateksti = ("Kaivuri törmää johonkin. Tähän suuntaan ei voi liikkua.")
                    return tarinateksti
        elif numerovalinta == 7:
            if self.kytkin == True:
                tarinateksti = ("Lakkaatte painamasta kytkintä.")
                self.kytkin = False
                return tarinateksti
            else:
                tarinateksti = ("Kaivuri nytkähtää vähän. Tiedätte sen verran vanhasta teknologiasta, että tunnistatte tämän kytkimeksi. Pidätte sitä pohjassa.")
                self.kytkin = True
                return tarinateksti
        elif numerovalinta == 8:
            if self.kasijarru == True or self.kytkin == False or self.virta == False:
                tarinateksti = ("Mitään ei tapahdu.")
                return tarinateksti
            else:
                if self.suunta == "etelään":
                    if self.etaisyys == 0:
                        tarinateksti = ("KAIVURI AJAA SUORAAN SEINÄSTÄ LÄPI! Tuulilasista lentää tiiliä ja laastia, mutta mikään ei osu teihin! Tämä oli tässä.")
                        self.seina_hp = 0
                        self.vaikutusalue.etela_estetty = False
                        pelaaja.nykyinen_valikko = "pelaajavalikko"
                        return tarinateksti
                    tarinateksti = ("Kaivuri liikkuu eteenpäin.")
                    self.etaisyys -= 1
                    return tarinateksti
                elif self.suunta == "pohjoiseen":
                    tarinateksti = ("Kaivuri liikkuu eteenpäin.")
                    self.etaisyys += 1
                    return tarinateksti
                elif self.suunta == "itään" or self.suunta == "länteen":
                    tarinateksti = ("Kaivuri törmää johonkin. Tähän suuntaan ei voi liikkua.")
                    return tarinateksti
        elif numerovalinta == 9:
            if self.virta == False:
                tarinateksti = ("Väännätte ruosteisia avaimia. Valot välähtävät päälle. Moottori alkaa hurista himmeästi. Toivottavasti tämä laite pysyy vielä vähän aikaa ehjänä.")
                self.virta = True
                return tarinateksti
            else:
                tarinateksti = ("Kaivuri hiljenee ja hämärtyy taas.")
                self.virta = False
                return tarinateksti
        elif numerovalinta == 10:
            if self.virta == False:
                tarinateksti = ("Mitään ei tapahdu.")
                return tarinateksti
            else:
                tarinateksti = ("Ajovalot välähtävät hetkeksi päälle, mutta sammuvat heti.")
                return tarinateksti
        elif numerovalinta == 0:
            pelaaja.nykyinen_valikko = "pelaajavalikko"