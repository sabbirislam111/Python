

""" 
input/listen
process/decide
output/talkback 

"""
greet_word =['hi', 'hello',]
buy_word =['buy', 'tata']


def listen():
    return input("Say something :")


def decide(command):
    command = command.lower()
    broken_word = command.split(" ")
    for word in broken_word:
        if word in greet_word:
            talkback("Hello i am Sabbir")
            break
        if word in buy_word:
            talkback("Buy see you again")
            break
    


def talkback(response):
    print(response)
    

while True:
    command = listen()
    decide(command)

