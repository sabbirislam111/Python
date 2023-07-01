def dp ( l1 , l2 ) : 
    def p ( ll1 , ll2 , n ) : 
        return ll1[n] * ll2[n] 
    r = 0 
    for i in range ( len ( l1 ) ) : 
      r += p ( l1 , l2 , i ) 
    return r 


print (dp ( [ 1 , 2 , 3 ] , [ 4 , 5 , 6 ] ))



#step 1.     ll1 = 1, ll2 = 4, n = 0 so ............ans = (1*4) = 4
#step 2.     ll1 = 2, ll2 = 5, n = 1 so ............ans = (5*2) = 10
#step 3.     ll1 = 3, ll2 = 6, n = 2 so ............ans = (3*6) = 18
# finally r += 4, 10, 18 (sequential) so currect answer is 32