file2 = open ( 'words.dat' , 'w' ) 
word = '' 
i = 0
while word != 'END': 
    i+=1
    word = input ( 'Enter a word (enter END to quit): ')
    if not word: break
    if word == 'END':
        continue
    else:
        file2.write ( word + '\n' ) 
file2.close ( )

file2 = open("words.dat", "r")
ans = file2.read()

file2.close()

idx = 0
for word in ans.split('\n'):
    if word == '':
        continue
    else:
        print(f'{idx}:{word}')
        idx += 1