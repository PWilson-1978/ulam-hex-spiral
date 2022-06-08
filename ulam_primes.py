import math as m
from datetime import datetime
# P Wilson 20220607 - this routine generates lists of the primes and nonprimes from the hex radiis that are associated with 5 and 7

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


def prime_spoke(tval, sval):

    for i in range(cNum,cNum2):
        tval = 6 * i + sval
        prime_id = 0

        #print('tval: ', tval)
       
        if tval % 2 == 0 or (tval > 10 and int(repr(tval)[-1])) == 5:
            bogus= 0
        else:
            if is_prime(tval) == True:
                 slistp.append(tval)
                 prime_id = 1

        if prime_id == 0:
            slistc.append(tval)

        print('tval: ', tval, 'prime: ', prime_id, 'mult of 6: ', i)

def is_prime(value):

    sval = int(m.sqrt(value))+1
         
    for l in range(2,sval):
        if value % l == 0:
            return False
    return True
               
########

slistp = []
slistc = []


prime_spoke(1,1)


slist1p = slistp
slist1c = slistc

slistp = []
slistc = []
print('slist1c len: ', len(slist1c))

prime_spoke(1,5)


print('1: ', slist1p)
print('')
print('2: ', slist1c)

print('')
print('3: ', slistp)
print('')
print('4: ', slistc)

print('slist1p len: ', len(slist1p))
print('slist1c len: ', len(slist1c))
print('slistp len:  ', len(slistp))
print('slistc len:  ', len(slistc))

print('')
print('Next start is: ', cNum2+1)


current_time = now.strftime("%H:%M:%S")
print("Start Time is :", current_time)

now = datetime.now()
end_time = now.strftime("%H:%M:%S") 
print('End Time is: ', end_time)
   
