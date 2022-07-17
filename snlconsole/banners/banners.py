import random
from colorama import Fore
import pyfiglet

list1 = Fore.GREEN + pyfiglet.figlet_format('SnL Console')

list2 = Fore.LIGHTBLUE_EX +"""
 #####         #           #####                                            
#     # #    # #          #     #  ####  #    #  ####   ####  #      ###### 
#       ##   # #          #       #    # ##   # #      #    # #      #      
 #####  # #  # #          #       #    # # #  #  ####  #    # #      #####  
      # #  # # #          #       #    # #  # #      # #    # #      #      
#     # #   ## #          #     # #    # #   ## #    # #    # #      #      
 #####  #    # #######     #####   ####  #    #  ####   ####  ###### ###### 
"""
list3 = Fore.LIGHTMAGENTA_EX + """
  mmmm         m               mmm                              ..#          
 #      m mm   #             m       mmm   m mm    mmm    mmm     #     mmm  
  #mmm  #   #  #             #      #   #  #   #  #   '  #   #    #    #___# 
      # #   #  #             #      #   #  #   #   '''m  #   #    #    # 
 mmmm#  #   #  #mmmmm          mmm   #m#   #   #  "mmm"  "#m#"    "mm  "#mm" 
"""
list4 = Fore.BLUE + """
┏━┓┏┓╻╻     ┏━╸┏━┓┏┓╻┏━┓┏━┓╻  ┏━╸
┗━┓┃┗┫┃     ┃  ┃ ┃┃┗┫┗━┓┃ ┃┃  ┣╸ 
┗━┛╹ ╹┗━╸   ┗━╸┗━┛╹ ╹┗━┛┗━┛┗━╸┗━╸
"""
list5 = Fore.LIGHTWHITE_EX + pyfiglet.figlet_format('SnL Console', font='slant')
mainList = [list1,list2,list3,list4,list5]

def banners():
    f = random.choice(mainList)
    print(f)
    
