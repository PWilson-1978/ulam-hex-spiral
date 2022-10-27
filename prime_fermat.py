import math as m
lastnum = lambda v: int(repr(v)[-1])

#my addition
def val_chk(val):
    if val < 10 or (val %6 in(1,5) and lastnum(val) in(1,3,7,9)):
        return True
    else:
        return False

def is_prime(val):
    for p in range(3,val):
        if val_chk(p):

            myval = (p**(val-1)+1) % val

            if myval == 1:
                return 1
            else:
                return 0  
######
for n in range(3000,20000):
    retval = 0
    if val_chk(n):
        retval = is_prime(n)
    if retval > 0:
        print(n)
