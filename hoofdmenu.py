import afsluitscherm
import galgje
import nummer_raad_spel
from colorama import Fore
import time
def asii_art():
    art = r"""                            
/'\_/`\                (  _  )                 ( )  _  ( ) _        ( )           (_ ) ( )_      _        
|     |   _ _          | (_) | _ _    _ _      | | ( ) | |(_)  ___  | |/')    __   | | | ,_)    (_)   __  
| (_) | /'_` )(`\/')   |  _  |( '_`\ ( '_`\    | | | | | || |/' _ `\| , <   /'__`\ | | | |      | | /'__`\
| | | |( (_| | >  <    | | | || (_) )| (_) )   | (_/ \_) || || ( ) || |\`\ (  ___/ | | | |_     | |(  ___/
(_) (_)`\__,_)(_/\_)   (_) (_)| ,__/'| ,__/'   `\___x___/'(_)(_) (_)(_) (_)`\____)(___)`\__) _  | |`\____)
                              | |    | |                                                    ( )_| |       
                              (_)    (_)                                                    `\___/'       """
    return art




def keuzemenu():
    while True:
        print(f'{Fore.YELLOW}Welkom bij...{Fore.RESET}')
        time.sleep(1)
        print(f'{Fore.CYAN}{asii_art()}{Fore.RESET}')
        print(
            f'{Fore.LIGHTMAGENTA_EX}1: Raad het nummer spel\n2: Galgje\n{Fore.RED}3: Het app winkeltje verlaten ;;{Fore.RESET}')
        keuze = int(input(
            f'{Fore.LIGHTMAGENTA_EX}Welkom in mijn app winkeltje welke app zou je willen gebruiken:\nJe kunt altijd terugkeren door stop te typen als je geen zin meer hebt.{Fore.RESET}'))
        if keuze == 1:
            print(nummer_raad_spel.start())
            time.sleep(1)
            print(f'{Fore.BLUE}We gaan terug naar het hoofd menu{Fore.RESET}')
            time.sleep(1)
        elif keuze == 2:
            print(galgje.start())
            time.sleep(1)
            print(f'{Fore.BLUE}We gaan terug naar het hoofd menu{Fore.RESET}')
            time.sleep(1)
        elif keuze == 3:
            time.sleep(1)
            afsluitscherm.start()
            break


keuzemenu()
