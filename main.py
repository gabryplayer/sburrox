import os
import random
import time
import pyfiglet


testo = "crunprem-crack"

ascii_art = pyfiglet.figlet_format(testo)

print(ascii_art)
print("-------------------------------------------------------------------------------------------------------------------------------------------")
print("READ THIS!")
print("Accounts that you get is not premium. HOW TO GET PREMIUM?")
print("For get premium go to buy the premium but in the pyamhent page you arledy get the card , do pay with this card and ur pyamhent was success.")
print("-------------------------------------------------------------------------------------------------------------------------------------------")
print("                                                           ")
print("-------------------------------------------------------------------------------------------------------------------------------------------")
print("1*] Crunchyroll Generating")
print("-------------------------------------------------------------------------------------------------------------------------------------------")
print("                                                           ")
choice = input("Ypur Choice> ")

if choice == "1": 

 cartella = "cttols"

nome_file = "config.txt"

percorso_file = os.path.join(cartella, nome_file)



while True:

    with open(percorso_file, "r") as file:

        frasi = file.readlines()


    frase_casuale = random.choice(frasi)


    print("[!] Wait for account")
    time.sleep(0.3)
    print("[!] Checking")
    time.sleep(0.3)
    print("[!] Finding One Working....")
    time.sleep(0.6)
    print("[+] Finded!")
    print("[+] Your Account Beend Gived Below.:")

    print("--------------------------------")
    print(frase_casuale)
    print("--------------------------------")

    print("[*] Succes.")


    time.sleep(0.1)


