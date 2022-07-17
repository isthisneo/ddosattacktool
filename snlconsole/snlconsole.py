#code with utf-8
#https://github.com/isthisneo
#snlconsole v1
#neo
#
#
#
#
#
#





import os
import pyfiglet
import time
import sys
import socket
from colorama import Fore
from banners import banners
from module import *

banners.banners()


altCizgi = '\033[4m'
duz = '\033[0m'
while True:
    console = input(Fore.LIGHTWHITE_EX + altCizgi + 'snl1' + duz + ' > ')
    if console == 'options' or 'show options':
        print("""""")