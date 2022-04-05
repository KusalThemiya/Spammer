import os

r ='\033[31;1m'
g ="\033[32;1m"
b ="\u001b[34m"

def banner():
    print(f"""{g}
                                                                 
  ______ ______   _____      _____     _____     ____   _______  
 /  ___/ \____ \  \__  \    /     \   /     \  _/ __ \  \_  __ \ 
 \___ \  |  |_> >  / __ \_ |  Y Y  \ |  Y Y  \ \  ___/   |  | \/ 
/____  > |   __/  (____  / |__|_|  / |__|_|  /  \___  >  |__|    
     \/  |__|          \/        \/        \/       \/           
               
    {b}Made by Themiya

{g}""")

                                           
banner()


from email import message
import pyautogui as pt
import time

limit = input("\u001b[33mHow many messages to send ?  ")
message = input("\u001b[33mEnter your message:  ")
i = 0 

time.sleep(10)

while i<int(limit):

    pt.typewrite(message)
    pt.press("enter")

    i+=1