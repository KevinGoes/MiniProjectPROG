from tkinter import *
import csv
import datetime
import random
import tkinter as tk
from tkinter import font  as tkfont

def omzettenASCII(omzetWaarde):
    lijst = list(omzetWaarde)
    i = 0
    omgezetteWaarde = []
    for letter in lijst:
        ASCII = ord(lijst[i]) - 3
        CHAR = chr(ASCII)
        omgezetteWaarde.append(CHAR)
        i += 1
    zin = ''.join(omgezetteWaarde)
    return zin


def terugomzettenASCII(omgezetteWaarde):
    lijst = list(omgezetteWaarde)
    i = 0
    omgezetteWaarde = []
    for letter in lijst:
        ASCII = ord(lijst[i]) + 3
        CHAR = chr(ASCII)
        omgezetteWaarde.append(CHAR)
        i += 1
    zin = ''.join(omgezetteWaarde)
    return zin


def infoPubliek():
    with open('stalling.csv', 'r', newline='') as myCSVFile:
        lezer = csv.DictReader(myCSVFile, delimiter=',')
        aantalRegels = 0
        stallingBezet = []
        for regel in lezer:
            aantalRegels += 1
            omgezet = terugomzettenASCII(regel['pq^ifkd'])
            stallingBezet.append(omgezet)
        return aantalRegels, stallingBezet

def infoPersoonlijk(invoerStalling, invoerWachtwoord):
    aantalRegels, stallingBezet = infoPubliek()
    while True:
        if invoerStalling in stallingBezet:
            while True:
                with open('stalling.csv', 'r', newline='') as myCSVFile:
                    aantalRegels = 0
                    wachtwoord = []
                    lezer = csv.DictReader(myCSVFile, delimiter=',')
                    for regel in lezer:
                        aantalRegels += 1
                        omgezet = terugomzettenASCII(regel['t^`eqtlloa'])
                        wachtwoord.append(omgezet)
                    regel = stallingBezet.index(invoerStalling)
                    if wachtwoord[regel] == invoerWachtwoord:
                        with open('registreren.csv', 'r', newline='') as myCSVFile:
                            return 'U kunt uw nu bij uw fiets'
                    else:
                        return 'fout'
        else:
            return 'fout'


# def ophalenGegevens():
#     with open('stalling.csv', 'r', newline='') as myCSVFile:
#         reader = csv.DictReader(myCSVFile, delimiter=',')
#         stalling = []
#         registratienummer = []
#         wachtwoorden = []
#         datum = []
#         for row in reader:
#             omgezet = terugomzettenASCII(row['pq^ifkd'])
#             stalling.append(omgezet)
#             omgezet = terugomzettenASCII(row['t^`eqtlloa'])
#             wachtwoorden.append(omgezet)
#             omgezet = terugomzettenASCII(row['a^qrj'])
#             datum.append(omgezet)
#             omgezet = terugomzettenASCII(row['uhjlvwudwlhqxpphu'])
#             registratienummer.append(omgezet)
#         return stalling, wachtwoorden, datum, registratienummer

# def ophalen():
#     stalling, wachtwoorden, datum, registratienummers = ophalenGegevens()
#     del registratienummers[indexRegistratienummer]
#     del wachtwoorden[indexRegistratienummer]
#     return stalling, wachtwoorden, datum, registratienummers


# def gegevensTerugzetten():
#     stalling, wachtwoorden, datum, registratienummers = ophalen()
#     stallingNieuw = []
#     wachtwoordenNieuw = []
#     datumNieuw = []
#     registratienummerNieuw = []
#     for regel in stalling:
#         omgezet = omzettenASCII(regel)
#         stallingNieuw.append(omgezet)
#     for regel in wachtwoorden:
#         omgezet = omzettenASCII(regel)
#         wachtwoordenNieuw.append(omgezet)
#     for regel in datum:
#         omgezet = omzettenASCII(regel)
#         datumNieuw.append(omgezet)
#     for regel in registratienummers:
#         omgezet = omzettenASCII(regel)
#         registratienummerNieuw.append(omgezet)
#     combined = [stallingNieuw, wachtwoordenNieuw, datumNieuw, registratienummerNieuw]
#     with open('stalling.csv', 'w', newline='') as myCSVFile:
#         writer = csv.writer(myCSVFile, delimiter=',')
#         writer.writerow(['pq^ifkd', 't^`eqtlloa', 'a^qrj', 'uhjlvwudwlhqxpphu'])
#         for i in zip(*combined):
#             writer.writerow(i)

