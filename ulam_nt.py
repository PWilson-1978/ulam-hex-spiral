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
filename1 = 'ulam_nt_' + now.strftime("%Y%m%d_%H%M%S") + '.txt'

print("Current Time is :", current_time)



# only values with end digits of 1,7,9,3 not 5
pprimes = set()
tprimes = set()



#########
def is_prime(value,*opt):
 
    global chktype
    my_opt = ''

    for myopt in opt:
       my_opt = myopt
    #print('my_opt = ', my_opt)

    if value in slistp:
        return True
    else:

        sval = m.sqrt(value)

        #print('Type of sval: ', type(sval))
        #print('square root: ', sval, ' of value: ', value)

        if m.floor(sval) == m.ceil(sval):
            #print('Square root is a whole number')
            return False

        if sval in slistp:
            print('sval in slistp')
            return True


        sslistp = list(slistp)
        sslistp.sort()

        if len(sslistp) > 0 and sslistp[-1] >= sval and sval >= sslistp[0]:

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

            if my_opt == '':   
                check_vals(pprimes)
                pprimes.clear()

            return True

####################
def check_vals(lval):
    #print('in check_vals')
    for val in lval:
        if val not in slistp:
             if is_prime(val,'pprimes'):
                 slistp.add(val)

###################
def is_prime_mini(fac):

    if fac % 2 == 0:
        return False

    if fac in slistp:
        return True

    if not (fac % 6 in(1,5) and lastnum(fac) in(1,3,7,9)):
        return False

    if fac not in pprimes:
        pprimes.add(fac)

    return True 

#######

# lambda functions
lastnum = lambda v: int(repr(v)[-1])
numchk  = lambda v,i: v > i and v % i > 0
#################

slistp = set([2,3,5,7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])


# nextprime - take a number and get the first prime higher to it

for i in range(cNum,int(cNum+cNumR)):
    if i % 6 in(1,5) and lastnum(i) != 5:
         if is_prime(i) == True:
             #print('prime value: ', i)
             tprimes.add(i)

now = datetime.now()
now_time = now.strftime("%H:%M:%S")


#handle the derived numbers  


# convert set to list to sort

tlist = list(tprimes)

sslistp = list(slistp)
sslistp.extend(tlist)
 
sslistp.sort()
#print('values in list:')
#print(sslistp)

file1 = open(filename1,"a")
file1.write(','.join(map(str,sslistp)))
file1.close()

print('Values saved in file ',filename1)

listnow = datetime.now()
list_time = now.strftime("%H:%M:%S")

print("Start Time was  :", current_time)
print("End Time was :", now_time)
print("Time for lists: ", list_time)
print('Range was: ', cNum, ' with range: ', cNumR)
print ('Next num: ', cNum2+1)
#print ('Starting point: ', cNumT)

