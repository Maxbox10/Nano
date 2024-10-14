import random
from colorama import Fore

def start():
    getal = random.randrange(1, 11)
    print(f'{Fore.LIGHTCYAN_EX}Welkom bij het nummer raadspel.\nHet is de bedoeling dat je het getal raad dit getal zit tussen 1 en 10.\n je hebt hiervoor 3 pogingen')
    for i in range(3):
        print(f'{Fore.LIGHTCYAN_EX}Poging: ',(i + 1))
        keuze = input(f'{Fore.LIGHTCYAN_EX}Geef me een getal: ').lower()
        if keuze == 'stop':
            break
        if getal == keuze:
            print(f'{Fore.GREEN}Gefeliciteerd je hebt gewonnen{Fore.RESET}')
            opnieuw = input(f'{Fore.LIGHTCYAN_EX}Wil je nog een keer proberen? typ y of n: ').lower()
            if opnieuw == 'y':
                start()
            else:
                break
        else:
            (print(f'{Fore.RED}Helaas probeer opnieuw{Fore.RESET}'))
        if i == 2:
            print(f'{Fore.RED}Helaas verloren je hebt 3 pogingen bereikt{Fore.RESET}.')
            opnieuw = input(f'{Fore.LIGHTCYAN_EX}Wil je nog een keer proberen? typ y of n: ').lower()
            if opnieuw == 'y':
                start()
            else:
                break