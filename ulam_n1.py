import math as m
from datetime import datetime

print("Numbers separated by : - starting and number range like 5020:100")
cStr = input()

cNuml = cStr.split(':')

cNum = int(cNuml[0])
cNum2 = int(cNuml[1])
cNumR = cNum2
cNum2 += cNum

print('cNum: ', cNum)
print('cNum2: ', cNum2)
print('cNumR: ', cNumR)

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time is :", current_time)


# only values with end digits of 1,7,9,3 not 5
pprimes = []
# 23030401
#47297 
#########
def is_prime(value,*opt):
 
    global chktype

    if value in slistp:
        return True
    else:

        sval = m.sqrt(value)

        #print('Type of sval: ', type(sval))
        #print('square root: ', sval)

        if m.floor(sval) == m.ceil(sval):
            #print('Square root is a whole number')
            return False

        if sval in slistp:
            print('sval in slistp')
            return True
        
        if len(slistp) > 0 and slistp[-1] >= sval and sval >= slistp[0]:
            chktype = 1
            #print('checking list')
            for l in slistp:
                if value % l == 0:
                   return False
            return True  
        else:
            chktype = 2

            sval = int(sval) + 1

            for l in range(2,sval):
                #check the value of l because only need primes
                if l <= 15 or (l > 15 and is_prime_mini(l)):                 
                    if value % l == 0:
                        return False

            if not opt == 'pprimes':
                print('value of opt: ', opt)

            if not opt == 'pprimes':    
                check_vals(pprimes)
                pprimes.clear()
            elif opt == '':
                slistp.append(l)

            return True

####################
def check_vals(lval):
    print('in check_vals')
    for val in lval:
        if val not in slistp:
             if is_prime(val,'pprimes'):
                 slistp.append(val)

###################
def is_prime_mini(fac):

    if fac % 2 == 0:
        return False

    if fac in slistp:
        return True

    if not lastnum(fac) in(1,3,7,9):
        return False

    if fac not in pprimes:
        pprimes.append(fac)

    return True 

#######

# lambda functions
lastnum = lambda v: int(repr(v)[-1])
numchk  = lambda v,i: v > i and v % i > 0
#################

slistp = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]


# nextprime - take a number and get the first prime higher to it

for i in range(cNum,int(cNum+cNumR)):
    if i % 6 in(1,5) and lastnum(i) in(1,3,7,9):
         if is_prime(i) == True:
             #print('prime value: ', i)
             slistp.append(i)
    
print('values in list:')
slistp.sort()
print(slistp)

now = datetime.now()
now_time = now.strftime("%H:%M:%S")

print("Start Time was  :", current_time)
print("End Time was :", now_time)
print('Range was: ', cNum, ' with range: ', cNumR)
print ('Next num: ', cNum2+1)
#print ('Starting point: ', cNumT)

