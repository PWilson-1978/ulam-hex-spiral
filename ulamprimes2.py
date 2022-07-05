import math as m
from datetime import datetime

# not current implement 
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

            valt = val - 1 if x == 1 else val + 1
            prime_id = 0

            print('valt: ', valt)
       
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

            print('valt: ', valt, 'prime: ', prime_id, 'mult of 6: ', i)

def is_prime(value):

    sval = int(m.sqrt(value))+1
         
    for l in range(2,sval):
        if value % l == 0:
            return False
    return True
               
########

slistap = []
slistac = []
slistbp = []
slistbc = []


slistp = []
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
   