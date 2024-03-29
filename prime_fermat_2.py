import math as m
import random as r
#from random import sample

lastnum = lambda v: int(repr(v)[-1])

#my addition
def val_chk(val):

    if val < 10 or (val %6 in(1,5) and lastnum(val) in(1,3,7,9)):
       return True
    else:
       return False

def is_prime(val):
    flist = []
    for i in range(0,2): #test 3 random values from the list

        p = r.choice(plist)
        #print('Value of p:', p)

        if val_chk(p):

            myval = p**(val-1) % val

            if myval == 1:
                flist.append(1)
            else:
                flist.append(0) 

    for i in flist:
        if i != 1:
            return 0
    return 1

###############
sval = 19013
eval = 19113

slist = []
for i in range(sval):
    if val_chk(i): 
        slist.append(i) 

for n in range(sval,eval):
    retval = 0
    
    # check to see if slist needs more values
    if n > sval:
        if val_chk(n) and n not in(slist):
            slist.append(n)
   
    # make sure list items are only up to the current value
    plist = r.sample(slist, 3)    

    if val_chk(n):
        #print('\n', n)
        retval = is_prime(n)

    if retval > 0:
        mval = (n - (n % 6)) / 6
        #print ('mult of 6: ', mval) 
        print('>>>>>> ', n, ' >>> mval: ', mval ,' with ', n % 6)

