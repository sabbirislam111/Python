import keyboard
a = "This is first page content--Now we are in the second page--Now we are in the third page--Now we are in the forth page--Now we are in the five page--Now we are in the six page--Now we are in the seven page--Now we are in the eight page--Now we are in the nine page"


s = a.split('--')
  
print("___________________________")
print(s[0]) 
print("___________________________")   


i = 1
while True:
    print("press Enter for next page")
    print("press q for next quit")
    print("press o for next skip page")

    
    if keyboard.read_key() == "xxx":
        pass

    elif keyboard.read_key() == "o":
        inp = int(input("Enter the page number : "))
        print("___________________________")
        print(s[inp])
        print("___________________________")
        i += inp

    elif keyboard.read_key() == "enter":
        print("___________________________")
        print(s[i])
        print("___________________________")
        i += 1   
    elif keyboard.read_key() == "q":
        break



    





    
   











