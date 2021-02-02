
from colorama import Fore, Back, Style, init
import time
from os import system
init(convert=True)
#╔ ╩ ╦ ╠ ═ ╬ ¤ ↑ ↓ ← → 
import keyboard
x = 1
y = 1
  

CorDaBox = Fore.MAGENTA

letrasNoBox = Fore.CYAN

selecao = Fore.YELLOW

print(f""" 
  ╔═══════════════╗
  ║ Arrow Down    ║
  ╚═══════════════╝
  
    
      """)



def selectex1():
    print(f"""{CorDaBox}                                                                         
                                    ╔═══════════════════════════════════════════╗
                                    ║ {letrasNoBox}{selecao}>> 1 = example1 {CorDaBox}                          ║
                                    ║ {letrasNoBox}2 = example2            {CorDaBox}                  ║
                                    ║ {letrasNoBox}3 = example3           {CorDaBox}                   ║
                                    ║ {letrasNoBox}4 = example4 {CorDaBox}                             ║
                                    ╚═══════════════════════════════════════════╝
    """)

def selectex2():
    print(f"""{CorDaBox}                                                                         
                                    ╔═══════════════════════════════════════════╗
                                    ║ {letrasNoBox}1 = example1 {CorDaBox}                             ║
                                    ║ {letrasNoBox}{selecao}>> 2 = example2            {CorDaBox}               ║
                                    ║ {letrasNoBox}3 = example3           {CorDaBox}                   ║
                                    ║ {letrasNoBox}4 = example4 {CorDaBox}                             ║
                                    ╚═══════════════════════════════════════════╝
    """)

def selectex3():
    print(f"""{CorDaBox}                                                                         
                                    ╔═══════════════════════════════════════════╗
                                    ║ {letrasNoBox}1 = example1 {CorDaBox}                             ║
                                    ║ {letrasNoBox}2 = example2            {CorDaBox}                  ║
                                    ║ {letrasNoBox}{selecao}>> 3 = example3           {CorDaBox}                ║
                                    ║ {letrasNoBox}4 = example4 {CorDaBox}                             ║
                                    ╚═══════════════════════════════════════════╝
    """)

def selectex4():
    print(f"""{CorDaBox}                                                                         
                                    ╔═══════════════════════════════════════════╗
                                    ║ {letrasNoBox}1 = example1     {CorDaBox}                         ║
                                    ║ {letrasNoBox}2 = example2            {CorDaBox}                  ║
                                    ║ {letrasNoBox}3 = example3           {CorDaBox}                   ║
                                    ║ {letrasNoBox}{selecao}>> 4 = example4 {CorDaBox}                          ║
                                    ╚═══════════════════════════════════════════╝
    """)


while True:
    try:
        if keyboard.is_pressed('esc'):
            break
        elif keyboard.is_pressed('down'):
            time.sleep(0.1)
            x+=1
            if x == 1:
                system('cls')
                selectex1()
            elif x == 2:
                system('cls')
                selectex2()
            elif x == 3:
                system('cls')
                selectex3()
            elif x == 4:
                system('cls')
                selectex4()
            

        elif keyboard.is_pressed('up'):
            time.sleep(0.1)
            x-=1
            if x == 1:
                system('cls')
                selectex1()
            elif x == 2:
                system('cls')
                selectex2()
            elif x == 3:
                system('cls')
                selectex3()
            elif x == 4:
                system('cls')
                selectex4()
    
        elif x >= 5:
            x=4  
        elif x <= 0:
            x=1
    except:
        break
