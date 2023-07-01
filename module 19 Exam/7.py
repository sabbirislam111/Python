import keyboard

a = "This is first page content--Now we are in the second page--Now we are in the third page--Now we are in the forth page--Now we are in the five page--Now we are in the six page--Now we are in the seven page--Now we are in the eight page--Now we are in the nine page"

s = a.split('--')
print(s[0])   
    
i = 1  

while True:
    if keyboard.read_key() == "oooo":
       pass
    
    elif keyboard.read_key() == "enter":
        print("___________________________")
        print(s[i])
        i += 1
    elif keyboard.read_key() == "q":
        break
        
    


