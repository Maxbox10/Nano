import random
from colorama import Fore
import time

def woorden_naar_lijst():
        with open('woorden.txt', 'r') as woordentxt:
            woorden = woordentxt.read().splitlines()
        return woorden


def galgjewoord(woorden):
    return random.choice(woorden).lower()

def start():
    textfile = open('woorden.txt', 'a')
    woorden = woorden_naar_lijst()
    spelwoord = galgjewoord(woorden)
    goed = []
    fout = []
    maxpogingen = 6
    pogingen = 0

    print(f'{Fore.LIGHTMAGENTA_EX}Welkom bij het spelletje Galgje.\nIn dit spel is er een willekeurig woord gekozen uit een lijst je kiest steeds 1 letter en dan krijg je te zien of hij in het woord zit of niet.\nHet spel stop als je alle letters uit het woord geraden hebt of 6 letters gekozen hebt die er niet in staan SUCCES.')
    naam = input('Wat is je naam:')
    print(f'Nou {naam} we gaan beginnen\nSucces')
    time.sleep(1)
    while pogingen < maxpogingen:

        raadwoord = ''.join([letter if letter in goed else '.' for letter in spelwoord])
        print(f'\nWoord: {raadwoord}')
        print(f'{Fore.RED}Foute lettertjes: {', '.join(fout)}{Fore.RESET}')
        print(f'{Fore.LIGHTMAGENTA_EX}Je hebt nog {maxpogingen - pogingen} pogingen over.')


        keuze = input("Kies een letter: ").lower()
        if keuze == 'stop':
            break

        # Controleer of de invoer geldig is
        if len(keuze) != 1:
            print('Voer alstublieft één enkele letter in.')
            continue

        # Als de speler een letter goed raadt
        if keuze in spelwoord:
            if keuze not in goed:
                goed.append(keuze)
                print(f'Hatsaa deze letter {Fore.GREEN}{keuze}{Fore.RESET}{Fore.LIGHTMAGENTA_EX} zit in het woord.')
                time.sleep(1)
            else:
                print(f'SUKKEL je hebt deze letter {Fore.GREEN}{keuze}{Fore.RESET}{Fore.LIGHTMAGENTA_EX} al geraden.')
                time.sleep(1)
        else:
            if keuze not in fout:
                fout.append(keuze)
                pogingen += 1
                print(f'{Fore.RED}{keuze}{Fore.RESET}{Fore.LIGHTMAGENTA_EX} zit niet in het woord.' )
                time.sleep(1)
            else:
                print(f'Je hebt de letter {Fore.RED}{keuze}{Fore.RESET}{Fore.LIGHTMAGENTA_EX}al fout geraden.')
                time.sleep(1)


        if all(letter in goed for letter in spelwoord):
            print(f'\nGefeliciteerd! Je hebt het woord {spelwoord} geraden!')
            jaofnee = input(
                'Omdat je hebt gewonnen mag je een woord toevoegen aan galgje wil je dit doen?\ntype y of n: ').lower()
            if jaofnee == 'y':
                toevoegen = input('Wat leuk welk woord zou je willen toevoegen en houw het een beetje leuk:').lower()
                if toevoegen in woorden:
                    print('Het bestond al maar nu weet je het zeker:)')
                    break
                else:
                    textfile.write(toevoegen + '\n')
                    textfile.close()
                    break
            if jaofnee == 'n':
                print('Ook niks toevoegen is goed bedankt voor het spelen')
                break
    else:
        print(f'{Fore.RED}Je hebt verloren. Het woord was {spelwoord}.{Fore.RESET}')