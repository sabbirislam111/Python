space_invaders = [ '. . .' ] 
player_pos = ( 200 , 25 ) 
level = 1 ; max_level = 10 

def play ( ) : 
    while ( level < max_level +1 ) :
         if len ( space_invaders ) == 0 : 
            level += 1 
            continue 
      
print(play())



# level is local variable
# max_level is global variables
# space_invaders, player_pos and len are built-in function