# def plekVrij(invoerRegistratienummer, invoerNieuwStallingNummer, wachtwoordStallingsplaats):
#     with open('registreren.csv', 'r', newline='') as myCSVFile:
#         lezer = csv.DictReader(myCSVFile, delimiter=',')
#         lijst = []
#         aantalRegels = 0
#         for regel in lezer:
#             aantalRegels += 1
#             omgezet = terugomzettenASCII(regel['uhjlvwudwlhqxpphu'])
#             lijst.append(omgezet)
#         if invoerRegistratienummer in lijst:
#                 if invoerNieuwStallingNummer in infoPubliek():
#                     return 'Kluisnietvrij'
#                 elif len(invoerNieuwStallingNummer) > 2:
#                     return 'Stallingnummertehoog'
#                 elif ',' in wachtwoordStallingsplaats:
#                     return 'KommaInWachtwoord'
#                 else:
#                     wachtwoord = omzettenASCII(wachtwoordStallingsplaats)
#                     vandaag = datetime.datetime.today()
#                     s = vandaag.strftime("%d-%b-%Y, %I:%M:%S")
#                     datum = omzettenASCII(s)
#                     invoer = omzettenASCII(invoerNieuwStallingNummer)
#                     invoerRegistratienummer = omzettenASCII(invoerRegistratienummer)
#                     return invoer, wachtwoord, datum, invoerRegistratienummer
#         else:
#             return 'Registratienummernietgoed'

# def stallen():
#     with open('stalling.csv', 'a', newline='') as myCSVFile:
#         schrijven = csv.writer(myCSVFile)
#         schrijven.writerow(plekVrij(invoerRegistratienummer, invoerNieuwStallingNummer, wachtwoordStallingsplaats))

# def registreren(invoerNaam, invoerANaam, invoerAGebDatum, invoerMerkFiets):
#     Nummer = range(10 ** 8)
#     RandomGetal = random.choice(Nummer)
#     while True:
#         fileOpen = open("registreren.csv", "r")
#         fileOpen.readlines()
#         if RandomGetal in fileOpen:
#             Nummer = range(10 ** 8)
#             RandomGetal = random.choice(Nummer)
#         else:
#             omgezetteGetal = omzettenASCII(str(RandomGetal))
#             fileOpen.close()
#             break
#     voornaam = omzettenASCII(invoerNaam)
#     achternaam = omzettenASCII(invoerANaam)
#     geboortedatum = omzettenASCII(invoerAGebDatum)
#     fietsenmerk = omzettenASCII(invoerMerkFiets)
#     omgezetteGetal = omzettenASCII(str(RandomGetal))
#     with open("registreren.csv", "a+") as MyCSVfile:
#         MyCSVfile.write(voornaam)
#         MyCSVfile.write("," + achternaam)
#         MyCSVfile.write("," + geboortedatum)
#         MyCSVfile.write("," + fietsenmerk)
#         MyCSVfile.write("," + str(omgezetteGetal) + "\n")
#     return RandomGetal


def tijd():
    vandaag = datetime.datetime.today()
    s = vandaag.strftime("%H")
    s = int(s)
    if s < 12:
        return('Goedemorgen')
    elif s >= 12 and s < 18:
        return('Goedemiddag')
    elif s > 18:
        return('Goedenavond')

def tijdKlok():
    vandaag = datetime.datetime.today()
    s = vandaag.strftime("%H:%M:%S")
    return s

def datum():
    vandaag = datetime.datetime.today()
    s = vandaag.strftime("%a %d-%m-%Y")
    return s

def toonHome():
    RegistrerenFrame.pack_forget()
    StallenFrame.pack_forget()
    OphalenFrame.pack_forget()
    InformatieFrame.pack_forget()
    InformatiePersoonlijkFrame.pack_forget()
    InformatiePersoonlijkFoutFrame.pack_forget()
    homeFrame.pack()

def toonRegistreren():
    homeFrame.pack_forget()
    StallenFrame.pack_forget()
    OphalenFrame.pack_forget()
    InformatieFrame.pack_forget()
    RegistrerenFrame.pack()

def toonStallen():
    RegistrerenFrame.pack_forget()
    homeFrame.pack_forget()
    OphalenFrame.pack_forget()
    InformatieFrame.pack_forget()
    StallenFrame.pack()

def toonOphalen():
    RegistrerenFrame.pack_forget()
    StallenFrame.pack_forget()
    homeFrame.pack_forget()
    InformatieFrame.pack_forget()
    OphalenFrame.pack()

def toonInformatie():
    RegistrerenFrame.pack_forget()
    StallenFrame.pack_forget()
    OphalenFrame.pack_forget()
    homeFrame.pack_forget()
    InformatieFrame.pack()

