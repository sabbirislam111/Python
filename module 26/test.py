from flask import Flask, request

database = {'sabbir': '32', 'salman': '234', 'sadia' : '234'}

for value in database.items():
    print(value[1])

