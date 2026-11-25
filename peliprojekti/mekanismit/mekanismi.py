class Mekanismi():
    def __init__(self, nimi):
        self.nimi = nimi
        # Ei ID:tä, koska mekanismin sijainti ei muutu. Se lisätään sijaintiinsa main.py:n sisällä.

    def kayta_mekanismi(self):
        print (f"Käytitte mekanismin {self.nimi}.")

    def kayta_esineella(self, pelaaja, esine):
        if esine in pelaaja.esineet:
            print (f"Käytitte mekanismin {self.nimi}.")

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

    def kayta_mekanismi(self, pelaaja): # Jos haluaa huoneeseen estetyn suunnan pelin alusta asti, tämä pitää tehdä huonetta luodessa.
        if self.mekanismi_kaytettava == False:
            print (f"Mekanismia {self.nimi} ei voi käyttää!")
        elif self.vaadittu_esine != "auto" and self.vaadittu_esine not in pelaaja.esineet:
                print (f"Mekanismi {self.nimi} vaatii esineen, jota teillä ei ole.")
        else:
            if self.mekanismi_vaihe == True:
                print (self.toimintokuvaus)
                if self.esta_pohjoinen == True or self.esta_pohjoinen == False: # Esim. jos kirjoittaa "auto", mikään ei muutu käytettäessä mekanismia.
                    self.vaikutusalue.pohjoinen_estetty = self.esta_pohjoinen
                    print (f"Pohjoinen estetty: {self.vaikutusalue.pohjoinen_estetty}!")
                if self.esta_ita == True or self.esta_ita == False:
                    self.vaikutusalue.ita_estetty = self.esta_ita
                    print (f"Itä estetty: {self.vaikutusalue.ita_estetty}!")
                if self.esta_etela == True or self.esta_etela == False:
                    self.vaikutusalue.etela_estetty = self.esta_etela
                    print (f"Etelä estetty: {self.vaikutusalue.etela_estetty}!")
                if self.esta_lansi == True or self.esta_lansi == False:
                    self.vaikutusalue.lansi_estetty = self.esta_lansi
                    print (f"Länsi estetty: {self.vaikutusalue.lansi_estetty}!")
                if self.kertakayttoinen == True:
                    self.mekanismi_kaytettava = False
                    print (f"Mekanismi {self.nimi} ei ole enää käytettävissä.")
                self.mekanismi_vaihe = False
            
            else:
                print (f"Mekanismi {self.nimi} käytettiin taas.")
                self.vaikutusalue.pohjoinen_estetty = not self.esta_pohjoinen
                print (f"Pohjoinen estetty: {self.vaikutusalue.pohjoinen_estetty}!")
                self.vaikutusalue.ita_estetty = not self.esta_ita
                print (f"Itä estetty: {self.vaikutusalue.ita_estetty}!")
                self.vaikutusalue.etela_estetty = not self.esta_etela
                print (f"Etelä estetty: {self.vaikutusalue.etela_estetty}!")
                self.vaikutusalue.lansi_estetty = not self.esta_lansi
                print (f"Länsi estetty: {self.vaikutusalue.lansi_estetty}!")
                self.mekanismi_vaihe = True

