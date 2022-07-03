def Spinner():
	l = ['|', '/', '-', '\\']
	for i in l+l+l:
		sys.stdout.write(f"""\r [{i}] Loading...""")
		sys.stdout.flush()
		sleep(0.1)

from colorama import Fore
from tqdm import tqdm, trange
from time import sleep
import os
import requests





os.system("title Loading Prophet's Tools V2.3")
print(f"{Fore.WHITE}")
progressbar = tqdm([2,4,6,8,9,10])
for item in progressbar:
    sleep(0.1)
    progressbar.set_description(' Loading: ')

from colorama import Fore
from tqdm import tqdm, trange
from time import sleep
import os
os.system("title Loading HUD...")
print(f"{Fore.LIGHTMAGENTA_EX}")
progressbar = tqdm([1,2,3])
for item in progressbar:
    sleep(0.1)
    progressbar.set_description(' Loading HUD... ')

from colorama import Fore
from tqdm import tqdm, trange
from time import sleep
import os
os.system("title Checking For Updates...")
print(f"{Fore.WHITE}")
progressbar = tqdm([1,2,])
for item in progressbar:
    sleep(0.1)
    progressbar.set_description(' Checking For Updates... ')

import colorama
from colored import fg, attr
from colorama import Fore, Back, Style, init
import requests
from time import sleep
import os
import os.path
from requests.api import options
import sys
import webbrowser
os.system('cls' if os.name == 'nt' else 'clear')
colorama.init(autoreset=True)

def menu():
    os.system("title Prophet's Tools V2.3")
    print(f"""{Fore.WHITE}
                               \x1b[38;5;213m╔═╗╦═╗╔═╗╔═╗╦ ╦╔═╗╔╦╗
                               \033[90m╠═╝╠╦╝║ ║╠═╝╠═╣║╣  ║
                               \033[37m╩  ╩╚═╚═╝╩  ╩ ╩╚═╝ ╩




      \x1b[38;5;213m╔═══════════════════════╦═══════════════════════╦═══════════════════════╗\033[37m
      \x1b[38;5;213m║ \033[37m[\x1b[38;5;213m1\033[37m] \033[37mIP Look Up        \x1b[38;5;213m║\033[37m [\x1b[38;5;213m4\033[37m] \033[37mSocials           \x1b[38;5;213m║\033[37m [\x1b[38;5;213m7\033[37m] \033[37mNitro Gen         \x1b[38;5;213m║\033[37m
      \x1b[38;5;213m║ \033[37m[\x1b[38;5;213m2\033[37m] \033[37m                  \x1b[38;5;213m║\033[37m [\x1b[38;5;213m5\033[37m] \033[37m                  \x1b[38;5;213m║\033[37m [\x1b[38;5;213m8\033[37m] \033[37m                  \x1b[38;5;213m║\033[37m
      \x1b[38;5;213m║ \033[37m[\x1b[38;5;213m3\033[37m] \033[37mSystem Info       \x1b[38;5;213m║\033[37m [\x1b[38;5;213m6\033[37m] \033[37m                  \x1b[38;5;213m║\033[37m [\x1b[38;5;213m9\033[37m]{Fore.RESET}{Fore.LIGHTRED_EX} Exit {Fore.RESET}             \x1b[38;5;213m║\033[37m
      \x1b[38;5;213m╚═══════════════════════╩═══════════════════════╩═══════════════════════╝\033[37m
      
	                                          
""")

menu()

option = int(input(f"{Fore.WHITE} [>] {Fore.RESET}"))


# IP look up 1
def fetch_data():
        menu()
if option == 1: 
    Spinner()
    sleep(0.4)
    os.system('start utilities\\ip1.bat')
    exit()

# system 3
def fetch_data():
        menu()
if option == 3: 
    Spinner()
    sleep(0.4)
    os.system('start utilities\\sys.bat')
    exit()


# Social 4
def fetch_data():
        menu()
if option == 4:
    Spinner()
    sleep(0.4)
    webbrowser.open_new('https://discord.gg/mc4hHAQVge')
    sleep(2)
    print(f" [>] {Fore.RED}Bye!!")
    sleep(2)
    exit()

# Nitro Generator 7
def fetch_data():
        menu()
if option == 7: 
        Spinner()
        sleep(0.4)
        os.system("ng.bat")
        exit()


# Exit 9
def fetch_data():
        menu()
if option == 9:
    sleep(0.4)
    print(f" [>] {Fore.LIGHTGREEN_EX}Thank you for using Prophet's Tools!")
    sleep(2.6)
    print(f" [>] {Fore.LIGHTGREEN_EX}Bye bye!")
    sleep(0.5)
    exit()
if __name__ == '__main__':
        fetch_data()	