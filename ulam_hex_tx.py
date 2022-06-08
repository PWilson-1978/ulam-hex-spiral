import turtle
import math as m
from datetime import datetime

'''
author: P Wilson, 20220529 
 
This routine will create a hexagon pattern with the primes all appearing on the upward diagonal radii.

At the end of the run, the start and stop time will display, along with the range used and the next number to start 
Also prints the list of primes from the range

If more than 250 is used for a range, the screen commands will stop, but the print will show. I found that on larger ranges, it seemed the screen commands were really slowing the process

Started with code from geekforgeeks, stackoverflow and possibly other sources

Still working on this routine.
'''

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


# open the list of prime values
with open("primes to 5000.txt", "r") as f:
    for line in f:
        prime_vals = line.split(',')

prime_vals = [int(i) for i in prime_vals]
#print(prime_vals)
prime_vals.sort()

cNumT = 0

############

# Start a work Screen
ws = turtle.Screen()

# Define a Turtle Instance
t = turtle.Turtle()
 
# executing loop 6 times for 6 sides
t.penup()

###########
def level_display(hex_info):
    

    global ccnt
    for i in range(6):
        cur_num = nlst[i]
        ccnt += 1
        t.penup()
        #t.width(ccnt/1000+1)
        #t.forward(ccnt*2)

        #Turn left the turtle by 300 degrees
        if hex_info == True:
            if i == 1:
               t.goto(6.19,30.73)
               t.left(30)
            else:
              t.left(60)
        else:
           t.left(60)
        
        prime_id = 0
        if isPrime(cur_num) == True:
            t.color('blue')
            #t.color('#3c79b8') #smokey blue hex
            if cur_num not in prime_vals:
                prime_vals.append(cur_num)
            prime_id = 1
        else:
            t.color('grey')

        if ccnt < 250:
            if ccnt > 7:
                t.write(cur_num)        

            if i == 5:
                t.penup()
                t.forward(ccnt*2)
            else:
                t.width(ccnt+5/1000+1.5)
                t.forward(ccnt*2)

        #if prime_id == 1 or (ccnt > 6 and ccnt < 200):
        if cur_num % 6 in (1,5):
            print('pos: ', t.pos(), 'i: ',i, 'num: ', cur_num, 'prime: ', prime_id)
#########
def adjust_start(value):
    global cNumT

    #adjust starting number to make sure the primes appear on the upward diagonals

    cNumT = value % 6
    print ('Initial starting point: ', cNumT)

    if cNumT != 2:
        for z in range(6):
            value -= 1
            if value % 6 == 2:
                return value
    return 0
###################
def isPrime(value):
    #print('Checking for prime value: ', value)
    pval = 0

    #if divisible by 2 or last digit is 5
    if value % 2 == 0 or int(repr(value)[-1]) == 5:
        return False

    if value % 6 in (1,5):
        sqrtval = m.sqrt(value)

        print('Current primechk: ', value, '; sqrt: ', sqrtval)

        if sqrtval > 2 or value > 1:
             if value in prime_vals:
                 return True
             else:
                 plen = len(prime_vals)
                 for i in prime_vals:
                      listval = i
                      if listval < value:
                          if value % listval == 0:
                              return False

                          if (prime_vals[-1] == listval and listval < sqrtval):
                              rval = mini_isPrime(sqrtval, value, listval)
                              return rval
                      
                 return True        

    return False
###################
def mini_isPrime2(sqrtval, value, listval):

    if sqrtval > 2:
         for i in range(listval,int(sqrtval)+1):
                 if value % i == 0:
                     return False
               
                 return True

####################
def mini_isPrime(sqrtval, value, listval):

     print('Listval: ', listval, '; value: ', value, '; sqrtval: ', sqrtval) 

     for i in range(listval,int(sqrtval)+1):
         prime_id = 0
 
         if i % 6 in(1,5):
             if i not in prime_vals:
                 #print('not in prime_vals - i:', i)
                 val = mini_isPrime2(sqrtval, i, listval)

                 if val == True:
                 
                      prime_vals.append(i)
                      prime_id = 1

             #print('i: ', i , ' - has prime_id: ', prime_id)

         if prime_id == 1:
             if value % i == 0:
                 return False
             

     return True
###################
# Main work

# adjust the start value so the primes will appear on the two upward diagonals
rNum = adjust_start(cNum)
if rNum != 0:
    cNum = rNum

print ('Starting point: ', cNum % 6)

tcnt = cNum
ccnt = 0
#prime_vals = []
hinfo = False

print('cNum: ', cNum, '; cNumR/6: ', int(cNumR/6))

# Add a few numbers to the start to keep from the crunch

for x in range(int(cNumR/6)):
     #print('Current iteration value: ', x, 'of ',int(cNumR/6))
     nlst = []
     if tcnt == cNum:
         hinfo = True

     for j in range(6):
         tcnt += 1
         nlst.append(tcnt)

     if nlst[-1] <= cNum2:
         bogus = level_display(hinfo)
     else:
       break

     hinfo = False
#####################

now = datetime.now()
now_time = now.strftime("%H:%M:%S")
prime_vals.sort()
print(prime_vals)

print("Start Time was  :", current_time)
print("End Time was :", now_time)
print('Range was: ', cNum, ' with range: ', cNumR)
print ('Next num: ', cNum2+1)
print ('Starting point: ', cNumT)


