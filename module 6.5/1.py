


dangerous_words = ['die', 'fire', 'kill', 'killer', 'missile', 'bomb', 'burst', 'shoot', 'president', 'burn']

s ="I am feeling very dizzy tonight. But I am sure I did not fire that missile when I was drunk. Being a very professional contract killer I do not fire or plant bombs until particularly needed. Also, I do not have the courage to shoot the President let alone burst a bomb or fire a missle. Stop blaming me or my wrath will burn you into ashes. Ashes is not a brand here, my wrath is like fire, you might die kiddo. So stop pulling my legs and focus on your job. Shoot through the exit now!"

broken_worda = s.split()

final_new_menu =[]
for word in broken_worda:
    if word in dangerous_words:
        final_new_menu.append(word)

lst = set(final_new_menu)
print(lst)


        
    