class Kaivinkone(Este):
    def __init__(self, nimi, vaikutusalue, toimintokuvaus="\nOlette kaivinkoneessa.", kertakayttoinen=True, esta_pohjoinen="auto", esta_ita="auto", esta_etela=False, esta_lansi="auto", vaadittu_esine="auto"):
        super().__init__(nimi, vaikutusalue, toimintokuvaus, kertakayttoinen, esta_pohjoinen, esta_ita, esta_etela, esta_lansi, vaadittu_esine)

    def kayta_mekanismi(self, pelaaja):
        print (self.toimintokuvaus)
        if self.vaikutusalue.etela_estetty == False:
            print ("Seinä on jo murrettu.")
            pelaaja.nykyinen_valikko = "pelaajavalikko"
        else:
            pelaaja.nykyinen_valikko = "kaivinkone"
            self.virta = False
            self.suunta = "pohjoiseen"
            self.etaisyys = 3
            self.seina_hp = 2
            self.kasijarru = False
            self.kytkin = False
            print ("Edessänne on viisi kahvaa, kolme poljinta ja kaksi nappia. Missään ei ole ohjeita. Avain on jo koneessa, mutta kone ei ole käynnissä.")
            print("Mitä haluatte tehdä?\n1: Kahva vasemmalla\n2: Kahva edessänne\n3: Kahva etuoikealla\n4: Kahva keskioikealla\n5: Kahva oikealla\n6: Poljin vasemmalla\n7: Poljin keskellä\n8: Poljin oikealla\n9: Nappi edessänne\n10: Nappi vieressänne\n0: POIS TÄÄLTÄ\nVastaus numerona: ")
    def toiminto(self, pelaaja, numerovalinta):
        if numerovalinta == "1":
            if self.virta == False:
                print ("Mitään ei tapahdu.")
            else:
                print ("Koura liikkuu ulommas.")
                if self.suunta == "etelään" and self.etaisyys == 2:
                    if self.seina_hp == 2:
                        print ("Koura törmää seinään ja jättää jälkeensä tuhoa, sirpaleita ja murtumia. Seinä on kuitenkin yhä tolpillaan. Tee se uudelleen.")
                        self.seina_hp = 1
                    elif self.seina_hp == 1:
                        print ("Tällä kertaa koura leikkaa suoraan seinän läpi. Tunnette hytissä tärähdyksiä vielä useita sekunteja osuman jälkeen. Seinä on murskattu.")
                        self.seina_hp = 0
                        self.vaikutusalue.etela_estetty = False
                elif self.suunta == "etelään" and self.etaisyys < 2:
                    print ("Kouralla ei ole tilaa kerätä voimaa. Se tömähtää seinään heikosti. Seinälle ei käy kuinkaan.")
        elif numerovalinta == "2":
            if self.virta == False:
                print ("Mitään ei tapahdu.")
            else:
                if self.suunta == "pohjoiseen":
                    self.suunta = "itään"
                elif self.suunta == "itään":
                    self.suunta = "etelään"
                elif self.suunta == "etelään":
                    self.suunta = "länteen"
                elif self.suunta == "länteen":
                    self.suunta = "pohjoiseen"
                print (f"Kaivinkone pyörii myötäpäivään. Se osoittaa nyt {self.suunta}.")
        elif numerovalinta == "3":
            if self.virta == False:
                print ("Mitään ei tapahdu.")
            else:
                print ("Koura liikkuu vaakasuorassa, mutta todella vähän. Huoltoryhmä on mokannut.")
        elif numerovalinta == "4":
            if self.kasijarru == False:
                print ("Kahva jäi asentoonsa. Kaivinkone nytkähti hieman. Jokin on nyt päällä.")
                self.kasijarru = True
            else:
                print ("Palautatte kahvan alkuperäiseen asentoonsa.")
                self.kasijarru = False
        elif numerovalinta == "5":
            if self.virta == False:
                print ("Mitään ei tapahdu.")
            else:
                print ("Hytti keinahtaa lievästi.")
        elif numerovalinta == "6":
            if self.kasijarru == True or self.kytkin == False or self.virta == False:
                print ("Mitään ei tapahdu.")
            else:
                if self.suunta == "etelään":
                    print ("Kaivuri liikkuu taaksepäin.")
                    self.etaisyys += 1
                elif self.suunta == "pohjoiseen":
                    if self.etaisyys == 0:
                        print ("Kaivuri ajaa suoraan seinästä läpi! Ette näe kaaosta, mutta kuulette sen ja tunnette tärinän luuytimissänne. Tämä oli tässä.")
                        self.seina_hp = 0
                        self.vaikutusalue.etela_estetty = False

                    print ("Kaivuri liikkuu taaksepäin.")
                    self.etaisyys -= 1
                elif self.suunta == "itään" or self.suunta == "länteen":
                    print ("Kaivuri törmää johonkin. Tähän suuntaan ei voi liikkua.")
        elif numerovalinta == "7":
            if self.kytkin == True:
                print ("Lakkaatte painamasta kytkintä.")
                self.kytkin = False
            else:
                print ("Kaivuri nytkähtää vähän. Tiedätte sen verran vanhasta teknologiasta, että tunnistatte tämän kytkimeksi. Pidätte sitä pohjassa.")
                self.kytkin = True
        elif numerovalinta == "8":
            if self.kasijarru == True or self.kytkin == False or self.virta == False:
                print ("Mitään ei tapahdu.")
            else:
                if self.suunta == "etelään":
                    if self.etaisyys == 0:
                        print ("Kaivuri ajaa suoraan seinästä läpi! Tuulilasista lentää tiiliä ja laastia, mutta mikään ei osu teihin! Tämä oli tässä.")
                        self.seina_hp = 0
                        self.vaikutusalue.etela_estetty = False
                    print ("Kaivuri liikkuu eteenpäin.")
                    self.etaisyys -= 1
                elif self.suunta == "pohjoiseen":
                    print ("Kaivuri liikkuu eteenpäin.")
                    self.etaisyys += 1
                elif self.suunta == "itään" or self.suunta == "länteen":
                    print ("Kaivuri törmää johonkin. Tähän suuntaan ei voi liikkua.")
        elif numerovalinta == "9":
            if self.virta == False:
                print ("Valot välähtävät päälle. Moottori alkaa hurista himmeästi. Toivottavasti tämä laite pysyy vielä vähän aikaa ehjänä.")
                self.virta = True
            else:
                print ("Kaivuri hiljenee ja hämärtyy taas.")
                self.virta = False
        elif numerovalinta == "10":
            if self.virta == False:
                print ("Mitään ei tapahdu.")
            else:
                print ("Ajovalot välähtävät hetkeksi päälle, mutta sammuvat heti.")
        elif numerovalinta == "0":
            pelaaja.nykyinen_valikko = "pelaaja_valikko"
            return