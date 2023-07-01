file2 = open ( 'words.dat' , 'w' ) 
word = '' 
i = 0
while word != 'END' : 
    i+=1
    word = input ( 'Enter a word (enter END to quit): ')
    if word == 'END':
        continue
    else:
        file2.write ( word + '\n' ) 
file2.close ( )

