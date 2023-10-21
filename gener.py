import random
from colorama import Fore, Style
import colorama

colorama.init()

countries = ['India', 'USA', 'UK', 'France', 'Japan', 'Germany', 'Italy', 'Australia']

while True:
    card_number = ''.join(random.choice('0123456789') for _ in range(12))
    cvv = ''.join(random.choice('0123456789') for _ in range(3))
    expire_date = '{:02d}/{:02d}'.format(random.randint(1, 12), random.randint(0, 99))
    country = random.choice(countries)

    print(Fore.GREEN + "[+]" + Fore.RED + " Live/" + Fore.GREEN + card_number + Fore.BLUE + "/cvv:" + Fore.YELLOW + cvv + Fore.MAGENTA + "/expire:" + Fore.CYAN + expire_date + Fore.WHITE + "/country:" + Fore.LIGHTMAGENTA_EX + country)
    print(Style.RESET_ALL) 