from cgi import print_arguments
from dataclasses import replace

replace_with = ["chief", "thief", "superintendent", "sweeper", "married", "left", "tried", "died"]
s = "I am the chief of Baghdad. Before that I used to be a superintendent of Bank Asia. Things have changed a lot since Jorina married me. A lot of girls tried to marry me."
mydict =""

def Convert_dict(replace_with):  
    init = iter(replace_with)  
    res_dct = dict(zip(init, init))  
    return res_dct  

dict = Convert_dict(replace_with)
# kyes = dict.keys()
# val = dict.values()
def replace_word():
    return s.replace("chief", "thief").replace("superintendent", "sweeper").replace("married","left").replace("tried", "died")


print(replace_word())
    
     




