""" def replace_comma_with_space(text):
    return (text.replace(',', ' '))

s = "I,have,been,practising,python,since,the,course,started"

# output = replace_comma_with_space(s)
for char in s:
    if char == ',':
        char = ' '
        print(char)     """


a = "I,have,been,practising,python,since,the,course,started"
b = ' '.join(str(a).split(','))
print(b)


# print(output)
