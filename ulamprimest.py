import math as m
from datetime import datetime

# p wilson 20220707 new method for evaluating prime

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


def prime_spoke(tval):

    for i in range(cNum,cNum2):

        val = 6 * i
        valt = val

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


            if prime_id == 0:
                slistc.append(valt)              
                slistac.append(valt) if x == 1 else slistbc.append(valt)
            else:
                slistp.append(valt)
                slistap.append(valt) if x == 1 else slistbp.append(valt)


            print('valt: ',valt,'; chk: ',chktype,'; prime: ', prime_id, '; mult6: ', i)

#########
def is_prime(value):
 
    global chktype

    if value in slistp:
        return True
    else:
        sval = int(m.sqrt(value))+1

        #print('square root: ', sval)

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
                if l < 4 or l % 2 > 0 and l % 3 > 0 and l % 5 > 0:
                    #print('l: ', l)
                    if value % l == 0:
                        return False

            return True


##########
def is_primeold(value):

    sval = int(m.sqrt(value))+1
         
    for l in range(2,sval):
        if value % l == 0:
            return False
    return True
               
########
chktype = 0
slistap = []
slistac = []
slistbp = []
slistbc = []

slistp = []
if cNum <= 100:
    slistp = [2,3,5]
slistc = []



prime_spoke(1)


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
   