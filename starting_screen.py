import keyboard
import time
import os

class Start():
    
    p = """
  _______          _            _        
 |__   __|        | |          (_)       
    | |      ___  | |_   _ __   _   ___  
    | |     / _ \ | __| | '__| | | / __| 
    | |    |  __/ | |_  | |    | | \__ \ 
    |_|     \___|  \__| |_|    |_| |___/ 
                                         
                                         """

    def select(self,direction, current):
        os.system('cls')
        s=["PLAY","SETTINGS","ABOUT"]
        b=""
        if direction=="left" and current>0:
            new = s[current-1]
            for i in range(3):
                if new == s[i]:
                    b+=" "*5+"["+new+"]"
                else:
                    b+=" "*5+s[i]
            return b, current-1
        elif direction=="right" and current<2:
            new = s[current+1]
            for i in range(3):
                if new == s[i]:
                    b+=" "*5+"["+new+"]"
                else:
                    b+=" "*5+s[i]
            return b, current+1
        else:
            return " "*5+(" "*5).join(s), current

        
