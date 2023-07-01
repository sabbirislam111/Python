
str = input("Enter the String :")
i = 0
ch2 = ''
# convert capital letter string to small letter string
while str[i:]:
    ch = ord(str[i])
    if ch >= 65 and ch <= 90:
        ch2 += chr(ch+32)
    elif ch >= 97 and ch <= 122:
        ch2 += chr(ch-32)
    else:
        ch2 += chr(ch)
    i += 1
print("Lower case String is:", ch2)