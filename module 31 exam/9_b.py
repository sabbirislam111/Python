file = open ( 'words.dat' , 'w' ) 
word = '' 
i = 0
while word != 'END' : 
    i+=1
    word = input ( 'Enter a word (enter END to quit): ')
    if word == 'END':
        continue
    else:
        file.write ( word + '\n' ) 
file.close ( )
print(i-1,'words are stored in the file')
