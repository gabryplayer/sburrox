import re
import random
import socket
import struct
from colorama import Fore, Style, init
import time
import concurrent.futures
import requests
import subprocess
import pyfiglet
from termcolor import colored
import time
import random
import string
import requests
from colorama import Fore, Style, init
import concurrent.futures
import pyfiglet
import keyboard


ascii_art = pyfiglet.figlet_format("sburrox_doxing", font="slant")

# Rendi il testo più grande duplicandolo
ascii_art = "\n".join([line * 1 for line in ascii_art.split("\n")])

# Aggiungi colore al testo
testo_colorato = colored(ascii_art, color='blue') 

# Stampa il testo colorato
print(testo_colorato)




# Chiedi all'utente di inserire una scelta


init(autoreset=True)

diavolo = r"""
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!                                                                         !!!!!!!!!!!
!!!!!!!!!!!                                                                         !!!!!!!!!!!
!!!!!!!!!!!                   1) Proxy generator                                    !!!!!!!!!!!
!!!!!!!!!!!                   2) Doss Tool                                          !!!!!!!!!!!
!!!!!!!!!!!                   3) discord-token-grabber                              !!!!!!!!!!!
!!!!!!!!!!!                   4) email-bomber                                       !!!!!!!!!!!
!!!!!!!!!!!                   5) ip-lookup                                          !!!!!!!!!!!
!!!!!!!!!!!                   6) phone-locator                                      !!!!!!!!!!!
!!!!!!!!!!!                   7) port-scanner                                       !!!!!!!!!!!
!!!!!!!!!!!                   8) Wifi Cracking                                      !!!!!!!!!!!
!!!!!!!!!!!                   9) Web Attacking                                      !!!!!!!!!!!
!!!!!!!!!!!                   10) Crunchyroll Premium Gen                           !!!!!!!!!!!
!!!!!!!!!!!                   11) Live CC Visa Generator                            !!!!!!!!!!!
!!!!!!!!!!!                   12) Nitro Generator                                   !!!!!!!!!!!
!!!!!!!!!!!    !tiktok- sburrox_doxing         !free accounts- https://t.me/scypeX  !!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

          free crunchyroll-disney-netflix-hbomax-nordvpn-expressvpn-hobo-etc..
                 !                https://t.me/scypeX               !
                 !                  Drop Every Days                 !

"""




print(diavolo)







choice = input("Your Choice:> ")


def genera_codice():
    # Crea una stringa casuale di 16 caratteri (numeri da 0 a 9 e lettere maiuscole/minuscole)
    caratteri_validi = string.digits + string.ascii_letters
    codice = ''.join(random.choice(caratteri_validi) for _ in range(16))
    return codice


if choice == '12':
    for _ in range(30000000000000000000000000000000000000000000000000000000000000000000000000000):
        codice_generato = genera_codice()
        print( Fore.GREEN +  f"https://discord.gift/{codice_generato}" + Style.RESET_ALL)
else:
    print("Invalid Choice.")


if choice == "11":
    try:
        # Esegue un altro file Python (sostituisci 'nome_file.py' con il nome del tuo file)
        subprocess.run(['python', 'gener.py'])
    except FileNotFoundError:
        print("Il file specificato non esiste.")
else:
    print("Success...")


if choice == "10":
    try:
        # Esegue un altro file Python (sostituisci 'nome_file.py' con il nome del tuo file)
        subprocess.run(['python', 'main.py'])
    except FileNotFoundError:
        print("Il file specificato non esiste.")
else:
    print("Success...")




if choice == "9":
    try:
        # Esegue un altro file Python (sostituisci 'nome_file.py' con il nome del tuo file)
        subprocess.run(['python', 'hulk.py'])
    except FileNotFoundError:
        print("Il file specificato non esiste.")
else:
    print("Success...")



if choice == "8":
    try:
        # Esegue un altro file Python (sostituisci 'nome_file.py' con il nome del tuo file)
        subprocess.run(['python', 'opiveret1.py'])
    except FileNotFoundError:
        print("Il file specificato non esiste.")
else:
    print("Success...")



if choice == "7":
    try:
        # Esegue un altro file Python (sostituisci 'nome_file.py' con il nome del tuo file)
        subprocess.run(['python', 'port-scanner.py'])
    except FileNotFoundError:
        print("Il file specificato non esiste.")
else:
    print("Success...")



if choice == "6":
    try:
        # Esegue un altro file Python (sostituisci 'nome_file.py' con il nome del tuo file)
        subprocess.run(['python', 'phone-locator.py'])
    except FileNotFoundError:
        print("Il file specificato non esiste.")
else:
    print("Success.")


if choice == "5":
    try:
        # Esegue un altro file Python (sostituisci 'nome_file.py' con il nome del tuo file)
        subprocess.run(['python', 'ip-lookup.py'])
    except FileNotFoundError:
        print("Il file specificato non esiste.")
else:
    print("Success...")


if choice == "4":
    try:
        # Esegue un altro file Python (sostituisci 'nome_file.py' con il nome del tuo file)
        subprocess.run(['python', 'email-bomber.py'])
    except FileNotFoundError:
        print("Il file specificato non esiste.")
else:
    print("Success...")


if choice == "3":
    try:
        # Esegue un altro file Python (sostituisci 'nome_file.py' con il nome del tuo file)
        subprocess.run(['python', 'discord-token-grabber.py'])
    except FileNotFoundError:
        print("Il file specificato non esiste.")
else:
    print("Success...")


if choice == "2":
    try:
        # Esegue un altro file Python (sostituisci 'nome_file.py' con il nome del tuo file)
        subprocess.run(['python', 'ddos.py'])
    except FileNotFoundError:
        print("Il file specificato non esiste.")
else:
    print("Success...")

if choice=="2":
 quest = input("Server:> ")
 print(Fore.BLUE + "Fatal: Invalid Server")
else:
    print("invalid choice")
    
if choice == "1":
    try:
        # Esegue un altro file Python (sostituisci 'nome_file.py' con il nome del tuo file)
        subprocess.run(['python', 'proxy.py'])
    except FileNotFoundError:
        print("Il file specificato non esiste.")
else:
    print("Success...")