def toonInformatiePersoonlijk():
    InformatieFrame.pack_forget()
    InformatiePersoonlijkFrame.pack()

def toonInformatiePubliek():
    InformatieFrame.pack_forget()
    InformatiePubliekFrame.pack()

def toonInformatiePersoonlijkOutput():
    InformatiePersoonlijkFrame.pack_forget()
    InformatiePersoonlijkFoutFrame.pack_forget()
    if infoPersoonlijk(invoerStalling.get(), invoerWachtwoord.get()) == 'fout':
        InformatiePersoonlijkFoutFrame.pack()
    else:
        InformatiePersoonlijkOutputFrame.pack()


root = Tk()
root.title = ('home')
root.configure(background='yellow')
homeFrame = Frame(master=root, background='yellow')
homeFrame.pack(fill="both", expand=True)
vandaag = Label(master=root, text='Vandaag' + '\n' + datum() + '\n' + tijdKlok(), background='yellow', foreground='blue', width=80, height=5, font=('Helvetica', 14, 'bold'))
vandaag.place(x=970, y=700)
homeLabel = Label(master=homeFrame, text=tijd() +',\nWelkom bij NS', background='yellow', foreground='blue', width=50, height=5, font=('Helvetica', 25, 'bold'))
homeLabel.pack(padx=20, pady=20)
Registreren = Button(master=homeFrame, text='Registreren', height=7, width=30, font=('Helvetica', 15, 'bold'),background='royalblue',foreground='white', command=toonRegistreren)
Registreren.place(x=390, y=250)
Stallen = Button(master=homeFrame, text='Stallen', height=7, width=30, font=('Helvetica', 15, 'bold'),background='royalblue',foreground='white', command=toonStallen)
Stallen.place(x=775, y=250)
Ophalen = Button(master=homeFrame, text='Ophalen', height=7, width=30, font=('Helvetica', 15, 'bold'),background='royalblue',foreground='white', command=toonOphalen)
Ophalen.place(x=390, y=450)
Informatie = Button(master=homeFrame, text='Informatie', height=7, width=30, font=('Helvetica', 15, 'bold'),background='royalblue',foreground='white', command=toonInformatie)
Informatie.place(x=775, y=450)

#Registreren
RegistrerenFrame = Frame(master=root, background='yellow')
RegistrerenFrame.pack(fill="both", expand=True)
RegistrerenLabel = Label(master=RegistrerenFrame, text='Registreren', background='yellow', foreground='blue', width=50, height=5, font=('Helvetica', 15, 'bold'))
RegistrerenLabel.pack(padx=20, pady=20)


#Stallen
StallenFrame = Frame(master=root, background='yellow')
StallenFrame.pack(fill="both", expand=True)
StallenLabel = Label(master=StallenFrame, text='Stallen', background='yellow', foreground='blue', width=50, height=5, font=('Helvetica', 15, 'bold'))
StallenLabel.pack(padx=20, pady=20)


#Ophalen
OphalenFrame = Frame(master=root, background='yellow')
OphalenFrame.pack(fill="both", expand=True)
OphalenLabel = Label(master=OphalenFrame, text='Ophalen', background='yellow', foreground='blue', width=50, height=5, font=('Helvetica', 15, 'bold'))
OphalenLabel.pack(padx=20, pady=20)


#Informatie
InformatieFrame = Frame(master=root, background='yellow')
InformatieFrame.pack(fill="both", expand=True)
InformatieLabel = Label(master=InformatieFrame, text='Informatie', background='yellow', foreground='blue', width=50, height=5, font=('Helvetica', 25, 'bold'))
InformatieLabel.pack(padx=20, pady=20)
PubliekeInformatieButton = Button(master=InformatieFrame, text='Publieke Informatie', height=7, width=30, font=('Helvetica', 15, 'bold'),background='royalblue',foreground='white', command=toonInformatiePubliek)
PubliekeInformatieButton.pack(side=LEFT)
PersoonlijkeInformatieButton = Button(master=InformatieFrame, text='Persoonlijke Informatie', height=7, width=30, font=('Helvetica', 15, 'bold'),background='royalblue',foreground='white', command=toonInformatiePersoonlijk)
PersoonlijkeInformatieButton.pack(side=RIGHT)


