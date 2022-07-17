import math as m
from datetime import datetime

# p wilson in process  new method for evaluating primes

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
#print("Current Time is :", current_time)

'''
highest value may not be a prime, so will need to always check when there are more
slist values to add
'''

############
def setup(value):
   
# divide numbers by 6 for loop

   nNum = cNum % 6
   nNum2 = nNum + value
   if value == 0:
       global loopcnt
       #set loop
       loopcnt += 1
       cNum3 = cNum + defamt
       value = defamt
      
       # for loop
       # set possible primes for range

       setHigh(cNum3)

       print('slistp: ', slistp)

       # spoke for range
       # loop for next group

   else:
       # high may not be prime so always check if slist has greater values
       setHigh(cNum2)     
       prime_spoke(1)

############
def slistToslistp(void):

    for i in slist:
        if is_prime(i):
            if i not in slistp:
                slistp.append(i)

############
def setHigh(value):
    print('setHigh value: ', value)

    # check this
    if (value+1 % 6 == 0 or value - 1 % 6 == 0):
        # in spoke
        bogus = 0
    else:
        newval = value % 6
        print('Newval: ', newval)
        value = (value - newval) + 1
        print('Value reset: ', value)

        slist.clear() #reinitialize list 
        prime_set(value)
        slistToslistp(1)
         
        #loop
        # check if higher values in slist than slistp     
############
def prime_spoke(tval):

    for i in range(cNum,cNum2-1):
        val = 6 * i
        valt = val

        prime_set(valt)
        if prime_id == 0:
            slistc.append(valt)              
            slistac.append(valt) if x == 1 else slistbc.append(valt)
        else:
            slistp.append(valt)
            slistap.append(valt) if x == 1 else slistbp.append(valt)

            
        print('valt: ',valt,'; chk: ',chktype,'; prime: ', prime_id, '; mult6: ', i)

##############
def prime_set(val):

        for x in(1,2):
            print('x: ', x)
            global chktype
            chktype = 0

            valt = val - 1 if x == 1 else val + 1
            prime_id = 0

            #print('valt: ', valt)
       
            if int(repr(valt)[-1]) == 5:
                bogus= 0
            else:
                if is_prime(valt) == True:
                    prime_id = 1



#########
def is_prime(value):
 
    global chktype

    if value in slistp:
        return True
    else:
        sval = int(m.sqrt(value))+1

        print('square root: ', sval)

        if sval in slistp:
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
            for l in range(2,sval):
                if isalmostprimeMini(l):
                   print('l ', l)
                   if value % l == 0:
                       return False

            return True
               
##########
def isalmostprimeMini(val):

# these values are used for the square root modulo, so they
# don’t completely need to be primes because just trying to 
# minimize the iterations

    if ((val-1) % 6 == 0 or (val+1) % 6 == 0):
        if val < 4 or not int(repr(val)[-1]) == 5:
            if val > 7 and val % 7 > 0:
                if val not in(slist):
                   slist.append(val)
                return True
    return False

###########
chktype = 0
loopcnt = 0
defamt = 1000

slistap = []
slistac = []
slistbp = []
slistbc = []

slistt = []
slistp = []
if cNum <= 100 or cNumR == 0:
    slistp = [2,3,5,7]
slistc = []
slist = [2,3,5,7]

#################

setup(cNumR)

#prime_spoke(1)


print('1: ', slistap)
print('')
print('2: ', slistac)

print('')
print('3: ', slistbp)
print('')
print('4: ', slistbc)

print('slistap len: ', len(slistap))
print('slistac len: ', len(slistac))
print('slistbp len: ', len(slistbp))
print('slistbc len: ', len(slistbc))

print('')
print('slistp: ', slistp)

print('slistc: ', slistc)

print('slistp len: ', len(slistp))
print('slibtc len: ', len(slistc))

print('')
print('Next start is: ', cNum2+1)


current_time = now.strftime("%H:%M:%S")
print("Start Time is :", current_time)

now = datetime.now()
end_time = now.strftime("%H:%M:%S") 
print('End Time is: ', end_time)
   