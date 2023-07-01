from distutils.command.clean import clean
def clean_string(text):
    for char in text:
        if char == ':':
            text = text.replace(char, '')
        elif char == ';':
            text = text.replace(char, '')
        elif char == '-':
            text = text.replace(char, '')
        elif char == ',':
            text = text.replace(char, '')
        elif char == '.':
            text = text.replace(char, '')
    return text   
s = "P::::::,,,,,h;;;;i,,,t--r;,:o..N"
output = clean_string(s)
print(output)