#Informatie Publiek
InformatiePubliekFrame = Frame(master=root, background='yellow')
InformatiePubliekFrame.pack
aantalStallingenVrij, stallingenVrij = infoPubliek()
InformatiePubliekLabel = Label(master=InformatiePubliekFrame, text='Informatie Publiek', background='yellow', foreground='blue', width=50, height=5, font=('Helvetica', 25, 'bold'))
InformatiePubliekLabel.pack(padx=20, pady=20)
InformatiePubliekLabel1 = Label(master=InformatiePubliekFrame, text='Er zijn in totaal {} stallingen vrij, stallingen {} zijn bezet'.format(100 - aantalStallingenVrij, stallingenVrij), background='yellow', foreground='blue', width=100, height=10, font=('Helvetica', 15, 'bold'))
InformatiePubliekLabel1.pack()
InformatiePersoonlijk = Frame(master=root, background='yellow')
InformatiePersoonlijk.pack


#Informatie Persoonlijk Output fout!
InformatiePersoonlijkFoutFrame = Frame(master=root, background='yellow')
InformatieFoutLabel = Label(master=InformatiePersoonlijkFoutFrame, text='Wachtwoord en/of Stalling is verkeerd ingevoerd!', background='yellow', foreground='red', width=50, height=5, font=('Helvetica', 15, 'bold'))
InformatieFoutLabel.pack(padx=50, pady=50)
invoerStallingLabel = Label(master=InformatiePersoonlijkFoutFrame, text='Voer hieronder uw Stalling nummer in:', background='yellow', foreground='blue', width=50, height=5, font=('Helvetica', 15, 'bold'))
invoerStallingLabel.pack(padx=10, pady=0)
invoerStallingFout = Entry(master=InformatiePersoonlijkFoutFrame, background='blue')
invoerStallingFout.pack(padx=20, pady=20)
invoerWachtwoordLabel = Label(master=InformatiePersoonlijkFoutFrame, text='Voer hieronder uw Wachtwoord van uw stalling in:', background='yellow', foreground='blue', width=50, height=5, font=('Helvetica', 15, 'bold'))
invoerWachtwoordLabel.pack(padx=10, pady=0)
invoerWachtwoordFout = Entry(master=InformatiePersoonlijkFoutFrame, background='blue')
invoerWachtwoordFout.pack(padx=20, pady=20)
InformatiePersoonlijkDoorgaan = Button(master=InformatiePersoonlijkFoutFrame, text='Doorgaan', height='3', width='14', background='blue', foreground='white', command=toonInformatiePersoonlijkOutput)
InformatiePersoonlijkDoorgaan.pack(padx=20, pady=20)
InformatiePersoonlijkFoutFrame.pack


#Informatie Persoonlijk output
InformatiePersoonlijkOutputFrame = Frame(master=root, background='yellow')
InformatieLabel = Label(master=InformatiePersoonlijkOutputFrame, text='Persoonlijke Informatie', background='yellow', foreground='blue', width=50, height=5, font=('Helvetica', 25, 'bold'))
InformatieLabel.pack(padx=20, pady=20)
InformatiePersoonlijkOutputLabel = Label(master=InformatiePersoonlijkOutputFrame, text='U kunt nu bij uw fiets!', background='yellow', foreground='blue', width=50, height=5, font=('Helvetica', 25, 'bold'))
InformatiePersoonlijkOutputLabel.pack(padx=20, pady=20)
InformatiePersoonlijkOutputFrame.pack


#Informatie Persoonlijk invoer
InformatiePersoonlijkFrame = Frame(master=root, background='yellow')
InformatieLabel = Label(master=InformatiePersoonlijkFrame, text='Persoonlijke Informatie', background='yellow', foreground='blue', width=50, height=5, font=('Helvetica', 25, 'bold'))
InformatieLabel.pack(padx=20, pady=20)
invoerStallingLabel = Label(master=InformatiePersoonlijkFrame, text='Voer hieronder uw Stalling nummer in:', background='yellow', foreground='blue', width=50, height=5, font=('Helvetica', 15, 'bold'))
invoerStallingLabel.pack(padx=10, pady=0)
invoerStalling = Entry(master=InformatiePersoonlijkFrame, background='blue')
invoerStalling.pack(padx=20, pady=20)
invoerWachtwoordLabel = Label(master=InformatiePersoonlijkFrame, text='Voer hieronder uw Wachtwoord van uw stalling in::', background='yellow', foreground='blue', width=50, height=5, font=('Helvetica', 15, 'bold'))
invoerWachtwoordLabel.pack(padx=10, pady=0)
invoerWachtwoord = Entry(master=InformatiePersoonlijkFrame, background='blue')
invoerWachtwoord.pack(padx=20, pady=20)
InformatiePersoonlijkDoorgaan = Button(master=InformatiePersoonlijkFrame, text='Doorgaan', height='3', width='14', background='blue', foreground='white', command=toonInformatiePersoonlijkOutput)
InformatiePersoonlijkDoorgaan.pack(padx=20, pady=20)
InformatiePersoonlijkFrame.pack


toonHome()
root.mainloop()